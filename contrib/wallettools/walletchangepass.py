from jsonrpc import ServiceProxy
access = ServiceProxy("http://127.0.0.1:21416")
pwd = raw_input("Enter old wallet passphrase: ")
pwd2 = raw_input("Enter new wallet passphrase: ")
access.walletpassphrasechange(pwd, pwd2)
