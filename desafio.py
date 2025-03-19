# Importar bibliotecas
import pandas as pd
df_estoque_minimo = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Automacao_unaerp/Desafio/arquivos_base/EstoqueMin.csv', sep=';')
df_estoque_minimo['ID Produto'] = df_estoque_minimo['ID Produto'].astype(str)

df_estoque_minimo

# importar base de dados
df_base_dados = pd.ExcelFile('/content/drive/MyDrive/Colab Notebooks/Automacao_unaerp/Desafio/arquivos_base/BaseDados.xlsx')
df_base_dados.sheet_names

# Separar dados da base de dados
df_estoque = df_base_dados.parse('fEstoque')
df_loja = df_base_dados.parse('dLoja')
df_produto = df_base_dados.parse('dProduto')

df_estoque['ID Produto'] = df_estoque['ID Produto'].astype(str)
df_estoque['ID Loja'] = df_estoque['ID Loja'].astype(str)
df_produto['ID Produto'] = df_produto['ID Produto'].astype(str)

# 1
estoque_atual = df_estoque.groupby('ID Produto')['Movimentação'].sum()
# Estoque_atual.columns = ['ID Produto','Estoque Atual']
# estoque_atual.rename(columns={'Movimentação': 'Estoque atual'}, inplace=True)#dicionario
estoque_atual = estoque_atual.rename('Estoque Atual')
estoque_atual.to_csv('/content/drive/MyDrive/Colab Notebooks/Automacao_unaerp/Desafio/respostas/estoque_atual.csv', sep=';')
     
# Adicionar estoque mínimo no estoque atual
analise_estoque = pd.merge(estoque_atual, df_estoque_minimo, on= 'ID Produto', how = 'inner')

#Itens críticos
itens_criticos = analise_estoque[analise_estoque['Estoque Atual'] < analise_estoque['Estoque Mínimo']]
itens_criticos['Diferença Estoque']= itens_criticos['Estoque Atual'] - itens_criticos['Estoque Mínimo']

# Quantidade a comprar
# Corrected line: Using itens_criticos instead of intens_criticos
itens_criticos['Quantidade a Comprar'] = itens_criticos['Diferença Estoque'] * -1 + itens_criticos['Estoque Mínimo']

# Adicionar preço nos itens críticos
intens_criticos = pd.merge(itens_criticos, df_produto, on='ID Produto', how='inner')

# Corrected line: Selecting columns from intens_criticos instead of itens_criticos
intens_criticos[['ID Produto','Estoque Atual','Estoque Mínimo', 'Diferença Estoque', 'Quantidade a Comprar','Produto','Custo Unit']]
          