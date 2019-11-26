S = list(input('< Give me S string <  '))
T = list(input('< Give me T string <  '))
N = []

def solution(S, T):
    if T == S:
        return 'NOTHING'
    else:
        if len(S) + 1 == len(T):
            S.append(1)
            for i, j in zip(S, T):
                if j != i:
                    N.append(j)
                    break
            return 'INSERT ' + ''.join(N)
        elif len(S) == len(T) + 1:
            T.append(1)
            for i, j in zip(S, T):
                if j != i:
                    N.append(i)
                    break
            return 'REMOVE ' + ''.join(N)
        elif len(S) == len(T):
            for i, j in zip(S, T):
                if j != i:
                    N.append(i)
                    break
            return 'MOVE ' + ''.join(N)
        else:
            return 'IMPOSSIBLE'


print(solution(S, T))
