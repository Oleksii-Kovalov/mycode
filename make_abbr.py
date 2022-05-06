def make_abbr(words: str) -> str:
    abbr = ""
    if len(words) <= 0:
        return abbr
    else: 
        abbr = words[0]      
        for i in range (len(words)):
            if words [i -1] == " ":
                abbr += words[i] 
                   
        return abbr.upper()
    # write your code here
    pass
