import imaplib
import getpass

imap_server = imaplib.IMAP4_SSL("imap.gmail.com",993)
user=input("email: ")
password=getpass.getpass("password: ")
imap_server.login('user', 'password')
