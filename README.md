# Ubuntu_reboot_auto_login  

永在线小脚本！电脑开机后进ubuntu系统之后不用输密码就可以自动联网并开启teamviewer，这样就可以直接远程。还设置了检测掉线后自动拨号联网(深大用的是DRcom)。若远程把远程的teamviewer关掉之后也不会GG，会自动重启然后把一切恢复。也就是只要你电脑还连着可以上网的网线，你就能通过teamviewer远程上你的电脑。  

|Author|苏一休|
|---|---
|E-mail|2270678755@qq.com  

![image](https://ae01.alicdn.com/kf/H676fffff7c384439aaa4124f082647994.gif)

## 缘由  

其实很早之前就写了个自动联网的脚本，但那时谁会想到得在家呆上4个月啊？？？所以并没有在实验室电脑上部署，只是开了Teamviewer然后就回家了。但蛋疼的事情来了，在家一次远程中因为我笔记本鼠标卡了，我一顿Alt+F4关一些窗口然后直接把实验室的Teamviewer关掉了！！！！！！那时是2月1号，根本没有人回学校，那叫一个叫天天不应叫地地不灵，我电脑又是接路由器的，所以IP什么的我压根没记，更别说通过旁边座位的人的电脑IP推出我的IP。所以很蛋疼得在笔记本上装了ubuntu，我笔记本显卡真的吐了，卢本伟很难受！所以就想搞个关于联网的和启动Teamviewer的脚本。今天备份代码所以把东西放github上。

## 搭建与部署  

先下载这份东西到一个目录

```Bash
git clone https://github.com/Suyixiu/Ubuntu_reboot_auto_login.git
```

修改/etc/rc.local

```Bash
sudo gedit /etc/rc.local
```

在exit 0之前添加这份东西中的Ubuntu_reboot_auto_login.sh的路径

```Bash
su -c '你下载这个包的路径/Ubuntu_reboot_auto_login.sh' 你ubuntu要登录的用户名 &
```

即完成了这个脚本的部署，接下来是修改一些脚本中的路径。你需要修改的地方有下面这些，首先是Ubuntu_reboot_auto_login.sh中的`你下载这个包的路径`改为你下载这个包的路径:neutral_face:

```Bash
#!/bin/bash
gsettings set org.gnome.system.proxy mode 'none'
time=$(date "+%Y%m%d-%H%M%S")
echo "${time}" > 你下载这个包的路径/test_run.log
/usr/bin/python3.5 你下载这个包的路径/Ubuntu_reboot_auto_login.py 2>你下载这个包的路径/py_run.log
```  

随后修改Ubuntu_reboot_auto_login.py中的一些东西，首先是`你的DRcom账号和密码`  

```python
data = {"DDDDD": "你的DRcom账号", "upass": "你的DRcom密码", ........}
```

其次是`你下载这个包的路径`改为你下载这个包的路径:neutral_face:

```python
if(os.system(u"ping www.baidu.com -c 1 > 你下载这个包的路径/ping.log") != 0):
    print("offline")

os.system("teamviewer > 你下载这个包的路径/teamviewer_run.log")
```

填写你要登录的ubuntu的用户的账号和密码  

```python
os.system("echo 你的ubuntu密码| sudo -S reboot")

if(offline_count == 0 and os.system("ps -u 你的ubuntu账号 | grep TeamViewer") != 0):
```

设置检测掉线和teamviewer线程是否存在的时间间隔，这里是60秒

```python
time.sleep(60)
```

改好上述配置之后记得把你的Ubuntu_reboot_auto_login.sh给chmod成777

```Bash
sudo chmod 777 你下载这个包的路径/Ubuntu_reboot_auto_login.sh
```  

如果没什么问题的话应该就大功告成了

## 文件说明  

* ping.log用于存放ping的结果
* python_run.log用于记录Ubuntu_reboot_auto_login.py运行的输出，如果py文件部分有问题可以看这个文件
* teamviewer_run.log用于记录teamviewer启动的log文件
* test.log用于测试开启自启是否成功运行脚本，如果成功运行则此文件中存放系统开机执行rc.local的时间

## 测试与运行  

先别重启先，把检测时间改小以方便测试，这里改成三秒`time.sleep(3)`。直接运行Ubuntu_reboot_auto_login.py看有木有出错。如果没有问题，网络也连着的话终端会打印`good`。teamviewer也会自动打开。

* 手动退出teamviewer，你会看到不到一会儿它又重启了。这说明保持teamviewer开启状态功能OK
* 拔掉网线，终端会打印`offline`，在打不到5次之前把网线插回去则会继续打印`good`。这说明检测网络连通性功能OK
* 注销DRcom账号，终端会打印一次`offline`随后自动拨号然后就登上了，随后继续打印`good`。这说明掉线重连功能OK
* 设置代理为手动然后是一个不正常的地址(模拟你远程的电脑挂了代理之后断网)，终端会打印`offline`5次之后重启，重启后查看此时的代理若变成`无`则说明恢复代理设置功能OK。
* 拔掉网线，不插回去，终端打印了5次`offline`之后笔记本会重启。这说明出现不可代码解决的问题时重启电脑功能OK
* 登录，查看`你下载这个包的路径/test_run.log`中是否有你的开机的时间记录。若有则说明这份东西开机自启么的问题
* 不登录，在输入密码界面的时候远程teamviewer它看能不能连上，若连上则说明这份脚本运行正常
* 看重启之后teamviewer是否开启，网络是否连通，一切是否正常。若没啥毛病则这份脚本的所有功能正常

若想关闭这份东西则直接调出ubuntu的系统监视器，搜索Ubuntu_reboot_auto_login然后杀死这个py就好了。如果出现了什么问题则看那几个log慢慢找问题。这是可能用到的几个链接  
[解决rc.local不执行脚本问题](https://blog.csdn.net/liuwinner/article/details/91040565)  
[python调用ubuntu命令行](https://www.cnblogs.com/hujq1029/p/7096247.html)

## 原理  
就很简单，就是一顿检测然后调命令行。DRcom登录部分用的request的post，检测网络连通性用的ping，检测teamviewer线程则直接用的命令行。

## 最后说明  

* 这是一份很简单的脚本实现了很实在的需求，网络账号掉线，Teamviewer炸掉，代理GG这些都是我遇到过的问题，因此就搞了这份东西咯。
* 这一切的前提都是你**电脑是连着一根能上网的网线**，村里没通网还搞个锤子🔨的远程。要是路由器炸了或者说网线断了或者说没网那在部署了我这份脚本之后你的电脑将一直不断得重启，重启间隔是你设置查询间隔的5倍。还是那句话**村里没通网还搞个锤子🔨的远程**。
* Enjoy！
