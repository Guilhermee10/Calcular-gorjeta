# Calculadora de gorjeta em python
def calcular_gorjeta():
    print("==== CALCULADORA DE GORJETA ===")


valor_conta = float(input('digite o valor da conta: R$'))

percentual_gorjeta = float(input("Digite o percentual de gorjeta desejado (ex: 10,15,20): "))

valor_gorjeta = valor_conta * (percentual_gorjeta / 100)

valor_total = valor_conta + valor_gorjeta


calcular_gorjeta()
print('\n === RESUMO DO PAGAMENTO ===')
print(f'Valor da conta: R$ {valor_conta:.2f}')
print(f'Percentual de gorjeta: {percentual_gorjeta:.1f}%')
print(f'Valor da gorjeta: R$ {valor_gorjeta:.2f}')
print(f'Valor total a pagar: R$ {valor_total:.2f}')
print('========================')

