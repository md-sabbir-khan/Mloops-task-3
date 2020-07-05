import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("sender_email_id", "sender_email_id_password") 
  
# message to be sent 
message = "Hey Developer, Finally the model is successfully trained"
  
# sending the mail 
s.sendmail("sender_email_id", "receiver_email_id", message) 
  
# terminating the session 
s.quit() 