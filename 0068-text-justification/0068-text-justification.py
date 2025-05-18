class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        n = len(words)
        self.MAX_WIDTH = maxWidth
        i = 0      
        while i < n:
            letters_count = len(words[i])
            j = i + 1
            space_slots = 0
            
            while j < n and space_slots + letters_count + len(words[j]) + 1 <= maxWidth:
                letters_count += len(words[j])
                space_slots += 1
                j += 1
            
            remaining_slots = maxWidth - letters_count
            
            each_word_space = 0 if space_slots == 0 else remaining_slots // space_slots
            extra_space = 0 if space_slots == 0 else remaining_slots % space_slots
            
            if j == n:
                each_word_space = 1
                extra_space = 0
            
            result.append(self.get_final_word(i, j, each_word_space, extra_space, words))
            i = j    
        return result
    
    def get_final_word(self, i: int, j: int, each_word_space: int, extra_space: int, words: list[str]) -> str:
        s = ""
        
        for k in range(i, j):
            s += words[k]
            
            if k == j - 1:
                continue
            
            for space in range(1, each_word_space + 1):
                s += " "
            
            if extra_space > 0:
                s += " "
                extra_space -= 1
        
        while len(s) < self.MAX_WIDTH:
            s += " "
        
        return s     