import click
import smtplib, ssl
from getpass import getpass

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
    message=input("message: ")

    context = ssl.create_default_context()

    if passw==confirm_pass:
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(send, passw)
            click.echo(click.style("connection established", bg='green'))
            server.sendmail(send, rec_mail, message)
            click.echo(click.style("message sent", bg='blue'))

    else:
        click.echo(click.style("paswords don't match", bg='red'))
