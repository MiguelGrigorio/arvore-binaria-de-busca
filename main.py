counter = 1
datas = []

with open("dados.csv", 'r') as f:
  for line in f:
    a = line.split(',')
    a[1] = a[1].replace('\n', '')
    
    try:
      a[0] = int(a[0])
    except:
      pass
    datas.append(a)

datas.pop(0)

class Arvore():
  def __init__(self, data, nome):
    self.data = data
    self.nome = nome
    self.left = None
    self.right = None
    
    self.busca(data)
    self.delete_node(data)

  def busca(self, data):
    global counter
   
    if self.data == data:
      return self.data, self.nome

    elif self.data > data:
      counter += 1
      if self.left == None:
        return None, data
      else:
        return self.left.busca(data)
        
    else:
      counter += 1
      if self.right == None:
        return None, data
      else:
        return self.right.busca(data)

  def insercao(self, data, nome):
    if data < self.data:
      if self.left == None:
        self.left = Arvore(data, nome)
      else:
        self.left.insercao(data, nome)
    else:
      if self.right == None:
        self.right = Arvore(data, nome)
      else:
        self.right.insercao(data, nome)

  #Identificar o menor elemento do nó
  def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

  #Usando a regra do menor elemento da direita
  def delete_node(self, value):
    if self is None:
        return self

    if value < self.data:
        self.left = self.left.delete_node(value)
    elif value > self.data:
        self.right = self.right.delete_node(value)
    else:
        if self.left is None:
            return self.right
        elif self.right is None:
            return self.left

        self.data = self.right.find_min().data
        self.right = self.right.delete_node(self.data)

    return self
    
def search_siape(search, print_ = False):
  global counter
  if search[0]:
    if print_ == True:
      print(f'O SIAPE {search[0]} foi encontrado na árvore! pertence a {search[1]}')
      print(f'Quantidade de buscas realizadas: {counter}\n')

    pos = counter
    counter = 1
    return pos
  
  else:
    if print_ == True:
      print(f'O SIAPE {search[1]} não foi encontrado')
      print(f'Quantidade de buscas realizadas: {counter}\n')
    counter = 1

def make_file(filename, tree: Arvore):

  node = tree
  with open(f"{filename}.csv", 'w') as d:
    d.write('SIAPE,Nome\n')
    
    def inorder(node = None):
      if node.left:
          inorder(node.left)
      d.write(f'{node.data},{node.nome}\n')
      if node.right:
          inorder(node.right)

    inorder(node)
    
# Organizando os dados na Árvore Binária
tree = None
for index in range(len(datas)):
  if index == 0:
    tree = Arvore(datas[index][0], datas[index][1])
  else:
    tree.insercao(datas[index][0], datas[index][1])

make_file('ordem_antes', tree)

search_siape(tree.busca(53062), True)
search_siape(tree.busca(25252), True)

tree.delete_node(18241)
tree.delete_node(32067)

make_file('removido', tree)

tree.insercao(32067, 'Júlio Moura')
make_file('inserido', tree)