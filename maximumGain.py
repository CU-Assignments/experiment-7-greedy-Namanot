class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        first, first_score, second, second_score = ("ab", x, "ba", y) if x >= y else ("ba", y, "ab", x)
        def remove_substring(s, target, points):
            arr = list(s)  
            left = 0  
            score = 0
            for right in range(len(arr)):
                arr[left] = arr[right]  
                if left > 0 and arr[left - 1] == target[0] and arr[left] == target[1]:
                    left -= 1  
                    score += points
                else:
                    left += 1  
            return "".join(arr[:left]), score
        remaining_s, max_points = remove_substring(s, first, first_score)        
        _, second_points = remove_substring(remaining_s, second, second_score)
        return max_points + second_points
        