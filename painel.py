import requests
import os
from colorama import init, Fore, Style

# Inicializa o colorama
init(autoreset=True)

def obter_nome_arquivo_saida(base_name="link_m3u_", extension=".txt"):
    index = 1
    while os.path.exists(f"{base_name}{index}{extension}"):
        index += 1
    return f"{base_name}{index}{extension}"

def extrair_links_m3u_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança um erro se a requisição falhar
    except requests.RequestException as e:
        print(Fore.RED + f"Erro ao acessar a URL: {e}")
        return None

    content = response.text
    lines = content.splitlines()
    m3u_links = [line for line in lines if line.startswith("http")]

    return m3u_links

def extrair_links_m3u_arquivo(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(Fore.RED + f"Arquivo não encontrado: {file_path}")
        return None

    m3u_links = [line.strip() for line in lines if line.startswith("http")]

    return m3u_links

def salvar_links_m3u(links, filename_base="link_m3u_"):
    filename = obter_nome_arquivo_saida(base_name=filename_base, extension=".m3u")
    with open(filename, "w") as file:
        for link in links:
            file.write(link + "\n")
    return filename

def converter_txt_para_m3u(file_path):
    links = extrair_links_m3u_arquivo(file_path)
    if links:
        filename = salvar_links_m3u(links, filename_base="converted_")
        print(Fore.GREEN + f"Arquivo .txt foi convertido e salvo como {filename}.")
    else:
        print(Fore.RED + "Nenhum link foi extraído.")

def main():
    print(Fore.CYAN + "Painel de Extração e Conversão de Links M3U")
    print(Fore.CYAN + "1. Extrair links M3U de uma URL")
    print(Fore.CYAN + "2. Extrair links M3U de um arquivo local (.txt ou .m3u)")
    print(Fore.CYAN + "3. Converter um arquivo .txt em um arquivo .m3u")
    opcao = input(Fore.YELLOW + "Digite o número da opção: ")

    if opcao == '1':
        url = input(Fore.YELLOW + "Digite a URL do arquivo M3U: ")
        links = extrair_links_m3u_url(url)
        if links:
            filename = salvar_links_m3u(links)
            print(Fore.GREEN + f"Links foram extraídos e salvos em {filename}.")
        else:
            print(Fore.RED + "Nenhum link foi extraído.")
    elif opcao == '2':
        file_path = input(Fore.YELLOW + "Digite o caminho completo para o arquivo (.txt ou .m3u): ")
        if os.path.isfile(file_path):
            links = extrair_links_m3u_arquivo(file_path)
            if links:
                filename = salvar_links_m3u(links)
                print(Fore.GREEN + f"Links foram extraídos e salvos em {filename}.")
            else:
                print(Fore.RED + "Nenhum link foi extraído.")
        else:
            print(Fore.RED + "Caminho do arquivo inválido ou arquivo não encontrado.")
    elif opcao == '3':
        file_path = input(Fore.YELLOW + "Digite o caminho completo para o arquivo .txt: ")
        if os.path.isfile(file_path):
            converter_txt_para_m3u(file_path)
        else:
            print(Fore.RED + "Caminho do arquivo inválido ou arquivo não encontrado.")
    else:
        print(Fore.RED + "Opção inválida.")

if __name__ == "__main__":
    main()
