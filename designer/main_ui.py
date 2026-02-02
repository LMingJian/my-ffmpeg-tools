# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
from designer import main_rc

class Ui_VideoCoverApp(object):
    def setupUi(self, VideoCoverApp):
        if not VideoCoverApp.objectName():
            VideoCoverApp.setObjectName(u"VideoCoverApp")
        VideoCoverApp.resize(600, 340)
        VideoCoverApp.setMinimumSize(QSize(600, 340))
        VideoCoverApp.setMaximumSize(QSize(600, 340))
        icon = QIcon()
        icon.addFile(u":/logo/resource/LLCover.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        VideoCoverApp.setWindowIcon(icon)
        VideoCoverApp.setStyleSheet(u"QMainWindow { background-color: #f5f7fa; } QFrame { background-color: white; border-radius: 8px; padding: 15px; } QPushButton { background-color: #4f46e5; color: white; border: none; padding: 8px 16px; border-radius: 4px; font-weight: 500; } QPushButton:hover { background-color: #4338ca; } QPushButton:disabled { background-color: #c7d2fe; } \n"
"#image_label, #mp4_label { \n"
"	color: #374151;\n"
"	border: 1px solid;\n"
"}")
        self.centralwidget = QWidget(VideoCoverApp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setSpacing(20)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.main_layout.addWidget(self.title_label)

        self.file_selection_card = QFrame(self.centralwidget)
        self.file_selection_card.setObjectName(u"file_selection_card")
        self.file_selection_card.setStyleSheet(u"QFrame { box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }")
        self.file_selection_card.setFrameShape(QFrame.Shape.StyledPanel)
        self.card_layout = QVBoxLayout(self.file_selection_card)
        self.card_layout.setSpacing(15)
        self.card_layout.setObjectName(u"card_layout")
        self.image_file = QHBoxLayout()
        self.image_file.setObjectName(u"image_file")
        self.image_label = QLabel(self.file_selection_card)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setStyleSheet(u"")

        self.image_file.addWidget(self.image_label)

        self.image_btn = QPushButton(self.file_selection_card)
        self.image_btn.setObjectName(u"image_btn")
        self.image_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.image_btn.setProperty(u"fixedWidth", 120)

        self.image_file.addWidget(self.image_btn)


        self.card_layout.addLayout(self.image_file)

        self.mp4_file = QHBoxLayout()
        self.mp4_file.setObjectName(u"mp4_file")
        self.mp4_label = QLabel(self.file_selection_card)
        self.mp4_label.setObjectName(u"mp4_label")

        self.mp4_file.addWidget(self.mp4_label)

        self.mp4_btn = QPushButton(self.file_selection_card)
        self.mp4_btn.setObjectName(u"mp4_btn")
        self.mp4_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.mp4_btn.setStyleSheet(u"")
        self.mp4_btn.setProperty(u"fixedWidth", 120)

        self.mp4_file.addWidget(self.mp4_btn)


        self.card_layout.addLayout(self.mp4_file)


        self.main_layout.addWidget(self.file_selection_card)

        self.process_btn = QPushButton(self.centralwidget)
        self.process_btn.setObjectName(u"process_btn")
        self.process_btn.setEnabled(False)
        self.process_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.process_btn.setStyleSheet(u"font-size: 16px;")
        self.process_btn.setProperty(u"fixedHeight", 40)

        self.main_layout.addWidget(self.process_btn)

        VideoCoverApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(VideoCoverApp)

        QMetaObject.connectSlotsByName(VideoCoverApp)
    # setupUi

    def retranslateUi(self, VideoCoverApp):
        VideoCoverApp.setWindowTitle(QCoreApplication.translate("VideoCoverApp", u"\u89c6\u9891\u5c01\u9762\u8bbe\u7f6e\u5de5\u5177", None))
        self.title_label.setText(QCoreApplication.translate("VideoCoverApp", u"\u89c6\u9891\u5c01\u9762\u8bbe\u7f6e\u5de5\u5177", None))
        self.image_label.setText(QCoreApplication.translate("VideoCoverApp", u"\u56fe\u7247\u6587\u4ef6", None))
        self.image_btn.setText(QCoreApplication.translate("VideoCoverApp", u"\u9009\u62e9\u56fe\u7247", None))
        self.mp4_label.setText(QCoreApplication.translate("VideoCoverApp", u"\u89c6\u9891\u6587\u4ef6", None))
        self.mp4_btn.setText(QCoreApplication.translate("VideoCoverApp", u"\u9009\u62e9\u89c6\u9891\u6587\u4ef6", None))
        self.process_btn.setText(QCoreApplication.translate("VideoCoverApp", u"\u751f\u6210\u5e26\u5c01\u9762\u89c6\u9891", None))
    # retranslateUi

