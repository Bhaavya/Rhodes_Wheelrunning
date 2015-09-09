import sys
import subprocess
from PyQt4.QtGui import *
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import *
from CLAMS_resources import *
import math
import WheelRunning
app = QApplication(sys.argv)
d=app.desktop()
w=d.width()
h=d.height()
class Options(QMainWindow):
 closed=pyqtSignal()
 logo=':/images/ratlogo.png'
 cursorURL=':/images/cheese.png'
 pupilURL=':/images/pupil.jpg'
 def __init__(self, parent=None):
    QMainWindow.__init__(self, parent)
    
    self.mainlayout=QWidget()
    self.mainlayout.setMouseTracking(True)
    self.setMouseTracking(True)
    self.setCentralWidget(self.mainlayout)
    self.setWindowTitle('Wheel running')
    
   
    

    self.ew=0
    self.eh=0
    self.pw=0
    self.ph=0
    cur=QPixmap(self.cursorURL)

    curs=QCursor(cur)
    self.mainlayout.setCursor(curs)
    
    self.rat=QWidget(self.mainlayout)
    self.rat.setMouseTracking(True)
    
    self.eye1=QWidget(self.rat)
    self.eye2=QWidget(self.rat)
    self.pupil1=QWidget(self.eye1)
    self.pupil2=QWidget(self.eye2)
    self.eye1.setMouseTracking(True)
    self.eye2.setMouseTracking(True)
    self.pupil1.setMouseTracking(True)
    self.pupil2.setMouseTracking(True)
    
    btn1=QPushButton("Wheel running",self)
 
 


  
    grid =QGridLayout()
    grid.setSpacing(4)
    
    grid.addWidget(btn1,0,4,5,2,Qt.AlignCenter)
    
    box=QVBoxLayout()
    box.addStretch(1)
    box.addLayout(grid)
    
    
    self.mainlayout.setLayout(box)
    btn1.clicked.connect(self.wr)
    self.closed.connect(app.quit)
    
    self.mainlayout.setStyleSheet(""".QWidget{background-color: 'white'}""")
    btn1.setStyleSheet(""".QPushButton{background-color: #1E90FF;color: 'white'}""")
 
    
    btn1.setMouseTracking(True)
 def wr(self):
     
        self.w1=wheel(self)
        self.w1.resize(w,h)
        self.w1.show()
        self.hide()
 def closeEvent(self, event):
            self.closed.emit()
            event.accept()
 def resizeEvent(self,event):
     global w
     global h
     w=(self.frameGeometry()).width()
     h=(self.frameGeometry()).height()
     ht=h*0.5
     wid=w*0.4
     nimg=QImage(self.logo).scaled(wid,ht)
     nimg.save(self.logo)
     
     self.rat.resize(wid,ht)
     self.ew=wid/7
     self.eh=ht/11
     self.eye1.resize(self.ew,self.eh)
     self.eye2.resize(self.ew,self.eh)
     rwid=(w-wid)/2

     rhit=(h-ht)/2

     self.rat.move(rwid,rhit)
     ewid1=(wid-self.ew)/2.5
     ewid2=(wid-self.ew)/1.76

     ehit=(ht-self.eh)/4.4
     self.eye1.move(ewid1,ehit)
     
     self.eye2.move(ewid2,ehit)
     self.pw=self.ew/4
     self.ph=self.ew/4
     if self.ph > (self.eh-2):
       self.ph=self.eh/1.5
     pwid1=(self.ew-self.pw)/2
     pwid2=(self.ew-self.pw)/2
     phit=(self.eh-self.ph)/2
    
    
     self.pupil1.resize(self.pw,self.ph)
     self.pupil2.resize(self.pw,self.ph)
     self.pupil1.move(pwid1,phit)
     self.pupil2.move(pwid2,phit)
     
     self.rat.setObjectName('rat')
     self.rat.setStyleSheet(""" .QWidget#rat{border-image: url(':/images/ratlogo.png')0 0 0 0 stretch stretch stretch stretch }""")
     self.pupil1.setStyleSheet(""" .QWidget{border-image: url(':/images/pupil.jpg')0 0 0 0 stretch stretch stretch stretch; }""")
     self.pupil2.setStyleSheet(""" .QWidget{border-image: url(':/images/pupil.jpg')0 0 0 0 stretch stretch stretch stretch; }""")
     self.eye1.setStyleSheet(""" .QWidget{background-color:'white';border:1px solid}""")
     self.eye2.setStyleSheet(""" .QWidget{background-color:'white';border:1px solid}""")
 
 def mouseMoveEvent(self,event):
  
   prev_pos1= self.pupil1.pos()
   prev_pos2= self.pupil2.pos()
   evx=(event.globalPos()).x()
   evy=(event.globalPos()).y()
   eyex1g=(self.pupil1.mapToGlobal(prev_pos1)).x()+self.pw/2
   eyey1g=(self.pupil1.mapToGlobal(prev_pos1)).y()+self.ph/2
   eyex2g=(self.pupil2.mapToGlobal(prev_pos2)).x()+self.pw/2
   eyey2g=(self.pupil2.mapToGlobal(prev_pos2)).y()+self.ph/2
   
   angle1=  math.atan2(evy-eyey1g , evx-eyex1g)
   angle2=  math.atan2(evy-eyey2g , evx-eyex2g)
  
   new_pos1_x=prev_pos1.x()+math.cos(angle1)*3.5
   new_pos1_y=prev_pos1.y()+math.sin(angle1)*3.5
   new_pos2_x=prev_pos2.x()+math.cos(angle2)*3.5
   
   new_pos2_y=prev_pos2.y()+math.sin(angle2)*3.5

   if  (new_pos1_x)<1.0:
       
       new_pos1_x=prev_pos1.x()
   if (new_pos1_y)<1.0:
       new_pos1_y=prev_pos1.y()
   if  (new_pos1_x)>(self.ew-self.pw-1.0):

       new_pos1_x=prev_pos1.x()
   if  (new_pos1_y)>(self.eh-self.ph-1.0):

       new_pos1_y=prev_pos1.y()
   self.pupil1.move(new_pos1_x,new_pos1_y)
   if  (new_pos2_x)<1.0:
    
    new_pos2_x=prev_pos2.x()
   if (new_pos2_y)<1.0:
            new_pos2_y=prev_pos2.y()
   if  (new_pos2_x)>(self.ew-self.pw-1.0):
                    
                    new_pos2_x=prev_pos2.x()
   if  (new_pos2_y)>(self.eh-self.ph-1.0):
                            
                            new_pos2_y=prev_pos2.y()
   self.pupil2.move(new_pos2_x,new_pos2_y)

class wheel(QMainWindow):
  closed=pyqtSignal()
  ifiles=list()
  ofile=''
  strifiles=QString()
  def __init__(self,parent=None):
    QMainWindow.__init__(self,parent)
    self.parent=parent
    self.mainlayout=QWidget()
    self.setCentralWidget(self.mainlayout)
    palette = QPalette()
    strifiles=QString()
    palette.setColor(QPalette.Background,QtCore.Qt.white)
   
    self.setWindowTitle('Wheel running')
    self.setPalette(palette)
    lbl2=QLabel('Enter Output file name',self)
    self.ledit2=QLineEdit(self)
    btn2=QPushButton('Add file',self)
    btn1=QPushButton('Add files',self)
    lbl1=QLabel('Enter name(s) of Input file(s) within quotes')
    self.ledit1=QLineEdit(self)
    lbl3=QLabel('Enter time duration for averaging',self)
    self.ledit3=QLineEdit(self)
    btn=QPushButton('Generate excel output',self)
    
    self.errlabel1=QLabel('Please select input file(s)',self)
    self.errlabel2=QLabel('Please select output file',self)
    self.errlabel3=QLabel('Please enter time duration',self)
    font=QFont()
    font.setPointSize(20);
    font.setBold((bool)('true'));
    
    self.errlabel1.setFont(font);
    self.errlabel2.setFont(font);
    self.errlabel3.setFont(font);
    self.errlabel1.hide()
    self.errlabel2.hide()
    self.errlabel3.hide()
    self.grid =QGridLayout()
    self.grid.setSpacing(20)
    self.grid.setRowStretch(0,1)
    self.grid.setRowStretch(9,1)
    self.grid.setColumnStretch(0,1)
    self.grid.setColumnStretch(11,1)
    self.grid.addWidget(lbl1,1,1,QtCore.Qt.AlignLeft)
    self.grid.addWidget(self.ledit1,1,2,1,7)
    self.grid.addWidget(btn1,1,10,QtCore.Qt.AlignLeft)
    self.grid.addWidget(lbl2,2,1,QtCore.Qt.AlignLeft)
    self.grid.addWidget(self.ledit2,2,2,1,7)
    self.grid.addWidget(btn2,2,10,QtCore.Qt.AlignLeft)
    self.grid.addWidget(lbl3,3,1,QtCore.Qt.AlignLeft)
    self.grid.addWidget(self.ledit3,3,2,1,7)
    
    self.grid.addWidget(btn,5,2,1,7,QtCore.Qt.AlignLeft)
    self.grid.addWidget(self.errlabel1,8,1,QtCore.Qt.AlignCenter)
    self.grid.addWidget(self.errlabel2,8,1,QtCore.Qt.AlignCenter)
    self.grid.addWidget(self.errlabel3,8,1,QtCore.Qt.AlignCenter)
    self.mainlayout.setLayout(self.grid)
    btn1.clicked.connect(self.selectFiles)
    btn2.clicked.connect(self.selectFile)
    btn.clicked.connect(self.callAct)
    btn.setStyleSheet(""".QPushButton{background-color: #1E90FF;color: 'white'}""")
    self.backAction = QAction(QIcon(":/images/Back.png"),"Back",self)
    
    self.backAction.triggered.connect(self.Back)
    self.backAction.setStatusTip("Back")
    self.toolbar = self.addToolBar("Back")
    self.toolbar.addAction(self.backAction)
    self.closed.connect(app.quit)
  def Back(self):
            self.parent.resize(w,h)
            self.parent.show()
            self.hide()
  def selectFiles(self):
                        fdialog=QFileDialog(self)
                        fdialog.setFileMode(QFileDialog.ExistingFiles)
                        lst=fdialog.getOpenFileNames()
                        
                        if lst!=[]:
                                for l in lst:
                                       self.ifiles.append(((str)(l)))
                                       self.strifiles=self.strifiles.append('"'+l+'"'+' ')
                                       self.ledit1.setText(self.strifiles)
  def selectFile(self):
                        fdialog1=QFileDialog(self)
                        fdialog1.setFileMode(QFileDialog.ExistingFile)
                        s=fdialog1.getOpenFileName()
                        if(len((str(s)).strip())!=0):
                                        self.ofile=s
                                        self.ledit2.setText(s)
  def callAct(self):
                                                                                            
                                                                                            
                if self.ifiles==[]:
                    
                        if(len((str(self.ledit1.text()).strip()))==0):
                        
                          self.errlabel2.hide();
                          self.errlabel3.hide()
                          self.errlabel1.show();
                          self.ifiles=list()
                          self.ofile=''
                                                                                                                            
                        else:
                            strifiles=(str(self.ledit1.text()).strip())
                            ifile=''
                            i=0
                            while i<len(strifiles):
                                if strifiles[i]=='"':
                                    i=i+1
                                    while strifiles[i]!='"':
                                        ifile+=strifiles[i]
                                        i=i+1
                                i=i+1
                                                    
                                if ifile!='':
                                                    self.ifiles.append(ifile)
                                                    ifile=''
                elif self.ofile=='':
                    
                                if(len((str(self.ledit2.text())).strip())==0):
                                    self.errlabel1.hide();
                                    self.errlabel3.hide()
                                    self.errlabel2.show()
                                    self.ifiles=list()
                                    self.ofile=''
                                                                                                                                                                                                    
                                                                                                                                                                                                    
                                else:
                                    self.ofile=str(self.ledit2.text())
                elif (len((str(self.ledit3.text())).strip())==0):
                    
                    self.errlabel1.hide();
                    self.errlabel2.hide();
                    self.errlabel3.show()
                else:
                  
                    self.errlabel1.hide()
                    self.errlabel2.hide()
                    self.errlabel3.hide()
                    strifiles=(str(self.ledit1.text()).strip())
                    self.ifiles=list()
                    print strifiles
                    
                    ifile=''
                    i=0
                    while i<len(strifiles):
                        if strifiles[i]=='"':
                            i=i+1
                            while strifiles[i]!='"':
                                ifile+=strifiles[i]
                                i=i+1
                        i=i+1
                    
                        if ifile!='':
                                            self.ifiles.append(ifile)
                                            ifile=''

                    self.ofile=str(self.ledit2.text())
                    i=self.ifiles
                    o=self.ofile
                   
                    d=(str(self.ledit3.text())).strip()
                    self.ledit1.clear()
                    self.ledit2.clear()
                    self.ledit3.clear()
                    self.ifiles=list()
                    self.ofile=''
                    self.strifiles=QString()
                    print i
                    print o
                    WheelRunning.main(i,o,d)
                        
  def closeEvent(self, event):
                    self.closed.emit()
                    event.accept()

  def resizeEvent(self,event):
    global w
    global h
    w=(self.frameGeometry()).width()
    h=(self.frameGeometry()).height()


def main():
    
      app.setQuitOnLastWindowClosed(False)
    
      mainwindow=Options()
      mainwindow.showMaximized()
      

      sys.exit(app.exec_())


if __name__ == '__main__':
    main()