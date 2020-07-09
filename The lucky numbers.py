def lucky_numbers(x):          #need to insert the offset value once we remove elements to get the absolutely correct outputs
    first_element = x[0]
    for i in x:
        if i % 2 != first_element % 2:
            x.remove(i)
    for i in x[1:]:
        if len(x) < i:
            return x
        for pos, val in enumerate(x):
            if int(pos+1) % i == 0:
                x.remove(val)
    print (x)
integers = [*range(1,26,1)]
print (integers)
print (lucky_numbers(integers))


