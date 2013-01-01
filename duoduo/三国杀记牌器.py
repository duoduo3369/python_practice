# -*- coding: utf-8 -*-  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *
import PyQt4
import sys  
  
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  
   
class Progess(QDialog):
    number = {'nan_man':3,'jue_dou':3,
              'guo_he':6,'shun_shou':5,
              'wu_xie':7,'tao':12} 
    def __init__(self,parent=None):  
        super(Progess,self).__init__(parent)
        self.setWindowTitle(self.tr("三国杀记牌器"))  
        self.layout=QGridLayout()
        self.clear()
        self.nan_man_progressbar_init(1)
        self.jue_dou_progressbar_init(4)
        self.guo_he_progressbar_init(7)
        self.shun_shou_progressbar_init()
        self.tao_progressbar_init()
        self.wu_xie_progressbar_init()
        self.tao_progressbar_init()

    def clear(self):
        clearButton = QPushButton(self.tr("重置"))
        self.layout.addWidget(clearButton)
        def do():
            self.reset(self.nan_man_progressBar,
                       self.nan_man_usedLineEdit,
                       self.nan_man_remainderLineEdit,
                       self.number.get('nan_man'))
            self.reset(self.jue_dou_progressBar,
                       self.jue_dou_usedLineEdit,
                       self.jue_dou_remainderLineEdit,
                       self.number.get('jue_dou'))
            self.reset(self.guo_he_progressBar,
                       self.guo_he_usedLineEdit,
                       self.guo_he_remainderLineEdit,
                       self.number.get('guo_he'))
            self.reset(self.tao_progressBar,
                       self.tao_usedLineEdit,
                       self.tao_remainderLineEdit,
                       self.number.get('tao'))
            self.reset(self.wu_xie_progressBar,
                       self.wu_xie_usedLineEdit,
                       self.wu_xie_remainderLineEdit,
                       self.number.get('wu_xie'))
            self.reset(self.shun_shou_progressBar,
                       self.shun_shou_usedLineEdit,
                       self.shun_shou_remainderLineEdit,
                       self.number.get('shun_shou'))
        self.connect(clearButton,SIGNAL("clicked()"),do)
    def reset(self,progressbar,usedEdit,remainderEdit,initNumber):
        progressbar.setValue(0)
        usedEdit.setText("0")
        remainderEdit.setText(str(initNumber))
    def nan_man_progressbar_init(self,fisrt_line=1):
        usedLabel=QLabel(self.tr("南蛮入侵"))
        self.nan_man_usedLineEdit=QLineEdit("0")        
        remainderLabel=QLabel(self.tr("剩余")) 
        self.nan_man_remainderLineEdit=QLineEdit(str(self.number.get('nan_man')))        
  
        self.nan_man_progressBar=QProgressBar()            
        self.nan_man_progressBar.setMinimum(0)  
        self.nan_man_progressBar.setMaximum(self.number.get('nan_man'))
        nan_man_startPushButton=QPushButton(self.tr("南蛮入侵"))        
          
        self.layout.addWidget(usedLabel,fisrt_line,0)  
        self.layout.addWidget(self.nan_man_usedLineEdit,fisrt_line,1)
        self.layout.addWidget(remainderLabel,fisrt_line,2)  
        self.layout.addWidget(self.nan_man_remainderLineEdit,fisrt_line,3)  
         
        self.layout.addWidget(self.nan_man_progressBar,fisrt_line+1,0,1,0)  
        self.layout.addWidget(nan_man_startPushButton,fisrt_line+2,0)  
        self.layout.setMargin(15)  
        self.layout.setSpacing(10)    
        self.setLayout(self.layout)            
        def increase():
            num=int(self.nan_man_usedLineEdit.text())+1
            if num > self.number.get('nan_man'):
                num = 0
                self.nan_man_progressBar.setValue(0)  
            for i in xrange(num):  
                    self.nan_man_progressBar.setValue(i+1)  
                    QThread.msleep(10)        
            self.nan_man_usedLineEdit.setText(str(num))
            self.nan_man_remainderLineEdit.setText(str(self.number.get('nan_man')-num))
            
        self.connect(nan_man_startPushButton,SIGNAL("clicked()"),increase)
    
    def jue_dou_progressbar_init(self,fisrt_line=4):
        
        usedLabel=QLabel(self.tr("决斗"))
        self.jue_dou_usedLineEdit=QLineEdit("0")        
        remainderLabel=QLabel(self.tr("剩余")) 
        self.jue_dou_remainderLineEdit=QLineEdit(str(self.number.get('jue_dou')))        
  
        self.jue_dou_progressBar=QProgressBar()            
        self.jue_dou_progressBar.setMinimum(0)  
        self.jue_dou_progressBar.setMaximum(self.number.get('jue_dou'))
        jue_dou_startPushButton=QPushButton(self.tr("决斗"))        
          
        self.layout.addWidget(usedLabel,fisrt_line,0)  
        self.layout.addWidget(self.jue_dou_usedLineEdit,fisrt_line,1)
        self.layout.addWidget(remainderLabel,fisrt_line,2)  
        self.layout.addWidget(self.jue_dou_remainderLineEdit,fisrt_line,3)  
         
        self.layout.addWidget(self.jue_dou_progressBar,fisrt_line+1,0,1,0)  
        self.layout.addWidget(jue_dou_startPushButton,fisrt_line+2,0)  
        self.layout.setMargin(15)  
        self.layout.setSpacing(10)    
        self.setLayout(self.layout)            
        def increase():
            num=int(self.jue_dou_usedLineEdit.text())+1
            if num > self.number.get('jue_dou'):
                num = 0
                self.jue_dou_progressBar.setValue(0)  
            for i in xrange(num):  
                    self.jue_dou_progressBar.setValue(i+1)  
                    QThread.msleep(10)        
            self.jue_dou_usedLineEdit.setText(str(num))
            self.jue_dou_remainderLineEdit.setText(str(self.number.get('jue_dou')-num))
        self.connect(jue_dou_startPushButton,SIGNAL("clicked()"),increase)
    
    def guo_he_progressbar_init(self,fisrt_line=7):
        
        usedLabel=QLabel(self.tr("过河拆桥"))
        self.guo_he_usedLineEdit=QLineEdit("0")        
        remainderLabel=QLabel(self.tr("剩余")) 
        self.guo_he_remainderLineEdit=QLineEdit(str(self.number.get('guo_he')))        
  
        self.guo_he_progressBar=QProgressBar()            
        self.guo_he_progressBar.setMinimum(0)  
        self.guo_he_progressBar.setMaximum(self.number.get('guo_he'))
        guo_he_startPushButton=QPushButton(self.tr("过河拆桥"))        
          
        self.layout.addWidget(usedLabel,fisrt_line,0)  
        self.layout.addWidget(self.guo_he_usedLineEdit,fisrt_line,1)
        self.layout.addWidget(remainderLabel,fisrt_line,2)  
        self.layout.addWidget(self.guo_he_remainderLineEdit,fisrt_line,3)  
         
        self.layout.addWidget(self.guo_he_progressBar,fisrt_line+1,0,1,0)  
        self.layout.addWidget(guo_he_startPushButton,fisrt_line+2,0)  
        self.layout.setMargin(15)  
        self.layout.setSpacing(10)    
        self.setLayout(self.layout)            
        def increase():
            num=int(self.guo_he_usedLineEdit.text())+1
            if num > self.number.get('guo_he'):
                num = 0
                self.guo_he_progressBar.setValue(0)  
            for i in xrange(num):  
                    self.guo_he_progressBar.setValue(i+1)  
                    QThread.msleep(10)        
            self.guo_he_usedLineEdit.setText(str(num))
            self.guo_he_remainderLineEdit.setText(str(self.number.get('guo_he')-num))
        self.connect(guo_he_startPushButton,SIGNAL("clicked()"),increase)

    def shun_shou_progressbar_init(self,fisrt_line=10):
        
        usedLabel=QLabel(self.tr("顺手牵羊"))
        self.shun_shou_usedLineEdit=QLineEdit("0")        
        remainderLabel=QLabel(self.tr("剩余")) 
        self.shun_shou_remainderLineEdit=QLineEdit(str(self.number.get('shun_shou')))        
  
        self.shun_shou_progressBar=QProgressBar()            
        self.shun_shou_progressBar.setMinimum(0)  
        self.shun_shou_progressBar.setMaximum(self.number.get('shun_shou'))
        guo_he_startPushButton=QPushButton(self.tr("顺手牵羊"))        
          
        self.layout.addWidget(usedLabel,fisrt_line,0)  
        self.layout.addWidget(self.shun_shou_usedLineEdit,fisrt_line,1)
        self.layout.addWidget(remainderLabel,fisrt_line,2)  
        self.layout.addWidget(self.shun_shou_remainderLineEdit,fisrt_line,3)  
         
        self.layout.addWidget(self.shun_shou_progressBar,fisrt_line+1,0,1,0)  
        self.layout.addWidget(guo_he_startPushButton,fisrt_line+2,0)  
        self.layout.setMargin(15)  
        self.layout.setSpacing(10)    
        self.setLayout(self.layout)            
        def increase():
            num=int(self.shun_shou_usedLineEdit.text())+1
            if num > self.number.get('shun_shou'):
                num = 0
                self.shun_shou_progressBar.setValue(0)  
            for i in xrange(num):  
                    self.shun_shou_progressBar.setValue(i+1)  
                    QThread.msleep(10)        
            self.shun_shou_usedLineEdit.setText(str(num))
            self.shun_shou_remainderLineEdit.setText(str(self.number.get('shun_shou')-num))
        self.connect(guo_he_startPushButton,SIGNAL("clicked()"),increase)
        
    def wu_xie_progressbar_init(self,fisrt_line=13):
        
        usedLabel=QLabel(self.tr("无懈可击"))
        self.wu_xie_usedLineEdit=QLineEdit("0")        
        remainderLabel=QLabel(self.tr("剩余")) 
        self.wu_xie_remainderLineEdit=QLineEdit(str(self.number.get('wu_xie')))        
  
        self.wu_xie_progressBar=QProgressBar()            
        self.wu_xie_progressBar.setMinimum(0)  
        self.wu_xie_progressBar.setMaximum(self.number.get('wu_xie'))
        guo_he_startPushButton=QPushButton(self.tr("无懈可击"))        
          
        self.layout.addWidget(usedLabel,fisrt_line,0)  
        self.layout.addWidget(self.wu_xie_usedLineEdit,fisrt_line,1)
        self.layout.addWidget(remainderLabel,fisrt_line,2)  
        self.layout.addWidget(self.wu_xie_remainderLineEdit,fisrt_line,3)  
         
        self.layout.addWidget(self.wu_xie_progressBar,fisrt_line+1,0,1,0)  
        self.layout.addWidget(guo_he_startPushButton,fisrt_line+2,0)  
        self.layout.setMargin(15)  
        self.layout.setSpacing(10)    
        self.setLayout(self.layout)            
        def increase():
            num=int(self.wu_xie_usedLineEdit.text())+1
            if num > self.number.get('wu_xie'):
                num = 0
                self.wu_xie_progressBar.setValue(0)  
            for i in xrange(num):  
                    self.wu_xie_progressBar.setValue(i+1)  
                    QThread.msleep(10)        
            self.wu_xie_usedLineEdit.setText(str(num))
            self.wu_xie_remainderLineEdit.setText(str(self.number.get('wu_xie')-num))
        self.connect(guo_he_startPushButton,SIGNAL("clicked()"),increase)
        
    def tao_progressbar_init(self,fisrt_line=16):
        
        usedLabel=QLabel(self.tr("桃"))
        self.tao_usedLineEdit=QLineEdit("0")        
        remainderLabel=QLabel(self.tr("剩余")) 
        self.tao_remainderLineEdit=QLineEdit(str(self.number.get('tao')))        
  
        self.tao_progressBar=QProgressBar()            
        self.tao_progressBar.setMinimum(0)  
        self.tao_progressBar.setMaximum(self.number.get('tao'))
        guo_he_startPushButton=QPushButton(self.tr("桃"))        
          
        self.layout.addWidget(usedLabel,fisrt_line,0)  
        self.layout.addWidget(self.tao_usedLineEdit,fisrt_line,1)
        self.layout.addWidget(remainderLabel,fisrt_line,2)  
        self.layout.addWidget(self.tao_remainderLineEdit,fisrt_line,3)  
         
        self.layout.addWidget(self.tao_progressBar,fisrt_line+1,0,1,0)  
        self.layout.addWidget(guo_he_startPushButton,fisrt_line+2,0)  
        self.layout.setMargin(15)  
        self.layout.setSpacing(10)    
        self.setLayout(self.layout)            
        def increase():
            num=int(self.tao_usedLineEdit.text())+1
            if num > self.number.get('tao'):
                num = 0
                self.tao_progressBar.setValue(0)  
            for i in xrange(num):  
                    self.tao_progressBar.setValue(i+1)  
                    QThread.msleep(10)        
            self.tao_usedLineEdit.setText(str(num))
            self.tao_remainderLineEdit.setText(str(self.number.get('tao')-num))
        self.connect(guo_he_startPushButton,SIGNAL("clicked()"),increase)


                  
app=QApplication(sys.argv)  
progess=Progess()  
progess.show()  
app.exec_()
