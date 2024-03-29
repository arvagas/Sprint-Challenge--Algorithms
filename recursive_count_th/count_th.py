'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    snippet = 'th'
    counter = 0
    
    if len(word) < 2:
        return 0
    elif word[:2] == snippet:
        counter += 1
        return count_th(word[1:]) + counter
    else:
        return count_th(word[1:])
