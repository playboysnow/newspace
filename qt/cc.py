# -*- coding:UTF-8 -*-
import sys,socket,requests,urllib,urllib2
import re,json
import qrcode,PIL
from urlparse import urlparse
# Import Qt GUI component
from PySide.QtGui import *

# Import GUI File
from http import Ui_Frame

class  Frame(QFrame,Ui_Frame):
	
	def  __init__(self,parent=None):
		super(Frame,self).__init__(parent)
		self.setupUi(self)
		self.pushButton.clicked.connect(self.cc)
		self.commandLinkButton.clicked.connect(self.check)
		self.pushButton_3.clicked.connect(self.clear)
		self.pushButton_2.clicked.connect(self.clearargv)
	def cc(self):
		url=self.lineEdit_2.text()
		method_txt=self.comboBox.currentText()
		varify_txt=self.comboBox_2.currentText()
		if varify_txt=='true':
			varify=True
		else:
			varify=False
		if method_txt=='get':
			method=requests.get
		elif method_txt=='post':
			method=requests.post
		elif method_txt=='head':
			method=requests.head
		else:
			method=requests.delete
		argv1=self.lineEdit_3.text()
		argv2=self.lineEdit_8.text()
		argv3 = self.lineEdit_4.text()
		argv4 = self.lineEdit_9.text()
		argv5 = self.lineEdit_5.text()
		argv6 = self.lineEdit_10.text()
		argv7 = self.lineEdit_6.text()
		argv8 = self.lineEdit_11.text()
		argv9 = self.lineEdit_7.text()
		argv10 = self.lineEdit_12.text()
		payload={
			argv1:argv2,
			argv3:argv4,
			argv5: argv6,
			argv7: argv8,
			argv9: argv10,
				 	 }
		try:
			r=method(url,data=payload,verify=varify)
		except:
			print "something wrong"
		t=r.text


		self.lineEdit_13.setText(t)
		print url,method_txt,r.text,payload,varify,r.headers
	def check(self):
		a = self.lineEdit_2.text()
		topHostPostfix = (
			'.com', '.la', '.io', '.co', '.info', '.net', '.org', '.me', '.mobi',
			'.us', '.biz', '.xxx', '.ca', '.co.jp', '.com.cn', '.net.cn',
			'.org.cn', '.mx', '.tv', '.ws', '.ag', '.com.ag', '.net.ag',
			'.org.ag', '.am', '.asia', '.at', '.be', '.com.br', '.net.br',
			'.bz', '.com.bz', '.net.bz', '.cc', '.com.co', '.net.co',
			'.nom.co', '.de', '.es', '.com.es', '.nom.es', '.org.es',
			'.eu', '.fm', '.fr', '.gs', '.in', '.co.in', '.firm.in', '.gen.in',
			'.ind.in', '.net.in', '.org.in', '.it', '.jobs', '.jp', '.ms',
			'.com.mx', '.nl', '.nu', '.co.nz', '.net.nz', '.org.nz',
			'.se', '.tc', '.tk', '.tw', '.com.tw', '.idv.tw', '.org.tw',
			'.hk', '.co.uk', '.me.uk', '.org.uk', '.vg', ".com.hk")

		regx = r'[^\.]+(' + '|'.join([h.replace('.', r'\.') for h in topHostPostfix]) + ')$'
		pattern = re.compile(regx, re.IGNORECASE)

		print "--" * 40
		parts = urlparse(a)
		host = parts.netloc
		m = pattern.search(host)
		res = m.group() if m else host
		print "unkown" if not res else res
		ip=socket.gethostbyname(host)
		self.lineEdit_13.setText(ip)
		print ip
	def clear(self):
		self.lineEdit_13.clear()
	def clearargv(self):
		self.lineEdit_3.clear()
		self.lineEdit_4.clear()
		self.lineEdit_5.clear()
		self.lineEdit_6.clear()
		self.lineEdit_7.clear()
		self.lineEdit_8.clear()
		self.lineEdit_9.clear()
		self.lineEdit_10.clear()
		self.lineEdit_11.clear()
		self.lineEdit_12.clear()



if __name__=='__main__':
	Program = QApplication(sys.argv)
	Window=Frame()
	Window.show()
	Program.exec_()