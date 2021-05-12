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
        self.removeTemplate.clicked.connect(self.remTemplate)
        
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
        self.button1Text.setText(data['buttons']['button1Text'])
        self.button2Text.setText(data['buttons']['button2text'])
        self.button1url.setText(data['buttons']['button1url'])
        self.button2url.setText(data['buttons']['button2url'])


                
    def closeEvent(self, event):
        if self.to_tray_check.isChecked():
            event.ignore()
            self.hide()
            self.tray_icon.showMessage(
                "Discord Presence",
                "Application was minimized to Tray",
                QIcon("icon.ico"),
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
            
        self.save()
        
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
                'end': self.end.text(),
                
                
                "buttons": { #button yes
                        "button1": str(self.button1check.isChecked()),
                        "button2": str(self.button2check.isChecked()),
                        "button1Text": self.button1Text.text(),
                        "button1url": self.button1url.text(),
                        "button2text": self.button2Text.text(),
                        "button2url": self.button2url.text()
                }
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
        self.button1Text.setText(data['buttons']['button1Text'])
        self.button1url.setText(data['buttons']['button1url'])
        self.button2Text.setText(data['buttons']['button2text'])
        self.button2url.setText(data['buttons']['button2url'])

    def newTemplate(self):
            QInputDialog.setStyleSheet(self, "background-color: green;")
            text, ok = QInputDialog.getText(self, 'input dialog', 'Create New Template')
            QInputDialog.setStyleSheet(self, "background-color: black;")
            if ok:
                f = open(f"./templates/{text}.json", 'w')
                f.writelines("""
{
        "client_id": 123456789,
        "small_image": "",
        "large_image_text": "",
        "large_image": "",
        "small_image_text": "",
        "state": "State",
        "details": "Details",
        "start": "",
        "end": "",
        "buttons":{     
                        "button1": "",
                        "button2": "",
                        "button1Text": "",
                        "button1url": "",
                        "button2text": "",
                        "button2url": ""
                }
        
}""")
                f.close()
                self.comboBox.addItem(text)
                self.comboBox.setCurrentText(text)      
                
    def remTemplate(self):
        if self.comboBox.currentText != "Main":
                try:
                        os.remove("./templates/" + self.comboBox.currentText() + ".json")
                except:
                        pass
                self.comboBox.clear()
                
                templates = []
                for filename in os.listdir("templates"):
                        if filename.endswith('.json'):
                                templates.append(filename[:-5])
                self.comboBox.addItems(templates)
                self.comboBox.addItem("Main")
          

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
                  
                        
                        my_presence = dict()

                        my_presence['state'] = data['state']
                        my_presence['large_image'] = data['large_image']
                        my_presence['large_text'] = data['large_image_text']
                        my_presence['small_image'] = data['small_image']
                        my_presence['small_text'] = data['small_image_text']
                        my_presence['details'] = data['details']
                        if not data['start']:
                                my_presence['start'] = data['start']
                        else:
                                my_presence['start'] = int(data['start'])
                        if not data['end']:
                                my_presence['end'] = data['end']
                        else:
                                my_presence['end'] = int(data['end'])
                                
                        if data['buttons']['button1'] == 'True' and data['buttons']['button2'] == 'True':
                                my_presence['buttons'] = [{'label': data['buttons']['button1Text'], 'url': data['buttons']['button1url']},
                                                          {'label': data['buttons']['button2text'], 'url': data['buttons']['button2url']}]
                                
                  
                        elif data['buttons']['button1'] == 'True':
                                my_presence['buttons'] = [{'label': data['buttons']['button1Text'], 'url': data['buttons']['button1url']}]
                                
                                
                        elif data['buttons']['button2'] == 'True':
                                my_presence['buttons'] = [{'label': data['buttons']['button2text'], 'url': data['buttons']['button2url']}]
                                

                        else:
                                my_presence['buttons'] = None
                         
                        rpc.update(**my_presence)
                         
                                # buttons=[{'label': data['buttons']['button1Text'], 'url': data['buttons']['button1url']},
                                #          {'label': data['buttons']['button2text'], 'url': data['buttons']['button2url']}])
                        time.sleep(5)
                        
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.ico'))
    window = Ui()
    app.exec_()