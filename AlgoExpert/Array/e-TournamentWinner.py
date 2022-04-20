competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"],
]

results = [0,0,1]

# "Python"
# C# beats HTML, Python beats C#, Python beats HTML

# Approach = Using an hashtable for each of the members
def calculate(comp, results):
    H = {}
    i = 0 
    while i < len(competitions):
        member = competitions[i]
        r = results[i]
        winner = member[1]
        if r :
            winner = member[0]
        
        if winner in H:
            H[winner] +=3 
        else:
            H[winner] = 3
        i+=1 

    max = 0 
    winner = ""
    for key,val in H.items():
        if val > max:
            max = val
            winner = key
    return winner


print(calculate(competitions,results))