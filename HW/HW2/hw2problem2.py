alphabet = 'abcdefghijklmnopqrstuvwxyz'
keypad = {' ':'0'}
for i in range(2,10):
    keys = ''; 
    if(alphabet[0] != 'p' and alphabet[0] != 'w'):
        keys = alphabet[:3]
        alphabet = alphabet[3:]
    else:
        keys = alphabet[:4]
        alphabet = alphabet[4:]
    for j in range(len(keys)):
        keypad.setdefault(keys[j],(str(i)*(j+1)))   

def lettertonum(sentence, keypad):
    result = ''
    for i in range(len(sentence)):
        result += keypad[sentence[i]]
    return result            

print(lettertonum('hello world', keypad))
