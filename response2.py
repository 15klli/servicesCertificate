# coding:UTF-8

from flask import Flask
import urllib
from flask import send_file,request
import pdfcrowd
import getHtml
import getRecords
import pdfkit

app=Flask(__name__)

@app.route('/result' ,methods=['POST'])
def handle():	
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
	outFile=str(studentNum)+".pdf"
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
	pdfkit.from_string(result,outFile,options=options)
	response = make_response(send_file(outFile))
	response.headers["Content-Disposition"] = "attachment; filename="+outFile+";"
	return response
@app.route('/')
def init():
	return send_file('certificate1_0.html')

if __name__ == '__main__':
	app.debug=True
	app.run(port=80,host='10.21.141.7')
