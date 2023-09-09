from os import getcwd
from flask import Flask, request, Response, make_response, send_from_directory
import json, way, time, base64
from datetime import datetime, date
from secrets import token_urlsafe


class ComplexEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


app = Flask(__name__)

email_yanzheng = {}  #用来存放邮箱验证码的临时储存{email:(key,time,way)}


def yanzheng(cookie):
    '''由cookie来验证账户,返回用户id和用户权限(1为管理)'''
    try:
        sql = '''SELECT id,quanxian FROM user_auto WHERE cookie=%s;'''
        user_1 = way.sql_re(sql, cookie)  #申请者id
        return user_1[0]

    except:
        pass


# @app.route('/get_page/<page>/<pailie>/<shuaixuan>', methods=['GET'])
# def get_page(page, pailie, shuaixuan):
#     '''获取页面资源'''
#     try:
#         page = int(page)
#         if shuaixuan == 'all':
#             sql = 'SELECT COUNT(*) FROM ziyuan;'
#             zongshu = way.sql_re(sql)[0][0]  #获取资源总数
#         else:
#             sql = 'SELECT COUNT(*) FROM ziyuan WHERE fenlei=\'%s\';'
#             zongshu = way.sql_re(sql, shuaixuan)[0][0]  #获取资源总数

#         if shuaixuan == 'all':
#             sql = '''SELECT id,fenlei,fenbianlv,title,zuozhe,user_id,size,format,pingfen,pinglun_num,love_num,time,download_way
#             FROM ziyuan ORDER BY %s LIMIT %s,%s;'''
#             ziyuan = way.sql_re(sql, (pailie, (page - 1) * 50, (page) * 50))
#         else:
#             sql = '''SELECT id,fenlei,fenbianlv,title,zuozhe,user_id,size,format,pingfen,pinglun_num,love_num,time,download_way
#             FROM ziyuan WHERE fenlei=\'%s\' ORDER BY %s LIMIT %s,%s;'''
#             ziyuan = way.sql_re(sql, (shuaixuan, pailie, (page - 1) * 50,
#                                       (page) * 50))

#         return json.dumps({
#             'zongshu': zongshu,
#             'ziyuan': ziyuan,
#             'now_page': page
#         })

#     except:
#         return '未知错误', 500


@app.route('/static/get_ziyuan/<id_1>', methods=['GET'])
def get_ziyuan(id_1):
    '''获取具体资源信息'''
    try:
        id_1 = int(id_1)
        sql = '''SELECT id,fenlei,fenbianlv,title,zuozhe,user_id
                ,size,format,time,way FROM ziyuan WHERE id=%s;'''
        ziyuan = way.sql_re(sql, id_1)[0]  #基本信息

        sql = '''SELECT AVG(pingfen) FROM pinglun WHERE ziyuan_id=%s;'''
        ziyuan2 = way.sql_re(sql, id_1)  #评分
        # print(ziyuan2,id_1)
        if ziyuan2[0][0]:
            ziyuan2 = ziyuan2[0]
        else:
            # print(ziyuan2,'efu')
            ziyuan2 = (0, )

        sql = '''SELECT COUNT(*) FROM love WHERE leixing=1 AND id_1=%s;'''
        ziyuan3 = way.sql_re(sql, id_1)  #喜欢数

        return json.dumps({'ziyuan': ziyuan + ziyuan2 + ziyuan3[0]},
                          cls=ComplexEncoder)
    except:
        raise
        return '未知错误', 500


@app.route('/static/ziyuan_pic/<id_1>', methods=['GET'])
def ziyuan_pic(id_1):
    '''获取资源预览图'''
    try:
        id_1 = int(id_1)
        sql = '''SELECT liulan 
                FROM ziyuan WHERE id=%s;'''
        ziyuan = way.sql_re(sql, id_1)
        # print()
        return json.dumps(
            {'pic': str(base64.b64encode(ziyuan[0][0]), encoding='utf8')})
    except:
        raise
        return '未知错误', 500


@app.route('/get_pinglun/<id_1>/<page>', methods=['GET'])
def get_pinglun(id_1, page):
    '''查看资源评论'''
    try:
        page = int(page)
        id_1 = int(id_1)
        sql = '''SELECT id,user_id,pingfen,time,text FROM pinglun WHERE ziyuan_id=%s ORDER BY time DESC LIMIT %s,%s;'''
        pinglun = way.sql_re(sql, (id_1, (page - 1) * 10, (page) * 10))

        return json.dumps({'pinglun': pinglun}, cls=ComplexEncoder)
    except:
        # raise
        return '未知错误', 500


@app.route('/del_pinglun/<id_1>', methods=['GET'])
def del_pinglun(id_1):
    '''删除评论'''
    try:
        id_1 = int(id_1)
        #验证身份
        cookie = request.cookies.get('cookie')
        user_1, quanxian = yanzheng(cookie, quanxian=True)

        sql = '''SELECT user_id FROM pinglun WHERE id=%s;'''
        user_2 = way.sql_re(sql, id_1)  #被删除者id

        if user_1 == user_2[0][0] or quanxian:
            sql = '''DELETE FROM pinglun WHERE id=%s;'''
            if way.sql_no(sql, id_1):
                return 'ok', 200
            return 'ok', 200

        return '权限不足', 500

    except:
        return '未知错误', 500


@app.route('/del_ziyuan/<id_1>', methods=['GET'])
def del_ziyuan(id_1):
    '''删除资源'''
    try:
        id_1 = int(id_1)
        #验证身份
        cookie = request.cookies.get('cookie')
        user_1, quanxian = yanzheng(cookie)  #申请者id

        sql = '''SELECT user_id FROM ziyuan WHERE id=%s;'''
        user_2 = way.sql_re(sql, id_1)  #被删除者id
        # print(user_2)

        if user_1 == user_2[0][0] or quanxian:
            sql = '''DELETE FROM ziyuan WHERE id=%s;'''
            if way.sql_no(sql, id_1):
                return 'ok', 200

        return '权限不足', 500

    except:
        # raise
        return '未知错误', 500


@app.route('/love_ziyuan/<id_1>', methods=['GET'])
def love_ziyuan(id_1):
    '''喜欢资源'''
    try:
        id_1 = int(id_1)
        #验证身份
        cookie = request.cookies.get('cookie')
        user_1 = yanzheng(cookie)[0]  #申请者id
        print(id_1, user_1, datetime.now())
        if user_1:
            sql = '''INSERT INTO love(leixing,id_1,user_id,time) VALUES(1,%s,%s,%s);'''
            if way.sql_no(sql, (id_1, user_1, datetime.now())):
                return 'ok', 200
        return '权限不足', 500
    except:
        return '未知错误', 500


@app.route('/get_love', methods=['GET'])
def get_love():
    '''查看喜欢资源'''
    try:
        #验证身份
        cookie = request.cookies.get('cookie')
        user_1 = yanzheng(cookie)[0]  #申请者id
        print(user_1, datetime.now())
        if user_1:
            sql = '''SELECT id_1 FROM love WHERE user_id=%s;'''
            info = way.sql_re(sql, user_1)

            return json.dumps({'key': info})
        return '权限不足', 500
    except:
        raise
        return '未知错误', 500


@app.route('/love_pinglun/<id_1>', methods=['GET'])
def love_pinglun(id_1):
    '''喜欢评论'''
    try:
        id_1 = int(id_1)
        #验证身份
        cookie = request.cookies.get('cookie')
        user_1, _ = yanzheng(cookie)  #申请者id
        if user_1:
            sql = '''INSERT INTO love(leixing,id_1,user_id,time) VALUES(0,%s,%s,%s);'''
            if way.sql_no(sql, (id_1, user_1, datetime.now())):
                return 'ok', 200
        return '权限不足', 500
    except:
        # raise
        return '未知错误', 500


@app.route('/send_pinglun', methods=['POST'])
def send_pinglun():
    '''发布评论'''
    try:
        id_1 = int(request.form['id'])
        #验证身份
        cookie = request.cookies.get('cookie')
        user_1 = yanzheng(cookie)[0]  #申请者id
        print(id_1, user_1, round(float(request.form['score']), 1),
              datetime.now(), request.form['text'])
        if user_1:
            sql = '''INSERT INTO pinglun(ziyuan_id,user_id,pingfen,time,text) VALUES(%s,%s,%s,%s,%s);'''
            if way.sql_no(
                    sql, (id_1, user_1, round(float(request.form['score']), 1),
                          datetime.now(), request.form['text'])):
                return 'ok', 200
        return '权限不足', 500
    except:
        raise
        return '未知错误', 500


@app.route('/jubao_pinglun', methods=['POST'])
def jubao_pinglun():
    '''举报评论'''
    try:
        id_1 = int(request.form['id'])
        #验证身份
        cookie = request.cookies.get('cookie')
        user_1 = yanzheng(cookie)  #申请者id
        if user_1:
            sql = '''INSERT INTO pinglun(leixing,id_1,user_id,time,text) VALUES(0,%s,%s,%s);'''
            if way.sql_no(
                    sql, (id_1, user_1, datetime.now(), request.form['text'])):
                return 'ok', 200
        return '权限不足', 500
    except:
        return '未知错误', 500


@app.route('/jubao_ziyuan', methods=['POST'])
def jubao_ziyuan():
    '''举报资源'''
    try:
        id_1 = int(request.form['id'])
        #验证身份
        cookie = request.cookies.get('cookie')
        user_1 = yanzheng(cookie)  #申请者id
        if user_1:
            sql = '''INSERT INTO pinglun(leixing,id_1,user_id,time,text) VALUES(1,%s,%s,%s);'''
            if way.sql_no(
                    sql, (id_1, user_1, datetime.now(), request.form['text'])):
                return 'ok', 200
        return '权限不足', 500
    except:
        return '未知错误', 500


@app.route('/static/head_pic/<id_1>', methods=['GET'])
def head_pic(id_1):
    '''获取用户头像'''
    try:
        id_1 = int(id_1)
        sql = '''SELECT head_pic 
                FROM ziyuan WHERE id=%s;'''
        ziyuan = way.sql_re(sql, id_1)

        return json.dumps(
            {'pic': base64.b64encode(bytes(ziyuan[0][0], encoding='utf8'))})
    except:
        return '未知错误', 500


@app.route('/user_info/<id_1>', methods=['GET'])
def user_info(id_1):
    '''用户信息'''
    try:
        id_1 = int(id_1)

        sql = '''SELECT id,name,fabu_id_ok,zhuce_time,zhuce_time_ok,
            love_ok,be_guanzhu_id_ok,guanzhu_ok FROM user_info WHERE id=%s;'''
        info = way.sql_re(sql, id_1)[0]
        re = dict()
        re['id'] = info[0]
        re['name'] = info[1]
        if info[2]:
            sql = '''SELECT id FROM ziyuan WHERE user_id=%s;'''
            ziyuan1 = way.sql_re(sql, id_1)
            if ziyuan1:
                re['fabu_id'] = ziyuan1
            else:
                re['fabu_id'] = None

        else:
            re['fabu_id'] = False  #false为禁止访问,None为没有
        if info[4]:
            re['zhuce_time'] = info[3]
        else:
            re['zhuce_time'] = False  #false为禁止访问,None为没有

        if info[5]:
            sql = '''SELECT id_1 FROM love WHERE user_id=%s AND leixing=1;'''
            ziyuan2 = way.sql_re(sql, id_1)

            if ziyuan2:
                re['love'] = ziyuan2
            else:
                re['love'] = None
        else:
            re['love'] = False  #false为禁止访问,None为没有

        if info[6]:
            sql = '''SELECT guanzhu_id FROM user_guanzhu WHERE be_guanzhu_id=%s;'''
            ziyuan3 = way.sql_re(sql, id_1)
            if ziyuan3:
                re['be_guanzhu_id'] = ziyuan3
            else:
                re['be_guanzhu_id'] = None
        else:
            re['be_guanzhu_id'] = False  #false为禁止访问,None为没有

        if info[7]:
            sql = '''SELECT be_guanzhu_id FROM user_guanzhu WHERE guanzhu_id=%s'''
            ziyuan4 = way.sql_re(sql, id_1)
            if ziyuan4:
                re['guanzhu'] = ziyuan4
            else:
                re['guanzhu'] = None
        else:
            re['guanzhu'] = False  #false为禁止访问,None为没有

        #用户被关注数
        sql = '''SELECT COUNT(*) FROM user_guanzhu WHERE be_guanzhu_id=%s;'''
        ziyuan5 = way.sql_re(sql, id_1)
        if ziyuan5:
            re['be_guanzhu_num'] = ziyuan5
        else:
            re['be_guanzhu_num'] = None

        return json.dumps(re)

    except:
        return '未知错误', 500


@app.route('/search/<count>/<pailie>/<shuaixuan>/<text>', methods=['GET'])
def search(count, pailie, shuaixuan, text):
    '''搜索资源count为具体id数'''
    try:
        count = int(count) - 1

        if shuaixuan == 'all':
            sql = '''SELECT id,title FROM ziyuan WHERE title LIKE %s ORDER BY %s LIMIT %s,%s;'''
            # print(
            #     '''SELECT id,title FROM ziyuan WHERE title LIKE %s ORDER BY %s LIMIT %s,%s;'''
            #     % ('%' + text + '%', pailie, count, 50))
            ziyuan = way.sql_re(sql, ('%' + text + '%', pailie, count, 50))
        else:
            sql = '''SELECT id,title FROM ziyuan WHERE fenlei=%s AND title LIKE %s ORDER BY %s LIMIT %s,%s;'''
            ziyuan = way.sql_re(
                sql, (shuaixuan, '%' + text + '%', pailie, count, 50))
        # print(ziyuan)
        # print(len(ziyuan))
        return json.dumps({
            'ziyuan': ziyuan,
        }, cls=ComplexEncoder)

    except:
        raise
        return '未知错误', 500


@app.route('/zongshu/<shuaixuan>/<text>', methods=['GET'])
def zongshu(shuaixuan, text):
    '''资源总数'''
    try:
        if shuaixuan == 'all':
            sql = 'SELECT COUNT(*) FROM ziyuan WHERE title LIKE %s;'
            zongshu = way.sql_re(sql, '%' + text + '%')[0][0]  #获取资源总数
        else:
            sql = 'SELECT COUNT(*) FROM ziyuan WHERE fenlei=%s AND title LIKE %s;'
            zongshu = way.sql_re(sql,
                                 (shuaixuan, '%' + text + '%'))[0][0]  #获取资源总数
        return json.dumps({'zongshu': zongshu})
    except:

        return '未知错误', 500


@app.route('/lianxiang/<text>', methods=['GET'])
def lianxiang(text):
    '''智能联想'''
    try:
        sql = '''SELECT title FROM ziyuan WHERE title LIKE %s ORDER BY time DESC LIMIT 7;'''
        # print(sql%'aa')
        ziyuan = way.sql_re(sql, '%' + text + '%')

        return json.dumps({'text': ziyuan})

    except:
        # raise
        return '未知错误', 500


@app.route('/static/download_file/<file>', methods=['GET'])
def download_file(file):
    pass


@app.route('/send_file', methods=['POST'])
def send_file():
    '''发布资源'''
    # print(base64.b64decode(bytes(request.form['liulan'],encoding='utf8')))
    try:
        if way.yanzheng(request.form['token'], request.remote_addr):
            user_id, _ = yanzheng(request.cookies.get('cookie'))

            sql = '''SELECT name FROM user_info WHERE id=%s;'''
            name = way.sql_re(sql, user_id)[0][0]

            sql = '''INSERT INTO ziyuan(fenlei,fenbianlv,title,zuozhe,user_id,size,
            format,time,way,liulan,sou) VALUE(%s,%s,%s,%s,
            %s,%s,%s,%s,%s,%s,%s);'''
            if way.sql_no(
                    sql,
                (
                    request.form['fenlei'],
                    request.form['fenbianlv'],
                    request.form['title'],
                    name,
                    user_id,
                    199999,  #尺寸是错的
                    request.form['format'],
                    datetime.now(),
                    'http://',
                    base64.b64decode(
                        bytes(request.form['liulan'], encoding='utf8')),
                    way.fenci(request.form['title']))):
                return 'ok'

        return '未知错误1', 500
    except:
        raise
        return '未知错误2', 500


@app.route('/login', methods=['POST'])
def login():
    '''登入'''
    try:
        email = request.form['email']
        key = request.form['key']
        sql = '''SELECT key_1,id FROM user_key WHERE email=%s;'''
        # print(way.sql_re(sql, email))
        key_2 = way.sql_re(sql, email)[0]
        if key == key_2[0]:
            cookie = token_urlsafe(16)  #生成一个cookie
            print(request.headers.get('Cf-Connecting-Ip'),
                  request.headers.get('Cf-Ipcountry'))
            sql = '''UPDATE user_auto SET cookie=%s,last_time=%s,last_ip=%s,last_city=%s WHERE id=%s;'''
            if way.sql_no(sql,
                          (cookie, datetime.now(),
                           request.headers.get('Cf-Connecting-Ip'),
                           request.headers.get('Cf-Ipcountry'), key_2[1])):
                res = make_response('ok')
                res.set_cookie('cookie', cookie)
                return res
            else:
                return '未知错误', 500
        else:
            return '电子邮件或密码错误1', 500

    except:
        raise
        return '电子邮件或密码错误2', 500


@app.route('/loginout', methods=['GET'])
def loginout():
    '''登出'''
    try:
        sql = '''UPDATE user_auto SET cookie=NULL WHERE cookie=%s;'''
        cookie = request.cookies.get('cookie')
        if way.sql_no(sql, cookie):
            return 'ok'
        else:
            return '未知错误1', 500

    except:
        return '未知错误2', 500


@app.route('/my_info', methods=['GET'])
def my_info():
    '''获取自己私人信息'''
    try:
        sql = '''SELECT id FROM user_auto WHERE cookie=%s;'''
        cookie = request.cookies.get('cookie')
        id_1 = way.sql_re(sql, cookie)[0][0]
        sql = '''SELECT * FROM user_info WHERE id=%s;'''
        info = way.sql_re(sql, id_1)[0]
        return json.dumps({'info': info}, cls=ComplexEncoder)
    except:
        # raise
        return '没有权限', 500


@app.route('/zhuce', methods=['POST'])
def zhuce():
    '''注册'''
    try:
        print(request.form, request.headers.get('Cf-Connecting-Ip'))
        step = request.form['step']
        if step == '1':  #如果当前处在第一部中
            print('第一步')
            if not way.yanzheng(
                    request.form['token'],
                    request.headers.get('Cf-Connecting-Ip')):  #比对人机验证码和ip
                return '人机验证失败', 500
            email = request.form['email']
            key = way.send_email(email)
            email_yanzheng[email] = (key, time.time(), 'zhuce')
            return json.dumps({'key': key})
        elif step == '2':
            print('第二部')
            print(request.form['email'], email_yanzheng[request.form['email']])
            print(time.time() - email_yanzheng[request.form['email']][1])

            # key = request.form['yanzheng_key']
            if email_yanzheng[request.form['email']][
                    2] == 'zhuce' and way.yanzheng_email(
                        email_yanzheng[request.form['email']][0],
                        request.form['email']) and time.time(
                        ) - email_yanzheng[request.form['email']][1] <= 600:
                print('验证通过')
                sql = '''INSERT INTO user_info(name,fabu_id_ok,zhuce_time,zhuce_time_ok,love_ok,
                be_guanzhu_id_ok,guanzhu_ok) VALUES(%s,%s,%s,%s,%s,%s,%s);'''
                if not way.sql_no(
                        sql,
                    (request.form['name'], 1, datetime.now(), 1, 1, 1, 1)):
                    return '未知错误1', 500

                sql = '''INSERT INTO user_key(key_1,email,two_step) VALUES(%s,%s,%s);'''
                if not way.sql_no(
                        sql, (request.form['key'], request.form['email'], 0)):
                    return '未知错误2', 500

                sql = '''INSERT INTO user_auto(last_time,last_ip,last_city,cookie,quanxian) VALUES(%s,%s,%s,%s,%s);'''
                if not way.sql_no(
                        sql,
                    (datetime.now(), request.headers.get('Cf-Connecting-Ip'),
                     request.headers.get('Cf-Ipcountry'), token_urlsafe(16),
                     0)):
                    return '未知错误3', 500
                return 'ok'
            return '邮箱验证失败', 500
        return '邮箱验证失败,没传入步数', 500
    except:
        raise
        return '未知错误4', 500


@app.route('/change_name', methods=['POST'])
def change_name():
    '''改变昵称,传入name'''
    try:
        user_id, _ = yanzheng(request.cookies.get('cookie'))
        sql = '''UPDATE user_info SET name=%s WHERE id=%s;'''
        if way.sql_no(sql, (request.form['name'], user_id)):
            return 'ok'
        return '未知错误1', 500
    except:
        return '未知错误2', 500


@app.route('/change_head_pic', methods=['POST'])
def change_head_pic():
    '''改变头像,传入二进制pic'''
    try:
        user_id, _ = yanzheng(request.cookies.get('cookie'))
        sql = '''UPDATE user_info SET head_pic=%s WHERE id=%s;'''
        if way.sql_no(sql, (base64.b64decode(
                bytes(request.form['pic'], encoding='utf8')), user_id)):
            return 'ok'
        return '未知错误1', 500
    except:
        return '未知错误2', 500


@app.route('/forget_key', methods=['POST'])
def forget_key():
    '''忘记密码'''
    try:
        pass
    except:
        return '未知错误', 500


@app.route('/test/test', methods=['GET'])
def test():
    '''用于测试,返回请求头信息'''
    a = (request.headers, request.cookies, request.remote_addr,
         request.remote_user)
    return str(a)


@app.route('/ok', methods=['GET'])
def ok():
    '''用于测试与服务器的通讯'''
    return 'ok'


@app.route('/static/news', methods=['GET'])
def news():
    '''显示服务器新闻'''

    return '''<div>测试测试,这是Glass服务器发来的文本</div>
    <div>    ----- From Glass Administrator'''


@app.route('/test/download_new', methods=['POST'])
def download_new():
    '''下载最新的程序'''
    ip = request.headers.get('Cf-Connecting-Ip')
    key = request.form['h-captcha-response']

    if way.real_yanzheng(key, ip):
        directory = getcwd()
        return send_from_directory(directory, 'Setup.exe', as_attachment=True)
    return '验证失败', 500


if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0', port='80')
