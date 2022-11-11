class Solution:
    def interpret(self, command: str) -> str:
        return_string = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                return_string += 'G'
                i += 1
            elif command[i:i + 2] == '()':
                return_string += 'o'
                i += 2
            else:
              
                return_string += 'al'
                i += 4

        return return_string        