#write a program using function to convert celsius to fahrenheit.

#formula : celsius/5 = (fahrenheit-32)/9

f = int(input("Enter tempreture in f: "))

def f_to_c():
    c = 5*(f-32)/9
    print(f"{round(c,2)} C")


f_to_c()    