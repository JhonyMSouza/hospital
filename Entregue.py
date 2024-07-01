class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero  # Inicializa o nodo com o número fornecido
        self.cor = cor  # Inicializa o nodo com a cor fornecida
        self.proximo = None  # Inicializa o ponteiro para o próximo nodo como None

    def __repr__(self):
        return f"[{self.cor},{self.numero}]"  # Representação do nodo no formato cor,numero

class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None  # Inicializa a lista com o ponteiro do head como None

    def __repr__(self):
        nodos = []  # Cria uma lista de representações dos nodos
        nodo = self.head  # Começo do nodo head
        while nodo:
            nodos.append(repr(nodo))  # Adiciona a representação do nodo à lista
            nodo = nodo.proximo  # Avança para o próximo nodo
        return "Lista de espera -> " + "  ".join(nodos)  # Exibição da lista de pacientes

    def __iter__(self):
        nodo = self.head  # Inicia do nodo head
        while nodo:
            yield nodo  # Retorna o nodo atual e avança para o próximo
            nodo = nodo.proximo  # Avança para o próximo nodo

    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo  # Se a lista estiver vazia, o nodo se torna o head
        else:
            nodoAtual = self.head  # Começa do nodo head
            while nodoAtual.proximo:
                nodoAtual = nodoAtual.proximo  # Percorre até o final da lista
            nodoAtual.proximo = nodo  # Insere o nodo no final

    def inserirComPrioridade(self, nodo):
        if not self.head or self.head.cor == 'V':
            nodo.proximo = self.head  # Se a lista estiver vazia ou o primeiro nodo for "V", insere no início
            self.head = nodo  # Atualiza o head para o novo nodo
        else:
            nodoAtual = self.head  # Começa do nodo head
            while nodoAtual.proximo and nodoAtual.proximo.cor == 'A':
                nodoAtual = nodoAtual.proximo  # Percorre até encontrar um nodo "V" ou o final da lista
            nodo.proximo = nodoAtual.proximo  # Insere o nodo antes do primeiro "V"
            nodoAtual.proximo = nodo  # Atualiza o próximo do nodo atual

    def inserir(self):
        while True:
            cor = input("Informe a cor do cartão (A ou V): ").upper()  # Solicita a cor do cartão ao usuário
            if cor not in ('A', 'V'):
                print("Cor inválida! Por favor, informe 'A' para amarelo ou 'V' para verde.")
            else:
                break  # Sai do loop se a cor for válida
        numero = int(input(f"Informe o número do cartão {cor}: "))  # Solicita o número do cartão ao usuário
        nodo = Nodo(numero, cor)  # Cria um novo nodo com os dados fornecidos
        if not self.head:
            self.head = nodo  # Se a lista estiver vazia, o nodo se torna o head
        elif cor == 'V':
            self.inserirSemPrioridade(nodo)  # Insere sem prioridade se a cor for "V"
        else:
            self.inserirComPrioridade(nodo)  # Insere com prioridade se a cor for "A"

    def imprimirListaEspera(self):
        if not self.head:
            print("A fila está vazia.")  # Imprime uma mensagem se a fila estiver vazia
        else:
            print("Lista de espera -> ", end='')  # Lista de espera -> " com os nodos
            for nodo in self:
                print(nodo, end='  ')  # Imprime cada nodo
            print('')

    def atenderPaciente(self):
        if not self.head:
            print("Não há pacientes para atender.")  # Imprime uma mensagem se não houver pacientes
        else:
            pacienteAtendido = self.head  # Armazena o paciente a ser atendido
            self.head = self.head.proximo  # Move o head para o próximo nodo
            print(f"Atendendo paciente cartão cor: {pacienteAtendido.cor} e número: {pacienteAtendido.numero}")

def menu():
    lista = ListaEncadeadaSimples()  # Cria uma nova lista encadeada simples
    while True:
        print("\n1 - Adicionar paciente à fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")

        op = input(">>> ")  # Lê a opção do usuário
        if op == '1':
            lista.inserir()  # Chama a função para inserir um novo paciente
        elif op == '2':
            lista.imprimirListaEspera()  # Chama a função para imprimir a lista de espera
        elif op == '3':
            lista.atenderPaciente()  # Chama a função para atender um paciente
        elif op == '4':
            print("Encerrando...")  # Encerra o programa
            break
        else:
            print("Opção inválida! Tente novamente.")  # Exibe uma mensagem de erro para opções inválidas

if __name__ == "__main__":
    menu()  # Inicia o programa chamando a função de menu
