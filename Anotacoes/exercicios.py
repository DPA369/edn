preco = 1000.00 # valro do produto USD
desconto = 0.15 # desconto de 15%
cotacao_dolar = 5.25 # cotacao do dolar em BRL
preco_com_desconto = preco - (preco * desconto) # calcula o preço com desconto
print(f"Preço original: {preco:.2f} USD")
print(f"Desconto: {desconto * 100:.2f}%")
print(f"\nO preço doCelular de Maria com desconto: {preco_com_desconto:.2f} USD")
print(f"O valor do celular em BRL é: {preco_com_desconto * cotacao_dolar:.2f} BRL (USD ${cotacao_dolar:.2f})")