def encrypt(sentence, letters, letterCount, shiftCount):
    result = "";
    for x in sentence:
        if(x == " "):
            result+=" "
        else:
            result+=letters[((letters.index(x.lower())+shiftCount) % letterCount)]
    result = result.upper()
    print("\nSentence: "+sentence+"... Encrypted to -> "+result)
    return result

def decrypt(sentence, letters, letterCount, shiftCount):
    result = "";
    for x in sentence:
        if(x == " "):
            result+=" "
        else:
            result+=letters[((letters.index(x.lower())-shiftCount) % letterCount)]
    result = result.lower();
    print("\nSentence: "+sentence+"... Decrypted to -> "+result)
    return result;


engLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
frLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
spLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
trLetters = ["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","q","w","x"];
f = open("input.txt", "r");
wholetxt = f.readlines();
f.close();
for line in wholetxt:
    x = line.replace("\n","")
    shiftCount,opr,lang,txt = x.split(":");
    shiftCount = int(shiftCount);
    selectedLetters = engLetters if lang =="0" else frLetters if lang == "1" else spLetters if lang == "2" else trLetters if lang == "3" else 0
    letterCount = len(selectedLetters)
    if opr == "0":
        encrypt(txt, selectedLetters, letterCount, shiftCount)
    elif opr =="1":
        decrypt(txt, selectedLetters, letterCount, shiftCount)
