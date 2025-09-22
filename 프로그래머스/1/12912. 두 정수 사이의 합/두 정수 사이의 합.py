def solution(a, b):
    answer = 0
    return answer
def solution(a, b):    
    if a == b:
        return a or b
    minimum, maximum = min(a, b), max(a, b)
    return (maximum + minimum) * (maximum - minimum + 1) // 2