import re  # Regular Expression -- RegEx

endereco = "Rua do Ensino, 85, Santa Monica, uberlandia , 83042-224"

# Cep : 5 digitos + hifen(opicional) + 2 digitos
padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")   # {} quantificadores
busca = padrao.search(endereco)  # Busca o padrão e retorna o Objeto MATCH ou NONE

if busca:
    cep = busca.group()
    print(cep)
