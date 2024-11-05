""" Faça um programa que receba a temperatura média
de cada mês do ano e armazene-as em uma lista.
Em seguida, calcule a média anual das temperaturas
e mostre a média calculada juntamente com todas as
temperaturas acima da média anual, e em que mês
elas ocorreram (mostrar o mês por extenso: 1 –
Janeiro, 2 – Fevereiro, . . . )."""

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",  "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperatura = []

for t in range(12):
    tempa = float(input(f"Digite a temperatura de {meses [t]} :"))
    temperatura.append(tempa)

media = sum(temperatura)/len(temperatura)
print(f"A media anual e {media}")

print("As temperaturas maiores que a media e ")
for t in range(12):
    if temperatura[t]> media:
        print(f"{meses[t],temperatura[t]}°C")