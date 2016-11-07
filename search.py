# -*- coding: utf-8 -*-
from Tkinter import *
import Tkinter as TK
import tkMessageBox
import re,os,sys,time
import urllib
from bs4 import BeautifulSoup
#import MySQLdb
#import matplotlib.pyplot as plt
reload(sys)
sys.setdefaultencoding('gb2312')

class windows():
	
	def __init__(self):
		self.root=Tk()
		self.root.title("电影搜索神器")
		self.root.geometry('600x400')
		self.frm=Frame(self.root)
		self.frm_L=Frame(self.frm)
		#self.frm_LL=Frame(self.frm_L)
		self.frm_R=Frame(self.frm)
		#self.frm_M=Frame(self.frm)
		Label(self.frm_L,text="全集网：").pack()
		self.stock_code_text=StringVar()
		stock_code=Entry(self.frm_L,textvariable=self.stock_code_text)
		self.stock_code_text.set("")
		stock_code.pack()
		
		self.frm_L.pack()
		#self.frm_LL.pack(side=RIGHT)
		
		self.frm_R.pack(side=BOTTOM)
		Button(self.frm_L,text="搜索",command=self.search).pack()
		
		self.frm.pack()
		
		
		
	def search(self):
		
		s_code=self.stock_code_text.get()
		url_code=urllib.unquote(s_code)
		print str(url_code),url_code
		url="http://so.loldytt.com/search.asp?keyword="+str(url_code)
		print url ,s_code
		urls=[]
		try:
	
			html = urllib.urlopen(url)
			bsObj = BeautifulSoup(html,'html.parser')
			mess=bsObj.find("div",{"class":"solb"}).findAll("a")
			print mess
			
			print "now is getting url"
			for link in mess:
				if 'href' in link.attrs:
					print (link.attrs['href'])
					urls.append(link.attrs['href'])
		except:
			print "network error"
		downurl=[]
		print "now is visiting url"
		for i in urls:
			
			newhtml=urllib.urlopen(i)
			page=BeautifulSoup(newhtml,'html.parser')
			try:
				#newmess=page.find("div",{"class":"con4"}).findAll(href=re.compile("thunder"))
				newmess=page.find("li",{"id":"li1_0"}).findAll("a")
				#print newmess
				for bt in newmess:
					if 'href' or 'text' in bt.attrs:
						print bt.attrs['href']
						c=bt.get_text()
						d=c.encode("gb2312","ignore")
						print d
						downurl.append(bt.attrs['href']     +     d)
						time.sleep(3)
			except AttributeError:
				print "there is a error"
		bturl=set(downurl)
		file=open(s_code,'w')
		print "now is saving bt" 
		for durl in bturl:
	
			file.write(str(durl)+'\n')
		file.close()
		print "all BT is saved"
	

if __name__=="__main__":
	d=windows()
	mainloop()