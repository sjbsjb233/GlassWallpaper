'''
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
'''

from sys import exit, argv
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qt_material import apply_stylesheet
import moxing, os
# from sai.houduan.main import download_file
import things
from yemian import Ui_MainWindow

from sys import path

path.extend(('D:\work\exercise_py\sai\gui\desktop_pet', ))
from desktop_pet.core.pets import DesktopPet

from win32api import ShellExecute

path = os.getcwd()
ziyuans = os.getcwd() + '\\ziyuans'  #资源的保存路径
# path = r'D:\work\exercise_py\sai\gui'
# ziyuans = r'D:\work\exercise_py\sai\ziyuans'  #资源的保存路径


class MyMain(QMainWindow, Ui_MainWindow, things.Form_things):

    def __init__(self, page_info, parent=None):
        super(MyMain, self).__init__(parent)
        self.setupUi(self)

        #开屏logo
        self.widget_start = QWidget(self)
        self.widget_start.setObjectName(u"widget")
        self.widget_start.setGeometry(QRect(0, 0, 1250, 855))
        self.widget_start.raise_()
        self.gridLayout_st = QGridLayout(self.widget_start)
        self.gridLayout_st.setObjectName(u"gridLayout")
        self.label_st = QLabel(self.widget_start)
        self.label_st.setObjectName(u"label")
        self.label_st.setMinimumSize(QSize(100, 100))
        self.label_st.setMaximumSize(QSize(100, 100))
        self.label_st.setText(QCoreApplication.translate(
            "Form", u"logo", None))
        self.label_st.setScaledContents(True)
        self.label_st.setPixmap(QPixmap('%s\pic\Glass_JE4_BE2.png' % path))
        self.gridLayout_st.addWidget(self.label_st, 0, 0, 1, 1)
        self.timer_start = QTimer()
        self.timer_start.timeout.connect(self.close_start)
        self.timer_start.start(1500)

        self.mediaplayer = None  #初始化媒体播放器,由hexin.py传入

        #图标设置
        self.setWindowIcon(QIcon(path + '\\pic\\favicon.ico'))

        # 无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setWindowOpacity(0.95)

        self.label_37.setScaledContents(True)

        self.page_info = page_info  #加载页面

        self.label_114.setScaledContents(True)  #logo自适应
        self.label_115.setScaledContents(True)  #logo自适应
        self.label_116.setScaledContents(True)  #logo自适应
        self.label_38.setScaledContents(True)
        self.groupBox_2.setVisible(False)  #高级选项不可见
        self.groupBox.setVisible(False)

        self.buju_pic()  #工坊列表初始化
        self.checkBox.clicked.connect(lambda: things.xianshimima(
            self.checkBox, self.lineEdit_9))  #显示密码按钮配置

        self.tabWidget.currentChanged.connect(
            lambda x: things.tab_change(x, (int, lambda: page_info.start_(
                self.gf_pailie, self.gf_shuaixuan, self.gf_search, 1, self.
                pic_list_gf, self.label_19), int, int, int, int)))

        self.gf_shuaixuan.currentTextChanged.connect(
            lambda: page_info.start_(self.gf_pailie, self.gf_shuaixuan, self.
                                     gf_search, 1, self.pic_list_gf))
        self.gf_pailie.currentTextChanged.connect(
            lambda: page_info.start_(self.gf_pailie, self.gf_shuaixuan, self.
                                     gf_search, 1, self.pic_list_gf))

        self.load_bendi()
        self.pushButton_13.clicked.connect(self.max_win)  #最大化按钮配置
        self.bofang_list_1()  #播放列表初始化

        self.gf_search.returnPressed.connect(
            lambda: page_info.start_(self.gf_pailie, self.gf_shuaixuan, self.
                                     gf_search, 1, self.pic_list_gf))

        self.lineEdit.returnPressed.connect(self.change_xunhuan_time)

        self.news = moxing.News_view()  #新闻定义,动画结束后显示

        #亚克力效果实现winapi
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.centralwidget.setAttribute(Qt.WA_TranslucentBackground)
        self.widget_21.setAttribute(Qt.WA_TranslucentBackground)
        self.frame_23.setAttribute(Qt.WA_TranslucentBackground)
        self.widget_2.setAttribute(Qt.WA_TranslucentBackground)
        self.frame_12.setAttribute(Qt.WA_TranslucentBackground)
        moxing.yakeli(self)

        #部分圆角化补充
        self.scrollArea_3.setStyleSheet(r'border-radius:5px')
        self.stackedWidget_2.setStyleSheet(r'border-radius:5px')
        self.tabWidget.setStyleSheet(r'''border-top-right-radius:5px;
        border-bottom-right-radius:5px;border-bottom-left-radius:5px;''')
        self.tabWidget.setStyleSheet(r'QTabBar::tab{border-radius:5px}')

        #加载mod
        self.load_mods()

        self.pushButton_4.clicked.connect(self.open)

        self.pushButton_20.clicked.connect(self.login)

        self.pushButton_2.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_21.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_3.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(1))

        self.pushButton_22.clicked.connect(self.zhuce_1)
        self.pushButton_23.clicked.connect(self.zhuce_2)
        self.pushButton_49.clicked.connect(self.login_out)

        self.pushButton_10.clicked.connect(
            lambda: moxing.warm('您确定要举报吗', things.pas, things.pas))

        self.comboBox_27.currentIndexChanged.connect(self.set_auto_login)

        self.downloadThings = things.download_files(self)
        # self.download_label_change=QTimer()
        # self.download_label_change.timeout.connect()
        self.pushButton.clicked.connect(self.download_1)
        self.pushButton_6.clicked.connect(self.delect_play_list)
        self.pushButton_7.clicked.connect(self.add_play_list)
        self.pushButton_8.clicked.connect(self.desktop_pet)  #桌面宠物
        self.pushButton_5.clicked.connect(lambda: ShellExecute(
            0, 'open', '%s\\Licence.txt' % path, '', path, 1))

        self.setSorce = moxing.Set_scroe(self)
        self.pushButton_9.clicked.connect(self.setSorce.show)

        self.pushButton_11.clicked.connect(self.love_ziyuan)

        self.pet = DesktopPet(tray=False)

        #我喜欢内容
        self.my_love_list = []
        self.get_love = things.Get_love()
        self.pushButton_15.clicked.connect(self.re_love_ziyuan)

        self.load_xunhuan_time()

        self.auto_login_11()

        # self.pic_list_gf[0].gf_1.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.pic_list_gf[0].gf_1.customContextMenuRequested.connect(lambda:things.create_rightmenu(self.pic_list_gf[0].gf_1))


if __name__ == '__main__':
    app = QApplication(argv)
    page_info = things.Get_page()  #工坊
    myWin = MyMain(page_info)
    apply_stylesheet(app, theme='dark_teal.xml')
    myWin.show()
    # a=moxing.warm('您确定要执行吗',things.pas,things.pas)
    exit(app.exec_())
