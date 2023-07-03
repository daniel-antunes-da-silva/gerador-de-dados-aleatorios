from random import randint, choice
print('='*50)
print('Bem-vindo ao gerador de dados. Caso queira finalizar o programa, digite "parar".')
dados = [{'nomes': ['Daniel', 'Rafael', 'Ryuk', 'Valda', 'Sidicréia']},
         {'e-mails': ['@gmail.com', '@outlook.com', '@hotmail.com', '@yahoo.com']},
         {'telefones': [int(str(9) + str(randint(00000000, 99999999)))]},
         # transformando em str para concatenar com o 9, e fazer com que sempre inicie com esse valor.
         # Porém, transformo pra int de novo, para que não permaneça como str.
         {'cidades': ['Rio de Janeiro', 'Angra dos Reis', 'Macaé', 'Maricá', 'Petrópolis']},
         {'estados': ['Rio de Janeiro', 'São Paulo', 'Rio Grande do Sul', 'Bahia', 'Acre']}]

while True:
    print('-'*50)
    print('Qual dado você quer que seja gerado aleatoriamente? ')
    escolha_usuario = str(input('[1] - Nomes\n'
                                '[2] - E-mails\n'
                                '[3] - Telefones\n'
                                '[4] - Cidade\n'
                                '[5] - Estado\n'
                                'Sua escolha: ')).lower()
    if escolha_usuario == 'parar':
        break
    if ',' in escolha_usuario:
        escolha_usuario = escolha_usuario.replace(',', '')
        if escolha_usuario.isnumeric():
            print(escolha_usuario.split(), len(escolha_usuario))
            escolha_usuario = escolha_usuario
        else:
            print('Valor incorreto.')
    if escolha_usuario.isnumeric():
        for c in escolha_usuario:
            escolha_usuario = c
            if escolha_usuario == '1' or '2' or '3' or '4' or '5':
                try:
                    posicao_na_lista = int(escolha_usuario) - 1
                    valores = dados[posicao_na_lista]
                    for k in valores.keys():
                        item_escolhido = choice(valores[k])
                        if escolha_usuario == '2':
                            # concatenando um nome aleatorio (em minúsculo) com a parte de trás do e-mail também aleatório.
                            item_escolhido = choice(dados[0]['nomes']).lower() + item_escolhido
                        print(item_escolhido)
                except (TypeError, ValueError):
                    print('Erro no tipo ou valor.')
                except Exception as causa:
                    print(f'Algo deu errado: {causa.__cause__}')
            else:
                print('Opção inválida.')
    else:
        print('Valor incorreto.')