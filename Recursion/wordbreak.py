class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def helper(st,s,wordDict):
            print(st)
            if not s:
                return st in wordDict
            if st in wordDict:
                if helper(s[0],s[1:],wordDict) or helper(st+s[0],s[1:],wordDict):
                    return True   
            return helper(st+s[0],s[1:],wordDict)       
        return helper("",s,wordDict)
        
