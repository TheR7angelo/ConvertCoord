import glob
import os
import re

from PySide6 import QtCore, QtWidgets, QtGui
from pyproj import Transformer

from src import *
from src.gui.dlg.RgbBox.RgbBox import RgbBox
from src.gui.ui import calculatrice_ui
from src.gui.events.Event import Event
from src.widgets import vb_wg


class CalculatriceDlg(calculatrice_ui.Ui_Option, QtWidgets.QDialog):
    dragPos: QtCore.QPoint
    cfg = Configue().cfg

    def __init__(
            self,
            fen_main,
            title,
            msg,
            ico,
            ico_rgb,
            txt_apply,
            txt_ok,
            width,
            height,
            opacity,
    ):
        super(CalculatriceDlg, self).__init__()

        self.fen_main = fen_main
        self.title = title
        self.msg = msg
        self.ico = ico
        self.ico_rgb = ico_rgb
        self.txt_ok = txt_ok
        self.txt_pb_appliquer = txt_apply
        self.width = width
        self.height = height
        self.opacity = opacity

        self.size_grip = QtWidgets.QSizeGrip(self)

        self.INIT()

        ### CREATION DES EVENT ###
        self.evt = Event(self)
        self.mousePressEvent = self.evt.mousePressEvent
        self.mouseMoveEvent = self.evt.mouseMoveEvent

    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        ### Fenetre ###
        self.setWindowTitle(self.title)
        self.setMinimumWidth(self.width)
        self.setMinimumHeight(self.height)
        self.setWindowOpacity(self.opacity)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowIcon(QtGui.QPixmap(f"{Img().calc()}th3.svg"))
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowModality(QtCore.Qt.WindowModal)

    def IN_SETUP_UI(self):
        ### Ui ###
        self.setupUi(self)
        self.vlay_main.setContentsMargins(v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP)

    def IN_CLASSE(self):

        ### QFrame ###
        Frame.Menu(self.fr_menu_top).top()
        Frame.Cadre(self.fr_main).th2()
        Frame.Dlg(self.fr_body).th(rgb=Rgb().th1())
        Frame.Menu(self.fr_menu_bottom).bottom_dlg()
        ### /QFrame ###

        ### QTableWidget
        TableWidget.Base(self.conversion).th()
        ### \QTableWidget

        ### QLabel ###
        Label.Base(self.lb_mt_ico).ico_custom(img=Img().calc())
        Label.Base(self.lb_mt_nom, font_size=Font().h3()).tr()
        ### /QLabel ###


        ### QPushButton ###
        PushButton.menu_top(self.pb_mt_quitter).quitter()

        ### /QPushButton ###

    def IN_WG(self):
        # Base
        self.setCursor(Functions().SET_CURSOR(cur=Cur().Arrow()))

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(Dim().h9())

        # Menu_top
        self.lb_mt_nom.setText(self.title)

        self.conversion.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.conversion.verticalHeader().hide()
        self.conversion.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.conversion.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)

        ### size_grip ###
        if self.cfg["var"]["resize"]:
            self.size_grip.setCursor(Functions().SET_CURSOR(Cur().fleche_nwse()))
            self.size_grip.setStyleSheet(
                f"""
                QSizeGrip {{
                image: url({Img().resize()}th3.svg);
                width: {Dim().h10()}px;
                height: {Dim().h10()}px;
                }}
                """
            )
            self.hlay_menu_bottom.addWidget(self.size_grip)

    def IN_CONNECTIONS(self):
        # Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        self.conversion.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.conversion.customContextMenuRequested.connect(lambda pos, child=self.conversion: self.customMenuEvent(pos, child))

        self.conversion.cellChanged.connect(self.convert)

    def IN_ACT(self):
        pass

    def IN_WG_BASE(self):
        pass

    def INIT(self):
        self.IN_BASE()
        self.IN_SETUP_UI()
        self.IN_CLASSE()
        self.IN_WG()
        self.IN_CONNECTIONS()
        self.IN_ACT()
        self.IN_WG_BASE()

    def convert(self, x, y):  # sourcery no-metrics

        def lambert(coord_x, coord_y, row):

            try:
                transformer = Transformer.from_crs("epsg:2154", "epsg:4326", always_xy=True)
                coord = transformer.transform(coord_x, coord_y)

                for y, value in enumerate(coord):
                    if value > 0:
                        sens = '+'
                        second_value = value
                    else:
                        sens = '-'
                        second_value = -value

                    lonSeconds = second_value * 60 * 60

                    seconds = float(lonSeconds % 60)
                    minutes = int((lonSeconds / 60) % 60)
                    degrees = int((lonSeconds / 60) / 60)

                    if sens == '-':
                        sens = 'W' if y == 0 else 'S'
                    else:
                        sens = 'E' if y == 0 else 'N'

                    self.conversion.setItem(row, y + 2, QtWidgets.QTableWidgetItem(f"{value}"))
                    self.conversion.setItem(row, y + 4, QtWidgets.QTableWidgetItem(f"{degrees}°{minutes}'{'%.4f'%seconds}\"{sens}"))
            except TypeError:
                pass

        def wgs(coord_x, coord_y, row):
            try:
                coord = [float(coord_x), float(coord_y)]
                transformer = Transformer.from_crs("epsg:4326", "epsg:2154", always_xy=True)
                coord_lambert = transformer.transform(coord_x, coord_y)

                for y, value in enumerate(coord):
                    if value > 0:
                        sens = '+'
                        second_value = value
                    else:
                        sens = '-'
                        second_value = -value

                    lonSeconds = second_value * 60 * 60

                    seconds = float(lonSeconds % 60)
                    minutes = int((lonSeconds / 60) % 60)
                    degrees = int((lonSeconds / 60) / 60)

                    if sens == '-':
                        sens = 'W' if y == 0 else 'S'
                    else:
                        sens = 'E' if y == 0 else 'N'

                    self.conversion.setItem(row, y, QtWidgets.QTableWidgetItem(f"{coord_lambert[y]}"))
                    self.conversion.setItem(row, y + 4, QtWidgets.QTableWidgetItem(f"{degrees}°{minutes}'{'%.4f'%seconds}\"{sens}"))
            except TypeError:
                pass

        def sexa(coord_x, coord_y, row):

            def sexa_dms(coord):
                coord = re.split('°|\'|"', coord)

                tmp = []
                for item in coord:
                    if item.replace('.', '', 1).isnumeric():
                        tmp.append(float(item))
                    else:
                        tmp.append(item)
                coord = tmp[:]
                del tmp

                if coord[3].lower() in ["n", "e"]:
                    return coord[0] + (coord[1] / 60) + (coord[2] / 3600)
                else:
                    return -(coord[0] + (coord[1] / 60) + (coord[2] / 3600))

            try:
                coord = [sexa_dms(item) for item in [coord_x, coord_y]]
                transformer = Transformer.from_crs("epsg:4326", "epsg:2154", always_xy=True)
                coord_lambert = transformer.transform(coord[0], coord[1])

                for y, value in enumerate(coord):
                    self.conversion.setItem(row, y, QtWidgets.QTableWidgetItem(f"{coord_lambert[y]}"))
                    self.conversion.setItem(row, y + 2, QtWidgets.QTableWidgetItem(f"{coord[y]}"))
            except TypeError:
                pass

        if self.conversion.item(x, y).text() != "":
            self.conversion.blockSignals(True)
            if y % 2:
                if self.conversion.item(x, y-1) is not None:
                    coord_x = self.conversion.item(x, y-1).text().replace(",", ".")
                    coord_y = self.conversion.item(x, y).text().replace(",", ".")
                    if y in (0, 1):
                        lambert(coord_x=coord_x, coord_y=coord_y, row=x)
                    elif y in (2, 3):
                        wgs(coord_x=coord_x, coord_y=coord_y, row=x)
                    elif y in (4, 5):
                        sexa(coord_x=coord_x, coord_y=coord_y, row=x)
            else:
                if self.conversion.item(x, y + 1) is not None:
                    coord_x = self.conversion.item(x, y).text()
                    coord_y = self.conversion.item(x, y + 1).text()
                    if y in (0, 1):
                        lambert(coord_x=coord_x, coord_y=coord_y, row=x)
                    elif y in (2, 3):
                        wgs(coord_x=coord_x, coord_y=coord_y, row=x)
                    elif y in (4, 5):
                        sexa(coord_x=coord_x, coord_y=coord_y, row=x)
            self.conversion.blockSignals(False)

    def customMenuEvent(self, eventPosition, child):

        contextMenu = QtWidgets.QMenu(self)
        Functions().SET_FONT(contextMenu, font=vb_wg.FONT, font_size=vb_wg.FONT_SIZE)

        contextMenu.setStyleSheet(f"""
                                .QMenu{{
                                background-color: rgba{Rgb().th3()};
                                border-top: {2}px solid rgba{Rgb().th1()};
                                border-bottom: {2}px solid rgba{Rgb().th1()};
                                border-right: {2}px solid rgba{Rgb().th1()};
                                border-left: {2}px solid rgba{Rgb().th1()};
                                border-top-right-radius: {3}px;
                                border-top-left-radius: {3}px;
                                border-bottom-right-radius: {3}px;
                                border-bottom-left-radius: {3}px;
                                }}
                                QMenu::item{{
                                background-color: rgba{Rgb().th3()};
                                color: rgba{Rgb().th1()};
                                }}
                                QMenu::item:hover{{
                                background-color: rgba{Rgb().th3()};
                                color: rgba{Rgb().bn1()};
                                }}
                                """)

        if child == self.conversion:
            # frame = QtWidgets.QFrame(self)
            # hbox = QtWidgets.QHBoxLayout()
            #
            # text_1 = QtWidgets.QLabel("Ajouter ")
            #
            # spin = QtWidgets.QSpinBox()
            # spin.setMinimum(1)
            # spin.setMaximum(10)
            #
            # text_2 = QtWidgets.QLabel(" ligne(s)")
            #
            # for w in [text_1, spin, text_2]:
            #     hbox.addWidget(w)
            #
            # frame.setLayout(hbox)
            #
            # wa = QtWidgets.QWidgetAction(self)
            # wa.setDefaultWidget(frame)
            #
            # contextMenu.addAction(wa)
            contextMenu.addAction("Ajouter ligne", lambda: self.ajout_ligne(child))
            contextMenu.addAction("Copier", lambda: self.copier(child))
            contextMenu.addAction("Coller", lambda: self.coller(child))
            contextMenu.addAction("Supprimer info", lambda: self.delete_data(child))
            contextMenu.addAction("Supprimer ligne(s)", lambda: self.supprime_ligne(child))

        contextMenu.exec(child.mapToGlobal(eventPosition))

    def ajout_ligne(self, table):
        row = table.currentRow()
        table.insertRow(row+1)

    def supprime_ligne(self, widget):
        rows = [index.row() for index in widget.selectedIndexes()]
        for row in reversed(rows):
            widget.removeRow(row)

    def delete_data(self, table):
        selected = table.selectedRanges()
        for row in range(selected[0].topRow(), selected[0].bottomRow() + 1):
            for col in range(selected[0].leftColumn(), selected[0].rightColumn() + 1):
                table.setItem(row, col, QtWidgets.QTableWidgetItem(""))

    def coller(self, table):
        data = QtWidgets.QApplication.clipboard().text()

        x_init = table.currentRow()
        y_init = table.currentColumn()

        row = data.split("\n")
        for x, col in enumerate(row):
            text = col.split("\t")
            for y, item in enumerate(text):
                if item != "":
                    table.setItem(x + x_init, y + y_init, QtWidgets.QTableWidgetItem(item))

    def copier(self, table):
        selected = table.selectedRanges()
        texte = ""
        for i in range(selected[0].topRow(), selected[0].bottomRow() + 1):
            for j in range(selected[0].leftColumn(), selected[0].rightColumn() + 1):
                try:
                    texte += table.item(i, j).text() + "\t"
                except AttributeError:
                    texte += "\t"
            texte = texte[:-1] + "\n"
        QtWidgets.QApplication.clipboard().setText(texte)

    def keyPressEvent(self, event):

        if self.conversion.hasFocus():
            if event.key() == QtCore.Qt.Key_C and (event.modifiers() & QtCore.Qt.ControlModifier):
                self.copier(table=self.conversion)

            elif event.key() == QtCore.Qt.Key_V and (event.modifiers() & QtCore.Qt.ControlModifier):
                self.coller(table=self.conversion)

            elif event.key() in [QtCore.Qt.Key_Delete, QtCore.Qt.Key_Backspace]:
                self.delete_data(table=self.conversion)

        event.accept()

