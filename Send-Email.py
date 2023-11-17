import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

Sender = "nawafalhu@gmail.com"
Password = "hpaz jofx lrcb gdja"
receve = "n.alhu10@gmail.com"

msg = MIMEMultipart()

msg['From'] = 'nawafalhu@gmail.com'
msg['To'] = 'n.alhu10@gmail.com'

msg['Subject'] = 'Email with Image'
with open(r'D:\2023\alqasabEid23\IMG_0022.JPG', 'rb') as f:
    image = MIMEImage(f.read())

image.add_header('image/jpeg', 'image/png')
image.add_header('Content-ID', '<image>')
msg.attach(image)

body = MIMEText('This email has an image attachment.')

msg.attach(body)

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
smtp.login(Sender, Password)

smtp.sendmail(Sender, receve, msg.as_string())