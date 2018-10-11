import smtplib
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("vk9339135@gmail.com","9739089478")
msg = "hello boss"
server.sendmail("vk9339135@gmail.com","pruthvirajkp150@gmail.com",msg)
print('mail is sent^.^')
server.quit()