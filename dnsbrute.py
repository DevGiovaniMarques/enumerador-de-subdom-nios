import sys
import dns.resolver

resolver = dns.resolver.Resolver()

try:
	with open("wordlist.txt", "r") as arq:
		subdominios = arq.read().splitlines()
except:
	print("Erro ao abrir arquivo")
	sys.exit(1)
      
alvo = 'bancocn.com'

for subdominio in subdominios:
    try:
        sub_alvo = "{}.{}".format(subdominio, alvo)
        resultados = resolver.resolve(sub_alvo, 'A')
        for resultado in resultados:
            print("{} -> {}".format(sub_alvo, resultado))
    except:
        pass
