import telnetlib
import time


IPAdd = raw_input("Type your IP Address to Telnet: ")
UN = raw_input("Type Username to access the router: ")
PW = raw_input("Password for Username: ")

TA = telnetlib.Telnet(IPAdd)
    
Config = open("config_backup.txt","w")
#Credentials

TA.read_until("Username: ")
TA.write(UN+"\n")
TA.read_until("Password: ")
TA.write(PW+"\n")
Config.write("enable\n")
Config.write("123\n")
Config.write("conf t\n")
time.sleep(3)

#Configuration Commands
Router_Ip_List = ["192.168.228.101","192.168.228.102","192.168.228.103"]
print(Router_Ip_List)

intName = raw_input("which interface you want to configure?\nA. Loopback\nB. Interface\n")
if intName.upper() == "A":
    LoB_No = raw_input("Which Loopback Number You want to configure?:\n")
    L0B_Ip = raw_input("Enter the IP address: \n")
    Config.write("int Lo "+LoB_No+"\n")
    Config.write("ip add "+L0B_Ip+" 255.255.255.255\n")
    Config.write("exit"+"\n")
    
elif intName.upper() == "B":
    int_No = raw_input("Which interface You want to configure?:\n")
    int_Ip = raw_input("Enter the IP address: \n")
    Config.write("int "+int_No+"\n")
    Config.write("ip add "+int_Ip+"\n")
    Config.write("no shut"+"\n")
    Config.write("exit"+"\n")
    time.sleep(3)
else:
    print("Not valid")
    
    

#Logout and close the session
    
Config.write("end\n")
Config.write("exit\n")
Config.close()
Config_file = TA.read_all()
print(Config_file)
time.sleep(3)
