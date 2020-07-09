

def remove_duplicates(x):
    previous_character = x[0]
    offset = 0
    for pos, char in enumerate(x[1:]):
        pos = pos-offset
        if char == previous_character:
            x = x[0:pos] + x[pos+1:]
            offset += 1
        previous_character = char
    return x

def replace_pi(x):
    offset = 0
    for pos, char in enumerate(x):
        print (pos)
        pos = pos - offset
        if char == 'i' and pos != 0 and x[pos-1] == 'p':
            x = x[0:pos-1] + '3.14' + x[pos+1:]
            offset -= 2
    return x

def duplicates_and_pi(x): #In the example sentence given, in the output the last 'pie' is left as is. However, the task
    words = x.split()      # specifies that all 'pi' string values should be replaced with '3.14', which would include 'pie'
    text = ""
    for i in words:
        i = remove_duplicates(i)
        i = replace_pi(i)
        text += (i + ' ')
    text.strip()
    return text







#print (remove_duplicates(x))
#print (replace_pi(x))
text = ('I donnt knooow pii value, so I wil go eat my ppiie...')
print (duplicates_and_pi(text))

