def solution(N):
    # write your code in Python 2.7
    b = bin(N)[2:]
    
    gaps = []
    
    gap = 0 # gap length
    bg = 0 # begin gap
    for i, item in enumerate(b):   
        if b[i:i+2] == '10':
            # beginning of a gap
            bg = 1
        
        if bg==1 and item == '0':
            gap += 1
        
        if item == '1' and i > 0:
            bg = 0
            gaps.append(gap)
    
    if len(gaps) == 0:
        return 0
    return max(gaps)