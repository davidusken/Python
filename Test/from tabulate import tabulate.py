from tabulate import tabulate

def output(): 

    grossSalJan = int(15000)
    netSalJan = int(10000)
    taxJan = int(5000)
    
    table = [["January",grossSalJan,netSalJan,taxJan],["February",0,0,0],["March",0,0,0]]
    headers = ["Gross salary", "Net salary", "Tax"]

    print(tabulate(table, headers, tablefmt="pretty"))
