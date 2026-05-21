class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
            return True
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        print("Valor de saque inválido.")
        return False

    def verificar_saldo(self):
        print(f"Saldo atual da conta {self.numero_conta}: R$ {self.saldo:.2f}")
        return self.saldo


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        print(f"Conta {conta.numero_conta} adicionada ao cliente {self.nome}.")

    def listar_contas(self):
        if self.contas:
            print(f"\nContas de {self.nome}:")
            for conta in self.contas:
                print(f"  Número: {conta.numero_conta}, Saldo: R$ {conta.saldo:.2f}")
        else:
            print(f"O cliente {self.nome} não possui contas.")


class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} adicionado ao banco {self.nome}.")

    def buscar_cliente_por_cpf(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def buscar_conta_por_numero(self, numero_conta):
        for cliente in self.clientes:
            for conta in cliente.contas:
                if conta.numero_conta == numero_conta:
                    return conta
        return None


banco_digital = Banco("Meu Banco Digital")
cliente1 = Cliente("Maria Silva", "123.456.789-00")
conta1_maria = ContaBancaria("001-X", "Maria Silva", 1000)
conta2_maria = ContaBancaria("002-Y", "Maria Silva", 500)
cliente1.adicionar_conta(conta1_maria)
cliente1.adicionar_conta(conta2_maria)
banco_digital.adicionar_cliente(cliente1)
cliente2 = Cliente("João Souza", "987.654.321-00")
conta1_joao = ContaBancaria("003-Z", "João Souza", 2000)
cliente2.adicionar_conta(conta1_joao)
banco_digital.adicionar_cliente(cliente2)

cliente1.listar_contas()
conta1_maria.depositar(200)
conta1_maria.sacar(300)
conta1_maria.verificar_saldo()
cliente_encontrado = banco_digital.buscar_cliente_por_cpf("123.456.789-00")
if cliente_encontrado:
    print(f"\nCliente encontrado: {cliente_encontrado.nome}")
conta_encontrada = banco_digital.buscar_conta_por_numero("003-Z")
if conta_encontrada:
    print(
        f"Conta encontrada: {conta_encontrada.numero_conta} "
        f"do titular {conta_encontrada.titular}"
    )
