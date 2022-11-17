__all__ =['addnum','divnum'] # restricts function to be exported when 'from module import *' directive is used in calling script
def addnum(a,b):
    return a+b

def divnum(a,b):
    return a/b

def sayhello():
    print("helloworld")