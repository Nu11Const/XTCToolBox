# XTCToolBox 2.0

## 1.注意事项

本软件采用Python3.7+PyQt5开发，请在运行之前准备好开发环境

### 2.编译运行
#### 1.安装Python
这个就不用讲解了吧
#### 2.安装PyQt5,win10toast,requests,rich,pyinstaller。

```bash
pip3 install PyQt5 win10toast requests rich pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple
```
如果已经安装过，可以忽略。
#### 3.打包
可以先直接运行，测试是否正常。

```bash
python3 main.py
```
打包命令：

```bash
pyinstaller -D -W -i ajfj2-yrv0f-002.ico main.py
```
之后就可以在dist文件夹查看文件并且运行了。
程序运行需要自备adb工具包，我自用ubuntu，这样安装:

```bash
sudo apt install adb
```
其他linux发行版自己去找对应版本的adb安装教程吧


