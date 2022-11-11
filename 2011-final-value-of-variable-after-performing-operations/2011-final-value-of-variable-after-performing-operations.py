class Solution:
    def finalValueAfterOperations(self, ops: List[str]) -> int:
        X=0
        for i in range(len(ops)):
            if ops[i]=='--X' or ops[i]=='X--':
                X=X-1
            else:
                X=X+1
        return X