import csv
import json
import pprint
import requests

chaves = []
valores = []

with open('/content/drive/MyDrive/Conversor de Moedas/simbolos.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader:
        chaves.append(row[0])
        valores.append(row[1])

dicionario_de_simbolos = dict(zip(chaves, valores))

with open("/content/drive/MyDrive/Conversor de Moedas/dicionario-de-simbolos.json", "w", encoding='utf-8') as f:
    json.dump(dicionario_de_simbolos, f, ensure_ascii=False, indent = 4)


# Mecânica para converter símbolos

#PASSOS
# Input do usuário, com o nome da moeda - FEITO
# Abrir o arquivo e pegar o símbolo da moeda informada - FEITO
# Devolver o símbolo da moeda - FEITO

nome_moeda = input("Informe o nome da moeda: ").title()

with open("/content/drive/MyDrive/Conversor de Moedas/dicionario-de-simbolos.json", "r") as arquivo:
  dicionario_de_simbolo = json.load(arquivo)

  simbolo_moeda = dicionario_de_simbolo.get(nome_moeda).lower()

# Mecãnica para gerar a URL para requisição

# URL base

date = "latest"
apiVersion = "v1"
endpoint = "currencies"

url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/{apiVersion}/{endpoint}/{simbolo_moeda}.json"

resposta = requests.get(url)
conteudo = resposta.content
conversao = json.loads(conteudo.decode("utf-8")).get(simbolo_moeda).get("brl")

formatacao = f"\nO valor do {nome_moeda} convertido para reais é R${round(conversao,2)}."
print(formatacao)
