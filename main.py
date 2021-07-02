#--------------------------------------------------------------------#
#------- > Exercicio 02 Lista 01
print('-'*20)
nome = input('Digite o seu primeiro nome: ')
sobrenome = input('Digite seu sobrenome: ')
ru = input('Digite o seu RU: ')

def EmailGenerator(nome, sobrenome, ru):
    gerador = [nome, sobrenome, ru]
    _gerador = gerador[0][0] + sobrenome + ru[-2]+ru[-1]
    return  _gerador

print('-'*20)
print(EmailGenerator(nome, sobrenome, ru)+"@algoritmos.com.br")


