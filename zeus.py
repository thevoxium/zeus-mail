import click
import smtplib, ssl
from getpass import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

port=465

@click.group()
def cli():
    pass


@cli.command()
@click.option('-s', '--send', 'send')
def email(send):
    passw=getpass()
    confirm_pass=getpass("confirm_passsword:")
    rec_mail=input("receiver's mail:")
    your_mess=input("message: ")

    context = ssl.create_default_context()

    if passw==confirm_pass:
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(send, passw)
            click.echo(click.style("connection established", bg='green'))

            attach = input("attachment(y,n)")
            if attach=='y':
                message = MIMEMultipart()
                message['From']=send
                message['To']=rec_mail
                message['Subject']=input("subject:")
                message.attach(MIMEText(your_mess, 'plain'))
                attach_filename="test.txt"
                attach_file = open(attach_filename, 'rb')
                payload = MIMEBase('application', 'octate-stream')
                payload.set_payload((attach_file).read())
                encoders.encode_base64(payload)
                payload.add_header('Content-Decomposition', 'attachment; filename="test.txt"')
                message.attach(payload)
                server.sendmail(send, rec_mail, message.as_string())

            else:
                server.sendmail(send, rec_mail, message)
                click.echo(click.style("message sent", bg='blue'))

    else:
        click.echo(click.style("paswords don't match", bg='red'))
