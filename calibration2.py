input=open("input1.txt", 'r')

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
Dict={'zero': 0,
      'one': 1,
      'two': 2,
      'three': 3,
      'four': 4,
      'five': 5,
      'six': 6,
      'seven': 7,
      'eight': 8,
      'nine': 9,
      '0': 0,
      '1': 1,
      '2': 2,
      '3': 3,
      '4': 4,
      '5': 5,
      '6': 6,
      '7': 7,
      '8': 8,
      '9': 9}

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def isSubstringOf(string):
    indices = {}
    for i in numbers:
        if string.find(i) > -1:
            indices.update({i: string.find(i)})
    for i in num:
        if string.find(i) > -1:
            indices.update({i: string.find(i)})
    a = min(indices, key=indices.get)
    return Dict[a]

numbersBack = ['orez', 'eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']
Dict2 = {'orez': 0,
         'eno': 1,
         'owt': 2,
         'eerht': 3,
         'ruof': 4,
         'evif': 5,
         'xis': 6,
         'neves': 7,
         'thgie': 8,
         'enin': 9,
         '0': 0,
         '1': 1,
         '2': 2,
         '3': 3,
         '4': 4,
         '5': 5,
         '6': 6,
         '7': 7,
         '8': 8,
         '9': 9}

def isBackSubstringOf(string):
    indices={}
    for i in numbersBack:
        if string.find(i) > -1:
            indices.update({i: string.find(i)})
    for i in num:
        if string.find(i) > -1:
            indices.update({i: string.find(i)})
    a = min(indices, key=indices.get)
    return Dict2[a]

l = []
for line in input:
    l.append(isSubstringOf(line)*10 + isBackSubstringOf(line[::-1]))
print(sum(l))

        
