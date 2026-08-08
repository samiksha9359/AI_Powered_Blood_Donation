import smtplib
from email.message import EmailMessage

# -------------------------------
# Gmail Configuration
# -------------------------------
SENDER_EMAIL = "shelkesamiksha9359@gmail.com"
APP_PASSWORD = "sulr txxv fuqp svwa"


# =====================================================
# Donor Registration Email
# =====================================================
def send_email(receiver_email, donor_name, blood_group):

    try:
        msg = EmailMessage()

        msg["Subject"] = "🩸 Blood Donor Registration Successful"
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver_email

        msg.set_content(f"""
Dear {donor_name},

Thank you for registering as a Blood Donor.

Your Registration has been completed successfully.

Blood Group : {blood_group}

Your willingness to donate blood can help save many lives.

Thank you for joining our
AI Powered Blood Donation Management System.

❤️ Donate Blood • Save Lives ❤️
""")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)

        return True

    except Exception as e:
        print(e)
        raise e


# =====================================================
# Blood Request Approval Email
# =====================================================
def send_approval_email(receiver_email, patient_name, blood_group, units):

    try:
        msg = EmailMessage()

        msg["Subject"] = "🩸 Blood Request Approved"
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver_email

        msg.set_content(f"""
Dear {patient_name},

Congratulations!

Your Blood Request has been APPROVED.

Blood Group : {blood_group}
Units : {units}

Please contact the Blood Bank for further process.

Thank you for using our
AI Powered Blood Donation Management System.

❤️ Stay Safe • Save Lives ❤️
""")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)

        return True

    except Exception as e:
        print("Approval Email Error:", e)
        return False