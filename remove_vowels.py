def remove_vowels(document: str) -> str:
    message = document.lower()
    search = "a", "e", "i", "o", "u", "y"
    for i in document:
        if i in search:
            message = message.replace (i, "")
    return message


    # write your code here
    pass
