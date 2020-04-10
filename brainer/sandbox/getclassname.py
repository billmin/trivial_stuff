import sys
class Hello():
 
    def hello(self):
        print('the name of method is ## {} ##'.format(sys._getframe().f_code.co_name))
        print('the name of class is ## {} ##'.format(self.__class__.__name__))
        print('the class type is ## {} ##'.format(self.__class__))
    def pop(self):
        print("this is pop opt")
 
if __name__ == "__main__":
    h = Hello()
    h.hello()
    print(type(h))
    print(Hello)
    h.pop()
