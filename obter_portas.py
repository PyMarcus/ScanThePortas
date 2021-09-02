# obter portas de dominios
import socket

portas = []
ausentes = []
presente2 = []
presentes = {}
lista_de_servicos = [
              "daytime",
              "ftp",
              "gopher",
              "http",
              "https",
              "imap",
              "kerberos-adm",
              "mysql-im",
              "pop3",
              "qotd",
              "ssh",
              "snmp",
              "smtp"]
try:
    for servicos in lista_de_servicos:
        if socket.getservbyname(servicos):
            presentes.setdefault(servicos, f'porta -> {socket.getservbyname(servicos)}')
            presente2.append(servicos)
except OSError:
    pass
for valores in lista_de_servicos:
    if valores in presente2:
        pass
    else:
        ausentes.append(valores)
for serv in presentes.items():
    print(f'estão presentes os servicos:{serv}')
print('---' * len(lista_de_servicos))
for val in ausentes:
    print(f'E ausentes os serviços: {val}')

