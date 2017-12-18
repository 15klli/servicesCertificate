# coding:UTF-8

from flask import Flask
import urllib
from flask import send_file,request,make_response
import sys
import pdfcrowd
import getHtml
import getRecords
import pdfkit
import time

app=Flask(__name__)

@app.route('/result' ,methods=['POST'])
def handle():	
	logoImg='http://tva2.sinaimg.cn/crop.0.0.180.180.180/80080e5ajw1e8qgp5bmzyj2050050aa8.jpg'	
	rs=urllib.urlopen(logoImg)
	if(len(rs.read())<=2251):
		return u'<h1 style="margin-top:20%;color:red;text-align:center">请等待服务器登录外网,或直接邮件至 <a href="mailto:15klli@stu.edu.cn">15klli@stu.edu.cn</a></h1>'
	name=request.form.get('name')
	studentNum=request.form.get('studentNum')		
	organization=request.form.get('organization')
	package=getRecords.getRecords(name)		
	if(package==-1):
		return 'nothing'
	# print package	
	package['name']=name
	package['studentNum']=studentNum
	package['organization']=organization
	result=getHtml.getHtml(package)
	reload(sys)
	sys.setdefaultencoding('gbk')
	outFile=u'【'+time.strftime("%Y%m%d", time.localtime())+u'】'+str(studentNum)+'+'+name+".pdf"
	# with open(outFile,'w'):
	# print outFile
	options = {
		'margin-top': '1.0in',
		'margin-right': '0.75in',
	    'margin-bottom': '0.75in',
	    'margin-left': '1.0in',
        'page-size': 'A4',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ]
    }
	pdfkit.from_string(result,output_path=u'已开服务证明/'+outFile,options=options)
	response = make_response(send_file(u'已开服务证明/'+outFile))
	response.headers["Content-Disposition"] = "attachment; filename="+outFile.encode('gbk')+";"
	reload(sys)
	sys.setdefaultencoding('UTF-8')
	return response
@app.route('/')
def init():
	return send_file('certificate1_0.html')

if __name__ == '__main__':
	app.debug=True
	app.run(port=80,host='10.21.141.7')
