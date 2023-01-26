from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os

company_names=[]
emails = []

#server initialization
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()

smtp.login('kavyanpatel1104@gmail.com', 'tojlsyeywebwpdni')


#message folder
def message(subject="Test",img=None,
			attachment=None, company_name=""):

            x=company_name
            text="Hello this is the template email for "+x
            # build message contents
            msg = MIMEMultipart()
            
            # Add Subject
            msg['Subject'] = subject
            

            # Add text contents
            msg.attach(MIMEText(text))

            # Check if we have anything
            # given in the img parameter
            if img is not None:
                
                # Check whether we have the lists of images or not!
                if type(img) is not list:
                    
                    # if it isn't a list, make it one
                    img = [img]

                # Now iterate through our list
                for one_img in img:
                    
                    # read the image binary data
                    img_data = open(one_img, 'rb').read()
                    # Attach the image data to MIMEMultipart
                    # using MIMEImage, we add the given filename use os.basename
                    msg.attach(MIMEImage(img_data,
                                        name=os.path.basename(one_img)))

            # We do the same for
            # attachments as we did for images
            if attachment is not None:
                
                # Check whether we have the
                # lists of attachments or not!
                if type(attachment) is not list:
                    
                    # if it isn't a list, make it one
                    attachment = [attachment]

                for one_attachment in attachment:

                    with open(one_attachment, 'rb') as f:
                        
                        # Read in the attachment
                        # using MIMEApplication
                        file = MIMEApplication(
                            f.read(),
                            name=os.path.basename(one_attachment)
                        )
                    file['Content-Disposition'] = f'attachment;\
                    filename="{os.path.basename(one_attachment)}"'
                    
                    # At last, Add the attachment to our message object
                    msg.attach(file)
            return msg

subject_variable = "Internship Possibility Test"

# Call the message function


# Make a list of emails, where you wanna send mail
to = [["prachiheda@gmail.com", "Amazon"],
	["kpatel46@ucsc.edu", "Google"], ["prachiheda@gmail.com", "Meta"]]
# Provide some data to the sendmail function!
for i in to:
    address=i[0]
    c_name=i[1]
    msg = message(subject_variable, None, r"PATEL_KAVYAN.pdf", c_name)
    smtp.sendmail(from_addr="kavyanpatel1104@gmail.com",
			    to_addrs=address, msg=msg.as_string())

# Finally, don't forget to close the connection
smtp.quit()
