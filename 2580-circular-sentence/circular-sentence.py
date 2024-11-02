class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(' ')
        if(len(sentence) == 1):
            if(sentence[0][-1] != sentence[0][0]):
                return False
        else:
            
            for i in range(len(sentence)-1):
                if(sentence[i][-1] != sentence[i+1][0]):
                    return False
        if(sentence[0][0]!=sentence[-1][-1]):
            return False
        return True