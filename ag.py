class Tensor:

  def __init__(self, data, children=(), op=''):
      self.data = data
      self.grad = 0.0 # initialized at 0, will be calculated and used other places
      self.prev = set(children) # set eliminates duplicates 
      self.op = op 
      self._backward = lambda: None


  def __add__(self, other):
      other = other if isinstance(other, Tensor) else Tensor(other)
      out = Tensor(self.data + other.data, (self, other), '+')

      def _backward():
          self.grad += out.grad
          other.grad += out.grad
          
      out._backward = _backward
      return out

# chain rule for addition is passing on grad from child node
# we want to increment to update grad in chain rule instance,
# or updating the variables used in chain rule


  def __mul__(self, other):
      other = other if isinstance(other, Tensor) else Tensor(other)
      out = Tensor(self.data * other.data, (self, other), '*')

      def _backward():
          self.grad += other.data * out.grad
          other.grad += self.data * out.grad

      out._backward = _backward
      return out

  def __pow__(self, n):
      # n = n if isinstance(n, Tensor) else Tensor(n)
      out = Tensor(self.data ** n, (self,), '**{n}')

      def _backward():
          self.grad += other.data * out.grad
          other.grad += self.data * out.grad

      out._backward = _backward
      return out

#__tanh__



#__relu__


#__neg__



#__sub__



  def backward(self):
      topo = []
      visited = set()

      def build_topo(node):
          if node not in visited:
              visited.add(node)
          for parent in node.prev:
              build_topo(parent)
          topo.append(node)
   
      build_topo(self)

      self.grad = 1.0
      for node in reversed(topo):
          node._backward()
      print(topo)

  def __repr__(self):
    return f"Tensor(data={self.data}, grad={self.grad})"


a = Tensor(2.0)
b = Tensor(3.0)
d = (a*b) + a
d.backward()
print("a value:", a.data,", b value:", b.data,", d value:", d.data)
print("a grad:", a.grad,", b grad:", b.grad,", d grad:", d.grad)






