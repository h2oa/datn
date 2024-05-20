import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-search", help = "Keyword for searching, example: smb", type = str, required = False)
parser.add_argument("-infor", help = "Information of module, example: exploit/unix/ftp/vsftpd_234_backdoor", type = str, required = False)
parser.add_argument("-portscan", help = "Port scan, example: ...", action="store_true", required = False)
parser.add_argument("-d2ip", help = "Find IP from domain, example: goole.com", type = str, required = False)


args = parser.parse_args()