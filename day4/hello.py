__all__ =['addnum','divnum'] # restricts function to be exported when 'from module import *' directive is used in calling script

def addnum(a,b):
    print(__name__)
    return a+b

def divnum(a,b):
    return a/b

#def sayhello():
#    print("helloworld")

# value for __name__ in the current script is __main__ and in calling script it is hello(module name)
    
if __name__ == '__main__':
    print("calling from module:", __name__) 
    print("calling from module:",addnum(35,7))
    print("calling from module:",divnum(35,7))