# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Reconnaissancedesimages(object):
    def setupUi(self, Reconnaissancedesimages):
        Reconnaissancedesimages.setObjectName("Reconnaissancedesimages")
        Reconnaissancedesimages.resize(400, 333)
        self.pushButton = QtWidgets.QPushButton(Reconnaissancedesimages)
        self.pushButton.setGeometry(QtCore.QRect(120, 50, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Reconnaissancedesimages)
        self.label.setGeometry(QtCore.QRect(70, 10, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.imageLabel = QtWidgets.QLabel(Reconnaissancedesimages)
        self.imageLabel.setGeometry(QtCore.QRect(110, 100, 171, 131))
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.resultat = QtWidgets.QLabel(Reconnaissancedesimages)
        self.resultat.setGeometry(QtCore.QRect(80, 240, 231, 31))
        self.resultat.setText("")
        self.resultat.setObjectName("resultat")

        self.retranslateUi(Reconnaissancedesimages)
        QtCore.QMetaObject.connectSlotsByName(Reconnaissancedesimages)

    def retranslateUi(self, Reconnaissancedesimages):
        _translate = QtCore.QCoreApplication.translate
        Reconnaissancedesimages.setWindowTitle(_translate("Reconnaissancedesimages", "Dialog"))
        self.pushButton.setText(_translate("Reconnaissancedesimages", "Choisir une image"))
        self.label.setText(_translate("Reconnaissancedesimages", "Le Classifieur Neuronal PMC"))
