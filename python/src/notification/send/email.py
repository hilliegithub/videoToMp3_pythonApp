import smtplib, os, logging, json, ssl
from email.message import EmailMessage

logging.basicConfig(level=logging.DEBUG)

def notification(message):
    try:
        message = json.loads(message)
        mp3_fid = message["mp3_fid"]
        sender_address = os.environ.get("GMAIL_ADDRESS")
        sender_password = os.environ.get("GMAIL_PASSWORD")
        receiver_address = message["username"]

        msg = EmailMessage()
        msg.set_content(f"mp3 file_id: {mp3_fid} is now ready")
        msg["Subject"] = "MP3 Download"
        msg["From"] = sender_address
        msg["To"] = receiver_address

        #session = smtplib.SMTP("smtp.gmail.com", 587)
        #session.starttls()
        #session.login(sender_address, sender_password)
        #session.send_message(msg, sender_address, receiver_address)
        #session.quit()

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender_address, sender_password)
            smtp.sendmail(sender_address,receiver_address, msg.as_string())

        logging.debug("Email sent!")

    except Exception as err:
        logging.debug(err)
        return err