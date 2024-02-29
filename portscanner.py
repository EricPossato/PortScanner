
import pandas as pd
import socket
import time


# cria dicionário com os portas e seus respectivos serviços
df = pd.read_csv('tcp.csv')
df = df.drop('protocol', axis=1)
port_dict = df.set_index('port').T.to_dict('list')

socket_scanned = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# website ou host
target = input('Qual host você quer scanear: ')
 
# pega o ip do host
target_ip = socket.gethostbyname(target)
print('Começando scan no host:', target_ip)
 

 
#função para scanear portas 
def port_scan(port):
    try:
        socket_scanned.connect((target_ip, port))
        return True
    except:
        return False
 
 
start = time.time()
 

# pega o range de portas que o usuário quer scanear 
# e chama a função port_scan para cada porta
starting_port = input('Digite o port inicial: ')
ending_port = input('Digite o port final: ')
for port in range(int(starting_port), int(ending_port)+1):
    if port_scan(port):
        if port in port_dict:
            print(f'port {port} : {port_dict[port][0]} está aberto')
        else:
            print(f'port {port} está aberto')
    else:
        if port in port_dict:
            print(f'port {port} : {port_dict[port][0]} está fechado')
        else:
            print(f'port {port} está fechado')

 
end = time.time()
print(f'Tempo de execução: {end-start:.2f} segundos')