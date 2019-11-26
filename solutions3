# via https://github.com/OlegMalinskiy

def solution(w1, w2):
 
  diff = len(w1) - len(w2)
 
  if diff == 0:
    if w1 == w2:
      return 'NOTHING'
 
    for i in range(len(w1)):
      if w1[i] != w2[i]:
        l = w2.find(w1[i])
        r1 = w1[:i] + w1[i+1:]
        r2 = w2[:l] + w2[l+1:]
 
        if r1 == r2:
          return f'MOVE {w1[i]}'
        else:
          return 'IMPOSSIBLE'
 
  elif diff > 1 or diff < -1:
    return 'IMPOSSIBLE'
  else:
 
    big = w1 if diff == 1 else w2
    small = w2 if diff == 1 else w1
    action = 'REMOVE' if diff == 1 else 'INSERT'
    # отдельно обработаем последнюю букву
    if small == big[:-1]:
      return f'{action} {big[-1:]}'
 
    for i in range(len(small)):
      if small[i] != big[i]:
        if small == big[:i] + big[i+1:]:
          return f'{action} {big[i]}'
        else:
          return 'IMPOSSIBLE'
       
       
 
   
 
 
 
print('')
print(solution("beans", "banes"))
print('Must return MOVE e')
 
print('')
print(solution("crow", "cow"))
print('Must return REMOVE r')
 
print('')
print(solution("cow", "coew"))
print('Must return INSERT e')
 
print('')
print(solution("o", "odd"))
print('Must return IMPOSSIBLE')
 
print('')
print(solution("music", "music"))
print('Must return NOTHING')
