input=open("input1.txt", 'r')


def findDigitIn(t):
    "findsthe first digit in t"
    for i in t:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return int(i)

def findLastDigitIn(t):
    x = t[::-1]
    for i in x:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return int(i)
        
#a = findDigitIn(input.readline())
#print(a)
#b= findLastDigitIn(input.readline())
#print(b)



l = []
for line in input:
    l.append((findDigitIn(line)*10 + findLastDigitIn(line)))

print(sum(l))
input.close()
