def solutions(S, T):
    Sl = len(S)
    Tl = len(T)
    if Sl-Tl > 1 or Sl-Tl < -1:
        print ("IMPOSSIBLE")
    else:
        if Sl-Tl == 1:
            if S[0:Tl] == T[0:Tl]:
                c = S[Tl]
                print("REMOVE", c)
            else:
                for x in range(Tl):
                    if S[x] != T[x]:
                        c = S[x]
                        if S[x+1:Sl] == T[x:Sl]:
                            print("REMOVE", c)
                            break
                        else: 
                            print("IMPOSSIBLE")
                            break
        if Sl-Tl == -1:
            if S[0:Sl] == T[0:Sl]:
                c = T[Sl]
                print("INCERT", c)
            else:
                for x in range(Sl):
                    if S[x] != T[x]:
                        c = T[x]
                        if S[x:Tl] == T[x+1:Tl]:
                            print("INCERT", c)
                            break
                        else: 
                            print("IMPOSSIBLE")
                            break
        if Sl-Tl == 0:
            if S == T:
                print("NOTHING")
            for x in range(Sl):
                if S[x] != T[x]:
                    if S[x] == T[Sl-1]:
                        print("MOVE", S[x])
                        break
                    c = S[x]
                    while S[x+1] == T[x]:
                        x=x+1
                    if c == T[x] and S[x+1:Sl] == T[x+1:Sl]:
                        print("MOVE", c)
                        break
                    else:
                        print("IMPOSSIBLE")
                        break
