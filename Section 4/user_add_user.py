import os
import crypt

password = "p@ssw0rd"
encPass = crypt.crypt(password, "22")
os.system("useradd -p " + encPass + " johnsmith")
