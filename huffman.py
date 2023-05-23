import heapalt
class Nodo:
    """La clase Nodo representa un nodo en un árbol de Huffman y tiene los siguientes atributos:

    caracter: un str que representa el caracter que el nodo contiene. Si el nodo no contiene un caracter, este atributo es None.
    frecuencia: un dict que contiene la frecuencia del caracter que el nodo contiene. Si el nodo no contiene un caracter, este atributo es la suma de las frecuencias de los caracteres en sus nodos hijos.
    izq: un Nodo que representa el hijo izquierdo del nodo actual.
    der: un Nodo que representa el hijo derecho del nodo actual.
    
    Además, la clase Nodo tiene los siguientes métodos especiales para sobrecargar los operadores de comparación:
    _lt_(self, otro): sobrecarga el operador < para comparar la frecuencia del nodo actual con la frecuencia del nodo otro.
    _le_(self, otro): sobrecarga el operador <= para comparar la frecuencia del nodo actual con la frecuencia del nodo otro.
    _eq_(self, otro): sobrecarga el operador == para comparar la frecuencia del nodo actual con la frecuencia del nodo otro.
    _ne_(self, otro): sobrecarga el operador != para comparar la frecuencia del nodo actual con la frecuencia del nodo otro.
    _gt_(self, otro): sobrecarga el operador > para comparar la frecuencia del nodo actual con la frecuencia del nodo otro.
    _ge_(self, otro): sobrecarga el operador >= para comparar la frecuencia del nodo actual con la frecuencia del nodo otro.
    """

    def __init__(self, caracter: str, frecuencia: dict):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izq = None
        self.der = None

    def __lt__(self, otro):
        return self.frecuencia[self.caracter] < otro.frecuencia[otro.caracter]

    def __le__(self, otro):
        return self.frecuencia[self.caracter] <= otro.frecuencia[otro.caracter]



    def __gt__(self, otro):
        return self.frecuencia[self.caracter] > otro.frecuencia[otro.caracter]

    def __ge__(self, otro):
        return self.frecuencia[self.caracter] >= otro.frecuencia[otro.caracter]


def hacer_arbol_huffman(heap,freq) -> Nodo:
    a=heap.extract_min()
    if(isEmpty(heap)):
        return a
    b=heap.extract_min()
    Node=Nodo(a.caracter+b.caracter,freq)
    freq[Node.caracter]=(a.frecuencia[a.caracter]+b.frecuencia[b.caracter])
    Node.izq=a
    Node.der=b
    return Node 


def asignar_codigos(nodo: Nodo, codigo: str, cifrado) -> None:
    
    """Asigna códigos de bits a cada caracter en el árbol de Huffman y los almacena en un diccionario.

    Args:
        nodo (Nodo): Nodo actual del árbol de Huffman.
        codigo (str): Código de bits construido hasta el momento en el recorrido del árbol.
        cifrado (dict): Diccionario que almacena los códigos de bits asignados a cada caracter en el árbol.
    """
    if(nodo.izq!=None or nodo.der!=None):
       
        if cifrado in nodo.izq.caracter:
            return asignar_codigos(nodo.izq,codigo+"0",cifrado)
        if cifrado in nodo.der.caracter:
            return asignar_codigos(nodo.der,codigo+"1",cifrado)
    return codigo

def isEmpty(heap):
    if(len(heap.heap)==0):
        return True
    return False

def cifrar_texto_huffman(texto: str) -> tuple:
    freq= {}
    heap=heapalt.MinHeap()
    placeholder=[]
    raiz=None
    for i in range(0,len(texto)):
        if(freq.get(texto[i])==None):
            freq[texto[i]]= 1
            Node= Nodo(texto[i],freq)
            placeholder.append(Node)
        else:
            freq[texto[i]]=freq[texto[i]]+1
    for i in placeholder:
        heap.insert(i)
    while(isEmpty(heap)==False):
        nodo=hacer_arbol_huffman(heap,freq)
        if(isEmpty(heap)):
            raiz=nodo
            break
        heap.insert(nodo)
    codigo= ""
    for i in range(len(texto)):
        codigo+=asignar_codigos(raiz,"",texto[i])

        
    



    """Cifra el texto de entrada utilizando el algoritmo de compresión de Huffman.

    Args:
        texto (str): El texto a comprimir.

    Returns:
        tuple: Una tupla de dos elementos que contiene el texto cifrado y la raiz del árbol
          de Huffman utilizados para el cifrado.
    """
    # Paso 0: calcular la frecuencia de cada caracter en el texto

    # Paso 1: Hacer árbol Huffman

    # Paso 2: Asignar códigos de bits a cada caracter en el árbol

    # Paso 3: codificar el texto con los códigos de bits asignados

    return codigo, raiz


def descifrar_texto_huffman(cifrado: str, nodo: Nodo) -> str:
    """Descifra el texto cifrado utilizando el árbol de Huffman especificado.

    Args:
        texto_cifrado (str): El texto cifrado.
        raiz_huffman (Nodo): La raíz del árbol de Huffman utilizado para cifrar el texto.

    Returns:
        str: El texto descifrado.
    """

    nodosup=nodo
    original=""
    cifrado+=" "
    i=0
    while(i<len(cifrado)):
        if(nodosup.izq!=None or nodosup.der!=None):
            if cifrado[i]=='0':
                nodosup=nodosup.izq
            if cifrado[i]=='1':
                nodosup=nodosup.der
        else:
            original+=nodosup.caracter
            nodosup=nodo
            i-=1
        i+=1
    return original 
texto = "Hola Mundo!"

texto_cifrado, raiz_huffman = cifrar_texto_huffman(texto)
print("Texto cifrado:", texto_cifrado)
# Debe inprimir "Texto cifrado: 1100001011011111110010101110010001101"

texto_descifrado = descifrar_texto_huffman(texto_cifrado, raiz_huffman)
print("Texto descifrado:", texto_descifrado)
# Debe inprimir "Texto descifrado: Hola Mundo!"
