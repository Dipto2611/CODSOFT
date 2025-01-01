"""TASK 2"""

#Simple Calculator using Cmd line

def mycalc():
    
    #taking nos. as input
    N1 = float(input("Enter 1st val:"))
    N2 = float(input("Enter 2nd val:"))
    
    #taking operator input

    ops = input("Enter operator:")

    #operations to be performed

    if ops == "+":
        return N1 + N2
    
    elif ops == "/":
        if N2 == 0:
            return "Error: Division by zero (Not possible)."
        return N1 / N2  
    
    elif ops == "*":
        return N1 * N2  
    
    elif ops == "-":
        return N1 - N2  
    
    else:
        return "Invalid operator."

#lastly call the mycalc func

print(mycalc())
