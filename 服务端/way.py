import base64
from random import randint
import pymysql, requests, jieba
# from snownlp import SnowNLP
# import pyotp
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib, re

#以下四行存储pop邮箱登入信息,用于注册时的验证码接收邮箱
_email_user = ''  #邮箱地址,例如team@sjbsjb.xyz
_email_pw = ''  #该邮箱地址的密码
_pop3_server = ''  #pop邮箱服务器的域名地址
_email_server = ''  #收件的邮箱地址,可以与_email_user相同

# 打开数据库连接
db = pymysql.connect(
    host="127.0.0.1",
    user="glass",
    password="",  #改我改我快改我
    database="glass")

_secret_hcap=''#hcap的人机验证api密钥,保密



def sql_re(sql, args=None):
    # '''有回复的mysql命令'''
    try:
        db.ping(reconnect=True)
        cursor = db.cursor()
        if args:
            cursor.execute(sql, args)
        else:
            cursor.execute(sql)

        # 获取所有记录列表
        results = cursor.fetchall()

        return results  #返回一个可迭代的行
    except:
        raise
        return False


def sql_no(sql, args=None):
    # '''无回复的mysql命令'''
    try:
        db.ping(reconnect=True)
        cursor = db.cursor()
        if args:
            cursor.execute(sql, args)
        else:
            cursor.execute(sql)

        db.commit()

        return True
    except:
        #错误时回滚
        db.rollback()
        raise
        return False


def send_email(email):
    key = randint(100000, 99999999)
    return str(key)


def yanzheng_email(key, email):
    # 连接到POP3服务器:
    server = poplib.POP3(_pop3_server)
    # 打开调试信息:
    server.set_debuglevel(1)

    # 身份认证:
    server.user(_email_user)
    server.pass_(_email_pw)

    # list()返回所有邮件的编号:
    resp, mails, octets = server.list()

    # 获取最新一封邮件, 注意索引号从1开始:
    index = len(mails)
    resp, lines, octets = server.retr(index)

    # 获得整个邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # 解析出邮件:
    msg = Parser().parsestr(msg_content)
    info = printMsg(msg)
    print(info, key, email)
    print('a', info[0] == email, info[1] == _email_server, info[2] == key)
    if info[0] == email and info[1] == _email_server and info[2] == key:
        return True
    return False


def yanzheng(key, ip):  #人机验证

    return True

    try:
        data = {'secret': _secret_hcap, 'response': key}
        re = requests.post("https://hcaptcha.com/siteverify", data=data).json()
        if re['success'] and re['hostname'] == ip:
            return True
        else:
            return False
    except:
        return False

def real_yanzheng(key, ip):
    try:
        data = {'secret': _secret_hcap, 'response': key,'remoteip':ip}
        re = requests.post("https://hcaptcha.com/siteverify", data=data).json()
        print(re)
        if re['success']:
            return True
        else:
            return False
    except:
        return False


def ip_city(ip):  #查询ip归属地
    city = requests.get('http://ip-api.com/json/%s' % ip).json()
    return '%s %s' % (city.get('countryCode'), city.get('region'))


def fenci(text):
    a = jieba.cut_for_search(text)
    # c = []
    # for b in a:
    #     c.append(''.join(SnowNLP(b).pinyin))
    # d = ' '.join(c)

    d = b' '.join(
        map(base64.b64encode, map(lambda c: bytes(c, encoding='utf8'), a)))
    return str(d, encoding='utf8')


# def yanzheng_code(code, user_id):
#     try:
#         sql = '''SELECT two_step_key FROM user_key WHERE id=%s;'''
#         secret_key = sql_re(sql, user_id)[0][0]
#         if secret_key:
#             t = pyotp.TOTP(secret_key)
#             result = t.verify(code)
#             return result
#         return False
#     except:
#         return False


def printMsg(msg):
    value = ['', '', '']
    i = 0
    for header in ['From', 'To', 'Subject']:
        value[i] = msg.get(header, '')
        if value[i]:
            if header == 'Subject':
                value[i] = decode_str(value[i], value)
            else:
                hdr, addr = parseaddr(value[i])
                value[i] = u'%s' % addr
        i += 1
    return value


def decode_str(s, value):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


# print(sql_re('SELECT COUNT(*) FROM user_info;'))

# print(fenci('你TM的就是个大傻逼'))