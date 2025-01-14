import pdfplumber
import re
import pandas as pd
import os

# Caminho do arquivo PDF
pdf_path = "teste.pdf"

# Função para extrair dados dos aprovados
def extrair_dados_aprovados(pdf_path):
    dados_aprovados = []
    unidade = ""
    curso = ""
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            linhas = text.split('\n')
            
            # Identificar a unidade e o curso
            for linha in linhas:
                if "Unidade:" in linha:
                    unidade = linha.split("Unidade:")[1].strip()
                if "Curso:" in linha:
                    curso = linha.split("Curso:")[1].strip()
            
            # Filtrar linhas com dados de aprovados
            for linha in linhas:
                # Verificar o padrão das linhas com dados de aprovados
                match = re.match(r"^(.*?)\s(\d{4}\.\d{2}\S+)\s([\d,]+)\s(SIM|NÃO)\s(SIM|NÃO)", linha)
                if match:
                    nome = match.group(1).strip()
                    inscricao = match.group(2).strip()
                    nota = match.group(3).replace(",", ".").strip()  # Ajustar nota como número decimal
                    afro = match.group(4).strip()
                    esc = match.group(5).strip()
                    
                    # Adicionar os dados em uma lista organizada
                    dados_aprovados.append({
                        "Unidade": unidade,
                        "Curso": curso,
                        "Nome": nome,
                        "Inscrição": inscricao,
                        "Nota": float(nota),  # Converter para número
                        "Afrodescendente": afro,
                        "Escolaridade Pública": esc
                    })
    return dados_aprovados, unidade

# Função para gerar um nome de arquivo único
def gerar_nome_arquivo(nome_base):
    contador = 1
    nome_arquivo = f"{nome_base}.xlsx"
    while os.path.exists(nome_arquivo):
        nome_arquivo = f"{nome_base}_{contador}.xlsx"
        contador += 1
    return nome_arquivo

# Executar a função para extrair dados
dados_aprovados, unidade_nome = extrair_dados_aprovados(pdf_path)

# Criar um DataFrame com os dados
df = pd.DataFrame(dados_aprovados)

# Gerar um nome de arquivo único baseado no nome da unidade
nome_base = unidade_nome.replace(" ", "_")
nome_arquivo = gerar_nome_arquivo(nome_base)

# Salvar o DataFrame em formato de planilha
df.to_excel(nome_arquivo, index=False)

print(f"Planilha salva com o nome: {nome_arquivo}")
