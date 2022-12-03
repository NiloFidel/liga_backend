from email.message import EmailMessage
import ssl
import smtplib
import os
import pandas as pd

_email_sender = 'nilo.fidel.mendoza@gmail.com'
_email_password = 'iyakqklshrankjvc'

_subjet = 'Envio de certificado personalizado'

#lista_certificados = [certificado for certificado in os.listdir('/home/sl/caene/') if certificado.endswith(".pdf")]
lista_excel = pd.read_excel(r'/home/sl/caene/lista_caene.xlsx') 

for index, fila in lista_excel.iterrows():
    #_pdf_content = fila['']
    _email_receiver = fila['email']
    _body = "Estimado/a "+fila['name']+" este es tu certificado del ELE22 Lima"
    _nombre_certificado = fila['id']

    em = EmailMessage()
    em['From'] = _email_sender
    em['To'] = _email_receiver
    em['Subject'] = _subjet
    em.set_content(_body)
    
    with open('/home/sl/caene/certificados/'+_nombre_certificado+".pdf", 'rb') as content_file:
        content = content_file.read()
        em.add_attachment(content, maintype='application', subtype='pdf', filename=_nombre_certificado)
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(_email_sender, _email_password)
        smtp.sendmail(_email_sender, _email_receiver, em.as_string())