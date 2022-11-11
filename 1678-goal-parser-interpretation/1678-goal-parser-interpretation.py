class Solution:
    def interpret(self, cmd: str) -> str:
        cmd = cmd.replace("()","o")
        cmd = cmd.replace('(al)','al')
        return cmd