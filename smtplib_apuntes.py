from email.mime.text import MIMEText
from smtplib import SMTP

# construir mensaje para enviar
mensaje = ("Contenido del mensaje...") 
   
# Configurar cuentas
remitente = "Nicobmart1203@gmail.com" #Correo de la cuenta que envia el mail
destinatario = "Nicobmart1203@gmail.com" #Correo al que mandar el mail

#Configuarar Mensaje
mensaje_correo = MIMEText(mensaje)
mensaje_correo["From"] = remitente
mensaje_correo["To"] = destinatario
mensaje_correo["Subject"] = "Prueba de envio de mail" # asunto del mail

#Coneccion
servidor = SMTP("smtp.gmail.com", 587)
servidor.ehlo()
servidor.starttls()

#Inicio de sesion
servidor.login(remitente, "jyywjgnrqykynuwv") #Se agrega el usuario de mail y la contraseña generada

#Enviar mail
servidor.sendmail(remitente, destinatario, mensaje_correo.as_string())

#Terminar Coneccion
servidor.quit()
print("Correo enviado")

