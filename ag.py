class Tensor:

  def __init__(self, data, children, op='')
    self.data = data.array # numpy array?
    self.grad = 0 # initialized at 0, will be calculated and used other places
    self.prev = set(children) # set object for multiple elements?
    self.op = op

  def __add__(self, other)
    if other is not value then value(other) else other = other
    out = Tensor(self.data + other.data, (self, other), '+')

    return out

    def backward(self, other)
      self.grad += out.grad * 1.0
      other.grad += out.grad * 1.0
# chain rule for addition is passing on grad from child node
# we want to increment to update grad in chain rule instance,
# or updating the variables used in chain rule
# we updated variables and so, probably want to return something?


__mul__
out = tensor(self.data * other.data, (self, other), '*')

       backward
         self = other.grad * 1.0
         other = self.grad * 1.0


__tanh__



__relu__


__neg__



__sub__


__pow__







