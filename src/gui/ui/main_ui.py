# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(1126, 642)
        self.vlay_main = QVBoxLayout(main)
        self.vlay_main.setSpacing(0)
        self.vlay_main.setObjectName(u"vlay_main")
        self.vlay_main.setContentsMargins(0, 0, 0, 0)
        self.fr_main = QFrame(main)
        self.fr_main.setObjectName(u"fr_main")
        self.fr_main.setFrameShape(QFrame.StyledPanel)
        self.fr_main.setFrameShadow(QFrame.Raised)
        self.vlay_fr_main = QVBoxLayout(self.fr_main)
        self.vlay_fr_main.setSpacing(0)
        self.vlay_fr_main.setObjectName(u"vlay_fr_main")
        self.vlay_fr_main.setContentsMargins(0, 0, 0, 0)
        self.fr_menu_top = QFrame(self.fr_main)
        self.fr_menu_top.setObjectName(u"fr_menu_top")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_menu_top.sizePolicy().hasHeightForWidth())
        self.fr_menu_top.setSizePolicy(sizePolicy)
        self.hlay_menu_top = QHBoxLayout(self.fr_menu_top)
        self.hlay_menu_top.setSpacing(0)
        self.hlay_menu_top.setObjectName(u"hlay_menu_top")
        self.hlay_menu_top.setContentsMargins(0, 0, 0, 0)
        self.lb_mt_ico = QLabel(self.fr_menu_top)
        self.lb_mt_ico.setObjectName(u"lb_mt_ico")

        self.hlay_menu_top.addWidget(self.lb_mt_ico)

        self.wg_mt_blank = QWidget(self.fr_menu_top)
        self.wg_mt_blank.setObjectName(u"wg_mt_blank")

        self.hlay_menu_top.addWidget(self.wg_mt_blank)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer_2)

        self.lb_mt_nom = QLabel(self.fr_menu_top)
        self.lb_mt_nom.setObjectName(u"lb_mt_nom")

        self.hlay_menu_top.addWidget(self.lb_mt_nom)

        self.horizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer_1)

        self.pb_mt_reduire = QPushButton(self.fr_menu_top)
        self.pb_mt_reduire.setObjectName(u"pb_mt_reduire")

        self.hlay_menu_top.addWidget(self.pb_mt_reduire)

        self.pb_mt_agrandir = QPushButton(self.fr_menu_top)
        self.pb_mt_agrandir.setObjectName(u"pb_mt_agrandir")

        self.hlay_menu_top.addWidget(self.pb_mt_agrandir)

        self.pb_mt_quitter = QPushButton(self.fr_menu_top)
        self.pb_mt_quitter.setObjectName(u"pb_mt_quitter")

        self.hlay_menu_top.addWidget(self.pb_mt_quitter)


        self.vlay_fr_main.addWidget(self.fr_menu_top)

        self.fr_body = QFrame(self.fr_main)
        self.fr_body.setObjectName(u"fr_body")
        self.fr_body.setFrameShape(QFrame.StyledPanel)
        self.fr_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.fr_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fr_menu_titre = QFrame(self.fr_body)
        self.fr_menu_titre.setObjectName(u"fr_menu_titre")
        self.fr_menu_titre.setFrameShape(QFrame.StyledPanel)
        self.fr_menu_titre.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fr_menu_titre)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.conversion = QTableWidget(self.fr_menu_titre)
        if (self.conversion.columnCount() < 6):
            self.conversion.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.conversion.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.conversion.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.conversion.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.conversion.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.conversion.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.conversion.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.conversion.rowCount() < 20):
            self.conversion.setRowCount(20)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(10, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(11, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(12, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(13, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(14, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(15, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(16, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(17, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(18, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.conversion.setVerticalHeaderItem(19, __qtablewidgetitem25)
        self.conversion.setObjectName(u"conversion")

        self.verticalLayout_2.addWidget(self.conversion)


        self.verticalLayout.addWidget(self.fr_menu_titre)


        self.vlay_fr_main.addWidget(self.fr_body)

        self.fr_menu_bottom = QFrame(self.fr_main)
        self.fr_menu_bottom.setObjectName(u"fr_menu_bottom")
        sizePolicy.setHeightForWidth(self.fr_menu_bottom.sizePolicy().hasHeightForWidth())
        self.fr_menu_bottom.setSizePolicy(sizePolicy)
        self.hlay_menu_bottom = QHBoxLayout(self.fr_menu_bottom)
        self.hlay_menu_bottom.setSpacing(0)
        self.hlay_menu_bottom.setObjectName(u"hlay_menu_bottom")
        self.hlay_menu_bottom.setContentsMargins(0, 0, 0, 0)
        self.lb_mb_version = QLabel(self.fr_menu_bottom)
        self.lb_mb_version.setObjectName(u"lb_mb_version")

        self.hlay_menu_bottom.addWidget(self.lb_mb_version)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_bottom.addItem(self.horizontalSpacer_4)


        self.vlay_fr_main.addWidget(self.fr_menu_bottom)


        self.vlay_main.addWidget(self.fr_main)


        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        ___qtablewidgetitem = self.conversion.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("main", u"Lambert 93 X", None));
        ___qtablewidgetitem1 = self.conversion.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("main", u"Lambert 93 Y", None));
        ___qtablewidgetitem2 = self.conversion.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("main", u"WGS84 X", None));
        ___qtablewidgetitem3 = self.conversion.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("main", u"WGS84 Y", None));
        ___qtablewidgetitem4 = self.conversion.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("main", u"WGS84 X SEXAGESIMAL", None));
        ___qtablewidgetitem5 = self.conversion.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("main", u"WGS84 Y SEXAGESIMAL", None));
        ___qtablewidgetitem6 = self.conversion.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("main", u"1", None));
        ___qtablewidgetitem7 = self.conversion.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("main", u"2", None));
        ___qtablewidgetitem8 = self.conversion.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("main", u"3", None));
        ___qtablewidgetitem9 = self.conversion.verticalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("main", u"4", None));
        ___qtablewidgetitem10 = self.conversion.verticalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("main", u"5", None));
        ___qtablewidgetitem11 = self.conversion.verticalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("main", u"6", None));
        ___qtablewidgetitem12 = self.conversion.verticalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("main", u"7", None));
        ___qtablewidgetitem13 = self.conversion.verticalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("main", u"8", None));
        ___qtablewidgetitem14 = self.conversion.verticalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("main", u"9", None));
        ___qtablewidgetitem15 = self.conversion.verticalHeaderItem(9)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("main", u"10", None));
        ___qtablewidgetitem16 = self.conversion.verticalHeaderItem(10)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("main", u"11", None));
        ___qtablewidgetitem17 = self.conversion.verticalHeaderItem(11)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("main", u"12", None));
        ___qtablewidgetitem18 = self.conversion.verticalHeaderItem(12)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("main", u"13", None));
        ___qtablewidgetitem19 = self.conversion.verticalHeaderItem(13)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("main", u"14", None));
        ___qtablewidgetitem20 = self.conversion.verticalHeaderItem(14)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("main", u"15", None));
        ___qtablewidgetitem21 = self.conversion.verticalHeaderItem(15)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("main", u"16", None));
        ___qtablewidgetitem22 = self.conversion.verticalHeaderItem(16)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("main", u"17", None));
        ___qtablewidgetitem23 = self.conversion.verticalHeaderItem(17)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("main", u"18", None));
        ___qtablewidgetitem24 = self.conversion.verticalHeaderItem(18)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("main", u"19", None));
        ___qtablewidgetitem25 = self.conversion.verticalHeaderItem(19)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("main", u"20", None));
        pass
    # retranslateUi

