import pdfplumber

# Caminho do arquivo PDF
pdf_path = "teste.pdf"

# Função para extrair dados dos aprovados
def extrair_aprovados(pdf_path):
    aprovados = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            # Filtrar linhas com dados de aprovados (exemplo de regra básica)
            for line in text.split('\n'):
                if "NÃO" in line or "SIM" in line:  # Ajustar conforme o padrão dos dados
                    aprovados.append(line)
    return aprovados

# Executar a função
aprovados = extrair_aprovados(pdf_path)

# Mostrar os dados extraídos
for aprovado in aprovados:
    print(aprovado)
