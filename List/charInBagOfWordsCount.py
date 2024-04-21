def charInBagOfWordsCount(bagOfWords,keyCharacter):
    count = 0
    
    for i in (bagOfWords):
        count += i.count(keyCharacter)
    return count

