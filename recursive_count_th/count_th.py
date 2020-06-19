'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    target = "th"
    len_th = len(target)
    # base case
    if len(word) == 0 or len(word) < len_th:
        return 0
    # check first two characters
    if word[0:len_th] == target:
        return count_th(word[1:])+1
    #  if not found, continue finding
    return count_th(word[1:])
