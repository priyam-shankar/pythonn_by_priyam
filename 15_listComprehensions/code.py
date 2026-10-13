squares = []
for i in range(6):
    squares.append(i*i)
    
print(squares)

#list comprehension 

sq = [i*i for i in range(6)]
print(sq)

sqs = [i*i for i in range(6) if(i%2 != 0)]
print(sqs)