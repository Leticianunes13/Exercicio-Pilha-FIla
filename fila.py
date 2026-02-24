from typing import Any # Importação do tipo Any para anotações de tipo
import unicodedata # Importação do módulo unicodedata para manipulação de caracteres acentuados e normalização de texto

EMPTY_NODE_VALUE = '__EMPTY_NODE_VALUE__' # Constante para representar um valor vazio em um nó da fila. Isso é usado para indicar que um nó não contém um valor válido, permitindo que a fila funcione corretamente mesmo quando está vazia.

class Node: # Classe que representa um nó na fila, contendo um valor e uma referência para o próximo nó. O construtor inicializa o valor do nó e define a referência para o próximo nó como None. O método __repr__ retorna uma representação em string do valor do nó, e o método __bool__ retorna True se o valor do nó não for igual ao valor vazio definido pela constante EMPTY_NODE_VALUE, indicando que o nó contém um valor válido.
    def __init__(self, value: Any): 
        self.value = value # Armazena o valor do nó, que pode ser de qualquer tipo, graças à anotação de tipo Any.
        self.next: Node = None # Inicializa a referência para o próximo nó como None, indicando que este nó é o último na fila até que um novo nó seja adicionado.
    
    def __repr__(self) -> str: #Imprime o valor da string em vez do endereço de memória.
        return f'{self.value}' 
    
    def __bool__(self) -> bool: # Retorna True se o valor do nó não for igual ao valor vazio definido pela constante EMPTY_NODE_VALUE, indicando que o nó contém um valor válido. Caso contrário, retorna False, indicando que o nó está vazio ou não contém um valor significativo.
        return bool(self.value != EMPTY_NODE_VALUE)
    
class Queue: #Classe contrutura de fila
    def __init__(self):
        self.head: Node = Node(EMPTY_NODE_VALUE) # Inicializa a cabeça da fila com um nó vazio, usando a constante EMPTY_NODE_VALUE para indicar que a fila está inicialmente vazia. A cabeça da fila é o ponto de entrada para os elementos da fila.
        self.tail: Node = self.head # Inicializa a cauda da fila apontando para a cabeça, indicando que a fila está vazia. A cauda da fila é o ponto de saída para os elementos da fila, e ambos head e tail apontam para o mesmo nó vazio até que um novo elemento seja adicionado à fila.
        
    def enqueue(self, value: Any) -> None: #Método para adicionar um elemento á fila. Ele recebe um valor de qualquer tipo
        new_node = Node(value) # Cria um novo nó com o valor fornecido, encapsulando o valor em um objeto Node para ser adicionado à fila.
        if not self.head: #Verifica se o inicio da fla está vazio
            self.head = new_node # CORREÇÃO: A cabeça da fila aponta para o novato que foi adicionado, indicando que a fila agora contém um elemento.
            self.tail = new_node # Isso garante que tanto a cabeça quanto a cauda da fila estejam corretamente atualizadas para refletir a adição do novo elemento.
        else: #Se a fila lá contem elementos, o próximo nó da cauda atual é atualizado para apontar para o novo nó.
            self.tail.next = new_node # Atualiza a referência do próximo nó da cauda atual para apontar para o novo nó, conectando o novo nó ao final da fila.
            self.tail = new_node  # Atualiza a referência da cauda para apontar para o novo nó, indicando que o novo nó é agora o último elemento da fila.
            
    def dequeue(self) -> Any: # Método para remover e retornar o elemento no início da fila.
        if not self.head: # Verifica se a cabeça da fila está vazia, o que indica que a fila não contém elementos para remover. Se a fila estiver vazia, uma exceção IndexError é levantada com a mensagem "A fila está vazia", informando ao usuário que não é possível realizar a operação de dequeue em uma fila vazia.
            raise IndexError("A fila está vazia")
        
        value = self.head.value # Armazena o valor do nó atual da cabeça da fila em uma variável chamada value, que será retornada após a remoção do nó.
        self.head = self.head.next #Atualiza a referência da cabeça da fila para apontar para o próximo nó, efetivamente removendo o nó atual da cabeça da fila. 
        
        if not self.head: # Se a fila tiver apenas um elemento, a cabeça e a cauda serão atualizadas para None, indicando que a fila está vazia após a remoção do elemento.
            self.tail = None
        
        return value 
    
    def is_empty(self) -> bool: # Método para verificar se a fila está vazia. Ele retorna True se a cabeça da fila for None, indicando que não há elementos na fila, e False caso contrário.
        return not self.head

class Stack: #Classe construtura de pilha
    def __init__(self): #Criamos uma pilha usando uma lista para armazenar os elementos
        self.pilha = []
        
    def push(self, item): #método para adicionar elementos na pilha. Ela recebe como parametro "item", que é o elemento a ser adicionado.
        self.pilha.append(item)
        
    def pop(self): # Método para remover o último elemento da pilha. Ele verifica também se a lista está vazia e caso sim, aciona o \indexError.
        if not self.is_empty():
            return self.pilha.pop()
        else:
            raise IndexError("A pilha está vazia")
    
    def is_empty(self): # Etiqueta especial para verificar se a pilha está vazia.
        return len(self.pilha) == 0

def menu(): #Função para exibir o menu com opções para o usuário.
    print("\n--- MENU ---")
    print("1. Verificar se é um palíndromo")
    print("2. Sair")
    
while True: # Ínicio do Loop principal do programa.
    menu()
    escolha = input("Escolha uma opção: \n") # Entrada que receberá a escolha do usuário
    
    if escolha == '1': # Se a escolha do usuário for '1', o programa solicitará que o usuário insira um texto para verificar se é um palíndromo.
        texto = input("Descubra se é um palíndromo: ") 
        
        # Tratamento da entrada
        texto_normalizado = unicodedata.normalize('NFD', texto.lower()) #Usamos a função normalize do módulo unicodedata para normalizar o texto, removendo acentos e convertendo todas as letras para minúsculas. 
        texto_limpo = ''.join(c for c in texto_normalizado if c.isalnum()) # Em seguida, usamos uma compreensão de lista para criar uma nova string (texto_limpo) que contém apenas os caracteres alfanuméricos do texto normalizado, removendo espaços e pontuações. 

        minha_pilha = Stack() #Instancia da classe Stack para armazenar os caracteres do texto em pilha.
        minha_fila = Queue() # Instancia da classe Queue para armazenar os caracteres do texto em fila.

        # 1. PRIMEIRO LAÇO: Guarda tudo na pilha e na fila
        for letra in texto_limpo:
            minha_pilha.push(letra)  
            minha_fila.enqueue(letra)
        
        palindromo = True

        # 2. SEGUNDO LAÇO: Tira da pilha e da fila e compara
        for letra_normal in texto_limpo:
            letra_invertida = minha_pilha.pop()
            letra_fila = minha_fila.dequeue()
        
            if letra_normal != letra_invertida or letra_normal != letra_fila:
                palindromo = False
                break
        
        # 3. RESULTADO FINAL: Fora dos laços (Indentação corrigida!)
        if palindromo: 
            print(f"-> '{texto}' É um palíndromo!")
        else:
            print(f"-> '{texto}' Não é um palíndromo!")

    elif escolha == '2':
        print("Saindo do programa...") 
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")