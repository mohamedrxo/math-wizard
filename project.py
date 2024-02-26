#import dependancies tkinter and sympy

import tkinter as tk
# tkinter is tool that can help use previde simple GUI
from sympy import sympify,diff,plot,limit,symbols,integrate,expand,oo
# sympy is function that can help us to calculate the derivative the limits and lot more
def calculer():
    # this function will help us to get the value of the function that we want to calclulate the derivative for
    lit.delete(0,10)
    
    a=sympify(b1.get())
    b=b2.get()
    y=symbols("x")
    if b=="oo" or b=="-oo":
        b=b2.get()
    else:
        b=int(b2.get())
    c=b3.get()
    m,n=c.split(",")
    m=int(m)
    n=int(n)
 
    if a!="" and b!="" and c!="":
        lit.insert(0,f"derivative of {a} is : {diff(a)} ")
        if b=="oo":
            lit.insert(1,f"the limit of {a} when it aproche {b} is from the left  : {limit( a,y,oo,dir='-')}")
            lit.insert(2,f"the limit of {a} when it aproche {b} is from the right : {limit( a,y,oo,dir='+')}")
        elif b=="-oo":
            lit.insert(1,f"the limit of {a} when it aproche {b} is from the left  : {limit( a,y,-oo,dir='-')}")
            lit.insert(2,f"the limit of {a} when it aproche {b} is from the right : {limit( a,y,-oo,dir='+')}")
        else:
            lit.insert(1,f"the limit of {a} when it aproche {b} is from the left  : {limit( a,y,b,dir='-')}")
            lit.insert(2,f"the limit of {a} when it aproche {b} is from the right : {limit( a,y,b,dir='+')}")
        
        if limit( a,y,b,dir='-')==limit( a,y,b,dir='+'):
                lit.insert(3,f" then the limits of the function when it approch {b} is {limit( a,y,b,dir='-')}")
        else:
            lit.insert(4,"this limit does not exist (D.N.E)")
        
        
       
        lit.insert(5,f"the interval of the function {a} over the interval {m} to {n} is : {integrate(a,(y,m,n))} ")
        plot(a,diff(a),(y,-10,10),title=f"f(x)={a}",legend=True)

def clear():
    b1.delete(0,50)
    b2.delete(0,50)
    b3.delete(0,50)
    lit.delete(0,50)


        
    
#creating that simple GUI with tkinter
root=tk.Tk()
l1=tk.Label(text="function")
b1=tk.Entry()
l2=tk.Label(text="limits")
b2=tk.Entry()
l3=tk.Label(text="intagral")
b3=tk.Entry()
lit=tk.Listbox(width=70)
# use calculer methode that we wrote in the button
bt=tk.Button(text="calculer",command=calculer)
btn=tk.Button(text="clear",command=clear)
l1.grid(column=0,row=0,columnspan=5)
b1.grid(column=2,row=0,columnspan=6)
l2.grid(column=0,row=1,columnspan=5)
b2.grid(column=2,row=1,columnspan=6)
l3.grid(column=0,row=2,columnspan=5)
b3.grid(column=2,row=2,columnspan=6)
bt.grid(column=5,row=3)
btn.grid(column=4,row=3)
lit.grid(column=0,row=4,columnspan=10)
root.mainloop()
#finishing our awesome project