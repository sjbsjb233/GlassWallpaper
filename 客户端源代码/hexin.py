from sys import exit, argv, path

path.extend(('D:\work\exercise_py\sai\play', 'D:\work\exercise_py\sai\gui'))

from gui.luoji import MyMain
from play.main import Wallpaper, pretreatmentHandle
from qt_material import apply_stylesheet
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui.things import Get_page
import win32gui
from os import getcwd

#moxing
from datetime import datetime
import os
from random import randint
from time import sleep
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import json

import sip
# import gui.things as things
# import gui.get as get

from ctypes import cdll
from ctypes.wintypes import HWND, DWORD

from win32api import ShellExecute
from psutil import Process, pids
from PyQt5.QtWebEngineWidgets import QWebEngineView


#main.py
import os, time
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import win32gui
import cv2, json
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget

#get.py
import requests, base64,hashlib, cv2
import numpy as np
from PyQt5.QtGui import QImage

path = getcwd()
ziyuans = getcwd() + '\\ziyuans'  #资源的保存路径
# path = r'D:\work\exercise_py\sai\gui'
# ziyuans = r'D:\work\exercise_py\sai\ziyuans'  #资源的保存路径

app = QApplication(argv)


class Bizhi:

    def __init__(self) -> None:
        pretreatmentHandle()
        h = win32gui.FindWindow(("Progman"), ("Program Manager"))
        self.myWin = Wallpaper(h)
        self.myWin.show()


class Gui:

    def __init__(self) -> None:
        page_info = Get_page()  #工坊pic多线程
        self.myWin = MyMain(page_info)
        apply_stylesheet(app, theme='dark_teal.xml')
        self.myWin.show()


gui = Gui()
bizhi = Bizhi()
gui.myWin.mediaplayer = bizhi.myWin  #将播放器传入 gui


class SystemTrayIcon(QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)
        self.menu = QMenu(parent)

        # about action
        aboutAction = QAction("主页", self)
        aboutAction.triggered.connect(gui.myWin.show)
        self.menu.addAction(aboutAction)

        # quit action
        quitAction = QAction("退出", self)
        quitAction.triggered.connect(self.quit_fun)
        self.menu.addAction(quitAction)

        #
        self.setContextMenu(self.menu)

        # listen activated
        self.activated.connect(self.iconActivated)
        self.show()

    def about_fun(self):
        QMessageBox.about(self.parent(), "about", "pyqt system tray")

    def quit_fun(self):
        exit(0)

    def iconActivated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            print('left click: TODO')
            gui.myWin.show()


tubiao = SystemTrayIcon(QIcon(path + r'\pic\favicon.ico'))

exit(app.exec_())