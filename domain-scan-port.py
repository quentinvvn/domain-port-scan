import socket
import subprocess
import sys
from datetime import datetime
import errno

subprocess.call('clear', shell=True)

remote_server = input('Entrez le nom de domaine : ')
remote_server_IP = socket.gethostbyname(remote_server)

print('IPV4 : ', remote_server_IP)

print('-'*60)
print('Veuillez attendre durant le scan de', remote_server_IP)
print('-'*60)

t1 = datetime.now()

try: 
    # Changez les valeurs de range pour choisir les ports que vous souhaitez scanner
    for port in range(79,84):
        connexion = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        resultat = connexion.connect_ex((remote_server_IP, port))
        
        if resultat == 0:
            print('Port{} : Ouvert'.format(port))
        
        else:
            print('Port{} : Fermé'.format(port))
    
except KeyboardInterrupt:
        print('Vous avez pressé Ctrl+C')
        sys.exit()

except:
    print('Quelque chose cloche !!!')
    sys.exit()

t2 = datetime.now()

Ttotal = t2 - t1
print('-'*60)
print('Scan terminé en',Ttotal)
