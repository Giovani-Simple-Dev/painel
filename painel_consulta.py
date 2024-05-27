import requests
from colorama import init, Fore
from time import sleep
import os

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

init(autoreset=True)

def exibir_banner():
    banner = """
██████╗  █████╗ ██╗███╗   ██╗███████╗██╗         ██████╗ ███████╗     ██████╗ ██████╗ ███╗   ██╗███████╗██╗   ██╗██╗  ████████╗ █████╗ ███████╗
██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██║         ██╔══██╗██╔════╝    ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║   ██║██║  ╚══██╔══╝██╔══██╗██╔════╝
██████╔╝███████║██║██╔██╗ ██║█████╗  ██║         ██║  ██║█████╗      ██║     ██║   ██║██╔██╗ ██║███████╗██║   ██║██║     ██║   ███████║███████╗
██╔═══╝ ██╔══██║██║██║╚██╗██║██╔══╝  ██║         ██║  ██║██╔══╝      ██║     ██║   ██║██║╚██╗██║╚════██║██║   ██║██║     ██║   ██╔══██║╚════██║
██║     ██║  ██║██║██║ ╚████║███████╗███████╗    ██████╔╝███████╗    ╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝███████╗██║   ██║  ██║███████║
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝    ╚═════╝ ╚══════╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝╚══════╝
    """
    print(banner)

# Chamar a função para exibir o banner
exibir_banner()



def menu():
  while True:
    cls()
    print(Fore.GREEN + "1. Consultar IP [ON]")
    print(Fore.GREEN + "2. Consultar CEP [ON]")
    print(Fore.RED + "3. Consultar CPF [OFF]")
    print(Fore.GREEN + "4. Consultar Feriados [ON]")
    print(Fore.GREEN + "5. Vericar Participantes do PIX [ON]")
    print(Fore.GREEN + "6. Consultar DDD [ON]")
    print(Fore.GREEN + "7. Corretoras Presentes na CVM [ON]")
    print(Fore.GREEN + "8. Consultar CNPJ [ON]")
    print(Fore.RED + "9. Consultar Nome [OFF]")
    print(Fore.RED + "10. Consultar APIs [OFF]")
    print(Fore.CYAN + "0. Sair")
    choice = input("Digite a opção: ")

    if choice == "1":
      consultar_ip()
    elif choice == "2":
      consultar_cep()
    elif choice == "4":
      consultar_feriados()
    elif choice == "5":
      participantes_pix()
    elif choice == "6":
      consultar_ddd()
    elif choice == "7":
      corretoras_cvm()
    elif choice == "8":
      consultar_cnpj()
    elif choice == "10":
      mensagem()
    elif choice == "0":
      print("Saindo...")
      break
    else: 
      print("Opção inválida")
      sleep(2)

def consultar_nome():
  nome = input("Digite o Nome: ")
  response = requests.get(f"http://ghostcenter.xyz/api/nome/{nome}")
  data = response.json()
  if response.status_code == 200:
    print(f"CPF: {data['cpf']}")
    print(f"Data de Nascimento: {data['data_nascimento']}")
  
def consultar_ip():
  ip = input("Digite o IP: ")
  response = requests.get(f"http://ip-api.com/json/{ip}")
  data = response.json()
  if data['status'] == 'sucess':
    print(f"IP: {data['query']}")
    print(f"País: {data['country']}")
    print(f"Região: {data['region']}")
    print(f"Cidade: {data['city']}")
  else:
    print("Erro na consulta do IP.")
  input("Pressione Enter para continuar... ")

def consultar_cep():
  cep = input("Digite o CEP: ")
  response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
  data = response.json()
  if 'erro' not in data:
    print(f"CEP: {data['cep']}")
    print(f"Logradouro: {data['logradouro']}")
    print(f"Bairro: {data['bairro']}")
    print(f"Cidade: {data['localidade']}")
    print(f"Estado: {data['uf']}")
  else:
    print("CEP inválido.")
  input("Pressione Enter para continuar...")
  
def consultar_feriados():
  ano = input("Digite o Ano: ")
  response = requests.get(f"https://brasilapi.com.br/api/feriados/v1/{ano}")
  feriados = response.json()
  if response.status_code == 200:
    for feriado in feriados:

      print(f"Data: {feriado['date']}")
    print(f"Nome: {feriado['name']}")
    print("-" * 20)
  else:
    print("Erro ao consultar feriados")
  input("Pressione Enter para continuar...")

def consultar_cnpj():
  cnpj = input("Digite o CNPJ: ")
  response = requests.get(f"https://receitaws.com.br/v1/cnpj/{cnpj}")
  data = response.json()
  if response.status_code == 200:
    

      print(f"CNPJ: {data['cnpj']}")
      print(f"Logradouro: {data['logradouro']}")
      print(f"Tipo: {data['tipo']}")
      print(f"Porte: {data['porte']}")
      print(f"Nome: {data['nome']}")
      print(f"Fantasia: {data['fantasia']}")
      print(f"Abertura: {data['abertura']}")
      print(f"Numero: {data['numero']}")
      print(f"Completemento: {data['complemento']}")
      print(f"CEP: {data['cep']}")
      print(f"Bairro: {data['bairro']}")
      print(f"Municipio: {data['municipio']}")
      print(f"Estado: {data['uf']}")
      print(f"EMAIL: {data['email']}")
      print(f"Telefone: {data['telefone']}")
      print(f"Situação: {data['situacao']}")
      print(f"Data de Situação: {data['data_situacao']}")
      print(f"Motivo de Situação: {data['motivo_situacao']}")
      print(f"Data de Situação Especial: {data['data_situacao_especial']}")
      print(f"Capital Social: {data['capital_social']}")
  else:
    print("Erro ao consultar o CNPJ.")
  input("Pressione Enter para continuar...")

def participantes_pix():
  response = requests.get(f"https://brasilapi.com.br/api/pix/v1/participants")
  data = response.json()
  if response.status_code == 200:
    for participante in data:

      print(f"ISPB: {participante['ispb']}")
      print(f"Nome: {participante['nome']}")
      print(f"Nome Reduzido: {participante['nome_reduzido']}")
      print(f"Modalidade de Participação: {participante['modalidade_participacao']}")
      print(f"Tipo de Participação: {participante['tipo_participacao']}")
      print(f"Início de Operação: {participante['inicio_operacao']}")
      print("-" * 20)
  else:
    print("Erro na Verificação")
  input("Pressione Enter para continuar...")

def consultar_ddd():
  ddd = input("Digite o DDD: ")
  response = requests.get(f"https://brasilapi.com.br/api/ddd/v1/{ddd}")
  data = response.json()
  if response.status_code == 200:
    print(f"Estado: {data['state']}")
    print(f"Cidades com o mesmo DDD: {data['cities']}")
  else:
    print("Erro ao consultar o DDD")
  input("Pressione Enter para continuar...")

def corretoras_cvm():
  response = requests.get(f"https://brasilapi.com.br/api/cvm/corretoras/v1")
  data = response.json()
  if response.status_code == 200:
    for corretora in data:
      print(f"BAIRRO: {corretora['bairro']}")
      print(f"CEP: {corretora['cep']}")
      print(f"CNPJ: {corretora['cnpj']}")
      print(f"COMPLEMENTO: {corretora['complemento']}")
  else:
    print("Erro ao Buscar Corretoras")
  input("Pressione Enter para continuar...")


def rastreio():
  input("Digite o Código de Rastreio: ")
  response = requests.get(f"https://gateway.apibrasil.io/api/v2/correios/rastreio")
  data = response.json()
  if response.status_code == 200:

    print(f"Descrição: {data['descricao']}")
    print(f"CEP: {data['cep']}")
    print(f"Cidade: {data['cidade']}")

def mensagem():
  print("Para ter acesso as APIs entre em: https://github.com/Giovani-Simple-Dev/painel/blob/main/README.md")
  input("Pressione Enter para continuar...")
mensagem()


if __name__ == "__main__":
  menu()