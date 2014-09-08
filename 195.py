
def hit(guess,solution):
    hits=0
    phist=0
    for i in range(len(guess)):
        if guess[i]==solution[i]:
            hits+=1
        elif guess[i] in solution:
            phist+=1
    print(hits,phist)

hit('yrgb','rggb')


