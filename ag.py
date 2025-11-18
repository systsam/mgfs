class Tensor:

  def __init__(self, data, children=(), op=''):
      self.data = data
      self.grad = 0.0 # initialized at 0, will be calculated and used other places
      self.prev = set(children) # set eliminates duplicates 
      self.op = op 

  def __add__(self, other):
     # if other is not value then value(other) else other = other
      out = Tensor(self.data + other.data, (self, other), '+')

      return out

      def backward(self, other):
          self.grad += out.grad
          other.grad += out.grad
          
      out.backward = backward
      return out

# chain rule for addition is passing on grad from child node
# we want to increment to update grad in chain rule instance,
# or updating the variables used in chain rule
# we updated variables and so, probably want to return something?


  def __mul__(self, other):
      out = Tensor(self.data * other.data, (self, other), '*')

      return out

      def backward(self, other):
          self.grad += other.data * out.grad
          other.grad += self.data * out.grad

      out.backward = backward
      return out

#__tanh__



#__relu__


#__neg__



#__sub__


#__pow__




  def __repr__(self):
    return f"Tensor(data={self.data}, grad={self.grad})"


x = Tensor(2.0)
y = Tensor(3.0)
out = x*y
out2 = x+out
print(x)
print(y)
print(out)
print(out2)
