class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        unique_rep = set()
        
        for word in words:
            rep = ""
            for c in word:
                rep += morse_code[ord(c)-ord('a')]
            unique_rep.add(rep)
        return len(unique_rep)
