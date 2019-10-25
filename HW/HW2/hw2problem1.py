original = "THE QUICK BROWN FOX JUMPS OVER A LAZY DOG"
encrypted = "RBA GMWOQ XJSCL ESV ZMDNK SHAJ U TUIP FSY"

encrypt = {}
for i in range(len(original)):
    encrypt.setdefault(original[i] ,encrypted[i])
    
def cipher(sentence, encrypt):     
    encryptsentence = ""

    for i in range(len(sentence)):
        if sentence[i] not in encrypt:
            encryptsentence += sentence[i]
        else:
            encryptsentence += encrypt[sentence[i]]
    return encryptsentence


sentence = "THE FIVE BOXING WIZARDS JUMP QUICKLY"
encryptsentence = cipher(sentence, encrypt)

print("Original sentence: ", sentence)
print("Encrypted sentence: ", encryptsentence)

sentence = "ITZLF E TFXFTOF WZYVFT LVEL WCPXFTLO EP FPWTGYLFM LFBL HEWS LC LVF CTZQZPEN UFOOEQF HEOFM CP LVF WZYVFT DTCU LVF DZTOL YTCHNFU. ENLVCAQV Z ZUEQZPF GCA YTCHEHNG VEXF DZQATFM CAL VCI LC MC LVEL ZD GCA ETF TFEMZPQ LVZO. GCA UEG ZPWNAMF LVF WCMF DCT LVZO HCPAO YTCHNFU ZP LVF WCMF DCT LVF DZTOL YTCHNFU."
encryptsentence = cipher(sentence, encrypt)

print("\nOriginal sentence: ", sentence)
print("Encrypted sentence: ", encryptsentence)

