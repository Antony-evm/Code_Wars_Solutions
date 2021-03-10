# Description:
# Find the longest substring within a string that contains at most 2 unique characters.
# This function will take alphanumeric characters as input.

# In cases where there could be more than one correct answer, the first string occurrence should be used.
#  For example, substring('abc') should return 'ab' instead of 'bc'.

# Although there are O(N^2) solutions to this problem, you should try to solve this problem in O(N) time. 
# Tests may pass for O(N^2) solutions but, this is not guaranteed.

# This question is much harder than some of the other substring questions. 
# It's easy to think that you have a solution and then get hung up on the implementation.

def substring(s): 
    u,n = set(s),len(s)
    count = dict(zip(u,[0]*len(u)))
    if len(u)<2:
        return s
    curr_start,curr_end,max_window_size,max_window_start = 0,0,1,0  
    
    for i in range(n): 
        count[s[i]] += 1
        curr_end+=1
        
        while len(set(s[curr_start:curr_end]))>2: 
            count[s[curr_start]] -= 1
            curr_start += 1
            
        if curr_end-curr_start > max_window_size: 
            max_window_size = curr_end-curr_start
            max_window_start = curr_start
            
    return s[max_window_start:max_window_start+max_window_size]