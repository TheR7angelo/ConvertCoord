import os
import sys

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QFileDialog, QTableWidgetItem

from src import *
from src.gui import *
from src.widgets import vb_wg
from src.scripts.script import convert


class main(Ui_main, QtWidgets.QWidget):
    dragPos: QtCore.QPoint

    cfg = Configue().cfg

    def __init__(self):
        super(main, self).__init__()

        ### AJOUTS DE BASE ###
        self.size_grip = QtWidgets.QSizeGrip(self)
        self.timer_double_click = QtCore.QTimer(self)
        self.timer_double_click.setSingleShot(True)
        self.timer_double_click.timeout.connect(self.traySingleClick)

        ### VARIABLES DE BASES ###
        self.win_state = QtCore.Qt.WindowNoState

        ### FONCTIONS AU LANCEMENT ###
        self.INIT(
            [self.IN_BASE, "Configuration des éléments principaux"],
            [self.IN_SETUP_UI, "Setup de l'interface graphique"],
            [self.IN_CLASSE, "Initialisation des Widgets"],
            [self.IN_WG, "Configuration de base des Widgets"],
            [self.IN_CONNECTIONS, "Ajout des connexions"],
            [self.IN_ACT, "Fonctions de base"],
            [self.IN_WG_BASE, "Etat de base des Widgets"],
            # [self.IN_TRAY, "Finalisation de la configuration"]
        )

        splash_screen.close()

        if maj := Maj().get_maj():
            rep = ResponseBox().INFO(title="Mise à jour disponible",
                                     msg=f"""
                                        Une mise à jour est disponible.\n
                                        Version: {maj[0]}\n
                                        Voulez-vous la télécharger ?"
                                        """,
                                     txt_ok="Oui",
                                     txt_cancel="Non")
            if rep:
                try:
                    os.startfile(maj[1])
                    sys.exit()
                except FileNotFoundError:
                    ResponseBox().ALERTE(title="Erreur",
                                         msg="Une erreur est survenue.\nMerci de réessayer ultérieurement.")

        self.convertiseur = convert()

        ### CREATION DES EVENT ###
        self.evt = Event(self)
        self.mousePressEvent = self.evt.mousePressEvent
        self.mouseDoubleClickEvent = self.evt.mouseDoubleClickEvent
        self.mouseMoveEvent = self.evt.mouseMoveEvent
        self.mouseReleaseEvent = self.evt.mouseReleaseEvent

    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        ### Fenetre principal ###
        self.setWindowTitle(Configue().cfg["infos"]["nom"])
        self.setWindowIcon(QtGui.QPixmap(f"{Img().main()}th3.svg"))
        self.setWindowOpacity(Configue().cfg["config"]["opacity"])
        self.setGraphicsEffect(Shadow().ombre_portee(self))

        self.e_resize_screen()

    def IN_SETUP_UI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ### Ui principal ###
        self.setupUi(self)
        self.vlay_main.setContentsMargins(v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP)

    def IN_CLASSE(self):

        ### QFrame ###
        Frame.Menu(self.fr_menu_top).top()
        Frame.Cadre(self.fr_main).th2()
        Frame.Base(self.fr_body).tr()
        Frame.Menu(self.fr_menu_bottom).bottom()
        ### /QFrame ###

        ### QLabel ###
        Label.Base(self.lb_mt_ico).ico_main()
        Label.Base(self.lb_mt_nom, font_size=Font().h3()).tr()
        Label.Base(self.lb_mb_version).tr()
        ### /QLabel ###

        ### QPushButton ###
        PushButton.menu_top(self.pb_mt_reduire).reduire()
        PushButton.menu_top(self.pb_mt_agrandir).agrandir()
        PushButton.menu_top(self.pb_mt_quitter).quitter()
        ### /QPushButton ###

        ### QTable ###
        TableWidget.Base(self.conversion).th()
        ### /QTable ###

        # TrayIcon.Main(self.tray_menu)

    def IN_WG(self):

        ### Base ###
        self.setCursor(Functions().SET_CURSOR(Cur().Arrow()))

        ### Nom de l'app ###
        self.lb_mt_nom.setText(self.cfg["infos"]["nom"])

        ### Widget blanc pour centrer le nom de l'app ###
        dim = Dim().h9() * 1.4
        Functions().SET_DIM(self.wg_mt_blank, width=dim * 3, height=dim)

        ### Version de l'app ###
        self.lb_mb_version.setText(f" Version : {self.cfg['infos']['version']}")

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

        #self.lineEdit.setPlaceholderText("Glisser déposer un dossier")

    def IN_CONNECTIONS(self):

        ### Menu_top ###
        self.pb_mt_reduire.clicked.connect(lambda: self.evt.e_reduire())
        self.pb_mt_agrandir.clicked.connect(lambda: self.evt.e_agrandir())
        self.pb_mt_quitter.clicked.connect(lambda: self.evt.e_cacher())

        self.conversion.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.conversion.customContextMenuRequested.connect(
            lambda pos, child=self.conversion: self.customMenuEvent(pos, child))

        self.conversion.cellChanged.connect(self.convert)

    def IN_ACT(self):

        self.threadpool = QtCore.QThreadPool()

    def IN_WG_BASE(self):
        pass

    # def IN_TRAY(self):
    #     ### Actions ###
    #     Functions.ADD_QACTION(
    #         self,
    #         tray=self.tray_menu,
    #         ico=Img().quitter(),
    #         ico_rgb="bn2",
    #         txt="Quitter",
    #         shortcut_txt="Shift+Esc",
    #         status_tip="Quitter",
    #         fct=self.e_quitter_tray,
    #         sht_1=Keys().shift(),
    #         sht_2=Keys().escape()
    #     )
    #
    #     # self.tray_menu.addSeparator()
    #
    #     self.tray.setContextMenu(self.tray_menu)
    #     self.tray.show()

    def INIT(self, *args):
        for fct in args:
            splash_screen.lb_chargement.setText(fct[1])
            splash_screen.pg_chargement.setValue(splash_screen.pg_chargement.value() + 100 / len(args))
            fct[0]()

        splash_screen.lb_chargement.setText("Lancement de l'application")
        splash_screen.pg_chargement.setValue(100)

    def convert(self, x: int, y: int):
        self.conversion.blockSignals(True)

        if y % 2:
            coordX = self.conversion.item(x, y - 1)
            coordY = self.conversion.item(x, y)
        else:
            coordX = self.conversion.item(x, y)
            coordY = self.conversion.item(x, y + 1)

        if coordX is not None and coordY is not None and coordX != "" and coordY != "":
            coordX = coordX.text().replace(",", ".")
            coordY = coordY.text().replace(",", ".")

            match y:
                case 0 | 1:
                    WcoordX, WcoordY = self.convertiseur.transform(de="2154", to="4326", coordX=coordX, coordY=coordY)
                    self.conversion.setItem(x, 2, QtWidgets.QTableWidgetItem(f"{WcoordX}"))
                    self.conversion.setItem(x, 3, QtWidgets.QTableWidgetItem(f"{WcoordY}"))

                    ScoordX, ScoordY = self.convertiseur.transform(de="2154", to="sexa", coordX=coordX, coordY=coordY)
                    self.conversion.setItem(x, 4, QtWidgets.QTableWidgetItem(f"{ScoordX}"))
                    self.conversion.setItem(x, 5, QtWidgets.QTableWidgetItem(f"{ScoordY}"))
                case 2 | 3:
                    LcoordX, LcoordY = self.convertiseur.transform(de="4326", to="2154", coordX=coordX, coordY=coordY)
                    self.conversion.setItem(x, 0, QtWidgets.QTableWidgetItem(f"{LcoordX}"))
                    self.conversion.setItem(x, 1, QtWidgets.QTableWidgetItem(f"{LcoordY}"))

                    ScoordX, ScoordY = self.convertiseur.transform(de="4326", to="sexa", coordX=coordX, coordY=coordY)
                    self.conversion.setItem(x, 4, QtWidgets.QTableWidgetItem(f"{ScoordX}"))
                    self.conversion.setItem(x, 5, QtWidgets.QTableWidgetItem(f"{ScoordY}"))
                case 4 | 5:
                    LcoordX, LcoordY = self.convertiseur.transform(de="sexa", to="2154", coordX=coordX, coordY=coordY)
                    self.conversion.setItem(x, 0, QtWidgets.QTableWidgetItem(f"{LcoordX}"))
                    self.conversion.setItem(x, 1, QtWidgets.QTableWidgetItem(f"{LcoordY}"))

                    WcoordX, WcoordY = self.convertiseur.transform(de="sexa", to="4326", coordX=coordX, coordY=coordY)
                    self.conversion.setItem(x, 2, QtWidgets.QTableWidgetItem(f"{WcoordX}"))
                    self.conversion.setItem(x, 3, QtWidgets.QTableWidgetItem(f"{WcoordY}"))

        self.conversion.blockSignals(False)

    def NotNull(self, value=None):
        return value != "" or value is not None

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

    def supprime_ligne(self, widget):
        rows = [index.row() for index in widget.selectedIndexes()]
        for row in reversed(rows):
            widget.removeRow(row)

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

    def delete_data(self, table):
        selected = table.selectedRanges()
        for row in range(selected[0].topRow(), selected[0].bottomRow() + 1):
            for col in range(selected[0].leftColumn(), selected[0].rightColumn() + 1):
                table.setItem(row, col, QtWidgets.QTableWidgetItem(""))

    def keyPressEvent(self, event):

        if self.conversion.hasFocus():
            if event.key() == QtCore.Qt.Key_C and (event.modifiers() & QtCore.Qt.ControlModifier):
                self.copier(table=self.conversion)

            elif event.key() == QtCore.Qt.Key_V and (event.modifiers() & QtCore.Qt.ControlModifier):
                self.coller(table=self.conversion)

            elif event.key() in [QtCore.Qt.Key_Delete, QtCore.Qt.Key_Backspace]:
                self.delete_data(table=self.conversion)

        event.accept()

    def e_resize_screen(self):

        if self.cfg["var"]["resize"]:
            self.setMinimumWidth(self.cfg["config"]["widht"])
            self.setMinimumHeight(self.cfg["config"]["height"])
        else:
            self.setFixedWidth(self.cfg["config"]["widht"])
            self.setFixedHeight(self.cfg["config"]["height"])

    #####
    def traySingleClick(self):
        screen = QtWidgets.QApplication.primaryScreen().availableGeometry()
        widget = toolBox.geometry()

        toolBox.open()
        toolBox.show()
        toolBox.activateWindow()

        toolBox.move(screen.width() - widget.width(), screen.height() - widget.height())

    def trayDoubleClick(self):
        self.timer_double_click.stop()
        self.show()
        fen.activateWindow()

        if fen.windowState() == QtCore.Qt.WindowMinimized:
            fen.setWindowState(QtCore.Qt.WindowActive)

    def trayActivate(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            self.timer_double_click.start(app.doubleClickInterval())

        elif reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.trayDoubleClick()

    def e_quitter(self):
        """Permet de quitter l'application"""
        if not Configue().cfg["var"]["auto_close"]:
            self.hide()
        elif ResponseBox().QUITTER():
            app.quit()

    def e_quitter_tray(self):
        self.show()
        fen.activateWindow()

        if fen.windowState() == QtCore.Qt.WindowMinimized:
            fen.setWindowState(QtCore.Qt.WindowActive)

        if ResponseBox().QUITTER():
            app.quit()

    #####
    def closeEvent(self, event):
        event.accept()
        app.quit()
    ###################
    ##    /EVENT     ##
    ###################


if __name__ == "__main__":
    Functions().GEN_SVG()

    app = QtWidgets.QApplication(sys.argv)
    splash_screen = SplashScreen()
    splash_screen.open()
    toolBox = ToolBoxUi()
    app.processEvents()

    fen = main()
    fen.show()

    sys.exit(app.exec())
