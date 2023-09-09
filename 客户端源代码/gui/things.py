from datetime import datetime
import hashlib, requests
import threading,os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json, sip
import get
import moxing
# from sys import path
# path.extend(('D:\work\exercise_py\sai\gui\desktop_pet',))
# from desktop_pet.core.pets import DesktopPet

path = os.getcwd()
ziyuans = os.getcwd() + '\\ziyuans'  #资源的保存路径
# path = r'D:\work\exercise_py\sai\gui'
# ziyuans = r'D:\work\exercise_py\sai\ziyuans'  #资源的保存路径


class download_files(QThread):

    def __init__(self, mainwin):
        self.mainwin = mainwin
        super().__init__()

    def run(self):
        print('download_files')
        try:
            obj = self.mainwin.right_now.gf_text
            file_url = self.mainwin.right_now.way
            if not progressbar(
                    file_url,
                    ziyuans + '\\%s.mp4' % self.mainwin.right_now.id_1, obj,
                    self.mainwin):
                print('fail')
                return
            json_path = path + '\\load.json'
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
                "",
                "id_1":
                self.mainwin.right_now.id_1,
                "id_2":
                info['load'][-1]['id_2'] + 1,
                "title":
                self.mainwin.right_now.title,
                "zuozhe":
                self.mainwin.right_now.zuozhe,
                "fenlei":
                "None",
                "fenbianlv":
                "",
                "size_1":
                -1,
                "format":
                self.mainwin.right_now.format,
                "time":
                str(datetime.now()),
                "user_id":
                1,
                "pingfen":
                3,
                "love_num":
                0,
                "way":
                ziyuans + '\/%s.mp4' % self.mainwin.right_now.id_1,
                "liulan":
                path + '/pic/Blue_Stained_Glass_JE3_BE3.png'
            })
            with open(json_path, 'w', encoding='utf8') as f:
                f.write(json.dumps(info))
            self.mainwin.downloading = False
            # self.mainwin.reload_local()

        except:
            moxing.warm('很抱歉,下载失败', pas, pas)


def progressbar(url, path, obj, mainwin):
    try:
        # if not os.path.exists(path):  # 看是否有该文件夹，没有则创建文件夹
        #     os.mkdir(path)
        print("开始下载")

        text = obj.text()  #原来的text值,以便后期恢复
        obj.setText(QCoreApplication.translate("Form", u'准备下载', None))

        response = requests.get(url, stream=True)  #stream=True必须写上
        size = 0  #初始化已下载大小
        chunk_size = 1024  # 每次下载的数据大小
        content_size = int(response.headers['content-length'])  # 下载文件总大小
        try:
            if response.status_code == 200:  #判断是否响应成功
                print('Start download,[File size]:{size:.2f} MB'.format(
                    size=content_size / chunk_size / 1024))  #开始下载，显示下载文件大小
                filepath = path  #设置图片name，注：必须加上扩展名
                # filepath = path + '\name.extension name'  #设置图片name，注：必须加上扩展名
                with open(filepath, 'wb') as file:  #显示进度条
                    for data in response.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        size += len(data)
                        jindu = '[下载进度]:%.2f%%' % float(
                            size / content_size * 100)
                        print('[下载进度]:%.2f%%' %
                              float(size / content_size * 100))
                        obj.setText(
                            QCoreApplication.translate("Form", u"%s" % jindu,
                                                       None))
                        QApplication.processEvents()
            print('下载完成!')
        except:
            print('下载失败')
            # raise
            return 0
            pass
        obj.setText(QCoreApplication.translate("Form", u"%s" % text,
                                               None))  #恢复原title
    except:
        # raise
        return 0
        pass
    return 1


def xianshimima(cheakbox, lineEdit):  #显示密码
    # print(cheakbox.isChecked())
    if cheakbox.isChecked():
        lineEdit.setEchoMode(QLineEdit.Normal)
    else:
        lineEdit.setEchoMode(QLineEdit.Password)


def tab_change(index, xingwei):
    '''标签改变时'''
    xingwei[index]()


class Form_things():
    '''主窗口继承的事件'''

    def buju_pic(self):
        '''工坊内容布局'''
        try:

            #工坊内容
            self.pic_list_gf = list()
            for row in range(12):
                for column in range(4):
                    b = moxing.Pic(self)
                    self.gridLayout_3.addWidget(b, row, column, 1, 1)
                    b.gf_pic.setScaledContents(True)
                    self.pic_list_gf.append(b)

            #多的两个补上
            b = moxing.Pic(self)
            self.gridLayout_3.addWidget(b, 13, 0, 1, 1)
            b.gf_pic.setScaledContents(True)
            self.pic_list_gf.append(b)

            b = moxing.Pic(self)
            self.gridLayout_3.addWidget(b, 13, 1, 1, 1)
            b.gf_pic.setScaledContents(True)
            self.pic_list_gf.append(b)
        except:
            pass

    def load_bendi(self):
        try:

            with open('%s%s' % (path, '\load.json'), 'r',
                      encoding='utf8') as f:
                load = json.loads(f.read())
            # print(load)

            #计算需要的行列数并部署
            num = len(load["load"])
            num_1 = 0
            row_1 = (num - 1) // 4 + 1
            #本地内容
            self.pic_list_local = list()
            for row in range(row_1):
                for column in range(4):
                    b = moxing.Pic(self)
                    self.gridLayout_8.addWidget(b, row, column, 1, 1)
                    b.gf_pic.setScaledContents(True)
                    liulan_path = load['load'][num_1].get('liulan').replace(
                        '/', '\\')
                    if liulan_path[0] == '\\':  #是否相对路径
                        liulan_path = path + liulan_path
                    b.gf_pic.setPixmap(QPixmap(liulan_path))
                    b.sudu = load['load'][num_1].get('sudu')
                    b.duiqi = load['load'][num_1].get('duiqi')
                    b.zuoyou = load['load'][num_1].get('zuoyou')
                    b.liangdu = load['load'][num_1].get('liangdu')
                    b.duibidu = load['load'][num_1].get('duibidu')
                    b.baohedu = load['load'][num_1].get('baohedu')
                    b.sediaopianyi = load['load'][num_1].get('sediaopianyi')
                    b.juedui = load['load'][num_1].get('juedui')
                    b.id_1 = load['load'][num_1].get('id_1')
                    b.id_2 = load['load'][num_1].get('id_2')
                    b.title = load['load'][num_1].get('title')
                    b.zuozhe = load['load'][num_1].get('zuozhe')
                    b.fenlei = load['load'][num_1].get('fenlei')
                    b.fenbianlv = load['load'][num_1].get('fenbianlv')
                    b.size_1 = load['load'][num_1].get('size_1')
                    b.format = load['load'][num_1].get('format')
                    b.time = load['load'][num_1].get('time')
                    b.user_id = load['load'][num_1].get('user_id')
                    b.pingfen = load['load'][num_1].get('pingfen')
                    b.love_num = load['load'][num_1].get('love_num')
                    b.way = load['load'][num_1].get('way').replace('/', '\\')

                    linshi_2 = load['load'][num_1].get('liulan').replace(
                        '/', '\\')
                    if linshi_2[0] == '\\':  #是否相对路径
                        linshi_2 = path + linshi_2
                    b.liulan = QPixmap(linshi_2)

                    b.isload = True

                    b.gf_text.setText(
                        QCoreApplication.translate("Form", u"%s" % b.title,
                                                   None))

                    self.pic_list_local.append(b)
                    num_1 += 1

                    if num == num_1:
                        break
        except:
            pass

    def load_right(self, pic):
        '''装载资源到右侧显示框'''
        try:
            if not pic.title:  #是否完成加载
                return None
            self.label_37.setPixmap(pic.liulan)
            self.label.setText(
                QCoreApplication.translate("Form", u"%s" % pic.title, None))
            self.label_3.setText(
                QCoreApplication.translate("Form", u"%s" % pic.zuozhe, None))
            # print(pic.pingfen)

            #计算并显示评分
            sorce = round(pic.pingfen, 1)
            half_star = QPixmap('%s\\pic\\half_star.png' % path)
            full_star = QPixmap('%s\\pic\\full_star.png' % path)
            less_star = QPixmap('%s\\pic\\less_star.png' % path)
            for bb in (self.label_16, self.label_17, self.label_18,
                       self.label_29, self.label_30):
                if sorce < 0.5:
                    bb.setPixmap(less_star)
                elif 0.5 <= sorce < 1:
                    bb.setPixmap(half_star)
                elif sorce >= 1:
                    bb.setPixmap(full_star)
                bb.setScaledContents(True)
                sorce -= 1

            self.label_4.setText(
                QCoreApplication.translate(
                    "Form", u'%s %sB' % (pic.format, pic.size_1), None))
            self.label_5.setText(
                QCoreApplication.translate("Form", u"%s" % pic.fenlei, None))

            self.pushButton.setText(
                QCoreApplication.translate("Form", u"订阅", None))

            self.groupBox.setVisible(False)
            self.groupBox_2.setVisible(False)
            self.groupBox_3.setVisible(False)

            self.right_now = pic  #当前右边菜单显示的本地obj

            if pic.isload:  #本地资源显示高级
                # self.groupBox.setVisible(True)
                if self.checkBox_3.isChecked():
                    self.groupBox_2.setVisible(True)

                self.groupBox_3.setVisible(True)
                self.horizontalSlider.setValue(pic.sudu)
                self.comboBox_2.setCurrentIndex(duiqi_zhuan(pic.duiqi))
                self.horizontalSlider_2.setValue(pic.zuoyou)
                self.horizontalSlider_5.setValue(pic.liangdu)
                self.horizontalSlider_6.setValue(pic.duibidu)
                self.horizontalSlider_7.setValue(pic.baohedu)
                self.horizontalSlider_8.setValue(pic.sediaopianyi)
                self.pushButton.setText(
                    QCoreApplication.translate("Form", u"取消订阅", None))

                #播放列表插队
                if self.mediaplayer:
                    self.mediaplayer.player.insert(pic.id_2)
        except:
            pass

    def searching(self):
        '''工坊内搜索资源'''
        try:
            text = self.gf_search.text()
            if not text:
                text = '%'
            self.page_info.start_(self.gf_pailie, self.gf_shuaixuan, text, 1,
                                  self.pic_list_gf)
        except:
            pass

    def mousePressEvent(self, event):
        try:
            self.m_flag = False
            self.size_change = False
            # if event.button() == Qt.LeftButton:
            if event.button() == Qt.LeftButton and (
                    event.y() <= self.height() - 25
                    or event.x() <= self.width() - 25):
                self.m_flag = True
                self.m_Position = event.globalPos() - self.pos()  #获取鼠标相对窗口的位置
                event.accept()
                self.lock = threading.Lock()
                # self.setCursor(QCursor(Qt.OpenHandCursor))  #更改鼠标图标

            elif event.button() == Qt.LeftButton and self.height() - event.y(
            ) <= 25 and self.width() - event.x() <= 25:
                self.setCursor(QCursor(Qt.SizeFDiagCursor))
                self.Position = self.pos()  #获取窗口绝对位置
                self.size_change = True
        except:
            pass

    def mouseReleaseEvent(self, QMouseEvent):

        try:
            if Qt.LeftButton and self.m_flag:
                self.move(QMouseEvent.globalPos() - self.m_Position)  #更改窗口位置
                QMouseEvent.accept()
        except:
            pass
        try:

            if Qt.LeftButton and self.size_change:
                pos = QMouseEvent.globalPos() - self.Position
                self.resize(pos.x(), pos.y())
                QMouseEvent.accept()
        except:
            pass
        try:
            # print('ccc')
            self.m_flag = False
            self.setCursor(QCursor(Qt.ArrowCursor))
            if self.size_change:
                self.win_changed()

            self.size_change = False
        except:
            # raise
            pass

    def win_changed(self):
        try:
            width = self.scrollArea_5.width()
            column = width // 200
            num = len(self.pic_list_local)
            num_1 = 0
            row_1 = (num - 1) // column + 1

            for row in range(row_1):
                for column_1 in range(column):
                    self.gridLayout_8.addWidget(self.pic_list_local[num_1],
                                                row, column_1, 1, 1)

                    num_1 += 1
                    if num == num_1:
                        break

            num = len(self.pic_list_gf)
            num_1 = 0
            row_1 = (num - 1) // column + 1
            for row in range(row_1):
                for column_1 in range(column):
                    self.gridLayout_3.addWidget(self.pic_list_gf[num_1], row,
                                                column_1, 1, 1)

                    num_1 += 1
                    if num == num_1:
                        break
        except:
            pass

    def max_win(self):
        '''max_zhuangtai (0|1)'''
        try:
            if 'max_zhuangtai' in self.__dir__():
                if self.max_zhuangtai:
                    self.showNormal()
                    self.max_zhuangtai = 0
                else:
                    self.showMaximized()
                    self.max_zhuangtai = 1
            else:
                self.max_zhuangtai = 1
                self.showMaximized()

            self.win_changed()
        except:
            pass

    def bofang_list_1(self):
        try:
            with open(path + '\load.json', encoding='utf8') as f:
                info = json.loads(f.read())
            self.bofang_list = []
            # print(info)
            for a in info['bofang']:
                #绑定关联对象
                for b in self.pic_list_local:
                    if b.id_2 == a:
                        # print('ok')
                        c = moxing.Bofang_s(self, b)
                        c.label.setPixmap(b.liulan)
                        self.horizontalLayout_4.addWidget(c)
                        self.bofang_list.append(c)
            self.label_2.setText(u"播放列表 (%s)" % len(self.bofang_list))
        except:
            pass

    def load_mods(self):
        '''加载mod'''
        try:
            with open(path + '\load.json', encoding='utf8') as f:
                info = json.loads(f.read())['mods']
            for mod in info:
                if mod['type'] == 1:  #一号模式,使用按钮和介绍
                    a = moxing.Mods(self, mod['instruction'],
                                    mod['Control_description'],
                                    mod['launcher'], mod['name'])
                    self.verticalLayout_15.addWidget(a)
        except:
            pass

    def open(self):
        try:
            vid = ['mp4', 'avi', 'wmv', 'rm', 'mov', 'm4v', 'flv', 'mv']
            pic = ['bmp', 'gif', 'jpeg', 'png', 'jpg', 'tif']

            path_1, filetype = QFileDialog.getOpenFileName(
                None, "选择文件", '.', "视频或图像文件(All Files (*))")  # ;;All Files (*)
            if path:
                name = path_1.split('/')[-1]
                format_1 = path_1.split('.')[-1]
                with open(path + '\load.json', encoding='utf8') as f:
                    info = json.loads(f.read())
                if format_1 in vid:
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
                        "title": name,
                        "zuozhe": name,
                        "fenlei": "None",
                        "fenbianlv": "0",
                        "size_1": -1,
                        "format": "vid",
                        "time": str(datetime.now()),
                        "user_id": 1,
                        "pingfen": 3,
                        "love_num": 0,
                        "way": path_1,
                        "liulan": path + '\\pic\\video.png'
                    })
                elif format_1 in pic:
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
                        "title": name,
                        "zuozhe": name,
                        "fenlei": "None",
                        "fenbianlv": "0",
                        "size_1": -1,
                        "format": "pic",
                        "time": str(datetime.now()),
                        "user_id": 1,
                        "pingfen": 3,
                        "love_num": 0,
                        "way": path_1,
                        "liulan": path_1
                    })
                else:
                    return
                with open(path + '\\load.json', 'w', encoding='utf8') as f:
                    f.write(json.dumps(info))
                self.load_bendi()
        except:
            pass

    def login(self):
        '''登入账号'''
        try:
            print('正在登入')
            email = self.lineEdit_7.text()
            key = self.lineEdit_9.text()
            print(email, key)
            info_111 = get.login(email, key)
            if info_111[0]:
                print('登入成功')
                info = get.get_myself()[1]
                print(info)
                self.stackedWidget.setCurrentIndex(2)
                self.label_39.setText(
                    QCoreApplication.translate("Form", info[1], None))
                self.label_42.setText(
                    QCoreApplication.translate("Form", '注册时间: %s' % info[3],
                                               None))

                self.love_ziyuan_paixu()
                self.get_love.start_(self)

            else:
                print(info_111[1])
                moxing.warm('登入失败 %s' % info_111[1], pas, pas)
        except:
            pass

    def auto_login(self, email, key):
        '''登入账号'''
        try:
            print('正在登入')
            print(email, key)
            info_111 = get.login(email, key, Encrypted=True)
            if info_111[0]:
                print('登入成功')
                info = get.get_myself()[1]
                print(info)
                self.stackedWidget.setCurrentIndex(2)
                self.label_39.setText(
                    QCoreApplication.translate("Form", info[1], None))
                self.label_42.setText(
                    QCoreApplication.translate("Form", '注册时间: %s' % info[3],
                                               None))

                self.love_ziyuan_paixu()
                self.get_love.start_(self)

            else:
                print(info_111[1])
        except:
            pass

    def zhuce_1(self):
        '''注册一个账号第一步'''
        try:

            self.label_15.setVisible(False)
            self.zhuce_user = self.lineEdit_11.text()
            self.zhuce_email = self.lineEdit_8.text()
            self.zhuce_keyword = hashlib.sha1(
                bytes(self.lineEdit_10.text(), encoding='utf8')).hexdigest()
            info_1 = get.zhuce_1(self.zhuce_email)
            if info_1[0]:
                self.lineEdit_14.setText(str(info_1[1]))
                self.stackedWidget.setCurrentIndex(3)
            else:
                print('fail')
        except:
            pass

    def zhuce_2(self):
        try:
            info = get.zhuce_2(self.zhuce_email, self.zhuce_keyword,
                               self.zhuce_user)
            if info[0]:
                self.auto_login(self.zhuce_email, self.zhuce_keyword)
            else:
                self.label_15.setVisible(True)
                self.label_15.setText('Glass 未收到您的验证邮件 (系统可能会有延迟)')
        except:
            pass

    def login_out(self):
        try:
            info = get.login_out()
            if info[0]:
                self.stackedWidget.setCurrentIndex(0)
        except:
            pass

    def auto_login_11(self):
        try:
            json_path = path + '\\load.json'
            with open(json_path, encoding='utf8') as f:
                info = json.loads(f.read())
            if info['setting']['auto_login']:
                self.auto_login(info['setting']['email'],
                                info['setting']['key'])
        except:
            pass

    def set_auto_login(self, code):
        '''设置自动登入状态'''
        try:
            print(code)
            if code:
                json_path = path + '\\load.json'
                with open(json_path, encoding='utf8') as f:
                    info = json.loads(f.read())
                info['setting']['auto_login'] = 0
                info['setting']['email'] = ''
                info['setting']['key'] = ''
            else:
                json_path = path + '\\load.json'
                with open(json_path, encoding='utf8') as f:
                    info = json.loads(f.read())
                info['setting']['auto_login'] = 1
                email = self.lineEdit_7.text()
                key = self.lineEdit_9.text()
                info['setting']['email'] = email
                info['setting']['key'] = hashlib.sha1(
                    bytes(key, encoding='utf8')).hexdigest()
        except:
            pass

    def delect_play_list(self):
        try:
            if self.right_now.isload:
                print('正在删除')
                #执行删除操作
                json_path = path + '\\load.json'
                with open(json_path, encoding='utf8') as f:
                    info = json.loads(f.read())
                    print(self.right_now.id_2, info['bofang'])

                    info['bofang'].remove(self.right_now.id_2)
                with open(json_path, 'w', encoding='utf8') as f:
                    f.write(json.dumps(info))
                for a in self.bofang_list:
                    self.horizontalLayout_4.removeWidget(a)
                    sip.delete(a)
                self.bofang_list_1()
        except:
            pass

    def add_play_list(self):
        try:
            if self.right_now.isload:
                print('正在添加')
                #执行添加操作
                json_path = path + '\\load.json'
                with open(json_path, encoding='utf8') as f:
                    info = json.loads(f.read())
                    info['bofang'].append(self.right_now.id_2)
                with open(json_path, 'w', encoding='utf8') as f:
                    f.write(json.dumps(info))
                for a in self.bofang_list:
                    self.horizontalLayout_4.removeWidget(a)
                    sip.delete(a)
                self.bofang_list_1()
        except:
            pass

    def download_1(self):
        try:
            print('start')
            if self.right_now.isload:
                print('正在删除')
                #执行删除操作
                json_path = path + '\\load.json'
                with open(json_path, encoding='utf8') as f:
                    info = json.loads(f.read())
                for a in info['load']:
                    if a['id_2'] == self.right_now.id_2:
                        info['load'].remove(a)
                        break
                with open(json_path, 'w', encoding='utf8') as f:
                    f.write(json.dumps(info))
                for a in self.pic_list_local:
                    self.gridLayout_8.removeWidget(a)
                    sip.delete(a)
                self.load_bendi()

            else:
                #下载操作
                print('start download 1')
                self.downloading = True
                self.downloadThings.start()
                self.flash_local = QTimer()
                self.flash_local.timeout.connect(self.is_downloading)
                self.flash_local.start(1000)

        except:
            pass

    def is_downloading(self):
        print('in下载状态中')
        if not self.downloading:
            print('不在下载状态中')
            self.reload_local()
            self.flash_local.stop()

    def change_xunhuan_time(self):
        try:
            sec = self.lineEdit.text()
            self.mediaplayer.player.change_xunhuan_time(int(sec))
            json_path = path + '\\load.json'
            with open(json_path, encoding='utf8') as f:
                info = json.loads(f.read())
            info['setting']['circulation_time'] = int(sec)
            with open(json_path, 'w', encoding='utf8') as f:
                f.write(json.dumps(info))
        except:
            pass

    def load_xunhuan_time(self):
        try:
            json_path = path + '\\load.json'
            with open(json_path, encoding='utf8') as f:
                info = json.loads(f.read())
            sec = info['setting']['circulation_time']
            self.lineEdit.setText(str(sec))
        except:
            pass

    def closeEvent(self, event):

        self.hide()
        event.ignore()

    def close_start(self):  #关闭开屏动画
        self.widget_start.setVisible(False)
        print('开屏动画结束')
        self.timer_start.stop()
        self.news.show()

    def desktop_pet(self):
        self.pet.show()
        self.pet.welcomePage()
        self.pushButton_8.setText(u'关闭')
        self.pushButton_8.clicked.connect(self.desktop_pet_stop)  #桌面宠物
        print('over')

    def desktop_pet_stop(self):
        self.pet.hide()
        self.pushButton_8.setText(u'开启')
        self.pushButton_8.clicked.connect(self.desktop_pet)  #桌面宠物

    def love_ziyuan(self):
        id_1 = self.right_now.id_1
        if id_1 != -1:
            status, info = get.love_ziyuan(id_1)
            if status:
                moxing.warm('已加入 我喜欢 列表', pas, pas)
            else:
                moxing.warm('操作失败,原因: %s' % info, pas, pas)

    def love_ziyuan_paixu(self):
        info = get.get_love()
        print(info)

        try:

            if info[0]:
                for reset in self.my_love_list:  #清除重置操作
                    # reset.reset()
                    self.gridLayout_9.removeWidget(reset)
                    sip.delete(reset)
                self.my_love_list = []

                #计算行列排序
                row_1 = 0
                colum_1 = 0
                try:
                    for num in range(len(info[1])):
                        b = moxing.Pic(self)
                        print(row_1, colum_1)
                        self.gridLayout_9.addWidget(b, row_1, colum_1, 1, 1)
                        b.gf_pic.setScaledContents(True)
                        b.id_1 = info[1][num][0]
                        self.my_love_list.append(b)

                        if not (colum_1 + 1) % 3:
                            row_1 += 1
                            colum_1 = 0
                        else:
                            colum_1 += 1
                except:
                    # raise
                    pass
        except:
            # raise
            pass

    def re_love_ziyuan(self):
        '''刷新喜欢列表'''
        self.love_ziyuan_paixu()
        self.get_love.start_(self)

    def reload_local(self):  #重载本地资源
        for a in self.pic_list_local:
            self.gridLayout_8.removeWidget(a)
            sip.delete(a)
        self.load_bendi()


class Get_page(QThread):

    # def __init__(self, shuaixuan, text):
    #     self.shuaixuan = shuaixuan
    #     self.text = text
    #     super(Get_page, self).__init__()

    def start_(self, pailie, shuaixuan, text, page, pic_list, loading_lab):
        # print('aaa')
        self.shuaixuan = shuaixuan
        self.text = text
        self.page = page
        self.pailie = pailie
        self.pic_list = pic_list
        self.loading_lab = loading_lab
        self.start()

    def run(self):
        # print(self.shuaixuan,self.pailie,self.text,self.page,self.pic_list)
        self.loading_lab.setVisible(True)
        text = self.text.text()
        if not text:
            text = '%'
        info = get.zongshu(self.shuaixuan, text)
        print(info)

        try:

            if info[0]:
                start = info[1] - (self.page * 50 - 1)
                if start < 0:
                    start = 1
                info1 = get.page_info(start, self.pailie, self.shuaixuan,
                                      text)[1]
                # print(info1)

                for reset in self.pic_list:  #清楚重置操作
                    reset.reset()

                try:
                    for b in range(50):
                        self.pic_list[b].gf_text.setText(
                            QCoreApplication.translate("Form",
                                                       u"%s" % info1[b][1],
                                                       None))
                except:
                    pass
                # for a in range(5):
                for a in range(50):
                    try:
                        info3 = get.ziyuan_pic(info1[a][0])[1]
                        self.pic_list[a].gf_pic.setPixmap(
                            QPixmap.fromImage(info3))
                        self.pic_list[a].liulan = QPixmap.fromImage(info3)
                    except:
                        break
                # for c in range(5):
                for c in range(50):
                    try:
                        info2 = get.get_ziyuan(info1[c][0])[1]
                        self.pic_list[c].id_1 = info2[0]
                        self.pic_list[c].fenlei = info2[1]
                        self.pic_list[c].fenbianlv = info2[2]
                        self.pic_list[c].title = info2[3]
                        self.pic_list[c].zuozhe = info2[4]
                        self.pic_list[c].user_id = info2[5]
                        self.pic_list[c].size_1 = info2[6]
                        self.pic_list[c].format = info2[7]
                        self.pic_list[c].time = info2[8]
                        self.pic_list[c].way = info2[9]
                        self.pic_list[c].pingfen = info2[10]
                        self.pic_list[c].love_num = info2[11]
                    except:
                        break
                print('finished')

                # print(info1)
            else:
                print(info[1])
            self.loading_lab.setVisible(False)
        except:
            pass


class Get_love(QThread):

    def start_(self, main):
        self.main = main
        # print('aaa')

        self.start()

    def run(self):
        try:
            for b in self.main.my_love_list:
                info1 = get.get_ziyuan(b.id_1)
                print(info1)
                b.gf_text.setText(
                    QCoreApplication.translate("Form", u"%s" % info1[1][3],
                                               None))
                b.id_1 = info1[1][0]
                b.fenlei = info1[1][1]
                b.fenbianlv = info1[1][2]
                b.title = info1[1][3]
                b.zuozhe = info1[1][4]
                b.user_id = info1[1][5]
                b.size_1 = info1[1][6]
                b.format = info1[1][7]
                b.time = info1[1][8]
                b.way = info1[1][9]
                b.pingfen = info1[1][10]
                b.love_num = info1[1][11]

                try:
                    info2 = get.ziyuan_pic(b.id_1)[1]
                    b.gf_pic.setPixmap(QPixmap.fromImage(info2))
                    b.liulan = QPixmap.fromImage(info2)
                except:
                    # raise
                    pass

        except:
            # raise
            pass


def duiqi_zhuan(qstr):
    if qstr == 'fugai':
        return 0
    elif qstr == 'ziyou':
        return 1
    elif qstr == 'juzhong':
        return 2
    elif qstr == 'zuoshang':
        return 3
    elif qstr == 'zuozhong':
        return 4


def pas(*arg):
    print('pass', arg)
    pass
