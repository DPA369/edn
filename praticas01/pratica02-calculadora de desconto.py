#2- Calculadora de Desconto
#Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

#* Nome do produto: "Camiseta"
#* Preço original: R$ 50.00
#* Porcentagem de desconto: 20%
#O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.


produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20

valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto

print("Produto:", produto)
print("Preço original: R$", round(preco_original, 2))
print("Desconto:", str(desconto_percentual) + "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço final com desconto: R$", round(preco_final, 2))
