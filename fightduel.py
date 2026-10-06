def wizards(N,start,duels):
#who has wand at the end
    #extra
    
    owner = start
    changed_hands = 1
    #print(duels[0][1])
    for i in range(N):
        if duels[i][1] == owner:
            owner = duels[i][0]
            changed_hands +=1
    print(owner)
    print(changed_hands)
#how many duels needed
wizards(3,"A",["BA","AB","BA"],)