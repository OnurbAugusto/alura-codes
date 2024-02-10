url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
print(url)

#Sanatização / limpeza dos dados
url = url.strip()

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia!")  # raise, diferente do retrun




#Separa a base e os parametros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao + 1:]

#Busca o valor de um parâmetro
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&',indice_valor) # a partir do indice do meu valor, ver se tem &
                                                            # para poder lidar com multiplos parâmetros
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]    #não tem o e_comercial
else:
    valor = url_parametros[indice_valor:indice_e_comercial] #tem o e_comercial
print(valor)







