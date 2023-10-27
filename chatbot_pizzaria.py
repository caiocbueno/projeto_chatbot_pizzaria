print('''
| Sabor da pizza| Preço |
| ------------- | ----- |
| Calabresa     | R$ 70 |
| Queijo        | R$ 50 |
| Pepperoni     | R$ 80 |
''')

valor_total = 0
total_calabresa = 0
total_queijo = 0
total_pepperoni = 0

def pedido_da_pizza():
    
    global total_calabresa
    global total_queijo
    global total_pepperoni
    global valor_total
    pedido = input('Digite o sabor desejado: ')
    if pedido == 'calabresa':
        valor_total += 70
        total_calabresa += 1
    elif pedido == 'queijo':
        valor_total += 50
        total_queijo += 1
    elif pedido == 'pepperoni':
        valor_total += 80
        total_pepperoni += 1

pedido_da_pizza()

condicao = True
while condicao:
    fazer_pedido = input('Deseja fazer outro pedido (S/N) ? ')
    if fazer_pedido == "s":
        pedido_da_pizza()
    elif fazer_pedido == "n":
        condicao = False


print('Resumo do pedido')
print(f'{total_calabresa} pizza(s) de calabresa')
print(f'{total_queijo} pizza(s) de queijo')
print(f'{total_pepperoni} pizza(s) de pepperoni')

print(f'Total a pagar: R${valor_total:.2f}')
