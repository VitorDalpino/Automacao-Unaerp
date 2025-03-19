
# !pip install requests - Comando se precisar
# Importar bibliotecas
import requests
import pandas as pd

# Importar dados do CEP
cep = '17210580'
response = requests.get(f"https://viacep.com.br/ws/{cep}/json/") # f = falando que vai substituir algo no link
data = response.json()
# Transformar em tabela
data = pd.DataFrame([data])
data['bairro']

# API financeira (Bolsa de valores)
# !pip install yfinance

import yfinance as yf

# Acao
acao = yf.Ticker('PETR4.SA')
acao.info

# Obter histórico
historico = acao.history(period='1y')
historico
# yf.download('PETRA.SA')

# prompt: Faça um gráfico de histórico com os dados da acao que seja dinamico e interativo

import plotly.graph_objects as go

# Criar o gráfico de candlestick
fig = go.Figure(data=[go.Candlestick(x=historico.index,
                open=historico['Open'],
                high=historico['High'],
                low=historico['Low'],
                close=historico['Close'])])

# Adicionar título e rótulos aos eixos
fig.update_layout(title=f'Histórico de Preços - {acao.info["symbol"]}',
                  xaxis_title='Data',
                  yaxis_title='Preço')

# Exibir o gráfico interativo
fig.show()