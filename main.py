from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon
import json
import asyncio
import pypresence
import webbrowser
import os
import markdown

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(598, 371)
        MainWindow.setStyleSheet("background-color: rgb(38, 38, 38);")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, -20, 481, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(0, 255, 255);")
        self.label.setObjectName("label")
        self.instructionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.instructionsButton.setGeometry(QtCore.QRect(460, 30, 75, 23))
        self.instructionsButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.instructionsButton.setObjectName("instructionsButton")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(460, 70, 75, 23))
        self.startButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(85, 255, 127);")
        self.startButton.setObjectName("startButton")
#         self.stopButton = QtWidgets.QPushButton(self.centralwidget)
#         self.stopButton.setGeometry(QtCore.QRect(460, 110, 75, 23))
#         self.stopButton.setStyleSheet("color: rgb(0, 0, 0);\n"
# "background-color: rgb(255, 0, 0);")
#        self.stopButton.setObjectName("stopButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 50, 118, 3))
        self.line.setStyleSheet("color: rgb(85, 255, 0);\n"
"background-color: rgb(85, 255, 127);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.clientID = QtWidgets.QLineEdit(self.centralwidget)
        self.clientID.setGeometry(QtCore.QRect(10, 100, 111, 21))
        self.clientID.setStyleSheet("background-color: rgb(255, 85, 127);")
        self.clientID.setObjectName("clientID")
        self.smallImage = QtWidgets.QLineEdit(self.centralwidget)
        self.smallImage.setGeometry(QtCore.QRect(10, 210, 111, 21))
        self.smallImage.setStyleSheet("background-color: rgb(255, 227, 192);")
        self.smallImage.setObjectName("smallImage")
        self.largeText = QtWidgets.QLineEdit(self.centralwidget)
        self.largeText.setGeometry(QtCore.QRect(10, 180, 111, 21))
        self.largeText.setStyleSheet("background-color: rgb(255, 227, 192);")
        self.largeText.setObjectName("largeText")
        self.largeImage = QtWidgets.QLineEdit(self.centralwidget)
        self.largeImage.setGeometry(QtCore.QRect(10, 150, 111, 21))
        self.largeImage.setStyleSheet("background-color: rgb(255, 227, 192);")
        self.largeImage.setObjectName("largeImage")
        self.smallText = QtWidgets.QLineEdit(self.centralwidget)
        self.smallText.setGeometry(QtCore.QRect(10, 240, 111, 21))
        self.smallText.setStyleSheet("background-color: rgb(255, 227, 192);")
        self.smallText.setObjectName("smallText")
        self.end = QtWidgets.QLineEdit(self.centralwidget)
        self.end.setGeometry(QtCore.QRect(10, 330, 111, 21))
        self.end.setStyleSheet("background-color: rgb(255, 227, 192);")
        self.end.setObjectName("end")
        self.start = QtWidgets.QLineEdit(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(10, 300, 111, 21))
        self.start.setStyleSheet("background-color: rgb(255, 227, 192);")
        self.start.setObjectName("start")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 100, 141, 16))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 85, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 150, 131, 16))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 85, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 180, 131, 16))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 85, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 210, 131, 16))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 85, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 240, 131, 16))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 85, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 280, 141, 16))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 85, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(130, 300, 131, 16))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 85, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(130, 330, 131, 16))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 85, 255);")
        self.label_9.setObjectName("label_9")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(410, 160, 171, 161))
        self.textBrowser.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.textBrowser.setObjectName("textBrowser")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(360, 210, 51, 16))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 85, 255);")
        self.label_10.setObjectName("label_10")
        self.state = QtWidgets.QLineEdit(self.centralwidget)
        self.state.setGeometry(QtCore.QRect(240, 180, 111, 21))
        self.state.setStyleSheet("background-color: rgb(255, 227, 192);")
        self.state.setObjectName("state")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(360, 180, 41, 16))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 85, 255);")
        self.label_11.setObjectName("label_11")
        self.details = QtWidgets.QLineEdit(self.centralwidget)
        self.details.setGeometry(QtCore.QRect(240, 210, 111, 21))
        self.details.setStyleSheet("background-color: rgb(255, 227, 192);")
        self.details.setObjectName("details")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 598, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.startButton.clicked.connect(self.dump)
#         self.stopButton.clicked.connect(self.stop)
        self.instructionsButton.clicked.connect(self.instruct)
#     def stop(self):
#         with open('./data.json') as f:
#                 data = json.load(f)
            
#         self.MainWindow.exit()

    def instruct(self):
        webbrowser.open_new_tab("https://github.com/yeti2006/custom_discord_presence/blob/main/README.md")

    def dump(self):
        data = {
                'client_id': int(self.clientID.text()),
                
                'small_image': self.smallImage.text(),
                'large_image_text': self.largeText.text(),
                'large_image': self.largeImage.text(),
                'small_image_text': self.smallText.text(),
                
                'state': self.state.text(),
                'details': self.details.text(),
                
                'start': self.start.text(),
                'end': self.end.text()
        }
  
        with open("./data.json", 'w') as file:
                json.dump(data, file, indent=4, sort_keys=False)
        self.presence()
                
    def presence(self):
        self.worker = WorkerThread()
        self.worker.start()
        
    def load_json(self, thing=None):
        def nullify(container) :
                for key in container:
                        if type(key) == list:
                                nullify(key)
                        elif type(key) == dict:
                                nullify(key)
                        elif type(container[key]) == dict or type(container[key]) == list:
                                nullify(container[key])
                        elif container[key] == '':
                                container[key] = None
        with open('./data.json') as f:
                data = json.load(f)
        return data[thing]
                


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "You're Awesome <3"))
        MainWindow.setWindowIcon(QIcon("./icon.ico"))
        self.label.setText(_translate("MainWindow", "Custom Discord Rich Presence 😎"))
        self.instructionsButton.setText(_translate("MainWindow", "Instructions"))
        self.startButton.setText(_translate("MainWindow", "Start Presence"))
  #      self.stopButton.setText(_translate("MainWindow", "Stop Presence")) 
        self.clientID.setText(_translate("MainWindow", str(self.load_json('client_id'))))
        self.smallImage.setText(_translate("MainWindow", str(self.load_json('small_image'))))
        self.largeText.setText(_translate("MainWindow", str(self.load_json('large_image_text'))))
        self.largeImage.setText(_translate("MainWindow", str(self.load_json('large_image'))))
        self.smallText.setText(_translate("MainWindow", str(self.load_json('small_image_text'))))
        self.end.setText(_translate("MainWindow", str(self.load_json('end'))))
        self.start.setText(_translate("MainWindow", str(self.load_json('start'))))
        self.label_2.setText(_translate("MainWindow", "Client ID *(Required)"))
        self.label_3.setText(_translate("MainWindow", "Large Image Name"))
        self.label_4.setText(_translate("MainWindow", "Large Image Text"))
        self.label_5.setText(_translate("MainWindow", "Small Image Name"))
        self.label_6.setText(_translate("MainWindow", "Small Image Text"))
        self.label_7.setText(_translate("MainWindow", "Timestamps"))
        self.label_8.setText(_translate("MainWindow", "#Start"))
        self.label_9.setText(_translate("MainWindow", "#End"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#55ff7f;\">Hey there ;)</span></p></p>\n<span style=\" color:#55ff7f;\">Click on Instructions for instructions. </span></p></p>\n<span style=\" color:#55ff7f;\">If you have entered everything correctly, clicking Start Presence would display your presence </span></p></body></p>\n<span style=\" color:#55ff7f;\">If something is wrong however, the app will close itself. Enter everything as per stated in the manual. </span></p></p>\n<span style=\" color:#55ff7f;\">Also, if you don't see your images in your presence, give it some time... It takes time to upload those images to discord (don't blame me)</span></p></html>"))
        self.label_10.setText(_translate("MainWindow", "Details*"))
        self.state.setText(_translate("MainWindow", "State"))
        self.label_11.setText(_translate("MainWindow", "State*"))
        self.details.setText(_translate("MainWindow", "Details"))

class WorkerThread(QThread):
        def run(self):
                def nullify(container) :
                        for key in container:
                                if type(key) == list:
                                        nullify(key)
                                elif type(key) == dict:
                                        nullify(key)
                                elif type(container[key]) == dict or type(container[key]) == list:
                                        nullify(container[key])
                                elif container[key] == '':
                                        container[key] = None
                                        
                with open("./data.json") as f:
                        data = json.load(f)
                        nullify(data)
                        
                
                loop = asyncio.new_event_loop()
                rpc = pypresence.Presence(client_id=data['client_id'], loop=loop)
                rpc.connect()
                while True:
                        rpc.update(state=data['state'],
                                large_image=data['large_image'],
                                large_text=data['large_image_text'],
                                small_image=data['small_image'],
                                small_text=data['small_image_text'],
                                details=data['details'],
                                start=data['start'],
                                end=data['end'])
                        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
