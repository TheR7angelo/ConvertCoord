import re
from pyproj import Transformer


class convert:

    @staticmethod
    def isFloat(value: str):
        return re.match(r'^-?\d+(?:\.\d+)$', value) is not None

    @staticmethod
    def isInt(value: str):
        return value.isnumeric()

    def isNombre(self, value: str):
        return self.isFloat(value=value) or self.isInt(value=value)

    @staticmethod
    def GetTransformer(de: str, to: str):
        return Transformer.from_crs(f"epsg:{de}", f"epsg:{to}", always_xy=True)

    @staticmethod
    def ToSexa(coordX: float, coordY: float):
        wsg = []
        coord = [coordX, coordY]
        for index, value in enumerate(coord):

            if value > 0:
                sens = '+'
            else:
                sens = '-'
                value = -value

            lonDegrees = value
            lonSeconds = lonDegrees * 60 * 60

            seconds = float(lonSeconds % 60)
            minutes = int((lonSeconds / 60) % 60)
            degrees = int((lonSeconds / 60) / 60)

            if sens == '-':
                sens = 'S' if index == 0 else 'W'
            else:
                sens = 'N' if index == 0 else 'E'
            wsg.append(f'{degrees}°{minutes}' + "'" + str("%.4f" % seconds) + '"' + sens)

        return wsg[0], wsg[1]

    @staticmethod
    def ToDms(coord):
        coord = re.split('°|\'|"', coord)
        coord = [item.strip() for item in coord]

        coord = [float(item) if item.replace('.', '', 1).isnumeric() else item for item in coord]

        if coord[3].lower() in ["n", "e"]:
            return coord[0] + (coord[1] / 60) + (coord[2] / 3600)
        else:
            return -(coord[0] + (coord[1] / 60) + (coord[2] / 3600))

    def transform(self, de: str, to: str, coordX: str, coordY: str):
        global transformer

        match de:
            case "2154":
                transformer = self.GetTransformer(de=de, to="4326")
                if self.isNombre(value=coordX) and self.isNombre(value=coordY):
                    match to:
                        case "2154":
                            return coordX, coordY
                        case "4326":
                            return transformer.transform(coordX, coordY)
                        case "sexa":
                            coordX, coordY = transformer.transform(coordX, coordY)
                            return self.ToSexa(coordX=float(coordY), coordY=float(coordX))
                        case "27582":
                            transformer = self.GetTransformer(de=de, to=to)
                            return transformer.transform(coordX, coordY)
                return self.error()

            case "4326":
                if self.isNombre(value=coordX) and self.isNombre(value=coordY):
                    transformer = self.GetTransformer(de=de, to=to)
                    match to:
                        case "2154" | "27582":
                            return transformer.transform(coordX, coordY)
                        case "4326":
                            return coordX, coordY
                        case "sexa":
                            return self.ToSexa(coordX=float(coordY), coordY=float(coordX))
                return self.error()

            case "sexa":
                coordX, coordY = self.ToDms(coord=coordX), self.ToDms(coord=coordY)
                match to:
                    case "2154" | "27582":
                        transformer = self.GetTransformer(de="4326", to=to)
                        return transformer.transform(xx=coordX, yy=coordY)
                    case "4326":
                        return coordX, coordY
                    case "sexa":
                        return self.ToSexa(coordX=float(coordX), coordY=float(coordY))
                return self.error()

            case "27582":
                match to:
                    case "2154" | "4326":
                        transformer = self.GetTransformer(de="27582", to=to)
                        return transformer.transform(coordX, coordY)
                    case "sexa":
                        transformer = self.GetTransformer(de=de, to="4326")
                        coordX, coordY = transformer.transform(coordX, coordY)
                        return self.ToSexa(coordX=float(coordY), coordY=float(coordX))
                    case "27582":
                        return coordX, coordY
                return self.error()

    @staticmethod
    def error():
        return "Nan", "Nan"

if __name__ == '__main__':
    convert = convert()
    # coord = convert.transform(de="2154", to="4326", coordX="466353.752", coordY="6343763.984")
    # test = convert.transform(de="4326", to="sexa", coordX=coord[0], coordY=coord[1])
    # test2 = convert.transform(de="sexa", to="2154", coordX=test[0], coordY=test[1])
    test3 = convert.transform(de="2154", to="sexa", coordX='412625.9', coordY='6455179.9')

    print(test3)
