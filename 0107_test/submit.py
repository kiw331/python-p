
from sys import stdin, exit

from sys import stdin
from itertools import combinations, permutations
from itertools import permutations

# n = input()

# a, b = map(int, input().split())

def solution(order):
    answer = 0
    
    for i in order:
        
        answer = 0
    
        #
        if i in 'cafelatte':
            answer += 5000
            
        else:
            answer += 4500
            
    print(answer)
            
    return answer

od = ['americanoice','cafelatte','hotcafelatte','anything']
a = solution(od)