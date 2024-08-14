from flask_mail import Message

from lib.consts import RECIPIENT_EMAILS, SENDING_EMAIL


def send_message(mail, subject, name, email, message):
    """
    Function that sends an email to the me as the owner of the website

    :param mail: The mail object that is used to send the email
    :param subject: The subject of the email
    :param name: The name of the person sending the email
    :param email: The email of the person sending the email
    :param message: The message that the person is sending

    :return: True if the email was sent, False otherwise
    """
    # Set up the basis of the email to send
    msg = Message(
        subject=f"Form Submitted: {subject}",
        sender=(name, SENDING_EMAIL),
        recipients=RECIPIENT_EMAILS,
        charset="utf-8",
        reply_to=email,
    )
    # Create the link to validate the email
    # Set up the body of the email
    msg.body = message
    # Send the email
    mail.send(msg)
    return True
