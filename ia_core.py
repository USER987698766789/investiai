import openai
import requests
import pandas as pd

# Insira sua OpenAI API Key aqui
openai.api_key = "SUA_API_KEY_AQUI"

def pegar_dados_crypto():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    return pd.DataFrame(response.json())

def analisar_oportunidades(dados_criptos):
    texto = "Analise os seguintes dados de criptomoedas e me diga quais estão com comportamento interessante ou oportunidades escondidas:
"
    for i, row in dados_criptos.iterrows():
        texto += f"{row['name']}: preço {row['current_price']}, variação 24h {row['price_change_percentage_24h']}%
"

    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": texto}]
    )
    return resposta['choices'][0]['message']['content']