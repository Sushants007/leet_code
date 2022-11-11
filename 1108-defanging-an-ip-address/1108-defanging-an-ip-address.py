class Solution:
    def defangIPaddr(self, ad: str) -> str:
        ans=''
        for i in range(len(ad)):
            if ad[i]=='.':
                ans=ans+'[.]'
            else:
                ans=ans+ad[i]
        return ans