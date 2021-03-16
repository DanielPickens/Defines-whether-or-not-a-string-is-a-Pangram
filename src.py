def isitaPangram(str): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in str.lower(): 
            return False
  
    return True
      
#next 
string = 'the quick brown fox jumps over the lazy dog'
if(isitaPangram(string) == True): 
    print("Yes") 
else: 
    print("No")
