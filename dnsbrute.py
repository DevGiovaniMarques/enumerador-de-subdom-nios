import sys
import dns.resolver

resolver = dns.resolver.Resolver()

try:
	alvo = sys.argv[1]
	wordlist = sys.argv[2]
except:
	print("Está faltando argumentos")
try:
	with open(wordlist, "r") as arq:
		subdominios = arq.read().splitlines()
except:
	print("Erro ao abrir arquivo")
	sys.exit()


for subdominio in subdominios:
    try:
        sub_alvo = "{}.{}".format(subdominio, alvo)
        resultados = resolver.resolve(sub_alvo, 'A')
        for resultado in resultados:
            print("{} -> {}".format(sub_alvo, resultado))
    except:
        pass
