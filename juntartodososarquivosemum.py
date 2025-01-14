import os
import pandas as pd

# Caminho da pasta com os arquivos XLSX
pasta_xlsx = "./jafoifinal"  # Substitua pelo caminho correto

# Função para juntar todos os arquivos XLSX em um único DataFrame
def juntar_arquivos_xlsx(pasta_xlsx):
    # Lista para armazenar os DataFrames
    lista_df = []

    # Percorrer todos os arquivos na pasta
    for arquivo in os.listdir(pasta_xlsx):
        if arquivo.endswith(".xlsx"):  # Verifica se o arquivo tem a extensão .xlsx
            arquivo_xlsx = os.path.join(pasta_xlsx, arquivo)
            
            # Carregar o arquivo Excel em um DataFrame
            df = pd.read_excel(arquivo_xlsx)
            
            # Adicionar o DataFrame à lista
            lista_df.append(df)
    
    # Concatenar todos os DataFrames em um único DataFrame
    df_consolidado = pd.concat(lista_df, ignore_index=True)
    
    return df_consolidado

# Função para salvar o DataFrame consolidado em um único arquivo Excel
def salvar_arquivo_consolidado(df_consolidado, nome_arquivo):
    df_consolidado.to_excel(nome_arquivo, index=False)
    print(f"Arquivo consolidado salvo como '{nome_arquivo}'")

# Chamar a função para juntar os arquivos
df_consolidado = juntar_arquivos_xlsx(pasta_xlsx)

# Gerar nome do arquivo de saída
nome_arquivo_saida = "arquivo_consolidado.xlsx"

# Salvar o DataFrame consolidado em um novo arquivo Excel
salvar_arquivo_consolidado(df_consolidado, nome_arquivo_saida)
