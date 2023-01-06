imovel = float(input("Valor do imóvel: "))
salario = float(input("Salario: "))
tempo = float(input("Tempo(anos): "))

prestacao = imovel / (tempo*12)

salario30 = salario * 30/100

if prestacao <= salario30: 
  print("Emprestimo aprovado.")
  print(f"Parcela = R$ {prestacao}")
else :
  print("Emprestimo negado.")
  print(f"Parcela = R$ {prestacao}")
  print(f"Limite R$ {salario30}")
