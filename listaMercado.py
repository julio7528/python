#lista do supermercado
import os
os.system("cls")

acessoMenu = True
lista = ['ovo','leite']

while acessoMenu:
    os.system("cls")
    print('Selecione uma opção:')
    print(f'\t[v] ver lista')
    print(f'\t[a] add lista')
    print(f'\t[r] rem lista')
    navegador = input()
        
    os.system("cls")         
    print("Lista atualizada de compras:")
    print(f'\tC: Nome') 
    for a,i in enumerate(lista):
        print(f'\t{a}- {i}')   
    
    if navegador == 'r':
        delItem = input("Digite o Código a ser removido: ")
        try:
            del lista[int(delItem)]
            print('Item deletado')
        except:
            print(f"Não foi possível remover o item: O código {delItem} nao existe")


    if navegador == 'a':
        addItem = input("Digite o Item a ser adicionado: ")
        cancelacadastro = False
        
        for i in lista:
            if i == addItem:
                print(f'\t{i}: Este item ja existe e nao será adicionado')  
                cancelacadastro = True
                break              
        
        if cancelacadastro == False:
            print(f'O produto {addItem} foi cadastrado com o código {len(lista)}')
            lista.append(addItem)
        cancelacadastro = False
    
    reinicia = input('Deseja voltar para o menu? [s] [n] ')
    
    if reinicia =='s' or reinicia == 'S':
        acessoMenu = True
        continue
    elif reinicia =='n' or reinicia == 'N':
        acessoMenu = False
        print('Saindo do programa de lista')
        continue

