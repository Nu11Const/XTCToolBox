![logo](https://s1.ax1x.com/2022/07/08/jB3IsJ.png)

> XTCToolBoxV3项目，是一个使用C++,Qt,CMake开发的可视化ADB程序,V3版仍在开发中，会有许多Bug，发现Bug请提交到Issue。

# 程序编译

## Windows

请安装好Qt，理论上任何版本都行，但为了不会出错，建议安装6.31版本(Stable最新版)

在这里下载:https://www.qt.io/download-thank-you

EXE直链:https://d13lb3tujbc8s0.cloudfront.net/onlineinstallers/qt-unified-windows-x64-4.4.1-online.exe

Qt安装Mingw版。

![image](https://s1.ax1x.com/2022/07/08/jB3OJK.png)

确认配置好Mingw,CMake,Qt的环境变量，开始编译。

在项目根目录执行:

```bash
cmake --build .\build --config Debug --target all
```

再打开Qt命令行，输入

```bash
cd bin & windeployqt 
```

然后进入build文件夹，把EXE文件拖入命令行，按下回车。

最后自行配置ADB环境即可使用。

## Linux

> >暂不支持。

## 关于已知Bug

1. 字体如果有空格，程序将自动设置宋体。
