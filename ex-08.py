contatos = {}


def adicionar_contato(nome, telefone, email):
    contatos[nome] = {"telefone": telefone, "email": email}
    print(f"Contato {nome} adicionado.")


def buscar_contato(nome):
    if nome in contatos:
        print(f"Nome: {nome}")
        print(f"Telefone: {contatos[nome]['telefone']}")
        print(f"Email: {contatos[nome]['email']}")
    else:
        print(f"Contato {nome} não encontrado.")


def listar_contatos():
    if contatos:
        print("\n--- Lista de Contatos ---")
        for nome, dados in contatos.items():
            print(f"Nome: {nome}, Telefone: {dados['telefone']}, Email: {dados['email']}")
    else:
        print("Nenhum contato cadastrado.")


adicionar_contato("Ana", "11987654321", "ana@email.com")
adicionar_contato("Bruno", "21912345678", "bruno@email.com")
listar_contatos()
buscar_contato("Ana")
buscar_contato("Carlos")
