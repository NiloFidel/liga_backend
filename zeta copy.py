from email.message import EmailMessage
import ssl
import smtplib
import os

email_sender = 'nilo.fidel.mendoza@gmail.com'
email_password = 'nfrbavggqpmmtxmr'
#email_receiver = '144987@unsaac.edu.pe'

subjet = 'Certificado ELE-22'
body = """Se envia certificado de participacion en el evento de CAENE ELE-22"""

em = EmailMessage()
em['From'] = email_sender
#em['To'] = email_receiver
em['Subject'] = subjet
em.set_content(body)

# with open('/home/sl/Downloads/Nilo_Fidel_CV.pdf', 'rb') as content_file:
#     content = content_file.read()
#     em.add_attachment(content, maintype='application', subtype='pdf', filename='example.pdf')

arr_txt = [x for x in os.listdir('/home/sl/caene/') if x.endswith(".pdf")]
#print(arr_txt)
for nombre_certificado in arr_txt:
    pdf_email = nombre_certificado.split('.pdf')
    email_receiver = pdf_email[0]
    #em['To'] = email_receiver
    with open('/home/sl/caene/'+nombre_certificado, 'rb') as content_file:
        content = content_file.read()
        #em.add_attachment(content, maintype='application', subtype='pdf', filename=nombre_certificado)
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())