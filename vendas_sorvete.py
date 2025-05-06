import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
import numpy as np  # Importa a biblioteca numpy para geração de valores aleatórios

# Criar a tabela com listas de mesmo tamanho
data = {
    "Data": pd.date_range(start="2025-01-01", periods=100, freq='D').strftime('%d/%m/%Y'),
    # Gera 100 datas consecutivas a partir de 01/01/2025, formatadas como dia/mês/ano
    
    "Vendas (unidades)": [120, 150, 170] * 33 + [200],  
    # Lista de 100 elementos representando a quantidade de vendas por dia
    
    "Temperatura (°C)": np.random.randint(18, 35, size=100)  
    # Gera 100 valores aleatórios de temperatura entre 18°C e 35°C
}

# Criando o DataFrame a partir do dicionário 'data'
df = pd.DataFrame(data)

# Exportando o DataFrame para um arquivo Excel, sem a coluna de índice
df.to_excel("dados_vendas.xlsx", index=False)

# Exibe mensagem confirmando a criação do arquivo
print("Arquivo Excel gerado com sucesso!")


