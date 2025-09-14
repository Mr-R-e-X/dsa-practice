class Valid_Anagram:
    
    # ! Time Complexity O(nlogn + mlogn)
    # ^ Space Complexity O(n+m)
    def sorting(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
    
    # * Time Complexity O(n+m)
    # * Space Complexity O(1), since we have most 26 different characters
    def hash_map(self, s:str, t:str)-> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[s[i]] = 1 + countT.get(s[i], 0)
        
        return countS == countT
    
    # * Time Complexity O(n+m)
    # * Space Complexity O(1), since we have most 26 different characters
    def hash_table(self, s:str, t:str)->bool:
        if len(s) != len(t):
            return False

        count_alphates = [0] * 26
        for i in range(len(s)):
            count_alphates[ord(s[i]) - ord('a')] += 1
            count_alphates[ord(s[i]) - ord('a')] -= 1
        
        for val in count_alphates:
            if val != 0:
                return False
        
        return True