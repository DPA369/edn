#1- Conversor de Moeda
#Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

#* Valor em reais: R$ 100.00
#* Taxa do dólar: R$ 5.20
#* Taxa do euro: R$ 6.15
#O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

valor_reais = 100.00
dolar = valor_reais / 5.20
euro = valor_reais / 6.15

print("Valor em dólares: US$", round(dolar, 2))
print("Valor em euros: €", round(euro, 2))
