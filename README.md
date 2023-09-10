# GlassWallpaper
![0](/pic/0.png)
> 本作品荣获 2022年杭州市学生信息素养提升实践活动程序设计项目作品 一等奖
## 创作思想（创作背景、目的和意义）
Windows系统自Vista版本以来就不再提供动态壁纸的支持。但随着科技的进步，电脑硬件逐步升级换代，现在的硬件早已不会因为动态壁纸的运行而卡顿。Glass Wallpaper(以下简称Glass)完美支持Windows 10(x64)系统运行动态桌面壁纸。完善自Windows Vista系统以来无法使用动态壁纸的缺陷，满足人们对电脑桌面的高端DIY美化的需求。
## 创作过程（运用了哪些技术或技巧完成主题创作，哪些是得意之处）
Glass内置VLC/OPENCV解码器支持软解码和硬解码，适配更多机型，对资源的消耗更小。Glass本地壁纸播放采用列表式轮回播放，完善传统壁纸软件单一手动切换壁纸的难题。Glass界面采用亚克力毛玻璃特效，更加附有科技感。Glass拥有自己的Linux公网服务器，客户端可以通过“工坊”来下载服务器Mysql数据库中的壁纸资源。Glass拥有完善的用户系统，可注册或登入Glass账号来完成同步。Glass服务端动态资源在遭受DDoS攻击时，会自动筛选可疑用户进行hCaptcha人机验证，静态资源由Cloudflare CDN缓存，缓解服务器压力。Glass采用https协议与服务器进行通讯。Glass内置大量受欢迎的人工智能库作为Glass MOD，可以将图片或视频转化为动漫风格，通过摄像机捕获面部来驱动一张动漫图片中的人物，手绘简易风景转化为真实风景图，动漫风格图片超高清重建。
## 原创部分
Glass壁纸播放引擎核心代码，壁纸窗体嵌套桌面窗体部分，工坊内容，前后端通讯，Glass用户系统，后端Mysql数据库检索逻辑，本地资源的检索存储，客户端页面设计，与深度学习MOD交互部分，Glass官网
## 参考资源（参考或引用他人资源及出处）
工坊内所有视频MP4资源素材来源于Minecraft游戏录制
## 制作用软件及运行环境
制作软件：Python3，Mysql5.5
运行环境：
客户端：Windows 10 (x64)，一张英伟达显卡(可不选，但人工智能MOD库效率会降低)，CUDA10.2环境
服务端：Linux Centos7，Mysql5.5，Python3.9，Miniconda
## 其他说明（需要特别说明的问题）
更为详细的内容请参阅《软件使用说明书》《源代码说明》以及《服务端客户端部署》。
帮助邮箱:support@sjbsjb.xyz
Glass官方网站：https://glass.sjbsjb.xyz



----------
# Glass客户端和服务端安装部署篇

![0](/pic/0.png)
## 客户端:
测试机环境:
		系统: Windows 10(x64) 专业版 21H2
		显卡: NVIDIA GeForce RTX 2060 Super
		内存: 16G DDR4
		CPU: Intel I7-9700K
	(仅作参考,请尽量保持一致)
为了确保Glass部分人工智能MOD库能正常调用显卡资源,请在启动Glass前配置CUDA10.1环境.若您没有英伟达显卡(暂不支持AMD显卡),则可跳过本篇客户端环境部署,直接安装并运行Glass,部分人工智能MOD库将会使用您的CPU进行计算(请注意,仅CPU环境下人工智能MOD库效率将会十分低下,部分可能会出现兼容性问题,请最好使用英伟达显卡!)

1.您可以在比赛压缩包中的”客户端”文件夹中找到cuda_10.2.89_win10_network.exe文件,打开并安装它(由于CUDA镜像在境外,下载速度可能有些慢,请耐心等待).您也可以访问英伟达官网
https://developer.nvidia.com/cuda-10.2-download-archive?target_os=Windows&target_arch=x86_64&target_version=10
来进行安装,安装程序会自动配置系统PATH环境

![1](/pic/Glass客户端和服务端安装部署篇/1.png)

2.安装完成后,打开比赛压缩包中”客户端”文件夹中的Setup.exe并按照上面的指示完成Glass客户端安装.您也可以访问Glass官网进行下载安装

![2](/pic/Glass客户端和服务端安装部署篇/2.png)

3.双击打开桌面图标即可运行

## 服务端
测试机环境:
		系统: Linux Centos 7
		CPU: AMD Ryzen 9 5950X 16-Core
请注意,客户端默认使用api.sjbsjb.xyz域名与Glass官方服务器通讯,若想让客户端与您使用的第三方服务端通讯,您可以修改客户端源代码get.py中的第7行”_yuming”变量中的字符串变为您的域名/IP,然后重新打包编译客户端源代码
由于Glass通讯采用https协议,传统修改hosts方法可能会引起证书错误而拒绝连接.若您不希望重新打包Glass客户端,您可以使用中间人攻击法,伪造CA证书,然后让Glass客户端与您的服务器获得正常连接

部署正片:

1.使用ssh服务登入Centos的root用户(这边用Xshell作为演示) 
测试机环境:
		系统: Linux Centos 7
		CPU: AMD Ryzen 9 5950X 16-Core
请注意,客户端默认使用api.sjbsjb.xyz域名与Glass官方服务器通讯,若想让客户端与您使用的第三方服务端通讯,您可以修改客户端源代码get.py中的第7行”_yuming”变量中的字符串变为您的域名/IP,然后重新打包编译客户端源代码
由于Glass通讯采用https协议,传统修改hosts方法可能会引起证书错误而拒绝连接.若您不希望重新打包Glass客户端,您可以使用中间人攻击法,伪造CA证书,然后让Glass客户端与您的服务器获得正常连接

部署正片:

1.使用ssh服务登入Centos的root用户(这边用Xshell作为演示) 

![3](/pic/Glass客户端和服务端安装部署篇/3.png)

![4](/pic/Glass客户端和服务端安装部署篇/4.png)

2.键入命令
yum install -y wget && wget -O install.sh http://download.bt.cn/install/install_6.0.sh && sh install.sh
来进行宝塔Linux面板的安装,你也可以访问宝塔官网进行下载https://www.bt.cn/
安装期间可能要键入y来许可安装
3.安装成功后依据上面的提示,进入面板,并进行验证

![5](/pic/Glass客户端和服务端安装部署篇/5.png)

4.选择左侧导航栏,软件商店,搜索”mysql”并安装,选择版本为5.5 

![6](/pic/Glass客户端和服务端安装部署篇/6.png)

5.安装完成后进入左侧导航栏的”数据库”,然后添加数据库,名称glass,用户名glass,密码随意,但你要记着(后面会添加linux的glass用户,与mysql用户是分离的,不要搞混)

![7](/pic/Glass客户端和服务端安装部署篇/7.png)

6.进入左侧导航栏的安全,然后端口出输入8880,备注随便写点,点放行.然后再同理放行3306端口以便连接Mysql数据库

![8](/pic/Glass客户端和服务端安装部署篇/8.png)

7.切回xshell,输入命令useradd -d /home/glass -m glass来创建一个名为glass的linux用户
8.输入passwd glass,然后再键入你想要设置的密码,请记住,此为linux的glass用户,与mysql的glass用户不一样,分离的
9.完成后,使用命令mysql -h 127.0.0.1 -u glass -p然后键入mysql的glass用户密码

![9](/pic/Glass客户端和服务端安装部署篇/9.png)

10.输入USE glass; 来进入glass数据库
11.然后输入

`CREATE TABLE user_info(id int NOT NULL AUTO_INCREMENT,
name char(10) NOT NULL,
fabu_id_ok BOOL NOT NULL,
zhuce_time DATETIME NOT NULL,
zhuce_time_ok BOOL NOT NULL,
love_ok BOOL NOT NULL,
be_guanzhu_id_ok BOOL NOT NULL,
guanzhu_ok  BOOL NOT NULL,
head_pic BLOB NULL,
PRIMARY KEY (id))ENGINE=InnoDB;`


`CREATE TABLE user_key(id INT NOT NULL AUTO_INCREMENT,
key_1 char(45) NOT NULL,
email char(25) NOT NULL,
two_step BOOL NOT NULL,
tow_step_key char(70) NULL,
PRIMARY KEY (id))ENGINE=InnoDB;`



`CREATE TABLE user_auto(id INT NOT NULL AUTO_INCREMENT,
last_time DATETIME NOT NULL,
last_ip CHAR(20) NOT NULL,
last_city CHAR(6) NOT NULL,
cookie CHAR(25) NULL,
quanxian BOOL NOT NULL,
PRIMARY KEY (id))ENGINE=InnoDB;`

`CREATE TABLE ziyuan(id INT NOT NULL AUTO_INCREMENT,
fenlei CHAR(5) NOT NULL,
fenbianlv CHAR(10) NOT NULL,
title CHAR(20) NOT NULL,
zuozhe CHAR(10) NOT NULL,
user_id INT NOT NULL,
size INT NOT NULL,
format CHAR(7) NOT NULL,
pinglun_num INT NOT NULL,
time DATETIME NOT NULL,
way TINYTEXT NOT NULL,
liulan BLOB NOT NULL,
sou CHAR(45) NOT NULL,
PRIMARY KEY (id),
FULLTEXT(sou))ENGINE=MyISAM;`



`CREATE TABLE pinglun(id INT NOT NULL AUTO_INCREMENT,
ziyuan_id INT NOT NULL,
user_id INT NOT NULL,
pingfen FLOAT NOT NULL,
text TINYTEXT NULL,
time DATETIME NOT NULL,
PRIMARY KEY (id))ENGINE=InnoDB;`

`CREATE TABLE user_guanzhu(id INT NOT NULL AUTO_INCREMENT,
be_guanzhu_id INT NOT NULL,
guanzhu_id INT NOT NULL,
time DATETIME NOT NULL,
PRIMARY KEY (id))ENGINE=InnoDB;`





`CREATE TABLE love(id INT NOT NULL AUTO_INCREMENT,
leixing BOOL NOT NULL,
id_1 INT NOT NULL,
user_id INT NOT NULL,
time DATETIME NOT NULL,
PRIMARY KEY (id))ENGINE=InnoDB;`

`CREATE TABLE jubao(id INT NOT NULL AUTO_INCREMENT,
leixing BOOL NOT NULL,
id_1 INT NOT NULL,
user_id INT NOT NULL,
text TINYTEXT NULL,
time DATETIME NOT NULL,
PRIMARY KEY (id))ENGINE=InnoDB;`

来创建一些必要的表
12.使用命令INSERT INTO ziyuan(feilei,fenbianlv,title,zuozhe,user_id,size,format,pingfen,pinglun_num,love_num,time,way,liulan,search) VALUE(<分类>,<分辨率>,<标题>,<作者>,<作者Glass ID> ,<文件大小B>,<文件格式(视频为vid,图片为pic>,<评分等级>,0 ,0 ,<当前时间YYYY-MM-DD HH:MM:SS> ,<资源下载地址> ,<资源预览图二进制>,”1”);
来插入一个新的资源,防止客户端因为服务端工坊无资源而报错,请自行修改<>为对应的内容
13.输入exit; 来退出Mysql回到Linux Bash
14.输入su glass切换到linux的glass用户
15.再输入cd ~ 进入glass的主目录
16.将比赛压缩包中”服务端”文件夹内的所有内容复制进linux glass用户的主目录中(/home/glass),并cd到该目录中取

![10](/pic/Glass客户端和服务端安装部署篇/10.png)

17.按照https://www.jianshu.com/p/a72566e539be上的教程部署Miniconda环境,部署成功后会有(base)开头

![11](/pic/Glass客户端和服务端安装部署篇/11.png)

18.使用pip3 install -r requirements.txt来安装一些glass服务端必要的依赖库

19.使用vim way.py然后键入字符“i”来进入文本编辑模式
20.使用小键盘中的上下左右定位到第21行，修改password变量中的字符串为您mysql中的glass用户密码
21.请您再同理修改当前文件第12行至15行的变量，安装右侧注释来修改，来完成注册验证码收件邮箱的配置

![12](/pic/Glass客户端和服务端安装部署篇/12.png)

19.最后的最后使用python3 main.py运行服务端主程序
20.如果客户端能正确解析到您的服务器的话,那么就可以访问了
21.以下的步骤您可以选择性部署,到现在位置glass客户端已经可以正常访问您的服务端了
22.如果您拥有一个属于自己的域名可以像glass官方服务器一样将域名的名称服务器指向cloudflare(以下简称”cf”)或是将子域的CNAME解析到cf
23.在cf中进入自己的域名,再进入DNS解析页面

![13](/pic/Glass客户端和服务端安装部署篇/13.png)

24).点击右侧”添加记录”,添加一个A解析,名称为”apis”,IPV4为你的服务器公网IP,保存.
25.然后再左侧导航栏中进入规则-页面规则,再点击”创建页面规则”
26.输入的网址参照下图,将主域修改为您的主域,边缘缓存TTL,时间1个月,保存部署

![14](/pic/Glass客户端和服务端安装部署篇/14.png)

27.大功告成,部署CDN加速主要是为了缓存一些资源,以缓解glass服务器静态资源的压力

# Glass软件说明书
本文档主要介绍Glass客户端详细功能,在此之前,请参阅《客户端服务端部署》完成对Glass客户端的CUDA环境部署(当然,您也可以选择直接安装Glass客户端,但在您使用人工智能MOD库是效率将会十分低下)

打开比赛压缩包中客户端的Setup.exe安装文件,请仔细阅读Glass使用协议以及开放代码许可,若您同意Glass使用协议,请勾选我接受协议,并点击下一步.若不同意,请退出
   
选择安装路径,然后点击下一步
 
稍作等待Glass已经开始安装,您可以喝杯咖啡,回来它就安装完成了
安装完成后启动Glass主程序,桌面上会有快捷方式
如果显示弹出此窗口就代表Glass已经成功启动了
 

在本地页面中您可以点击图片来在右侧查看资源详细信息
 
您可以点击取消订阅来删除该资源,请注意该操作不会删除源文件,仅删除记录
界面下侧是壁纸播放列表,壁纸会按照播放列表中的顺序播放,您可以点击”打开”来添加本地图片视频资源,也可以点击删除,将选中的资源移除播放列表,还可以点击加入,将当前选中的资源加入播放列表.
Glass内置一些优秀的人工智能库,您可以在右侧资源详细信息中向下滑看到MOD栏
动漫风格转换器: 您可以选中一幅图片资源,点击”图片转化为动画”右侧的按钮,并稍作等待就可以在本地资源中看到新增了一个动漫风格资源.请注意,若图片原本就是动漫风格,请勿二次转化,否则得到的图片风格将会很奇怪

动漫风格转换器2: 您可以选中一个本地视频资源,点击”视频转化为动漫” 右侧的按钮,并稍作等待就可以在本地资源中看到新增了一个动漫风格视频资源.请注意,若视频原本就是动漫风格,请勿二次转化,否则得到的视频风格将会很奇怪,另外Glass原本内置的视频不支持视频转动漫,因为它们原本就是动漫风格的

虚拟形象驱动: 通过摄像机捕获面部关键点来驱动一张动漫人物图像,您可以导入并选择一张128*128像素并且带有透明通道的PNG类型图像,该图片的动漫人物必须处于图像中央位置,背景必须为透明(非白色!),然后点击”虚拟图像驱动”右侧的按钮,等待10秒左右的初始化即可在壁纸左下角看到被驱动的动漫形象.请注意,若您戴有眼镜,则可能会因为反光等原因而导致眼部追踪不精确,出现眼部驱动误差.此外,若您导入的图片大小或背景不规范,Glass将会报错
示范:
您可以导入Glass安装目录中的ziyuans文件夹中的图片资源
 
其中,最后的5张图片就是虚拟形象驱动地示例图,导入它们
 
点击”启动”即可在左下角看到,这是您可以面对摄像机摇头晃脑眨眼睛,体验虚拟形象驱动的感觉
 



风景图像合成器: 将一副简单手绘的单一色调图转化为真实的风景图象,即使您是一个画画小白,它也能让你画出惊艳的真实风景图.直接点击右侧”风景图生成器”右侧按钮,然后Glass会弹出一个新的窗口
 
您可以选择左侧调色盘中的画面元素在左侧画板中进行绘画,默认底色元素为”天空”,然后点击右侧渲染.请注意,请耐心等待渲染过程,请不要连续点击渲染按钮,否则可能会导致显存溢出而报错
 
若您对您画的图像感到满意,可以点击下面的添加到Glass Wallpaper,然后你的本地资源库中就会多一幅漂亮的风景图
 
如果您觉得该图片分辨率过低,您还可以点击右侧”图像超分辨率重建”的按钮,来进行AI图像超高清恢复,该功能主要适用于动漫风格的低分辨率图像.这时您就可以发现本地资源库多了一个非常清晰的风景图,画面的分辨率提高2K多的分辨率
 
对于图像超分辨率重建,Glass提供两种不同的引擎,其一是上述所用的realesrgan引擎,对于细节化处理较差,但是整体提升效果很好,适用于分辨率严重过低的图片.其二是中国bilibili开发的RealCUGAN动漫图像重构引擎,整体效果较好.

RealCUGAN引擎还提供视频超分辨率重建,您可以将右侧MOD栏滑到底即可看到这最后一项MOD功能,这对动漫类型的视频画质起到极大的改善
 


Glass拥有属于自己的壁纸工坊,内置大量壁纸资源,您可以选择自己心意的资源,然后点击右侧的订阅按钮,下载进度将显示在左侧资源标题上(由于Glass官方服务器位于境外,显示速度可能有些慢,还请耐心等待)
 
Glass工坊将保持资源稳步更新,可能您现在在Glass工坊中看到的页面资源数量会与上面示例图不符,另外,Glass工坊中的资源皆来源于Minecraft游戏中录制

此外,若您喜欢该资源,则可点击右侧详情栏中喜欢按钮,在这之前您必须拥有并登入Glass账号,才能进行 喜欢 操作.您还可以在登入后对资源进行评分,评分按钮紧靠喜欢按钮
 

点击上侧选项卡”我”即可显示用户界面
 

在此,您可以登入,您也可以使用您自己的邮箱来注册一个Glass账号,密码皆用SHA-1加密上传至Glass服务器,保存到Glass数据库中
 
点击下一步,发送以下文本到Glass官方邮箱进行邮箱验证
 
验证邮件发送完成后点击”我已发送”,Glass将会检查您的邮件验证码是否匹配,若成功则会自动跳转到个人主页
主页中您可以看到您最近 喜欢 过的所有资源,并同步到服务器数据库中.您可以在您的其他设备中登入Glass账号看到该账号所喜欢的资源.非常方便快捷
 
在设置页面中您可以进行一些Glass基本设置
 

其他说明:
1.Glass由Cloudflare提供CDN加速服务以及域名解析
2.程序中有些”sjbsjb233”、”sjb”的字样(包括域名中也出现”sjb”),这是沈俊百(ShenJunbai)的简拼(sjb)也是我的网名,请不要误会.
3.Glass唯一域名是api.sjbsjb.xyz,用于客户端与Glass官方服务器通讯中
4.由于Glass官方服务器部署在境外,所以与其连接的时候速度会有些慢,还请谅解.有时也可能出现无法与Glass官方服务器连接的情况,可能是因为境外线路不稳定或是处于高峰期流量被Qos,请等待一些时间后再次尝试连接.
5.由IP Geolocation API提供网络IP归属地查询API服务,Glass服务端用此记录用户的登入地点
6.由hCaptain提供人机验证网络API,减少Glass服务器动态资源过度消耗,拦截恶意刷Glass账号以及Glass账号暴力破解
7.工坊资源由NFT Storage提供存储和下载服务,以缓解Glass官方服务器压力,Glass官方服务器数据库仅存储资源基本信息,资源预览图,以及资源NFT Storage下载链接
# Glass源代码篇
本文件夹内容为Glass客户端源代码，Glass服务端源代码在比赛项目压缩包主目录中的“服务端”文件夹中（服务端本来就因没有打包而闭源）
Glass将在比赛结束后将源代码以 “GPL开源协议“ 发布到Github和Gitee中，并保持维护，为开源社区贡献一份力

若要打包请使用pip3安装必要的库，参照源代码的import语句来安装对应的库

