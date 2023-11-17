import smtplib
Email = "nawafalhu@gmail.com"
Password = "hpaz jofx lrcb gdja"

with smtplib.SMTP("smtp.gmail.com") as connection :
    connection.starttls()
    connection.login(user=Email, password=Password)
    connection.sendmail(from_addr=Email, to_addrs="n.alhu10@gmail.com", msg="Subject:test\n\nhello from python")