# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m². 

altura = float(input("Digite a altura da parede em metros: "))
largura = float(input("Digite a largura da parede em metros: "))

area = largura * altura
tinta = area / 2

print(f"A parede possuí {area:.2f} m² e será necessário {tinta:.2f} litros de tinta.")
