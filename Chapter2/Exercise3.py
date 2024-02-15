Stones = [1,7,4,3,1,9,4,2,1,78,45]
w = 16

#need to sort first because you have to maximize the amount
def stone_amount(Stones, w):
    amount = 0
    weight = 0

    for i in range(len(Stones)):
        weight = weight + Stones[i]
        amount = amount+1
        if weight > w:
            return amount-1

print(stone_amount(Stones,w))