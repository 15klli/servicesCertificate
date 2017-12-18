# coding:UTF-8
import sys
import time

reload(sys)
sys.setdefaultencoding( "utf-8" )

html_tail=u"""			
		</table>		
		</div>
		</div>
		<div style="padding-top:30px;text-align: right;">
			<p>汕头大学青年志愿者协会</p>
			<p>"""+time.strftime("%Y-%m-%d", time.localtime())+"""&nbsp&nbsp&nbsp&nbsp
			&nbsp&nbsp&nbsp&nbsp		
	</div>
	</body>
	</html>
	"""
def initHead(package):
	name=package['name']
	studentNum=package['studentNum']
	totalTime = package['totalTime']
	inTime=package['inTime']
	outTime=package['outTime']
	records=package['records']
	organization=package['organization']
	num=len(records)
	html_head=u"""
	<!DOCTYPE html>
	<html>
	<head>
		<title>汕头大学青年志愿者协会服务时数证明开具</title>
		<meta charset="utf-8">
	</head>
	<body>
		<div>
		<img src="http://tva2.sinaimg.cn/crop.0.0.180.180.180/80080e5ajw1e8qgp5bmzyj2050050aa8.jpg" style="position: fixed;z-index: -1;opacity: 0.1;float: center" height="80%" width="100%">
		<h1 style="text-align: center;">汕头大学青年志愿者协会志愿者服务证明</h1>
		<div style="text-align: left;">
			&nbsp&nbsp<u>&nbsp"""+str(name)+u'&nbsp</u>同学（学号：<u>&nbsp'+str(studentNum)+u"""&nbsp</u>）在汕头大学期间参加以下志愿者服务，特此证明！
		</div>
		<div style="padding: 25px">
			<table border="1" width="100%" cellpadding="10" style="text-align: center;">
			<tr>
				<td>所属组织</td>
				<td colspan="4" >"""+str(organization)+u"""</td>
			</tr>
			<tr>
				<td rowspan="2">服务时间</td>
				<td colspan="2">校内服务</td>
				<td colspan="2">校外服务</td>			
			</tr>
			<tr>
				<td >"""+str(inTime)+u"""</td>
				<td>小时</td>
				<td>"""+str(outTime)+   u"""</td>
				<td>小时</td>
			</tr>
			<tr>
				<td>总计</td>
				<td colspan="4">"""+ str(totalTime)+ u"""小时</td>
				
			</tr>
			<tr>
				<td rowspan=" """+str(num)+'">'+ u"服务经历</td>"
	return html_head

def getRecordRow(record):
	activityName=record['name']
	last=record['time']

	part1=' <td colspan="3">'+activityName+'</td>'
	part2='<td>'+str(last)+'小时</td></tr>'
	code=part1+part2
	return code

def getHtml(package):
	html_body=''	
	records=package['records']
	
	if(len(records)<1):
		return 'nothing'
	html_head=initHead(package)		
	n=1
	for i in records:				
		code=getRecordRow(records[i])
		if(n==1):
			n=0
		else:
			code='<tr>'+code
		html_body+=code
	html_body+='</tr>'
	return html_head+html_body+html_tail