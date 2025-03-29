import dns.resolver

//testando pull
resolver = dns.resolver.Resolver()
wordlist = ['www', 'mail', 'ftp', 'webmail', 'admin', 'test', 'dev', 'blog', 'api', 'secure','shop','advanced','dvwa']
alvo = 'bancocn.com'

for subdominio in wordlist:
    try:
        sub_alvo = "{}.{}".format(subdominio, alvo)
        resultados = resolver.resolve(sub_alvo, 'A')
        for resultado in resultados:
            print("{} -> {}".format(sub_alvo, resultado))
    except:
        pass


