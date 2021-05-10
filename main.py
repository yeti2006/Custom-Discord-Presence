from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon

import sys
import os
import json
import time
import webbrowser

import pypresence
import asyncio

        #nullify function to convert empty values to None
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

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('interface.ui', self)
        self.show()
        
            #Tray Menu and Tray CheckBox
    
        self.to_tray_check = self.findChild(QCheckBox, 'checkBox')
        self.to_tray_check.setChecked(True)
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(
            QIcon('icon.ico'))
        
        '''
        Define and add steps to work with the system tray icon
        show - show window
        hide - hide window
        exit - exit from application
        '''
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        
            #Buttons & Functions
        self.reloadButton.clicked.connect(self.reload)
        self.startButton.clicked.connect(self.presence)
        self.instructionsButton.clicked.connect(self.instruct)
        self.saveButton.clicked.connect(self.save)
        self.addNewTemplate.clicked.connect(self.newTemplate)
        
            #Console
        self.textBrowser = self.findChild(QTextBrowser, 'textBrowser')
        
            #template ComboBox
        self.comboBox = self.findChild(QComboBox, 'comboBox')
        
        templates = []
        for filename in os.listdir("templates"):
                if filename.endswith('.json'):
                        templates.append(filename[:-5])
        self.comboBox.addItems(templates)
        
        self.comboBox.activated.connect(lambda: self.template(filename=self.comboBox.currentText()))
        
            #Line Edit objects || Initialiazing last save
        with open('data.json') as f:
                data = json.load(f)
                nullify(data)
                
        self.clientID.setText(str(data['client_id']))
        self.largeImage.setText(data['large_image'])
        self.largeText.setText(data['large_image_text'])
        self.smallImage.setText(data['small_image'])
        self.smallText.setText(data['small_image_text'])
        self.state.setText(data['state'])
        self.details.setText(data['details'])
        self.start.setText(data['start'])
        self.end.setText(data['end'])
      
    def closeEvent(self, event):
        if self.to_tray_check.isChecked():
            event.ignore()
            self.hide()
            self.tray_icon.showMessage(
                "Custom Discord Presence",
                "Application was minimized to Tray",
                QSystemTrayIcon.Information,
                2000
            )

    def reload(self):
        
        def restart_program():
                """Restarts the current program.
                Note: this function does not return. Any cleanup action (like
                saving data) must be done before calling this function."""
                python = sys.executable
                os.execl(python, python, * sys.argv)

        restart_program()
        
    def presence(self):
            
        if self.comboBox.currentText() != "Main":
                file = "templates/" + self.comboBox.currentText() + ".json"
                
        else:
                file = "./data.json"
            
        with open(file) as f:
                data = json.load(f)
                nullify(data)
        self.save()
        self.textBrowser.clear()
        self.textBrowser.setHtml(
                f"""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"> 
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li  white-space: pre-wrap; 
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;"\>\n
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; color:#55ff00;">Hi :D I'll be your console so you can know what's going on</span></p>\n
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; color:#55ff00;">--------------</span></p>\n
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; color:#55ff00;"><br /></p>\n
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; color:#00FFFF;">Presence Status: Presence is displayed</span></p>\n
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; color:#55ff00;">    | presence_status Displaying</span></p>\n
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; color:#55ff00;"><br /></p>\n
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; color:#55ff00;">Details:</span></p>\n
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; color:#55ff00;">    | state: {data['state']}</span></p>\n
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; color:#55ff00;">    | details: {data['details']}</span></p>\n
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; color:#55ff00;"><br /></p>\n
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; color:#55ff00;">Images:</span></p>\n
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; color:#55ff00;">    | large image: {data['large_image']}</span></p>\n
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; color:#55ff00;">        | large image text: {data['large_image_text']}</span></p>\n
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; color:#55ff00;"><br /></p>\n
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; color:#55ff00;">    | small image: {data['small_image']}</span></p>\n
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; color:#55ff00;">        | small image text: {data['small_image_text']}</span></p>\n
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; color:#55ff00;"><br /></p>\n
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; color:#55ff00;">Timestamps:</span></p>\n
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; color:#55ff00;">    | start: {data['start']}</span></p>\n
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; color:#55ff00;">    | end: {data['end']}</span></p></body></html>"""
)
        self.worker = WorkerThread(options=self.comboBox.currentText())
        self.worker.start()
        
    def instruct(self):
        webbrowser.open_new_tab("https://github.com/yeti2006/custom_discord_presence/blob/main/README.md#custom-discord-rpc")

    def save(self):
        
        if self.comboBox.currentText() != "Main":
                file = "templates/" + self.comboBox.currentText() + ".json"
                
        else:
                file = "./data.json"
        
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
        
  
        with open(file, 'w') as file:
                json.dump(data, file, indent=4, sort_keys=False) 
                
    def template(self, filename):
        if self.comboBox.currentText() != "Main":
                file = "templates/" + self.comboBox.currentText() + ".json"
                
        else:
                file = "./data.json"    
        
        with open(file) as f:
                data = json.load(f)
                
        self.clientID.setText(str(data['client_id']))
        self.largeImage.setText(data['large_image'])
        self.largeText.setText(data['large_image_text'])
        self.smallImage.setText(data['small_image'])
        self.smallText.setText(data['small_image_text'])
        self.state.setText(data['state'])
        self.details.setText(data['details'])
        self.start.setText(data['start'])
        self.end.setText(data['end'])

    def newTemplate(self):
            text, ok = QInputDialog.getText(self, 'input dialog', 'Create New Template')
            if ok:
                f = open(f"./templates/{text}.json", 'w')
                f.writelines("""
{
        "client_id": 123456789,
        "small_image": "",
        "large_image_text": "example",
        "large_image": "large",
        "small_image_text": "",
        "state": "State",
        "details": "Details",
        "start": "1620206474",
        "end": ""
}""")
                f.close()
                self.comboBox.addItem(text)        

class WorkerThread(QThread):
        def __init__(self, options):
                super().__init__()
                self.options = options
                
        def run(self):
                
                if self.options != "Main":
                        file = "templates/" + self.options + ".json"
                        print(self.options)
                
                else:
                        file = "./data.json"
                                        
                with open(file) as f:
                        data = json.load(f)
                        nullify(data)
                        
                loop = asyncio.new_event_loop()
                rpc = pypresence.Presence(client_id=data['client_id'], loop=loop)
                rpc.connect()
                print("Presence connected")
                        
                while True:
                        rpc.update(state=data['state'],
                                large_image=data['large_image'],
                                large_text=data['large_image_text'],
                                small_image=data['small_image'],
                                small_text=data['small_image_text'],
                                details=data['details'],
                                start=data['start'],
                                end=data['end'])
                        time.sleep(5)
                        
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.ico'))
    window = Ui()
    app.exec_()