import telnetlib
IPAdd = raw_input("Enter IP address: ")

username = raw_input("Enter your Username: ")
password = raw_input("Enter Your Password: ")
Tel = telnetlib.Telnet(IPAdd)

Tel.read_until("Username: ")
Tel.write(username+"\n")
Tel.read_until("Password: ")
Tel.write(password+"\n")

Tel.write("enable\n")
Tel.write("123\n")
Tel.write("conf t\n")
Tel.write("do sh ip int bri\n")

Tel.write("exit\n")
Tel.write("end\n")
