from datetime import datetime
import os
from random import randint
import re
from time import sleep
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import json
import get

import sip
# import gui.things as things
# import gui.get as get

from ctypes import cdll
from ctypes.wintypes import HWND, DWORD

from win32api import ShellExecute
from psutil import Process, pids

path = os.getcwd()
ziyuans = os.getcwd() + '\\ziyuans'  #资源的保存路径
# path = r'D:\work\exercise_py\sai\gui'
# ziyuans = r'D:\work\exercise_py\sai\ziyuans'  #资源的保存路径


def search(name):  #查找进程是否存在
    try:
        pids_1 = pids()
        for pid in pids_1:
            if Process(pid).name() == name:
                return True
        return False
    except:
        True


#pic模型
class Pic(QWidget):

    def __init__(self, Form):
        super().__init__(Form)
        self.setObjectName(u"gf_1")
        self.setGeometry(QRect(165, 145, 200, 200))
        self.setStyleSheet('')
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(200)
        sizePolicy1.setVerticalStretch(200)
        sizePolicy1.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy1)
        self.setMinimumSize(QSize(200, 200))
        self.setMaximumSize(QSize(200, 200))
        self.setSizeIncrement(QSize(0, 0))
        self.gf_text = QLabel(self)
        self.gf_text.setObjectName(u"gf_text")
        self.gf_text.setGeometry(QRect(0, 160, 200, 40))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(20)
        sizePolicy2.setHeightForWidth(
            self.gf_text.sizePolicy().hasHeightForWidth())
        self.gf_text.setSizePolicy(sizePolicy2)
        self.gf_text.setStyleSheet(u"background:rgba(47, 53, 66,.4);\n"
                                   "color:#ffffff")
        self.gf_text.setAlignment(Qt.AlignCenter)
        self.gf_pic = QLabel(self)
        self.gf_pic.setObjectName(u"gf_pic")
        self.gf_pic.setGeometry(QRect(0, 0, 200, 200))
        self.gf_pic.raise_()
        self.gf_text.raise_()
        self.gf_text.setText(QCoreApplication.translate("Form", u" ", None))

        self.setStyleSheet(
            r'QWidget:hover{border:3px solid #3498db !important;}')

        self.mainwin = Form  #主窗口

        #本地部分
        self.sudu = 100
        self.duiqi = 'fugai'
        self.zuoyou = 50
        self.liangdu = 50
        self.duibidu = 50
        self.baohedu = 50
        self.sediaopianyi = 50
        self.juedui = None
        self.id_1 = None  #网络id
        self.id_2 = None  #本地id
        self.title = None
        self.zuozhe = None
        self.fenlei = None
        self.fenbianlv = None
        self.size_1 = None
        self.format = None
        self.time = None
        self.user_id = None
        self.pingfen = None
        self.love_num = None
        self.way = None
        self.liulan = None
        self.isload = False  #是否为本地资源

    def mousePressEvent(self, event):
        self.mainwin.load_right(self)
        pass

    def play(self):
        pass

    def reset(self):
        '''重置'''
        self.sudu = 100
        self.duiqi = 'fugai'
        self.zuoyou = 50
        self.liangdu = 50
        self.duibidu = 50
        self.baohedu = 50
        self.sediaopianyi = 50
        self.juedui = None
        self.id_1 = None  #网络id
        self.id_2 = None  #本地id
        self.title = None
        self.zuozhe = None
        self.fenlei = None
        self.fenbianlv = None
        self.size_1 = None
        self.format = None
        self.time = None
        self.user_id = None
        self.pingfen = None
        self.love_num = None
        self.way = None
        self.liulan = None
        self.isload = False  #是否为本地资源
        self.gf_text.setText(QCoreApplication.translate("Form", u" ", None))
        self.gf_pic.setPixmap(QPixmap(''))


class warm(QWidget):
    '''警告框'''

    def __init__(self, text, okthing, quxiaothing):
        super().__init__()
        self.resize(481, 278)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                            QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                              QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                              QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addWidget(self.widget)

        QMetaObject.connectSlotsByName(self)

        self.setWindowTitle(QCoreApplication.translate("Form", u"警告", None))

        self.label.setText(text)
        self.pushButton.setText(
            QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("Form", u"\u53d6\u6d88", None))
        self.pushButton.clicked.connect(lambda: self.zhixing(okthing))
        self.pushButton_2.clicked.connect(lambda: self.zhixing(quxiaothing))

        self.show()

    def zhixing(self, things):
        things()
        self.destroy()


class Bofang_s(QWidget):
    '''播放列表的模型'''

    def __init__(self, Form, guanlian):
        super().__init__(Form)
        self.setObjectName(u"widget")
        self.setGeometry(QRect(120, 70, 80, 80))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(80)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(80, 80))
        self.setMaximumSize(QSize(80, 80))
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 80, 80))
        self.label.setScaledContents(True)
        self.guanlian = guanlian

    def mousePressEvent(self, event):
        self.guanlian.mousePressEvent(None)


class WebView(QWidget):  #用于spade的画板

    def __init__(self, url, mainwin, mods):
        super().__init__()
        self.mainwin = mainwin
        self.mods = mods
        self.resize(1400, 855)
        self.qwebengine = QWebEngineView(self)
        self.qwebengine.load(QUrl(url))
        # self.qwebengine.load(QUrl(r"http://127.0.0.1:50000/"))

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.qwebengine)

        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                            QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.clicked.connect(self.save_pic)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                              QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addWidget(self.widget_2)

        self.setWindowTitle(
            QCoreApplication.translate(
                "Form", u"Glass 风景图生成器 基于Semantic Image Synthesis with SPADE",
                None))
        self.pushButton.setText(
            QCoreApplication.translate("Form",
                                       u"\u6dfb\u52a0\u5230 Glass Wallpaper",
                                       None))

    def closeEvent(self, event):
        os.system('c:\windows\system32\\taskkill /F /IM %s' % 'gangan.exe')
        event.accept()

    def save_pic(self):
        file_name = str(randint(100000, 9999999999)) + '.png'
        os.system(
            'copy "%s" "%s"' %
            (self.mods.main_path + '\\1.png', ziyuans + '\\' + file_name))
        way = (ziyuans + '\\' + file_name).replace('\\', '/')

        with open(path + '\\load.json', encoding='utf8') as f:
            info = json.loads(f.read())
        info['load'].append({
            "sudu": 100,
            "duiqi": "fugai",
            "zuoyou": 50,
            "liangdu": 50,
            "duibidu": 50,
            "baohedu": 50,
            "sediaopianyi": 50,
            "juedui": 0,
            "id_1": -1,
            "id_2": info['load'][-1]['id_2'] + 1,
            "title": u"风景生成器",
            "zuozhe": u"风景生成器",
            "fenlei": "None",
            "fenbianlv": "10244",
            "size_1": -1,
            "format": "pic",
            "time": str(datetime.now()),
            "user_id": 1,
            "pingfen": 3,
            "love_num": 0,
            "way": way,
            "liulan": way
        })
        with open(path + '\\load.json', 'w', encoding='utf8') as f:
            f.write(json.dumps(info))
        for a in self.mainwin.pic_list_local:
            self.mainwin.gridLayout_8.removeWidget(a)
            sip.delete(a)
        self.mainwin.load_bendi()


class Star(QLabel):  #评价窗口星标类

    def __init__(self, Form, score, main):
        self.main = main  #打分主窗口
        self.score = score
        super().__init__(Form)

    def mousePressEvent(self, e):  # 单击
        self.main.choose_score = self.score
        self.main.set_score(self.score)
        self.main.pushButton.setText(
            QCoreApplication.translate("Form", "提交 %s'" % self.score, None))

    def leaveEvent(self, e):  # 鼠标离开label
        self.main.set_score(self.main.choose_score)

    def enterEvent(self, e):  # 鼠标移入label
        self.main.set_score(self.score)


class Set_scroe(QWidget):
    '''资源打分窗口'''

    def __init__(self, main):
        self.main = main

        super().__init__()
        self.resize(447, 300)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(330, 200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 35))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                              QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_1 = Star(self.widget_3, 1, self)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(20, 20))
        self.label_1.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.label_1)

        self.label_2 = Star(self.widget_3, 2, self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(20, 20))
        self.label_2.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = Star(self.widget_3, 3, self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(20, 20))
        self.label_3.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_4 = Star(self.widget_3, 4, self)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(20, 20))
        self.label_4.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_5 = Star(self.widget_3, 5, self)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(20, 20))
        self.label_5.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.label_5)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                               QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_30)

        self.verticalLayout.addWidget(self.widget_3)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.pushButton.setText(
            QCoreApplication.translate("Form", u"提交 1'", None))

        #设置空星图标
        self.half_star = QPixmap('%s\\pic\\half_star.png' % path)
        self.full_star = QPixmap('%s\\pic\\full_star.png' % path)
        self.less_star = QPixmap('%s\\pic\\less_star.png' % path)
        self.label_1.setPixmap(self.full_star)
        self.label_1.setScaledContents(True)
        self.label_2.setPixmap(self.less_star)
        self.label_2.setScaledContents(True)
        self.label_3.setPixmap(self.less_star)
        self.label_3.setScaledContents(True)
        self.label_4.setPixmap(self.less_star)
        self.label_4.setScaledContents(True)
        self.label_5.setPixmap(self.less_star)
        self.label_5.setScaledContents(True)

    def show(self):
        self.title = self.main.right_now.title
        self.id_1 = self.main.right_now.id_1  #资源网络id
        self.setWindowTitle(
            QCoreApplication.translate(
                "Form", '为此 %s 评分 (id:%s)' % (self.title, self.id_1), None))

        self.label.setText('为此 %s 评分 (id:%s)' % (self.title, self.id_1))
        self.pushButton.clicked.connect(self.submit)
        self.pushButton.setEnabled(True)

        if self.id_1 == -1:  #是否为本地
            self.label.setText('你不能对本地资源进行评分!')
            self.setWindowTitle(
                QCoreApplication.translate("Form", u'你不能对本地资源进行评分!', None))
            self.pushButton.setEnabled(False)

        #相关分数的定义
        self.choose_score = 1  #已选择的分数

        super().show()

    def set_score(self, score):  #改变分数
        #清空操作
        self.label_1.setPixmap(self.full_star)
        self.label_2.setPixmap(self.less_star)
        self.label_3.setPixmap(self.less_star)
        self.label_4.setPixmap(self.less_star)
        self.label_5.setPixmap(self.less_star)

        self.choose_score = score
        zhizhen = 0
        for a in (self.label_1, self.label_2, self.label_3, self.label_4,
                  self.label_5):
            if zhizhen == score:
                break
            else:
                a.setPixmap(self.full_star)
                zhizhen += 1

    def submit(self):
        '''提交评分'''
        status, info = get.set_score(self.choose_score, self.id_1)
        if status:
            warm('打分成功', self.close, self.close)
        else:
            warm('打分失败,原因: %s' % info, self.close, self.close)


class News_view(QWidget):  #显示Glass新闻

    def __init__(self):
        super().__init__()
        self.resize(650, 550)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout.addWidget(self.groupBox)

        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(530, 20, QSizePolicy.Expanding,
                                            QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.verticalLayout.addWidget(self.widget)

        self.setWindowTitle(
            QCoreApplication.translate("Form", u"Glass - 新闻", None))
        self.groupBox.setTitle(
            QCoreApplication.translate("Form", u"Glass - \u65b0\u95fb", None))
        self.pushButton.setText(
            QCoreApplication.translate("Form", u"\u5173\u95ed", None))

        self.pushButton.clicked.connect(self.close)

        self.qwebengine = QWebEngineView(self)
        # self.qwebengine.load(QUrl('https://www.baidu.com'))  #测试
        self.qwebengine.load(QUrl('%s/static/news' % get._yuming))
        self.horizontalLayout_2.addWidget(self.qwebengine)

    def mouseMoveEvent(self, e: QMouseEvent):
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None


def yakeli(a):
    hWnd = HWND(int(a.winId()))  # 直接HWND(self.winId())会报错
    gradientColor = DWORD(0x30F2F2F2)  # 设置和亚克力效果相叠加的背景颜色
    cdll.LoadLibrary(r'win_acrylic\acrylic_dll\acrylic.dll').setBlur(
        hWnd, gradientColor)


class Mods(QWidget):

    def __init__(self, Form, instruction, Control_description, launcher, name):
        super().__init__(Form)
        self.mainwin = Form
        self.launcher = path + launcher  #相对路径
        self.setObjectName(u"widget")
        self.setGeometry(QRect(300, 80, 280, 50))
        self.setMinimumSize(QSize(0, 50))
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding,
                                            QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.label.setText(
            QCoreApplication.translate("Form", u"%s" % instruction, None))
        self.pushButton.setText(
            QCoreApplication.translate("Form", u"%s" % Control_description,
                                       None))
        if name == 'cartoon':
            self.pushButton.clicked.connect(self.cartoon_pic)
        if name == 'cartoon_vid':
            self.pushButton.clicked.connect(self.cartoon_vid)
        if name == 'head_anime':
            self.pushButton.clicked.connect(self.head_anime)
        if name == 'gangan':
            self.pushButton.clicked.connect(self.gangan)
        if name == 'realesrgan':
            self.pushButton.clicked.connect(self.realesrgan)
        if name == 'realcugan':
            self.pushButton.clicked.connect(self.realcugan)
        if name == 'realcugan_vid':
            self.pushButton.clicked.connect(self.realcugan_vid)

    def cartoon_pic(self):
        '''普通图片变为动漫'''
        if self.mainwin.right_now and self.mainwin.right_now.format == 'pic':
            # argv = (None, str(self.mainwin.right_now), path + '\load.json',
            #         self.launcher, ziyuans)
            self.pushButton.setEnabled(False)
            self.pushButton.setText(
                QCoreApplication.translate("Form", u"正在转换", None))
            json_path = path + '\\load.json'
            id_2 = str(self.mainwin.right_now.id_2)
            main_path = self.launcher.replace('/', '\\')
            print(main_path)

            with open(json_path, encoding='utf8') as f:
                info = json.loads(f.read())

            for xinxi in info['load']:
                # print(xinxi['id_2'],id_2)
                if str(xinxi['id_2']) == id_2:
                    if xinxi['juedui']:
                        lujin = path + xinxi['juedui']
                    else:
                        lujin = xinxi['way']
                    format = xinxi['format']
                    break
            #目标文件地址
            file_name = lujin.split('/')[-1]
            mubiao_file_path = '%s\\test_pic\\%s' % (main_path, file_name)
            print(file_name, mubiao_file_path, lujin)
            #复制文件
            os.system(('copy "%s" "%s"' %
                       (lujin.replace('/', '\\'), mubiao_file_path)))

            aa = ShellExecute(
                0, 'open', '%s\\test.exe' % main_path,
                r'--checkpoint_dir checkpoint/generator_Hayao_weight --test_dir test_pic --style_name H',
                main_path, 1)

            print('111')

            # sleep(5)
            while search('test.exe'):
                # print(2)
                sleep(3)

            print(mubiao_file_path)
            if os.path.exists('%s\\results\\H\\%s' % (main_path, file_name)):

                if os.path.exists(ziyuans + '\\' + file_name):  #检查是否已经存在防止重名
                    os.system(
                        'copy "%s" "%s"' %
                        ('%s\\results\\H\\%s' %
                         (main_path, file_name), ziyuans + '\\1' + file_name))
                    way = (ziyuans + '\\1' + file_name).replace('\\', '/')
                else:
                    os.system(
                        'copy "%s" "%s"' %
                        ('%s\\results\\H\\%s' %
                         (main_path, file_name), ziyuans + '\\' + file_name))
                    way = (ziyuans + '\\' + file_name).replace('\\', '/')
                with open(json_path, encoding='utf8') as f:
                    info = json.loads(f.read())

                info['load'].append({
                    "sudu": 100,
                    "duiqi": "fugai",
                    "zuoyou": 50,
                    "liangdu": 50,
                    "duibidu": 50,
                    "baohedu": 50,
                    "sediaopianyi": 50,
                    "juedui": 0,
                    "id_1": -1,
                    "id_2": info['load'][-1]['id_2'] + 1,
                    "title": u"动漫转换器",
                    "zuozhe": u"动漫转换器",
                    "fenlei": "None",
                    "fenbianlv": "10244",
                    "size_1": -1,
                    "format": "pic",
                    "time": str(datetime.now()),
                    "user_id": 1,
                    "pingfen": 3,
                    "love_num": 0,
                    "way": way,
                    "liulan": way
                })
                with open(json_path, 'w', encoding='utf8') as f:
                    f.write(json.dumps(info))
                os.remove('%s\\results\\H\\%s' % (main_path, file_name))
                os.remove(mubiao_file_path)
            self.pushButton.setEnabled(True)
            self.pushButton.setText(
                QCoreApplication.translate("Form", u"转换", None))
            for a in self.mainwin.pic_list_local:
                self.mainwin.gridLayout_8.removeWidget(a)
                sip.delete(a)
            self.mainwin.load_bendi()

        else:
            print('have not')

    def cartoon_vid(self):
        '''把视频转化为动漫'''
        if self.mainwin.right_now and self.mainwin.right_now.format == 'vid':
            self.pushButton.setEnabled(False)
            self.pushButton.setText(
                QCoreApplication.translate("Form", u"正在转换", None))
            json_path = path + '\\load.json'
            id_2 = str(self.mainwin.right_now.id_2)
            main_path = self.launcher.replace('/', '\\')
            print(main_path)

            with open(json_path, encoding='utf8') as f:
                info = json.loads(f.read())

            for xinxi in info['load']:
                # print(xinxi['id_2'],id_2)
                if str(xinxi['id_2']) == id_2:
                    if xinxi['juedui']:
                        lujin = path + xinxi['juedui']
                    else:
                        lujin = xinxi['way']
                    format = xinxi['format']
                    break
            #目标文件地址
            file_name = lujin.split('/')[-1]
            mubiao_file_path = '%s\\video\\input\\%s' % (main_path, file_name)
            print(file_name, mubiao_file_path, lujin)
            #复制文件
            os.system(('copy "%s" "%s"' %
                       (lujin.replace('/', '\\'), mubiao_file_path)))

            aa = ShellExecute(
                0, 'open', '%s\\video2anime.exe' % main_path,
                '--video video/input/%s --checkpoint_dir checkpoint/generator_Hayao_weight --output video/output'
                % file_name, main_path, 1)

            print('111')

            # sleep(5)
            while search('video2anime.exe'):
                # print(2)
                sleep(3)

            print(mubiao_file_path)
            if os.path.exists('%s\\video\output\\%s' % (main_path, file_name)):
                if os.path.exists(ziyuans + '\\' + file_name):  #防止名字重复
                    os.system(
                        'copy "%s" "%s"' %
                        ('%s\\video\output\\%s' %
                         (main_path, file_name), ziyuans + '\\1' + file_name))
                    way = (ziyuans + '\\1' + file_name).replace('\\', '/')
                else:
                    os.system(
                        'copy "%s" "%s"' %
                        ('%s\\video\output\\%s' %
                         (main_path, file_name), ziyuans + '\\' + file_name))
                    way = (ziyuans + '\\' + file_name).replace('\\', '/')
                with open(json_path, encoding='utf8') as f:
                    info = json.loads(f.read())

                info['load'].append({
                    "sudu":
                    100,
                    "duiqi":
                    "fugai",
                    "zuoyou":
                    50,
                    "liangdu":
                    50,
                    "duibidu":
                    50,
                    "baohedu":
                    50,
                    "sediaopianyi":
                    50,
                    "juedui":
                    0,
                    "id_1":
                    -1,
                    "id_2":
                    info['load'][-1]['id_2'] + 1,
                    "title":
                    u"动漫转换器",
                    "zuozhe":
                    u"动漫转换器",
                    "fenlei":
                    "None",
                    "fenbianlv":
                    "10244",
                    "size_1":
                    -1,
                    "format":
                    "vid",
                    "time":
                    str(datetime.now()),
                    "user_id":
                    -1,
                    "pingfen":
                    0,
                    "love_num":
                    0,
                    "way":
                    way,
                    "liulan":
                    path + '/pic/Blue_Stained_Glass_JE3_BE3.png'
                })
                with open(json_path, 'w', encoding='utf8') as f:
                    f.write(json.dumps(info))
                os.remove('%s\\video\\output\\%s' % (main_path, file_name))
                os.remove(mubiao_file_path)
            self.pushButton.setEnabled(True)
            self.pushButton.setText(
                QCoreApplication.translate("Form", u"转换", None))
            for a in self.mainwin.pic_list_local:
                self.mainwin.gridLayout_8.removeWidget(a)
                sip.delete(a)
            self.mainwin.load_bendi()

        else:
            print('have not')

    def head_anime(self):
        '''虚拟形象驱动 ,传入png地址和png输出地址'''
        if self.mainwin.right_now and self.mainwin.right_now.format == 'pic':
            self.pushButton.setText(
                QCoreApplication.translate("Form", u"关闭", None))
            self.pushButton.clicked.connect(self.head_anime_closed)
            json_path = path + '\\load.json'
            id_2 = str(self.mainwin.right_now.id_2)
            main_path = self.launcher.replace('/', '\\')
            print(main_path)

            with open(json_path, encoding='utf8') as f:
                info = json.loads(f.read())

            for xinxi in info['load']:
                # print(xinxi['id_2'],id_2)
                if str(xinxi['id_2']) == id_2:
                    if xinxi['juedui']:
                        lujin = path + xinxi['juedui']
                    else:
                        lujin = xinxi['way']
                    break
            ShellExecute(0, 'open', '%s\\puppeteer.exe' % main_path,
                         '"%s" "%s"' % (lujin, path + '\\aa.png'), main_path,
                         0)

            self.mainwin.mediaplayer.player.head_anime(path + '\\aa.png')

    def head_anime_closed(self):
        self.mainwin.mediaplayer.player.rm_head_anime()
        self.pushButton.setText(QCoreApplication.translate(
            "Form", u"开始", None))
        self.pushButton.clicked.connect(self.head_anime)

        os.system('c:\windows\system32\\taskkill /F /IM %s' % 'puppeteer.exe')

    def gangan(self):
        '''风景图生成器'''
        self.main_path = self.launcher.replace('/', '\\')
        print(self.main_path)
        ShellExecute(0, 'open', '%s\\gangan.exe' % self.main_path, 'app.py',
                     self.main_path, 0)
        sleep(3)
        self.fengjing = WebView('http://127.0.0.1:50000/', self.mainwin, self)
        self.fengjing.show()

    def realesrgan(self):
        '''图像超分辨率重建'''
        if self.mainwin.right_now and self.mainwin.right_now.format == 'pic':
            self.pushButton.setEnabled(False)
            self.pushButton.setText(
                QCoreApplication.translate("Form", u"正在重建", None))
            json_path = path + '\\load.json'
            id_2 = str(self.mainwin.right_now.id_2)
            main_path = self.launcher.replace('/', '\\')
            print(main_path)

            with open(json_path, encoding='utf8') as f:
                info = json.loads(f.read())

            for xinxi in info['load']:
                # print(xinxi['id_2'],id_2)
                if str(xinxi['id_2']) == id_2:
                    if xinxi['juedui']:
                        lujin = path + xinxi['juedui']
                    else:
                        lujin = xinxi['way']
                    format = xinxi['format']
                    break
            #目标文件地址
            file_name = lujin.split('/')[-1]
            # mubiao_file_path = '%s\\test_pic\\%s' % (main_path, file_name)
            print(file_name, lujin)
            if os.path.exists(ziyuans + '\\' + file_name):  #防止重名
                way = (ziyuans + '\\1' + file_name)
            else:
                way = (ziyuans + '\\' + file_name)

            print(
                '%s\\realesrgan-ncnn-vulkan.exe' % main_path,
                '-i %s -o %s -n realesrgan-x4plus' %
                (lujin.replace('/', '\\'), way))
            aa = ShellExecute(
                0, 'open', '%s\\realesrgan-ncnn-vulkan.exe' % main_path,
                '-i "%s" -o "%s" -n realesrgan-x4plus' %
                (lujin.replace('/', '\\'), way), main_path, 1)

            print('111')

            # sleep(5)
            while search('realesrgan-ncnn-vulkan.exe'):
                # print(2)
                sleep(3)

            with open(json_path, encoding='utf8') as f:
                info = json.loads(f.read())
            info['load'].append({
                "sudu": 100,
                "duiqi": "fugai",
                "zuoyou": 50,
                "liangdu": 50,
                "duibidu": 50,
                "baohedu": 50,
                "sediaopianyi": 50,
                "juedui": '',
                "id_1": -1,
                "id_2": info['load'][-1]['id_2'] + 1,
                "title": u"超分辨率重建",
                "zuozhe": u"超分辨率重建",
                "fenlei": "None",
                "fenbianlv": "10244",
                "size_1": -1,
                "format": "pic",
                "time": str(datetime.now()),
                "user_id": 1,
                "pingfen": 3,
                "love_num": 0,
                "way": way,
                "liulan": way
            })
            with open(json_path, 'w', encoding='utf8') as f:
                f.write(json.dumps(info))

            self.pushButton.setEnabled(True)
            self.pushButton.setText(
                QCoreApplication.translate("Form", u"转换", None))
            for a in self.mainwin.pic_list_local:
                self.mainwin.gridLayout_8.removeWidget(a)
                sip.delete(a)
            self.mainwin.load_bendi()

        else:
            print('have not')

    def realcugan(self):
        '''图像超分辨率重建'''
        if self.mainwin.right_now and self.mainwin.right_now.format == 'pic':
            # argv = (None, str(self.mainwin.right_now), path + '\load.json',
            #         self.launcher, ziyuans)
            self.pushButton.setEnabled(False)
            self.pushButton.setText(
                QCoreApplication.translate("Form", u"正在转换", None))
            json_path = path + '\\load.json'
            id_2 = str(self.mainwin.right_now.id_2)
            main_path = self.launcher.replace('/', '\\')
            print(main_path)

            with open(json_path, encoding='utf8') as f:
                info = json.loads(f.read())

            for xinxi in info['load']:
                # print(xinxi['id_2'],id_2)
                if str(xinxi['id_2']) == id_2:
                    if xinxi['juedui']:
                        lujin = path + xinxi['juedui']
                    else:
                        lujin = xinxi['way']
                    format = xinxi['format']
                    break
            #目标文件地址
            file_name = lujin.split('/')[-1]
            mubiao_file_path = '%s\\to-test1\\%s' % (main_path, file_name)
            print(file_name, mubiao_file_path, lujin)
            #复制文件
            os.system(('copy "%s" "%s"' %
                       (lujin.replace('/', '\\'), mubiao_file_path)))

            #修改配置文件
            config = open('%s\config.py' % main_path, encoding='utf8').read()
            a1 = re.sub('mode=".*?"', 'mode="image"', config)
            with open('%s\config.py' % main_path, 'w', encoding='utf8') as f:
                f.write(a1)

            aa = ShellExecute(0, 'open', '%s\\go.bat' % main_path, r'',
                              main_path, 1)

            print('111')

            sleep(4)
            while search('execc.exe'):
                # print(2)
                sleep(1)

            print(mubiao_file_path)
            out_path = '%s\\to-test1-output3x\\%s_3x.png' % (
                main_path, file_name.split('.')[0])  #转换完的文件输出地址
            print(out_path)

            if os.path.exists(out_path):

                if os.path.exists(ziyuans + '\\' + file_name):  #检查是否已经存在防止重名
                    os.system(
                        'copy "%s" "%s.png"' %
                        (out_path, ziyuans + '\\1' + file_name.split('.')[0]))
                    way = (ziyuans + '\\1' + file_name.split('.')[0] +
                           '.png').replace('\\', '/')
                else:
                    print('copy "%s" "%s.png"' %
                          (out_path, ziyuans + '\\' + file_name.split('.')[0]))

                    os.system(
                        'copy "%s" "%s.png"' %
                        (out_path, ziyuans + '\\' + file_name.split('.')[0]))
                    way = (ziyuans + '\\' + file_name.split('.')[0] +
                           '.png').replace('\\', '/')
                with open(json_path, encoding='utf8') as f:
                    info = json.loads(f.read())

                info['load'].append({
                    "sudu": 100,
                    "duiqi": "fugai",
                    "zuoyou": 50,
                    "liangdu": 50,
                    "duibidu": 50,
                    "baohedu": 50,
                    "sediaopianyi": 50,
                    "juedui": 0,
                    "id_1": -1,
                    "id_2": info['load'][-1]['id_2'] + 1,
                    "title": u"超分辨率重建",
                    "zuozhe": u"超分辨率重建",
                    "fenlei": "None",
                    "fenbianlv": "10244",
                    "size_1": -1,
                    "format": "pic",
                    "time": str(datetime.now()),
                    "user_id": 1,
                    "pingfen": 0,
                    "love_num": 0,
                    "way": way,
                    "liulan": way
                })
                with open(json_path, 'w', encoding='utf8') as f:
                    f.write(json.dumps(info))
            else:
                print('找不到转换完后的图片')
            try:
                os.remove(mubiao_file_path)
                os.remove(out_path)
            except:
                pass

            self.pushButton.setEnabled(True)
            self.pushButton.setText(
                QCoreApplication.translate("Form", u"转换", None))
            for a in self.mainwin.pic_list_local:
                self.mainwin.gridLayout_8.removeWidget(a)
                sip.delete(a)
            self.mainwin.load_bendi()

        else:
            print('have not')

    def realcugan_vid(self):
        '''视频超分辨率重建'''
        if self.mainwin.right_now and self.mainwin.right_now.format == 'vid':
            self.pushButton.setEnabled(False)
            self.pushButton.setText(
                QCoreApplication.translate("Form", u"正在重建", None))
            json_path = path + '\\load.json'
            id_2 = str(self.mainwin.right_now.id_2)
            main_path = self.launcher.replace('/', '\\')
            print(main_path)

            with open(json_path, encoding='utf8') as f:
                info = json.loads(f.read())

            for xinxi in info['load']:
                # print(xinxi['id_2'],id_2)
                if str(xinxi['id_2']) == id_2:
                    if xinxi['juedui']:
                        lujin = path + xinxi['juedui']
                    else:
                        lujin = xinxi['way']
                    format = xinxi['format']
                    break
            #目标文件地址
            file_name = lujin.split('/')[-1]
            # mubiao_file_path = '%s\\test_pic\\%s' % (main_path, file_name)
            print(file_name, lujin)
            if os.path.exists(ziyuans + '\\' + file_name):  #防止重名
                way = (ziyuans + '\\1' + file_name)
            else:
                way = (ziyuans + '\\' + file_name)

            #修改配置文件
            config = open('%s\config.py' % main_path, encoding='utf8').read()
            a1 = re.sub('mode=".*?"', 'mode="video"', config)
            a2 = a1.split('\n')
            print(a2)
            print(a2[23])
            a2[23] = 'inp_path=r"%s"' % lujin.replace('/', '\\')
            a2[24] = 'opt_path=r"%s"' % way
            # a1 = re.sub('inp_path=r".*"',
            #             'inp_path=r"%s"' % lujin.replace('/', '\\'), a1)
            # a1 = re.sub('opt_path=r".*"',
            #             'opt_path=r"%s"' % way, a1)
            with open('%s\config.py' % main_path, 'w', encoding='utf8') as f:
                f.write('\n'.join(a2))

            aa = ShellExecute(0, 'open', '%s\\go.bat' % main_path, '',
                              main_path, 1)

            print('111')

            sleep(4)
            while search('execc.exe'):
                # print(2)
                sleep(1)

            if os.path.exists(way):
                with open(json_path, encoding='utf8') as f:
                    info = json.loads(f.read())
                info['load'].append({
                    "sudu":
                    100,
                    "duiqi":
                    "fugai",
                    "zuoyou":
                    50,
                    "liangdu":
                    50,
                    "duibidu":
                    50,
                    "baohedu":
                    50,
                    "sediaopianyi":
                    50,
                    "juedui":
                    '',
                    "id_1":
                    -1,
                    "id_2":
                    info['load'][-1]['id_2'] + 1,
                    "title":
                    u"超分辨率重建",
                    "zuozhe":
                    u"超分辨率重建",
                    "fenlei":
                    "None",
                    "fenbianlv":
                    "10244",
                    "size_1":
                    -1,
                    "format":
                    "vid",
                    "time":
                    str(datetime.now()),
                    "user_id":
                    1,
                    "pingfen":
                    3,
                    "love_num":
                    0,
                    "way":
                    way,
                    "liulan":
                    path + '/pic/Blue_Stained_Glass_JE3_BE3.png'
                })
                with open(json_path, 'w', encoding='utf8') as f:
                    f.write(json.dumps(info))

                self.pushButton.setEnabled(True)
                self.pushButton.setText(
                    QCoreApplication.translate("Form", u"转换", None))
                for a in self.mainwin.pic_list_local:
                    self.mainwin.gridLayout_8.removeWidget(a)
                    sip.delete(a)
                self.mainwin.load_bendi()

        else:
            print('have not')
