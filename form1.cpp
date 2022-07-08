#include "form1.h"
#include "ui_form1.h"
#include<fstream>

Form1::Form1(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form1)
{
    ui->setupUi(this);
    setWindowFlags( (windowFlags() | Qt::CustomizeWindowHint) & ~Qt::WindowMaximizeButtonHint);
}

Form1::~Form1()
{
    delete ui;
}

void Form1::on_pushButton_clicked()
{
    QString str = ui->fontComboBox->currentText();
    qDebug()<<str;
    std::fstream ofs;
    ofs.open("lang.ini",std::ios::out);
    ofs<<str.toStdString();
    ui->pushButton->setFont(str);
    ofs.close();
}

