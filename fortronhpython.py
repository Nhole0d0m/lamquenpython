length=3
iter_ = (x for x in range( length))
for value in iter_:
    print('->', value)
c=0
while 1:
    #print(next(iter_))
    #c+=1 
    try:
       print(next(iter_))
    except StopIteration:
        break
    
howkteam={'name':'kteam', 'kter':69}
for key,value in howkteam.items():
    print(key,'->',value)
