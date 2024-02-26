import re

class ExtratorURL:
    def __init__(self, url):                # Recebe uma URL
        self.url = self.sanitiza_url(url)   # Instancia um atributo ao objeto já sanitizado
        self.valida_url()                   # Valida a URL

    def sanitiza_url(self, url):            # Recebe a URL
        return url.strip()                  # Tira os espaços da URL

    def valida_url(self):
        if not self.url:                  #if self.url == "":, como o if aplica por dentro dos panos o bool,de não verdadeiro, ou seja falso, str vazia retorna falso
            raise ValueError("A URL está vazia!") #Retorna erro de valor

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")   #RegEx
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametro(self):
        indice_interrogacao = self.url.find('?')
        url_parametro = self.url[indice_interrogacao + 1:]
        return url_parametro

    def get_valor_parametro(self,parametro_busca):
        indice_parametro = self.get_url_parametro().find(parametro_busca) #Usa a função para obter o parâmetro de dentro dela busca oq queremos
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametro().find('&', indice_valor)
        if indice_e_comercial == -1:
            return self.get_url_parametro()[indice_valor:]
        else:
            return self.get_url_parametro()[indice_valor:indice_e_comercial]

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return "URL:" + self.url + "\n" + "Base:" + self.get_url_base() + "\n" + "Parametro:" + self.get_url_parametro()

    def __eq__(self, other):
        return self.url == other.url

    def conversor(self,quantidade,VALOR_DOLAR):
        novo_valor = quantidade * VALOR_DOLAR
        return novo_valor

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)
valor_quantidade = float(extrator_url.get_valor_parametro("quantidade"))
print(valor_quantidade)
print(len(extrator_url))
print(extrator_url)
print(extrator_url == extrator_url2)

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
conversao = extrator_url.conversor(valor_quantidade,VALOR_DOLAR)
print(conversao)









