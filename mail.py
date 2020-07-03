import smtplib 

	# creates SMTP session 
	s = smtplib.SMTP('smtp.gmail.com', 587) 

	# start TLS for security 
	s.starttls()   

	# Authentication 
	s.login("sabbirisdon@gmail.com", "*tiktaktoe#")
 
	# message to be sent 
	message = "Hey Developer, Finally the model is successfully trained. "

	# sending the mail 

	s.sendmail("sabbirisdon@gmail.com", "khan.mdsabbir@gmail.com", message)
	# terminating the session 

	s.quit()

