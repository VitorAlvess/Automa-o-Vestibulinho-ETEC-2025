import pandas as pd
import re
import csv

def processar_dados(input_file, output_file):
    # Tente ler o arquivo CSV com opções de tratamento de erro
    try:
        df = pd.read_csv(input_file, header=None, names=['dados'], dtype={'dados': str}, 
                          delimiter=',', quoting=csv.QUOTE_NONE, on_bad_lines='skip')
    except Exception as e:
        print(f"Erro ao ler o CSV: {e}")
        return

    # Expressão regular para capturar os dados necessários
    regex = r'(\d{3,4}\.00S) (.*?), (\d+) (.*? - .*) Período: (.*?), (\d+) (.*?), (\d{4}\.\d{2}S\.\d{5}-\d), ([\d,]+)'

    dados_organizados = []

    # Processar linha a linha, ignorando valores não string
    for dado in df['dados']:
        if isinstance(dado, str):  # Certificar que estamos lidando com uma string
            matches = re.findall(regex, dado)
            for match in matches:
                dados_organizados.append({
                    "Classificação": match[0],
                    "Unidade": match[1],
                    "Código Curso": match[2],
                    "Curso": match[3],
                    "Período": match[4],
                    "Número de Inscrição": match[5],
                    "Nome": match[6],
                    "Inscrição": match[7],
                    "Nota": float(match[8].replace(",", "."))
                })

    df_organizado = pd.DataFrame(dados_organizados)
    df_organizado.to_csv(output_file, index=False)

    print(df_organizado)

# Defina os caminhos dos arquivos
input_file = 'dadosgerais.csv'
output_file = 'dados_organizados.csv'
processar_dados(input_file, output_file)

