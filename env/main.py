import os
import PyPDF2
from flask import Flask, jsonify, request
from pathlib import Path 

#function to rotate pdf pages
def rotatePage(path,n,angle):
    pdf_in = open(path, 'rb')
    angle=int(angle)
    path=Path(path).name.replace('.pdf','')
    path=os. getcwd().replace("\\","/")+'/output_pdf/'+path+'(rotated)'+'.pdf'
    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()  
    for pageNum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pageNum)
        if pageNum==int(n)-1:
            page.rotateClockwise(angle)
        pdf_writer.addPage(page)
    pdf_out = open(path, 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()
    return path


app= Flask(__name__)
@app.route("/", methods=["POST"]) # Post the test json using postman as in the readme file
def setName():
    if request.method=='POST':
        posted_data = request.get_json()
        path=rotatePage(posted_data['file_path'],posted_data['page_number'],posted_data['angle_of_rotation'])
        return jsonify({"file_path":path})

if __name__=='__main__':
    app.run()
    
   
