# -*- coding: utf-8 -*-
import sys
import csv
import xlwt
filename=sys.argv[1]
#新建excel文件
myexcel = xlwt.Workbook(encoding = 'utf-8')
#新建sheet页
mysheet = myexcel.add_sheet("testsheet")
#打开csv文件，事实证明file和open 效果一样的，网上建议用open打开
csvfile = file(filename,"rb")
#csvfile = open("test.csv","rb")

#读取文件信息
reader = csv.reader(csvfile)
l = 0
#通过循环获取单行信息
for line in reader:
	r = 0
	#通过双重循环获取单个单元信息
	for i in line:
#		print l,r
		#通过双重循环写入excel表格
		mysheet.write(l,r,i)
		r=r+1
	l=l+1
#最后保存到excel
excelname=str(filename.split(".")[0]) + ".xls"
myexcel.save(excelname)
