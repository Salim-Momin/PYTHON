def goodday(name):
    print("Good Day " + name)

goodday("Salim")    #this is also called function argument

def goodmor(name,greet):
    print("Good morning "+ name +"\n" +greet)


goodmor("Salim","Thank You!")    


def greet(name):
    gr = "hello " + name
    return gr      #"return" deliver the value in variable

a = greet("Salim")

print(a) #output is "hello Salim"