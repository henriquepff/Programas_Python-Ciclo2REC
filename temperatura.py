#lê a temperatura em graus Celsius
temperatura = float(input("\nDigite a temperatura em °C: "))

#classificação da temperatura
if temperatura < 0:
    print("\nFrio Extremo\n")
elif 0 <= temperatura <= 10:
     print("\nFrio\n")
elif 11 <= temperatura <=25:
      print("\nAmeno\n")
elif 26 <= temperatura <= 35:
      print("\nQuente\n")
else:
      print("\nMuito Quente\n")


