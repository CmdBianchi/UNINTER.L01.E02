#--------------------------------------------------------------------#
#------- > Exercicio 02 Lista 01
print('-'*30)
name = input('Digite o seu primeiro nome: ')
surname = input('Digite seu sobrenome: ')
ru = input('Digite o seu RU: ')

def EmailGenerator(nome, sobrenome, ru):
    gerador = [nome, sobrenome, ru]
    _gerador = gerador[0][0] + sobrenome + ru[-2]+ru[-1]
    return  _gerador

print('-'*30)
print(EmailGenerator(name, surname, ru)+"@algoritmos.com.br")


