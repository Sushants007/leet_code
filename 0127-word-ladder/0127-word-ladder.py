class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        deque = collections.deque([(beginWord, 1)])
        ls = string.ascii_lowercase
        wordList = set(wordList)
        while deque:
            word, dist = deque.popleft() # BFS one word by one word
            if word == endWord:
                return dist
            for i in range(len(word)):
                for c in ls:
                    if word[i] != c:
                        newWord = word[:i]+c+word[i+1:]
                        if newWord in wordList:
                            wordList.remove(newWord)
                            deque.append((newWord, dist+1))
        return 0