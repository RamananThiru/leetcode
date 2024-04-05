# April 5, 2024


# Problem: https://leetcode.com/problems/find-common-characters/ 



class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        prev_hash = {}
        prev_hash = self.countFrequency(words.pop(0))
        for i in words:
            freq_hash = self.countFrequency(i)

            if prev_hash:
                result = self.compareHashes(prev_hash, freq_hash)
                print(result)
                prev_hash = result
        result_array = []        
        for key, value in prev_hash.items():
            result_array.extend([key] * value)        
        return result_array    


    def countFrequency(self , word):
        hash = {}

        for i in word:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1       
        return hash


    def compareHashes(self, hash1, hash2):
        result_hash = {}
        for key, value in hash1.items():
            if key in hash2:
                result_hash[key] = min(value, hash2[key])
        return result_hash     
                  
        
