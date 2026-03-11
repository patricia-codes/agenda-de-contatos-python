import json

agenda = []

def salvar_agenda():
  with open("agenda.json", "w") as arquivo:
    json.dump(agenda, arquivo)
  print("Agenda foi salva com sucesso!")


def carregar_agenda():
  try:
    with open('agenda.json', "r") as arquivo:
      agenda = json.load(arquivo)
    print("Agenda carregada com sucesso!")
    return agenda
  except:
    print("Nenhuma agenda foi encontrada! Começando uma nova agenda.\n")
    return []


def adicionar_contato(nome, telefone, email):
    contato = {
      'nome': nome,
      'telefone': telefone,
      'email': email
    }

    agenda.append(contato)
    print(f"Contato {nome} adicionado!")


def exibir_contatos():
  print("\nContatos na Agenda:")
  for contato in agenda:
    print("Nome: ", contato['nome'])
    print("Telefone: ", contato['telefone'])
    print("Email: ", contato['email'])


def editar_contato():
  nome = input("Digite o nome do contato que deseja editar: ")
  for contato in agenda:
    if contato['nome'] == nome:
      contato['telefone'] = input("Digite o novo telefone: ")
      contato['email'] = input("Digite o novo email: ")
      print("Contato atualizado!\n")
      break
    else:
      print("Contato não encontrado!")


def remover_contato():
  nome = input("Digite o nome do contato que deseja remover: ")
  for contato in agenda:
    if contato['nome'] == nome:
      agenda.remove(contato)
      print("Contato removido!")
      return

  print("Contato não encontrado!\n")

agenda = carregar_agenda()

while True:
  print("\n-- Menu da Agenda")
  print("1. Adicionar contato")
  print("2. Exibir Agenda")
  print("3. Editar Contato")
  print("4. Remover Contato")
  print("5. Salvar agenda")
  print("6. Sair")

  opcao = input("Digite a opção desejada: ")

  if opcao == '1':
    #Coleta de Informações
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")

    adicionar_contato(nome, telefone, email)


  elif opcao == '2':
    exibir_contatos()

  elif opcao == '3':
    editar_contato()

  elif opcao == '4':
    remover_contato()

  elif opcao == '5':
    salvar_agenda()

  elif opcao == '6':
    print("Encerrando a agenda!")
    break

  else:
    print("Opção inválida! Digite novamente!")
