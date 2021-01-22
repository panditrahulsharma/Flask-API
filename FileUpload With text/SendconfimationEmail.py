import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
load_dotenv()


sender_email =  os.getenv("MAIL_USERNAME")
password = os.getenv("MAIL_PASSWORD")

message = MIMEMultipart("alternative")


def sendConfirmation(user_data):
	sender_email =  os.getenv("MAIL_USERNAME")
	password = os.getenv("MAIL_PASSWORD")
	message["Subject"] = "Paper Successfully Received- Online Submission: Paper ID- {}".format(user_data['ProjectId'])
	html = """\
	<html>
	  <body>
	    <p>Dear Author/Research Scholar,<br>
		<p>	 Thank you for submitting your manuscript {0} to IJRASET. We are in the process of evaluating your manuscript. At this point your manuscript:</p>
		<p>- Has been assigned to an editor and is awaiting reviewer confirmations</p>
		<p>We evaluate all manuscript submissions as expeditiously as possible and appreciate your patience throughout the peer review process. You can track the status of your manuscript within our peer review system by navigating to www.ijraset.com/status.php</p>
		<p> For any future communication your are advised to refer your Paper ID- {1}. </p>
		<p>With Warm Regards</p>
		<p>Editor-In Chief</p>
		<p>IJRASET Publications</p>
		<p>www.ijraset.com, Email id: ijraset@gmail.com</p>
	  </body>
	</html>
	""".format(user_data['PaperName'],user_data['ProjectId'])

	# html=render_template('email/account_confirmation.html', username='rahul pandit', link="nkjwfnwejfnkwejfwnkj")

	# print(html)

	# Turn these into plain/html MIMEText objects
	# part1 = MIMEText(text, "plain")
	part2 = MIMEText(html, "html")

	# Add HTML/plain-text parts to MIMEMultipart message
	# The email client will try to render the last part first
	# message.attach(part1)
	message.attach(part2)

	receiver_email=user_data['AuthorEmail']
	# Create secure connection with server and send email
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
	    server.login(sender_email, password)
	    server.sendmail(
	        sender_email, receiver_email, message.as_string()
	    )

