import smtplib

#E-mail recipiente
email_from = "enzocrimadesouza@gmail.com"
#E-mail destinatário
email_to = ["estevancrima@hotmail.com"]

#Servidor SMTP
smtp = "smtp.gmail.com"

#Inicia instancia da funcao SMTP, onde e especificando o servidor de SMTP e a porta
server = smtplib.SMTP(smtp, 587)
#Defini conexoes usando tls
server.starttls()
#Realiza login no servidor de SMTP passando usuraio e senha
server.login(email_from, open('senha.txt').read().strip())

#Corpo do e-mail
msg = "olá"

#Envia email
server.sendmail(email_from, email_to, msg)

#Fecha conexao
server.quit()



