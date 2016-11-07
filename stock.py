# -*- coding: utf-8 -*-
from Tkinter import *
import Tkinter as TK
import tkMessageBox
import re,os,sys
import MySQLdb
import matplotlib.pyplot as plt
reload(sys)
sys.setdefaultencoding('utf-8')

class windows():
	
	def __init__(self):
		self.root=Tk()
		self.root.title("盈亏表")
		self.root.geometry('400x300')
		self.frm=Frame(self.root)
		self.frm_L=Frame(self.frm)
		#self.frm_LL=Frame(self.frm_L)
		self.frm_R=Frame(self.frm)
		self.frm_M=Frame(self.frm)
		Label(self.frm_L,text="股票代码：").pack()
		self.stock_code_text=StringVar()
		stock_code=Entry(self.frm_L,textvariable=self.stock_code_text)
		self.stock_code_text.set("")
		stock_code.pack()
		
		Label(self.frm_L,text="股票名称：").pack()
		self.stock_name_text=StringVar()
		stock_name=Entry(self.frm_L,textvariable=self.stock_name_text)
		self.stock_name_text.set("")
		stock_name.pack()
		Label(self.frm_L,text="费率：").pack()
		self.stock_rate_text=StringVar()
		stock_rate=Entry(self.frm_L,textvariable=self.stock_rate_text)
		self.stock_rate_text.set("")
		stock_rate.pack()
		self.frm_L.pack(side=LEFT)
		#self.frm_LL.pack(side=RIGHT)
		
		Label(self.frm_R,text="买入价位：").pack()
		self.stock_bprice_text=StringVar()
		stock_bprice=Entry(self.frm_R,textvariable=self.stock_bprice_text)
		self.stock_bprice_text.set("")
		stock_bprice.pack()
		Label(self.frm_R,text="卖出价位：").pack()
		self.stock_sprice_text=StringVar()
		stock_sprice=Entry(self.frm_R,textvariable=self.stock_sprice_text)
		self.stock_sprice_text.set("")
		stock_sprice.pack()
		Label(self.frm_R,text="交易数量：").pack()
		self.stock_num_text=StringVar()
		stock_num=Entry(self.frm_R,textvariable=self.stock_num_text)
		self.stock_num_text.set("")
		stock_num.pack()
		self.frm_R.pack(side=RIGHT)

		Button(self.frm_L,text="存入数据库",command=self.save).pack(side=BOTTOM)
		Button(self.frm_M,text="结果",command=self.cal).pack(side=BOTTOM)
		Button(self.frm_R,text="图表分析",command=self.analysis).pack(side=BOTTOM)
		Button(self.frm, text="清空", command=self.delete).pack(side=TOP)
		self.frm_M.pack(side=BOTTOM)
		self.frm.pack()
		
		
		
		
	def cal(self):
		#price=self.stock_bprice_text.get()
		#print self.s_bprice
		try:
			s_code=self.stock_code_text.get()
			s_name=self.stock_name_text.get()
			s_rate=self.stock_rate_text.get()
			s_bprice=self.stock_bprice_text.get()
			s_sprice=self.stock_sprice_text.get()
			s_num=self.stock_num_text.get()
			s1=float(s_bprice)
			s2=float(s_sprice)
			s3=float(s_num)
			s4=float(s_rate)
			sum=(s2-s1)*s3-10-s2*s3*s4/10000
			string=str("您目前的盈亏为 %f" % sum)
			print "您目前的盈亏为 %f" % sum
			tkMessageBox.showinfo(title='结果',message=string)
		except:
			out=str("请确认输入的是数字而不是其他字符！！！")
			print "请确认输入的是数字而不是其他字符！！！"
			tkMessageBox.showinfo(title="警告",message=out)
	
		
	def save(self):
		try:
			s_code=self.stock_code_text.get()
			s_name=self.stock_name_text.get()
			s_rate=self.stock_rate_text.get()
			s_bprice=self.stock_bprice_text.get()
			s_sprice=self.stock_sprice_text.get()
			s_num=self.stock_num_text.get()
			s5=float(s_code)
			s6=str(s_name)
			s1=float(s_bprice)
			s2=float(s_sprice)
			s3=float(s_num)
			s4=float(s_rate)
			sum=(s2-s1)*s3-10-s2*s3*s4/10000
			string=str("您目前的盈亏为 %f" % sum)
			#print "insert into stock(code,name,b_price,s_price,num,rate,profit) values  (%f,%s,%f,%f,%f,%f,%f)" % (s5,repr(s6),s1,s2,s3,s4,sum)
			#print s1,s2,s3,s4,s5,s_code,s6,s_name 
			
			#print "您目前的盈亏为 %f" % sum
			tkMessageBox.showinfo(title='结果',message=string)
			
			try:
				save=MySQLdb.connect(host='10.3.247.91',user='root',passwd='mysql',db='cal_stock')
				#save=MySQLdb.connect(host='rm-bp12a3q2p8q14i0yk.mysql.rds.aliyuncs.com',user='re5sh0bjj8',passwd='Mysqlweb20',db='re5sh0bjj8')
				#save.query("grant all on *.* to 'root'@'10.2.48.100' identified by 'mysql'")
			except Exception,e:
				print e
				sys.exit()
	
			cursor=save.cursor()
			action="insert into stock(code,name,b_price,s_price,num,rate,profit) values (%f,%s,%f,%f,%f,%f,%f)" % (s5,repr(s6),s1,s2,s3,s4,sum)
		#	action="insert into stock(code,name,b_price,s_price,num,rate,profit) values (%f,%s,%f,%f,%f,%f,%f)" % (s5,s6,s1,s2,s3,s4,sum)
		#	action1="insert into aliyun_stock(code,name,b_price,s_price,num,rate,profit) values ("+s5+","+s6+","+s1+","+s2+","+s3+","+s4+","+sum+" )"
			try:
				cursor.execute(action)
			except Exception,e:
				print e
			cursor.close()
			save.commit()
			save.close()
		except:
			out=str("请确认输入的是数字而不是其他字符！！！")
			print "请确认输入的是数字而不是其他字符！！！"
			tkMessageBox.showinfo(title="警告",message=out)

	def analysis(self):
		try:
			save=MySQLdb.connect(host='10.3.247.91',user='root',passwd='mysql',db='cal_stock')
			#save=MySQLdb.connect(host='rm-bp12a3q2p8q14i0yk.mysql.rds.aliyuncs.com',user='re5sh0bjj8',passwd='Mysqlweb20',db='re5sh0bjj8')
			#save.query("grant all on *.* to 'root'@'10.2.48.100' identified by 'mysql'")
		except Exception,e:
			print e
			sys.exit()
	
		cursor=save.cursor()
		
		action="select id,profit from stock"
		try:
			cursor.execute(action)
		except Exception,e:
			print e
		num=cursor.fetchall()
		cursor.close()
		save.commit()
		save.close()
		x=[]
		y=[]
		i=0
		while i>=0:
			try:
				a=num[i][0]
				print a
				b=num[i][1]
				print b
				x.append(a)
				y.append(b)
				i+=1
			except IndexError:
				break
			print x,y

		plt.plot(x,y)
		plt.show()
	def delete(self):
		self.stock_code_text.set("")
		self.stock_name_text.set("")
		self.stock_num_text.set("")
		self.stock_rate_text.set("")
		self.stock_sprice_text.set("")
		self.stock_bprice_text.set("")
		self.stock_sprice_text.set("")
		pass

if __name__=="__main__":
	d=windows()
	mainloop()