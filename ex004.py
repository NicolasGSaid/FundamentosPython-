#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
 
algo = input('Digite algo: ') 

def checa_tipo_primitivo (algo):
    checagens = {
        "é numérico": algo.isnumeric(),
        "é alfabético": algo.isalpha(),
        "é alfanumérico": algo.isalnum(),
        "é apenas espaços": algo.isspace(),
        "está em maiúsculas": algo.isupper(),
        "esta em minúsculas": algo.islower(),
        "está capitalizado": algo.istitle()
    }
    return checagens

for i in checa_tipo_primitivo(algo):
    print(f'O que você digitou {i}?', checa_tipo_primitivo(algo)[i])
    