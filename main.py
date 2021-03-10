class A():
    def __init__(self, a=100):
        self._a = a
    
    def print_var(self):
        print(self._a)

class B(A):
    def __init__(self, b=200):
        self._b = b
        super().__init__()
    
    def print_ext(self):
        self.print_var()

if __name__ == "__main__":
    b = B()
    b.print_ext()