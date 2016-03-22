def solution(N):
    # write your code in Python 2.7
    b = bin(N)[2:]
    
    gaps = []
    
    gap = 0 # gap length
    bg = 0 # begin gap
    for i, item in enumerate(b):
        # import ipdb; ipdb.set_trace()   
        if bg == 1 and item == '0':
            gap += 1
        
        if b[i - 1 : i + 1] == '01' and i > 0:
            bg = 0
            gaps.append(gap)
            gap = 0 # reset gap

        if b[i:i+2] == '10':
            # beginning of a gap
            bg = 1
    
    if len(gaps) == 0:
        return 0
    return max(gaps)