# A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. 
# (We may insert each character at any position, and may insert 0 characters.)

# Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.

class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        n = len(queries)
        m = len(pattern)
        answer = []
        
        pattern_upper_case = 0
        for i in range(m):
            if(pattern[i].isupper()):
                pattern_upper_case += 1
                
        for i in range(n):
            upper_case = 0
            counter = 0 
            for j in range(len(queries[i])):
                if(counter < m):
                    if(queries[i][j] == pattern[counter]):
                        counter += 1
                if(queries[i][j].isupper()):
                    upper_case += 1
            if(counter == m and upper_case == pattern_upper_case):
                answer.append(True)
            else:
                answer.append(False)
                
        return answer
                