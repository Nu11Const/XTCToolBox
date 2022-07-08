#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <iostream>
#include <windows.h>
#include <stdio.h>
#include <thread>
#include <fstream>
#include <QMessageBox>
#include <QFileDialog>
#include <QDebug>
#include <thread>
#include<QThread>

void loadStyle(const QString &qssFile){
    //加载样式表
    QString qss;
    QFile file(qssFile);
    if (file.open(QFile::ReadOnly)) {
        //用QTextStream读取样式文件不用区分文件编码 带bom也行
        QStringList list;
        QTextStream in(&file);
        //in.setCodec("utf-8");
        while (!in.atEnd()) {
            QString line;
            in >> line;
            list << line;
        }

        file.close();
        qss = list.join("\n");
        QString paletteColor = qss.mid(20, 7);
        qApp->setPalette(QPalette(paletteColor));
        qApp->setStyleSheet(qss);
    }
}

MainWindow::MainWindow(QWidget *parent)

    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    loadStyle(":/qss/lightblue.css");
    //stackedWidget = new QStackedWidget;
    AllocConsole();    //为调用进程分配一个新的控制台
    std::fstream _file;
 
	std::string path = "lang.ini";
 
	_file.open(path, std::ios::in);
	if (!_file)
	{
		QMessageBox::critical(this,"程序内部错误！",tr("no"));
	}
	else
	{
	    while(_file>>buf)
	    {
		    QFont font = this->font();
            font.setFamily(buf);
            auto listWidget = findChildren<QWidget*>();
            for (auto& widget : listWidget)
            {
                widget->setFont(font);
            }
	    }
	}
    _file.close();
    font_change();
    ShowWindow(GetConsoleWindow(), SW_HIDE);    //隐藏自己创建的控制台
}

MainWindow::~MainWindow()
{
    delete ui;
}






void MainWindow::on_commandLinkButton_clicked()
{
    std::string     output;
    FILE*           data    = popen("adb get-state"," r");
    for(char c = getc(data);c != EOF;c = getc(data))
    {
        output  += c;
    }
    pclose(data);
    std::string::size_type idx;
    idx=output.find("device");
    if(idx == std::string::npos)
    {
        ui->plainTextEdit->document()->setPlainText("设备未连接");
    } else {
        std::string     output;
        FILE*           data    = popen("adb shell getprop ro.product.brand"," r");
        for(char c = getc(data);c != EOF;c = getc(data))
        {
            output  += c;
        }
        pclose(data);
        //分割
        std::string product = output;
        std::string     output1;
        FILE*           data1    = popen("adb shell getprop ro.product.model"," r");
        for(char c = getc(data1);c != EOF;c = getc(data1))
        {
            output1  += c;
        }
        pclose(data1);
        std::string model = output1;
        //分割
        std::string     output2;
        FILE*           data2   = popen("adb shell getprop ro.build.version.release"," r");
        for(char c = getc(data2);c != EOF;c = getc(data2))
        {
            output2  += c;
        }
        pclose(data2);
        std::string release = output2;
        std::string pretext = ("设备已经连接\n设备品牌:"+product+"设备型号:"+model+"设备系统版本:"+release);
        const char* text = pretext.data();
        ui->plainTextEdit->document()->setPlainText(text);

    }
}

void MainWindow::on_pushButton_3_clicked()
{
    system("adb reboot 2> xtc.log");
    std::ifstream in("xtc.log");
        if (!in) {
            std::cerr << "error in in" << std::endl;
        } else {
            std::cerr << "successfully open in file" << std::endl;
            std::string s;
            while (in >> s) {
                std::string::size_type idx;
                idx=s.find("error");
                if(idx == std::string::npos)
                {
                    std::cout << "";
                } else {
                    QMessageBox::critical(this,"错误",tr("未连接设备"));
                }
        }
    }
}

void MainWindow::on_pushButton_4_clicked()
{
    system("adb reboot fastboot 2> xtc.log");
    std::ifstream in("xtc.log");
        if (!in) {
            std::cerr << "error in in" << std::endl;
        } else {
            std::cerr << "successfully open in file" << std::endl;
            std::string s;
            while (in >> s) {
                std::string::size_type idx;
                idx=s.find("error");
                if(idx == std::string::npos)
                {
                    std::cout << "";
                } else {
                    QMessageBox::critical(this,"错误",tr("未连接设备"));
                }
        }
    }
}

void MainWindow::on_pushButton_5_clicked()
{
    system("adb reboot bootloader 2> xtc.log");
    std::ifstream in("xtc.log");
        if (!in) {
            std::cerr << "error in in" << std::endl;
        } else {
            std::cerr << "successfully open in file" << std::endl;
            std::string s;
            while (in >> s) {
                std::string::size_type idx;
                idx=s.find("error");
                if(idx == std::string::npos)
                {
                    std::cout << "";
                } else {
                    QMessageBox::critical(this,"错误",tr("未连接设备"));
                }
        }
    }
}

void MainWindow::on_pushButton_6_clicked()
{
    system("adb reboot edl 2> xtc.log");
    std::ifstream in("xtc.log");
        if (!in) {
            std::cerr << "error in in" << std::endl;
        } else {
            std::cerr << "successfully open in file" << std::endl;
            std::string s;
            while (in >> s) {
                std::string::size_type idx;
                idx=s.find("error");
                if(idx == std::string::npos)
                {
                    std::cout << "";
                } else {
                    QMessageBox::critical(this,"错误",tr("未连接设备"));
                }
        }
    }
}

void MainWindow::on_pushButton_clicked()
{
    QString str = ui->comboBox->currentText();//获取comboBox选项
    std::string boxtext = str.toStdString();
    QString str1 = ui->lineEdit->text();
    std::string linetext = str1.toStdString();
    if(boxtext == "普通"){
        std::string command = "adb install "+linetext;
        const char *charmand = command.c_str();
        std::string     output2;
        FILE*           data2   = popen(charmand," r");
        for(char c = getc(data2);c != EOF;c = getc(data2))
        {
            output2  += c;
        }
        pclose(data2);
        std::string::size_type idx;
        idx=output2.find("XTC-Company");
        if(idx == std::string::npos){

        } else {
            QMessageBox::critical(this,"错误",tr("连接设备为XTC设备！请确认SBoot是否正确安装！"));
        }
    } else if(boxtext == "覆盖") {
        std::string command = "adb install -r "+linetext;
        const char *charmand = command.c_str();
        std::string     output2;
        FILE*           data2   = popen(charmand," r");
        for(char c = getc(data2);c != EOF;c = getc(data2))
        {
            output2  += c;
        }
        pclose(data2);
        std::string::size_type idx;
        idx=output2.find("XTC-Company");
        if(idx == std::string::npos){

        } else {
            QMessageBox::critical(this,"错误",tr("连接设备为XTC设备！请确认SBoot是否正确安装！"));
        }
    } else {
        QMessageBox::critical(this,"程序内部错误！",tr("错误代码0x000a，请将报错以及照片发送给作者！"));
        system("start https://vmtask.top/archives/11.html");
        Sleep(1000);
        abort();
    }
}

void MainWindow::on_actionsh_triggered(){
    system("adb shell screencap -p /sdcard/test.png");
    system("adb pull /sdcard/test.png screen.png");
    system("screen.png");
}
void MainWindow::on_action_5_triggered(){
    system("start https://vmtask.top");
}
void MainWindow::on_pushButton_2_clicked()
{
    QString sPath = QFileDialog::getOpenFileName(this,"文件对话框",".","安装包(*.apk);;");
    std::string filebak = sPath.toStdString();
    const char *filename = filebak.c_str();
    ui->lineEdit->setText(filename);
}

void MainWindow::on_pushButton_7_clicked()
{
    std::string     output;
    FILE*           data    = popen("adb get-state"," r");
    for(char c = getc(data);c != EOF;c = getc(data))
    {
        output  += c;
    }
    pclose(data);
    std::string::size_type idx;
    idx=output.find("device");
    if(idx == std::string::npos)
    {
        QMessageBox::critical(this,"错误",tr("未连接设备！"));
    } else {
        ui->stackedWidget->setCurrentWidget(ui->stackedWidgetPage1);
    }
}

void MainWindow::on_pushButton_8_clicked()
{
    std::string     output;
    FILE*           data    = popen("adb get-state"," r");
    for(char c = getc(data);c != EOF;c = getc(data))
    {
        output  += c;
    }
    pclose(data);
    std::string::size_type idx;
    idx=output.find("device");
    if(idx == std::string::npos)
    {
        QMessageBox::critical(this,"错误",tr("未连接设备！"));
    } else {
        ui->stackedWidget->setCurrentWidget(ui->stackedWidgetPage2);
    }
}
void MainWindow::on_actionADB_triggered(){
    system("start cmd.exe");
}
void MainWindow::on_action_3_triggered(){
    form->show();

}
/*void MainWindow::on_action_5_triggered(){
    system("start https://vmtask.top");
}*/

void MainWindow::on_pushButton_10_clicked()
{
    QString sPath = QFileDialog::getOpenFileName(this,"文件对话框",".","所有文件(*);;");
    std::string filebak = sPath.toStdString();
    const char *filename = filebak.c_str();
    ui->lineEdit_2->setText(filename);
}
void pushFile()
{

}
void MainWindow::on_pushButton_11_clicked()
{
    QMessageBox::warning(this,"提醒！",tr("大文件会卡死！请耐心等待"));
    QString str1 = ui->lineEdit_2->text();
    std::string linetext1 = str1.toStdString();
    std::string command = "adb push "+linetext1+" /sdcard/";
    const char *comrun = command.c_str();
    system(comrun);
}

void MainWindow::on_pushButton_12_clicked()
{
    QMessageBox::warning(this,"提醒！",tr("大文件会卡死！请耐心等待"));
    QString str1 = ui->lineEdit_3->text();
    std::string linetext1 = str1.toStdString();
    std::string command = "adb pull "+linetext1+" .";
    const char *comrun = command.c_str();
    system(comrun);
    QMessageBox::information(this,"提醒！",tr("下载完毕"));
}

void MainWindow::on_pushButton_13_clicked()
{
    system("adb shell reboot -p 2> xtc.log");
    std::ifstream in("xtc.log");
        if (!in) {
            std::cerr << "error in in" << std::endl;
        } else {
            std::cerr << "successfully open in file" << std::endl;
            std::string s;
            while (in >> s) {
                std::string::size_type idx;
                idx=s.find("error");
                if(idx == std::string::npos)
                {
                    std::cout << "";
                } else {
                    QMessageBox::critical(this,"错误",tr("未连接设备"));
                }
                idx=s.find("found");
                if(idx == std::string::npos)
                {
                    std::cout << "";
                } else {
                    QMessageBox::critical(this,"错误",tr("未连接设备"));
                }
        }
    }
}

void MainWindow::on_pushButton_14_clicked()
{
    int num1 = ui->spinBox->value();
    int num2 = ui->spinBox->value();
    std::string comstring = "adb shell wm size "+std::to_string(num1)+"x"+std::to_string(num2);
    const char *comrun = comstring.c_str();
    system(comrun);
}

void MainWindow::on_pushButton_9_clicked()
{
    std::string     output;
    FILE*           data    = popen("adb get-state"," r");
    for(char c = getc(data);c != EOF;c = getc(data))
    {
        output  += c;
    }
    pclose(data);
    std::string::size_type idx;
    idx=output.find("device");
    if(idx == std::string::npos)
    {
        QMessageBox::critical(this,"错误",tr("未连接设备！"));
    } else {
        ui->stackedWidget->setCurrentWidget(ui->stackedWidgetPage3);
        std::string     fbl;
        FILE*           data    = popen("adb shell wm size"," r");
        for(char c = getc(data);c != EOF;c = getc(data))
        {
            fbl  += c;
        }
        pclose(data);
        std::string     dpi;
        FILE*           data1    = popen("adb shell wm density"," r");
        for(char c = getc(data1);c != EOF;c = getc(data1))
        {
            dpi  += c;
        }
        pclose(data1);
        std::string pretext = "当前DPI情况:"+dpi+"\n当前分辨率状态:"+fbl;
        const char* text = pretext.data();
        ui->plainTextEdit_2->document()->setPlainText(text);
    }
}

void MainWindow::on_pushButton_15_clicked()
{
    int num1 = ui->spinBox_3->value();
    std::string comstring = "adb shell wm density "+std::to_string(num1);
    const char *comrun = comstring.data();
    system(comrun);
}

void MainWindow::on_pushButton_16_clicked()
{
    system("adb shell wm size reset");
}

void MainWindow::on_pushButton_17_clicked()
{
    system("adb shell wm density reset");
}

void MainWindow::on_pushButton_18_clicked()
{
    std::string     output;
    FILE*           data    = popen("adb get-state"," r");
    for(char c = getc(data);c != EOF;c = getc(data))
    {
        output  += c;
    }
    pclose(data);
    std::string::size_type idx;
    idx=output.find("device");
    if(idx == std::string::npos)
    {
        QMessageBox::critical(this,"错误",tr("未连接设备！"));
    } else {
        ui->stackedWidget->setCurrentWidget(ui->stackedWidgetPage4);
        std::string     output;
        FILE*           data    = popen("adb shell dumpsys battery"," r");
        for(char c = getc(data);c != EOF;c = getc(data))
        {
            output  += c;
        }
        pclose(data);
        const char* text = output.data();
        ui->plainTextEdit_3->document()->setPlainText(text);
    }
}

void MainWindow::on_pushButton_21_clicked()
{
    system("adb shell dumpsys battery reset");
    QMessageBox::information(this,"提示",tr("完成重置"));
    std::string     output;
    FILE*           data    = popen("adb shell dumpsys battery"," r");
    for(char c = getc(data);c != EOF;c = getc(data))
    {
        output  += c;
    }
    pclose(data);
    const char* text = output.data();
    ui->plainTextEdit_3->document()->setPlainText(text);
}

void MainWindow::on_pushButton_19_clicked()
{
    int num1 = ui->spinBox_4->value();
    std::string pretext = "adb shell dumpsys battery set level "+std::to_string(num1);
    const char *text = pretext.data();
    system(text);
    std::string     output;
    FILE*           data    = popen("adb shell dumpsys battery"," r");
    for(char c = getc(data);c != EOF;c = getc(data))
    {
        output  += c;
    }
    pclose(data);
    const char* text1 = output.data();
    ui->plainTextEdit_3->document()->setPlainText(text1);
}

void MainWindow::on_checkBox_stateChanged(int arg1)
{
    if(arg1 == 2){
        system("adb shell dumpsys battery set status 1");
        std::string     output;
        FILE*           data    = popen("adb shell dumpsys battery"," r");
        for(char c = getc(data);c != EOF;c = getc(data))
        {
            output  += c;
        }
        pclose(data);
        const char* text = output.data();
        ui->plainTextEdit_3->document()->setPlainText(text);
    }
}

void MainWindow::on_checkBox_2_stateChanged(int arg1)
{
    if(arg1 == 2){
        system("adb shell dumpsys battery set wireless 1");
        std::string     output;
        FILE*           data    = popen("adb shell dumpsys battery"," r");
        for(char c = getc(data);c != EOF;c = getc(data))
        {
            output  += c;
        }
        pclose(data);
        const char* text = output.data();
        ui->plainTextEdit_3->document()->setPlainText(text);
    }
}

void MainWindow::on_checkBox_3_stateChanged(int arg1)
{
    if(arg1 == 2){
        system("adb shell dumpsys battery set usb 1");
        std::string     output;
        FILE*           data    = popen("adb shell dumpsys battery"," r");
        for(char c = getc(data);c != EOF;c = getc(data))
        {
            output  += c;
        }
        pclose(data);
        const char* text = output.data();
        ui->plainTextEdit_3->document()->setPlainText(text);
    }
}

void MainWindow::on_checkBox_4_stateChanged(int arg1)
{
    if(arg1 == 2){
        system("adb shell dumpsys battery set ac 1");
        std::string     output;
        FILE*           data    = popen("adb shell dumpsys battery"," r");
        for(char c = getc(data);c != EOF;c = getc(data))
        {
            output  += c;
        }
        pclose(data);
        const char* text = output.data();
        ui->plainTextEdit_3->document()->setPlainText(text);
    }
}


void MainWindow::on_pushButton_23_clicked()
{
    QString text = ui->lineEdit_5->text();
    std::string pretext = text.toStdString();
    std::string command = "adb connect "+pretext;
    const char *comrun = command.data();
    system("adb tcpip 5555");
    system(comrun);
    std::string     output;
    FILE*           data    = popen("adb get-state"," r");
    for(char c = getc(data);c != EOF;c = getc(data))
    {
        output  += c;
    }
    pclose(data);
    std::string::size_type idx;
    idx=output.find("device");
    if(idx == std::string::npos)
    {
        QMessageBox::critical(this,"错误",tr("连接失败！"));
    } else {
        QMessageBox::information(this,"提示",tr("连接成功，请拔下数据线。"));
    }
}


void MainWindow::on_pushButton_22_clicked()
{
    QString text = ui->lineEdit_4->text();
    std::string pretext = text.toStdString();
    std::string comtext = "adb connect "+pretext;
    const char *comrun = comtext.data();
    std::string     output;
    FILE*           data    = popen(comrun," r");
    for(char c = getc(data);c != EOF;c = getc(data))
    {
        output  += c;
    }
    pclose(data);
    std::string::size_type idx;
    idx=output.find("cannot");
    if(idx == std::string::npos){
        QMessageBox::information(this,"提示",tr("连接成功"));
    } else {
        QMessageBox::warning(this,"提示",tr("连接失败"));
    }
}


void MainWindow::on_pushButton_20_clicked()
{
     ui->stackedWidget->setCurrentWidget(ui->stackedWidgetPage5);
}


void MainWindow::on_commandLinkButton_2_clicked()
{
    int num1 = ui->spinBox_5->value();
    qDebug()<<num1;
    std::string pretext = "adb shell screenrecord /sdcard/launch.mp4 --time-limit "+std::to_string(num1);
    system(pretext.data());
    qDebug()<<num1*1000;
    QThread::sleep(num1*1000+1000);
    system("adb pull /sdcard/launch.mp4 .");
    system("adb shell rm /sdcard/launch.mp4");
    system("launch.mp4");
}


void MainWindow::on_pushButton_24_clicked()
{
    std::string     output;
    FILE*           data    = popen("adb get-state"," r");
    for(char c = getc(data);c != EOF;c = getc(data))
    {
        output  += c;
    }
    pclose(data);
    std::string::size_type idx;
    idx=output.find("device");
    if(idx == std::string::npos)
    {
        QMessageBox::critical(this,"错误",tr("未连接设备！"));
    } else {
        ui->stackedWidget->setCurrentWidget(ui->stackedWidgetPage6);
    }
}


void MainWindow::on_pushButton_30_clicked()
{
    QString str = ui->lineEdit_6->text();
    std::string str1 = "adb shell am start -n "+str.toStdString();
    system(str1.data());
    QMessageBox::information(this,"提示",tr("打开成功"));
}


void MainWindow::on_pushButton_25_clicked()
{
    std::string     output;
    FILE*           data    = popen("adb get-state"," r");
    for(char c = getc(data);c != EOF;c = getc(data))
    {
        output  += c;
    }
    pclose(data);
    std::string::size_type idx;
    idx=output.find("device");
    if(idx == std::string::npos)
    {
        QMessageBox::critical(this,"错误",tr("未连接设备！"));
    } else {
        ui->stackedWidget->setCurrentWidget(ui->stackedWidgetPage7);
    }
}


void MainWindow::on_pushButton_26_clicked()
{
    system("adb shell am start -n com.baidu.input.xtcime/com.baidu.input.xtcime.demo.SettingActivity");
    QMessageBox::information(this,"提示",tr("打开成功"));
}



void MainWindow::on_pushButton_29_clicked()
{
    system("adb shell am start -n com.xtc.selftest/com.xtc.selftest.MainActivity");
    QMessageBox::information(this,"提示",tr("打开成功"));
}


void MainWindow::on_pushButton_27_clicked()
{
    system("adb shell am start com.xtc.setting/com.xtc.setting.module.dev.activity.DevMainActivity");
    QMessageBox::information(this,"提示",tr("打开成功"));
}


void MainWindow::on_pushButton_28_clicked()
{
    system("start cmd.exe");
}
void MainWindow::on_action_2_triggered(){
    form1->show();
}
void MainWindow::font_change(){
    QFont font;
    font.setPointSize(35);
    ui->label->setFont(font);
    font.setPointSize(15);
    ui->plainTextEdit->setFont(font);
    ui->label_2->setFont(font);
    ui->label_3->setFont(font);
    ui->label_5->setFont(font);
    ui->label_6->setFont(font);
    ui->label_7->setFont(font);
    font.setPointSize(12);
    ui->plainTextEdit_2->setFont(font);
    font.setPointSize(15);
    ui->label_8->setFont(font);
    ui->label_12->setFont(font);
    font.setPointSize(12);
    ui->plainTextEdit_3->setFont(font);
    font.setPointSize(15);
    ui->label_10->setFont(font);
    ui->label_13->setFont(font);
    font.setPointSize(20);
    ui->label_14->setFont(font);
    ui->label_16->setFont(font);
    font.setPointSize(15);
    ui->label_17->setFont(font);
    ui->label_18->setFont(font);
}