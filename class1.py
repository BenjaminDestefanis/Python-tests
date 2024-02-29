
""" Test 1 - Word Length [Largo de palabra] """

def word_length(word):
    # La function de retornar el largo de la palabra(word) recibida
    # Si (word) es un numero, retornar el mensaje "No recibe numeros."
    # Tu codigo AQUI:
    if isinstance(word, int):
        return "No recibe numeros."
    else:
        return len(word)
    
    
"""" Test 2 - is Palindrome? [Es palindromo] """
    
