# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ttc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from tic_tac_toe import Game


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        #
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 420)
        MainWindow.setMinimumSize(QtCore.QSize(370, 420))
        MainWindow.setMaximumSize(QtCore.QSize(370, 420))
        MainWindow.setToolTip("")
        MainWindow.setWindowIcon(QtGui.QIcon('materials/ttc_logo.png'))

        # adding tic_tac_toe instance
        self.ttt = Game()
        self.counter = 0

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(42, 250, 291, 91))
        self.textBrowser.setObjectName("textBrowser")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(70, 370, 211, 41))
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.textEdit.setAutoFillBackground(True)
        self.textEdit.setFrameShape(QtWidgets.QFrame.HLine)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setReadOnly(True)
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setObjectName("textEdit")

        self._add_buttons()
        self._add_lines()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def _add_buttons(self):
        """
            adding all 9 buttons, adding index for each of them , connecting all of them to _move function
                   and adding white background

            first number is row and the second is the column number
            ex) g11 means first row and first column

            the indices are from 0 to 8

        """
        self.g11 = QtWidgets.QPushButton(self.centralwidget)
        self.g11.setGeometry(QtCore.QRect(50, 50, 91, 61))
        self.g11.setText("")
        self.g11.setObjectName("g11")

        self.g21 = QtWidgets.QPushButton(self.centralwidget)
        self.g21.setGeometry(QtCore.QRect(50, 110, 91, 61))
        self.g21.setText("")
        self.g21.setObjectName("g21")

        self.g31 = QtWidgets.QPushButton(self.centralwidget)
        self.g31.setGeometry(QtCore.QRect(50, 170, 91, 61))
        self.g31.setText("")
        self.g31.setObjectName("g31")

        self.g12 = QtWidgets.QPushButton(self.centralwidget)
        self.g12.setGeometry(QtCore.QRect(140, 50, 91, 61))
        self.g12.setText("")
        self.g12.setObjectName("g12")

        self.g32 = QtWidgets.QPushButton(self.centralwidget)
        self.g32.setGeometry(QtCore.QRect(140, 170, 91, 61))
        self.g32.setText("")
        self.g32.setObjectName("g32")

        self.g22 = QtWidgets.QPushButton(self.centralwidget)
        self.g22.setGeometry(QtCore.QRect(140, 110, 91, 61))
        self.g22.setText("")
        self.g22.setObjectName("g22")

        self.g13 = QtWidgets.QPushButton(self.centralwidget)
        self.g13.setGeometry(QtCore.QRect(230, 50, 91, 61))
        self.g13.setText("")
        self.g13.setObjectName("g13")

        self.g23 = QtWidgets.QPushButton(self.centralwidget)
        self.g23.setGeometry(QtCore.QRect(230, 110, 91, 61))
        self.g23.setText("")
        self.g23.setObjectName("g23")

        self.g33 = QtWidgets.QPushButton(self.centralwidget)
        self.g33.setGeometry(QtCore.QRect(230, 170, 91, 61))
        self.g33.setText("")
        self.g33.setObjectName("g33")

        self.buttons = [self.g11, self.g12, self.g13, self.g21, self.g22, self.g23, self.g31, self.g32, self.g33]

        self.g11.index = 0
        self.g12.index = 1
        self.g13.index = 2

        self.g21.index = 3
        self.g22.index = 4
        self.g23.index = 5

        self.g31.index = 6
        self.g32.index = 7
        self.g33.index = 8

        self.g11.clicked.connect(lambda: self._move(self.g11))
        self.g12.clicked.connect(lambda: self._move(self.g12))
        self.g13.clicked.connect(lambda: self._move(self.g13))

        self.g21.clicked.connect(lambda: self._move(self.g21))
        self.g22.clicked.connect(lambda: self._move(self.g22))
        self.g23.clicked.connect(lambda: self._move(self.g23))

        self.g31.clicked.connect(lambda: self._move(self.g31))
        self.g32.clicked.connect(lambda: self._move(self.g32))
        self.g33.clicked.connect(lambda: self._move(self.g33))

        # # this code doesnt work as expected
        # for index, button in enumerate(self.buttons, 0):
        #     button.index = index
        #     button.clicked.connect(lambda: self._move_gui(button))

        # adding white background for all buttons
        for button in self.buttons:
            button.setStyleSheet("background-color : white")

    def _add_lines(self):
        """
        adds 2 vertical and 2 horizontal lines to separate buttons

            line and line2 are horizontal lines
            line3 and line4 are vertical lines
        """

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 100, 271, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(50, 160, 271, 20))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(130, 50, 20, 181))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")

        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(220, 50, 20, 181))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(5)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")

    def _move(self, button: QtWidgets.QPushButton):
        """
        if any buttons were clicked it will add the player sign to that button , disable the button
           and check for player win or draw

        :parameters
                    -button: QtWidgets.QPushButton
                             the corresponding button that was clicked

        adds the player sign to the corresponding button
        """

        # if counter is even player1 must play else player2
        player = self.ttt.player1 if self.counter % 2 == 0 else self.ttt.player2

        if player == self.ttt.player1:
            button.setStyleSheet('QPushButton {background-color: white; color: red; font-size: 15pt;}')
        else:
            button.setStyleSheet('QPushButton {background-color: white; color: blue; font-size: 15pt;}')

        # disable button after first touch
        button.setDisabled(True)

        # add player sign to the button
        self.ttt.grid.board[button.index] = player.sign
        button.setText(player.sign)
        self.ttt.grid.empty_places -= 1

        # checking for player win or draw
        self._check_positions()
        self.counter += 1

    def _check_positions(self):
        """
        checks the win or draw conditions

        adds the corresponding message to the textBrowser
        """
        # checks for player win
        if self.ttt.check_win():
            if self.counter % 2 == 0:
                self._write_player1_wins()
            else:
                self._write_player2_wins()

            # asking to play again or not
            self._add_dialog_buttons()

        # checks for draw
        if self.ttt.check_draw():
            self._write_draw()

            # asking to play again or not
            self._add_dialog_buttons()

    def _add_dialog_buttons(self):
        """
        asking the user to play again or no

        if yes it will clear last game result and grid signs
        if no it will close the application
        """
        # asking the user to play again or not
        button = QtWidgets.QMessageBox.question(self.centralwidget, 'Play Again', 'Play Another Game? ')
        if button == QtWidgets.QMessageBox.Yes:
            # clearing the winning part message
            self.clear_buttons()
        else:
            sys.exit(app.exec_())

    def clear_buttons(self):
        """it clears last game result and player signs from grid"""
        self.retranslateUi(MainWindow)
        self.ttt = Game()
        for button in self.buttons:
            button.setText('')
            button.setEnabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TicTacToe"))
        self.textBrowser.setHtml(_translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                "p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    player1: </span><span style=\" font-size:12pt; color:#ff0000;\">X</span><span style=\" font-size:12pt;\">        player2: </span><span style=\" font-size:12pt; color:#0000ff;\">O</span></p></body></html>"))

        self.textEdit.setHtml(_translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">AminJml81</span></p></body></html>"))

    def _write_player1_wins(self):
        """adds corresponding message to the textBrowser"""

        _translate = QtCore.QCoreApplication.translate
        self.textBrowser.setHtml(
            _translate("MainWindow", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    player1: </span><span style=\" font-size:12pt; color:#ff0000;\">X   </span><span style=\" font-size:12pt;\">   player2: </span><span style=\" font-size:12pt; color:#0000ff;\">O</span></p>\n"
                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ff0000;\">    </span></p>\n"
                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ff0000;\">       </span><span style=\" font-size:16pt; color:#ff0000;\">   player1 won</span></p></body></html>"))

    def _write_player2_wins(self):
        """adds corresponding message to the textBrowser"""

        _translate = QtCore.QCoreApplication.translate
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    player1: </span><span style=\" font-size:12pt; color:#ff0000;\">X   </span><span style=\" font-size:12pt;\">   player2: </span><span style=\" font-size:12pt; color:#0000ff;\">O</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ff0000;\">    </span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ff0000;\">       </span><span style=\" font-size:16pt; color:#0000ff;\">   player2 won</span></p></body></html>"))

    def _write_draw(self):
        """adds corresponding message to the textBrowser"""

        _translate = QtCore.QCoreApplication.translate
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">    player1: </span><span style=\" font-size:12pt; color:#ff0000;\">X   </span><span style=\" font-size:12pt;\">   player2: </span><span style=\" font-size:12pt; color:#0000ff;\">O</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; color:#ff0000;\">    </span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ff0000;\">                DR</span><span style=\" font-size:14pt; color:#0000ff;\">AW</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())