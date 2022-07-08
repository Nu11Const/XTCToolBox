import os
import sys
import time

def installapps():
    apk = input("请输入apk路径:")
    print("正在安装")
    os.popen("adb install " + apk)
    print("安装完毕")
    time.sleep(3)
    main()
    os.system("cls")

def screenrecord():
    log = input("是否打开log?输入y/n:")
    re = input("请确认录制位置:")
    listtime = input("视频录制秒数：")
    log = str(log)
    if ("y" in log):
        os.system("adb shell screenrecord  --time-limit" + " " + listtime + " " + "--verbose" + " " + re)
        os.popen("adb pull " + re + " " + os.getcwd())
        print("视频已导出，请前往" + os.getcwd() + "查看")
        os.system("explorer " + os.getcwd())
        main()
        os.system("cls")
    else:
        os.system("adb shell screenrecord  --time-limit" + " " + listtime + " " + re)
        os.popen("adb pull " + re + " " + os.getcwd())
        print("视频已导出，请前往" + os.getcwd() + "查看")
        os.system("explorer " + os.getcwd())
        time.sleep(5)
        main()
        os.system("cls")

def screenshot():
    os.system("adb shell screencap -p /sdcard/1.jpg")
    os.popen("adb pull /sdcard/1.jpg" + " " + os.getcwd())
    os.system("explorer " + os.getcwd())
    print("截图已经保存到" + os.getcwd())
    main()
    os.system("cls")

def toolbox():
    print("1.打开指定应用 2.打开输入法选择 3.打开自检")
    print("4.打开开发者选项（阉割) 5.返回主页面 6.调整dpi")
    个性控制 = input("请输入您的选择:")
    个性控制 = str(个性控制)
    if (个性控制 == "1"):
        start = input("请输入包名:")
        start2 = input("请输入Activity:")
        os.popen("adb shell am start -n " + start + "/" + start2)
        print("启动成功")
        main()
        os.system("cls")
    if (个性控制 == "2"):
        os.popen("adb shell am start -n com.baidu.input.xtcime/com.baidu.input.xtcime.demo.SettingActivity")
        print("启动成功")
        main()
        os.system("cls")
    if (个性控制 == "3"):
        os.popen("adb shell am start -n com.xtc.selftest/com.xtc.selftest.MainActivity")
        print("启动成功")
        main()
        os.system("cls")
    if (个性控制 == "4"):
        os.popen("adb shell am start com.xtc.setting/com.xtc.setting.module.dev.activity.DevMainActivity")
        print("打开成功")
        main()
        os.system("cls")
    if (个性控制 == "6"):
        dpi = input("请输入DPI数值：")
        os.popen("adb shell wm density " + dpi)
        print("切换成功")
        main()
        os.system("cls")

def files():
    print("1.文件提取 2.文件导入")
    file = input("请输入您的选择：")
    file = int(file)
    if (file == '1'):
        watch = input("请输入在手表的文件地址：")
        pc = input("请输入目标地址：")
        pc.replace("\"", "/")
        os.system("adb pull " + watch + " " + pc)
        print("提取到" + pc)
        os.popen("explorer " + pc)
        time.sleep(3)
        main()
        os.system("cls")
    if (file == '2'):
        pc = input("请输入要导入的文件:")
        watch = input("请输入目标地址:")
        os.system("adb push " + pc + " " + watch)
        print("导入到" + watch)
        time.sleep(3)
        main()
        os.system("cls")

def colors():
    os.system("color /?")
    color = input("帮助文件已打开，请输入颜色:")
    color = "color " + color
    os.system("del color.txt")
    os.system("echo " + color + ">color.txt")

def tcpipconnect():
    a = os.popen('adb shell netcfg wlan0')
    ip = (a[10:22])
    os.popen("adb tcpip 5555")
    time.sleep(2)
    os.system("adb connect " + ip)
    print("连接成功")
    time.sleep(5)
    main()
    os.system("cls")

def commmand():
    print("输入main退出")
    while 3 > 2:
        command = input("命令行>")
        os.system(command)

def pythoncommand():
    while True:
        x = input("(python) >")
        if x in globals().keys():
            print(globals()[x])
            continue
        if(x == "exit"):
            main()
        try:
            exec(x)
        except Exception as err:
            print(err)

def installupdate():
    print("正在检查更新......")
    url = 'https://gitee.com/smart-rice/xtctool-box/raw/master/updates.txt'  # 设置网站路径
    check = os.popen("curl " + url).read()
    if (check > version):
        print("目前有最新版本，版本号为" + check, "请问是否安装？")
        question = input("输入y/n:")
        question = str(question)
        if (question == "y"):
            print("正在连接到服务器")
            server = os.popen("curl https://gitee.com/smart-rice/xtctool-box/raw/master/servers.txt").read()
            os.system("downloader " + server)
            print("安装程序已经开始，请检查您的任务栏")
            os.system("Setup.exe")
    else:
        print("没有新的更新，5秒后返回主界面")
        time.sleep(5)
        main()

def connect():
    print("请插入设备，插入后按回车键退出重开")
    pause = input("")
    connectbl = os.popen("adb devices").read()
    次数 = connectbl.count("device")
    if (次数 == 2):
        os.system("cls")
        main()
    if (次数 == 1):
        connect()

def main():
    print("XTCToolBox 1.1 Release")
    print("欢迎进入XTCToolBox")
    print("---------------------")
    print("1.安装应用      2.录屏")
    print('3.截屏          4.退出')
    print("5.个性控制      6.文件管理")
    print("7.窗口设置      8.有线转无线")
    print('9.命令行        10.软件更新')
    print('11.查看设备连接情况')
    zcx = input("请输入您的选择:")
    zcx = str(zcx)
    if(zcx == "1"):
        installapps()
    if(zcx == 2):
        screenrecord()
    if(zcx == 3):
        screenshot()
    if(zcx == 4):
        exit()
    if(zcx == 5):
        toolbox()
    if(zcx == 6):
        files()
    if(zcx == 7):
        pass

if __name__=='__main__':
    main()
