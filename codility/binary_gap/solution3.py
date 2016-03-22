# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


def solution(N):
    # write your code in Python 2.7
    N = bin(N)[2:]
    if not N.endswith('1'):
        N = N.split('1')[:-1]
    else:
        N = N.split('1')
    N = [elem for elem in N if elem]
    if N:
        return len(max(N))
    return 0
