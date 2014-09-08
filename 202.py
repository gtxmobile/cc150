from random import randint
def shuffle(cards):
    for i in range(len(cards)):
            idx=randint(i,len(cards)-1)
            tmp=cards[i]
            cards[i]=cards[idx]
            cards[idx]=tmp
    print(len(cards),cards)

shuffle([i for i in range(1,53)])

