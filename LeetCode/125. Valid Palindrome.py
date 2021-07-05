# 36ms / 15.6 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)
        return s==s[::-1]

# 48ms / 19.2 MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
        for char in s:
            #is char alphabet or number
            if char.isalnum():
                strs.append(char.lower())
        while(len(strs)>1):
            if(strs.popleft()!=strs.pop()):
                return False
        return True

#288ms / 19.6MB
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs=[]
        for char in s:
            #is char alphabet or number
            if char.isalnum():
                strs.append(char.lower())
        while(len(strs)>1):
            if(strs.pop(0)!=strs.pop()):
                return False
        return True
