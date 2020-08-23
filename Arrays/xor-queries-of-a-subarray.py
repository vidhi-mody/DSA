class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []
        n  = len(arr)
        
        look_up_table = [0] * (n)
        look_up_table[0] = arr[0]

        for i in range(1,n):
            look_up_table[i] = look_up_table[i-1] ^ arr[i]

        for q in queries:
            if(q[0]-1 < 0):
                result.append(look_up_table[ q[1]])
            else:
                left = look_up_table[ q[0]-1]    
                right = look_up_table[ q[1]]
                result.append( left ^ right )
            
        return result