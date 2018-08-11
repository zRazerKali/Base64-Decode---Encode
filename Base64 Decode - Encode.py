import base64,os

os.system("cls||clear")

#Coded By J0K3R00T

def banner():

	print ("""

\033[31m\033[1m/=========================\\
\033[31m\033[1m|   Coded By Jukenovisk   | 
\033[31m\033[33m|         Base64          |        
\033[32m|  Encoding And Decoding  |
\033[32m\=========================/

 \033[32m\033[1m[1] Encoding
 \033[31m\033[1m[2] Decoding\n """)
banner()
escolha = raw_input(" \033[1m\033[35mNumero ==> ")
if escolha == "1":
	encode = raw_input(" \033[36mMensagem: ").encode('utf-8')
	joker = base64.b64encode(encode)
	print
	print(" \033[32mResultado: " + '\033[31m'+ joker)

elif escolha == "2":
	juke = raw_input(" \033[36mMensagem: ").encode('utf-8')
	juvis = base64.b64decode(juke)
	print
	print(" \033[32mResultado: " + '\033[31m'+ juvis)
else:
	print
	print " \033[31m\033[1mErro Na Escolha !!!"

