def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    count_letter = 0
    for i in phrase.lower():
        if i == letter.lower():
            count_letter += 1
        else:
            count_letter += 0
    return count_letter        
    pass
