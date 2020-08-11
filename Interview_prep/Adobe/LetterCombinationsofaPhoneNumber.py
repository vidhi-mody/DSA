class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        def find_combination(combination, next_digits):
            
            if len(next_digits) == 0:
                answer.append(combination)  
            
            else:
                for letter in mapping[next_digits[0]]:
                    find_combination(combination+letter, next_digits[1:])
                    
        if digits :
            find_combination("", digits)
        return answer