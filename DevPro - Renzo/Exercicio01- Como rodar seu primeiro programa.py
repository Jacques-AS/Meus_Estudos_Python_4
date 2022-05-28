'''
17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que
a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
arredonde os valores para cima, isto é, considere latas cheias.
'''
import math
area = float(input("Digite o Tamanho da Área m²: "))
# litro = 6 metros
galao = (3.6 * 6)
lata = (18 * 6)

valor_galao = 25.00
valor_lata = 80.00

# tipo1_galao = area / galao + (10*(area / galao)/100)

tipo1_galao = math.ceil(area / galao + (10*(area / galao)/100))
custo_galao = tipo1_galao * 25.00

tipo2_lata = math.ceil(area / lata + (10*(area / lata)/100))
custo_lata = tipo2_lata * 80.00

tipo3_lata = math.floor(area / lata + (10*(area / lata)/100))
custo_lata3 = tipo3_lata * 80.00
litros_faltantes = area % lata
tipo_galao4 = math.ceil(litros_faltantes / galao)
custo_galao4 = tipo_galao4 * 25.00
misto = custo_lata3 + custo_galao4

print(f'Comprar {tipo1_galao:.0f} Galão de 3.6 Litros de Tinta, Custo R$ {custo_galao:.2f}')
print(f'Comprar {tipo2_lata:.0f} Lata de 18 Litros de Tinta, Custo R$ {custo_lata:.2f}')
print(f'Comprar {tipo3_lata:.0f} Lata de 18 Litros de Tinta e mais {tipo_galao4:.0f} Galão de 3.6 Litros de Tinta , Custo R$ {misto:.2f}')
