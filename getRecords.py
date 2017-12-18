# coding:UTF-8
import xlrd

def getRecords(name):
	inFile=xlrd.open_workbook('all.xlsx')
	sheet=inFile.sheet_by_index(0)
	postion=0
	flag=0
	nameCol=sheet.col_values(1)
	activityNameCol=sheet.col_values(0)
	timeCol=sheet.col_values(2)
	isOutServies=sheet.col_values(3)
	num=len(nameCol)
	while( postion<num):
		if nameCol[postion]!= name:	
			postion+=1
		else: break
	if(postion==num):
		return -1
	totalTime=0
	inTime=0
	outTime=0
	records={}
	while(nameCol[postion]==name):
		time=timeCol[postion]					
		# todo 判断是校内/外服务
		totalTime+=float(time)
		# print totalTime
		if(isOutServies[postion]==1):
			outTime+=float(time)
		else:
			inTime+=float(time)
		temp={}
		temp['name']=activityNameCol[postion]
		temp['time']=time
		records[activityNameCol[postion]]=temp

		postion+=1
	package={'totalTime':totalTime,'records':records,
				'inTime':inTime,'outTime':outTime}
	return package