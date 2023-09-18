import telnetlib
import time


IPAdd = raw_input("Type your IP Address to Telnet: ")
UN = raw_input("Type Username to access the router: ")
PW = raw_input("Password for Username: ")

TA = telnetlib.Telnet(IPAdd)
    

#Credentials

TA.read_until("Username: ")
TA.write(UN+"\n")
TA.read_until("Password: ")
TA.write(PW+"\n")
TA.write("enable\n")
TA.write("123\n")
TA.write("conf t\n")
time.sleep(3)

#Configuration Commands
Router_Ip_List = ["192.168.228.101","192.168.228.102","192.168.228.103"]
print(Router_Ip_List)

intName = raw_input("which interface you want to configure?\nA. Loopback\nB. Interface\n")
if intName.upper() == "A":
    LoB_No = raw_input("Which Loopback Number You want to configure?:\n")
    L0B_Ip = raw_input("Enter the IP address: \n")
    TA.write("int Lo "+LoB_No+"\n")
    TA.write("ip add "+L0B_Ip+ " 255.255.255.255\n")
    TA.write("exit"+"\n")
    
elif intName.upper() == "B":
    int_No = raw_input("Which interface You want to configure?:\n")
    int_Ip = raw_input("Enter the IP address: \n")
    TA.write("int "+int_No+"\n")
    TA.write("ip add "+int_Ip+"\n")
    TA.write("no shut"+"\n")
    TA.write("exit"+"\n")
    time.sleep(3)
else:
    print("Not valid")
    
    

#Logout and close the session
    
TA.write("end\n")
TA.write("exit\n")

Config_file = TA.read_all()
print(Config_file)
time.sleep(3)
