#Validdor de CPF
import random
import os
os.system("cls")

print('Selecione uma opção:')
print(f'\t[1] verificar Validade de um CPF')
print(f'\t[2] gerar um cpf válido')
navegador = input()

if navegador == '1' :
    print('Programa de Validação de CPF')
    cpf = input('Digite o CPF no formato XXX.XXX.XXX-XX: ')
elif navegador == '2' :
    print('Programa de Geraçãode CPF')
    # cpf = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"."+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"."+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+"-00"
    # print(cpf)
    
    cpf = ""
    for i in range(3):
        cpf += str(random.randint(0,9))
    cpf += "."
    for i in range(3):
        cpf += str(random.randint(0,9))
    cpf += "."
    for i in range(3):
        cpf += str(random.randint(0,9))
    cpf += "-00"

else :
    print('Falha: Opção no menu Inexistente')
    exit()   

if (len(cpf) == 14) and (cpf[11] == "-") and (cpf[3] == ".") and (cpf[7] == "."):
    print('Aviso: Parametro de caractere ok')
    if (cpf[0:3:1]).isdigit() and (cpf[4:7:1]).isdigit() and (cpf[8:11:1]).isdigit() and (cpf[12:14:1]).isdigit():
        print('Aviso: Parametro de numero ok')
        #Coleta de soma por contagem
        coleta1 = (((int(cpf[0])*10)+(int(cpf[1])*9)+(int(cpf[2])*8)+(int(cpf[4])*7)+(int(cpf[5])*6)+(int(cpf[6])*5)+(int(cpf[8])*4)+(int(cpf[9])*3)+(int(cpf[10])*2))*10)%11
        if int(coleta1) > 9:
            coleta1 = 0
        print(f'Avaliação: Resultado do penultimo dígito: {coleta1}')        
        
        coleta2 = (((int(cpf[0])*11)+(int(cpf[1])*10)+(int(cpf[2])*9)+(int(cpf[4])*8)+(int(cpf[5])*7)+(int(cpf[6])*6)+(int(cpf[8])*5)+(int(cpf[9])*4)+(int(cpf[10])*3)+(int(coleta1)*2))*10)%11
        if int(coleta2) > 9:
            coleta2 = 0
        print(f'Avaliação: Resultado do último dígito: {coleta2}')

        if navegador == '2':            
            cpfSub = cpf
            cpfSub = f'{cpfSub[:12]}{coleta1}{coleta2}{cpfSub[14:]}'
            cpf = cpfSub
            print(f'Resultado Final: CPF Gerado {cpf}')
            exit()
       
        if (int(coleta1) == int(cpf[12])) and (int(coleta2) == int(cpf[13])):
            print(f'Resultado Final: O CPF {cpf} é válido ')
            exit()
        else:
            print(f'Resultado Final: O CPF {cpf} é inválido')
            exit()
    else:
        print('CPF inválido - Foi digitado caracteres ou letras incompatíveis')
        print('Digite o CPF no formato XXX.XXX.XXX-XX')
        exit()
else:
    print('CPF inválido - Foi digitado no formato incompatível')
    print('Digite o CPF no formato XXX.XXX.XXX-XX')
    exit() 

