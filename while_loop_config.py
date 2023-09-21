import telnetlib
import time


IPAdd = raw_input("Type your IP Address to Telnet: ")
UN = raw_input("Type Username to access the router: ")
PW = raw_input("Password for Username: ")
EPW = raw_input("Type Password Preivilege: ")

TA = telnetlib.Telnet(IPAdd)
    
#Credentials

TA.read_until("Username: ")
TA.write(UN+"\n")
TA.read_until("Password: ")
TA.write(PW+"\n")
TA.write("enable\n")
TA.write(EPW+"\n")
TA.write("conf t\n")
time.sleep(3)

#Configuration Commands
Router_Ip_List = ["192.168.228.101","192.168.228.102","192.168.228.103"]
print(Router_Ip_List)
RConfig = raw_input("Do you want to configure Router?")

while RConfig.upper() == "YES":
    PAns = raw_input("Do you want to configure Routing Protocol?\nA. Yes\n ")
    while PAns.upper() == "A":
        Protocol = raw_input("which protocol you want to configure?\nA. RIP \nB OSPF\n")
        if Protocol.upper() == "A":
            TA.write("router rip")
            RNID = raw_input("PLease Enter the network ID: ")
            TA.write("network "+RNID+"\n")
            TA.write("exit")
        
        
        elif Protocol.upper() == "B":
            TA.write("router ospf 10")
            RNID = raw_input("PLease Enter the network ID: ")
            TA.write("network "+RNID+" 0.0.0.255 area 0\n")
            TA.write("exit")
            
        else:
            
            print("Please select correct protocol!!!")
   

print("Configuration Successful!!!")
            
           

#Logout and close the session
    
TA.write("end\n")
TA.write("exit\n")
time.sleep(3)
TA = TA.read_all()
time.sleep(3)
