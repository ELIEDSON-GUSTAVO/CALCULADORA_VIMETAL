import webview
import os
import sys

# Caminho correto para encontrar o index.html no executável
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS  # Diretório temporário onde os arquivos do executável estão
else:
    base_path = os.getcwd()

# Caminho para o index.html
html_path = os.path.join(base_path, "index.html")

# Verifica se o arquivo existe antes de abrir
if not os.path.exists(html_path):
    print(f"Erro: Arquivo {html_path} não encontrado!")

# Criar a janela do aplicativo com WebView
webview.create_window("Meu App", html_path)
webview.start()
