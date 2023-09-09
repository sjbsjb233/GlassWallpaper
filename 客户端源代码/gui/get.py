import requests, base64, hashlib
from numpy import uint8, frombuffer
from PyQt5.QtGui import QImage
from cv2 import imdecode, IMREAD_COLOR, COLOR_BGR2RGB, cvtColor
from socket import gethostname

_huihua = requests.session()
_yuming = 'https://api.sjbsjb.xyz'
_version = '1.0'

_huihua.headers = {'User-Agent': 'GLASS_%s_%s' % (_version, gethostname())}

# _yuming = 'http://127.0.0.1:8880'
# print(_huihua.get('https://api.sjbsjb.xyz/test').status_code)

# _huihua.headers = {'CF-Connecting-IP': '23.154.177.5'}


def login(email, key, Encrypted=False):
    try:
        if Encrypted:
            data = {'email': email, 'key': key}
        else:
            data = {
                'email': email,
                'key': hashlib.sha1(bytes(key, encoding='utf8')).hexdigest()
            }
        info = _huihua.post(_yuming + '/login', data=data)
        if info.status_code == 200:
            return True, '%s %s' % (info.status_code, info.text)
        return False, '%s %s' % (info.status_code, info.text)
    except:
        pass


def ziyuan_pic(id_1):
    try:
        '''传入资源id,返回的对象直接用于label.setPixmap(QPixmap.fromImage())'''
        info = _huihua.get(_yuming + '/static/ziyuan_pic/%s' % id_1)
        if info.status_code == 200:
            pic = base64.b64decode(info.json().get('pic'))
            # img_io = io.BytesIO(pic)
            # pix = Image.open(img_io)

            # qimg = ImageQt(pix)
            # pixmap = QtGui.QPixmap.fromImage(qimg)

            img = imdecode(frombuffer(pic, uint8), IMREAD_COLOR)
            frame = cvtColor(img, COLOR_BGR2RGB)
            height, width, bytesPerComponent = frame.shape
            bytesPerLine = bytesPerComponent * width
            pixmap = QImage(frame.data, width, height, bytesPerLine,
                            QImage.Format_RGB888)

            return True, pixmap
        return False, '%s %s' % (info.status_code, info.text)
    except:
        pass


# def load_image(path):
#     img = cv2.imdecode(np.frombuffer(pic, np.uint8), cv2.IMREAD_COLOR)
#     frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     height, width, bytesPerComponent = frame.shape
#     bytesPerLine = bytesPerComponent * width
#     pixmap = QImage(frame.data, width, height, bytesPerLine,
#                     QImage.Format_RGB888)


def zongshu(shuaixuan, text):
    '''返回资源总数'''
    try:
        index = shuaixuan.currentIndex()
        info = _huihua.get(_yuming + '/zongshu/%s/%s' %
                           (_shuaixuan_zhuan(index), text))
        if info.status_code == 200:
            return True, info.json().get('zongshu')
        return False, '%s %s' % (info.status_code, info.text)
    except:
        pass


def page_info(start, pailie, shuaixuan, text):
    try:
        # print(pailie.currentIndex(),shuaixuan.currentIndex())
        # print(_pailie_zhuan(pailie.currentIndex()))
        info = _huihua.get(_yuming + '/search/%s/%s/%s/%s' %
                           (start, _pailie_zhuan(pailie.currentIndex()),
                            _shuaixuan_zhuan(shuaixuan.currentIndex()), text))
        # print(info.json())
        if info.status_code == 200:
            return True, info.json().get('ziyuan')

        return False, '%s %s' % (info.status_code, info.text)
    except:
        pass


def get_ziyuan(id_1):
    try:
        info = _huihua.get(_yuming + '/static/get_ziyuan/%s' % id_1)
        if info.status_code == 200:
            return True, info.json().get('ziyuan')
        return False, '%s %s' % (info.status_code, info.text)
    except:
        pass


def get_myself():
    try:
        info = _huihua.get(_yuming + '/my_info')
        if info.status_code == 200:
            return True, info.json().get('info')
        return False, '%s %s' % (info.status_code, info.text)
    except:
        pass


def zhuce_1(email):
    try:
        data = {'step': 1, 'token': 'gds', 'email': email}
        info = _huihua.post(_yuming + '/zhuce', data=data)
        print(info.text)
        if info.status_code == 200:
            return True, info.json().get('key')
        return False, '%s %s' % (info.status_code, info.text)
    except:
        pass


def zhuce_2(email, key, name):
    try:
        data = {'step': 2, 'email': email, 'key': key, 'name': name}
        info = _huihua.post(_yuming + '/zhuce', data=data)
        if info.status_code == 200:
            return True, 'ok'
        return False, '%s %s' % (info.status_code, info.text)
    except:
        pass


def login_out():
    try:
        info = _huihua.get(_yuming + '/loginout')
        if info.status_code == 200:
            return True, 'ok'
        return False, '%s %s' % (info.status_code, info.text)
    except:
        pass


def set_score(score, id_1):
    try:
        data = {'id': id_1, 'score': score, 'text': '0'}
        info = _huihua.post(_yuming + '/send_pinglun', data=data)
        if info.status_code == 200:
            return True, 'ok'
        return False, '%s %s' % (info.status_code, info.text)
    except:
        # raise
        pass


def love_ziyuan(id_1):
    try:
        info = _huihua.get(_yuming + '/love_ziyuan/%s' % id_1)
        if info.status_code == 200:
            return True, 'ok'
        return False, '%s %s' % (info.status_code, info.text)
    except:
        # raise
        pass

def get_love():
    try:
        info = _huihua.get(_yuming + '/get_love')
        if info.status_code == 200:
            return True, info.json().get('key')
        return False, '%s %s' % (info.status_code, info.text)
    except:
        # raise
        pass


def _shuaixuan_zhuan(index):
    if index == 0:
        return 'all'
    elif index == 1:
        return 'yx'
    elif index == 2:
        return 'dm'
    elif index == 3:
        return 'kj'
    elif index == 4:
        return 'fj'
    elif index == 5:
        return 'zz'


def _pailie_zhuan(index):
    if index == 0:
        return 'time'
    elif index == 1:
        return 'title'
    elif index == 2:
        return 'size'
