offensive = ['Strength:Flare' , 'HP:Ultima' , 'Speed:Nothing' , 'Vit:Quake']
support = ['HP:Ultima' , 'Magic:Flare' , 'Defense:Quake' , 'Spiret:Curega']
defense = ['HP:Ultima' , 'Vit:Reflect' , 'Magic:Flare' , 'Strength:Quake']
offMagic = ['Damage:Ultima' , 'Status:Confusion' , 'GF:Eden']
supMagic = ['Heal:Curega' , 'Overtime:Regen' , 'Cure:Esuna']
defMagic = ['Protection:Shell' , 'AntiSpells:Reflect' , 'GF:Carbuncle']
cards = ['Laguna' , 'Alexander' , 'Rinoa' , 'Squall' , 'Edea']
cheap = ['Squall:Punishment' , 'Irvine:Ulysses' , 'Rinoa:Rising Sun' , 'Selphie:Morning Star' , 'Zell:Gauntlet' , 'Quistis:Slaying Tail']
expensive = ['Squall:Lionheart' , 'Irvine:Exeter' , 'Zell:Ergize' , 'Selphie:Strange Vision' , 'Rinoa:Shooting Star' , 'Quistis:Save the Queen']
x , y , z , h = offensive

e , d , a , b = support

j , c , k , i = defense

u , q , p = offMagic

f , m , n = supMagic

l , g , t = defMagic

X , Y , Z , D , H = cards

Q , A , E , T , P , R = cheap

r , S , F , M , N , B = expensive
ff8Junction = 'ff8 junction'

ff8Magic = 'ff8 magic'

ff8Weapons = 'ff8 Weapons'

ff8Cards = 'ff8 cards'

I = 1

Yes = 'Yes'

No = 'No'

while I < 2 :
    print('Hello World!')
    Choice = input('what would you like to do >> ')
    if Choice == ff8Junction :
        print('What are you priortizing?')
        Off = 'off'
        Sup = 'sup'
        Def = 'def'
        Choice2 = input()
        if Choice2 == Off :
            print(x)
            print(y)
            print(z)
            print(h)
        elif Choice == Sup :
            print(e)
            print(d)
            print(a)
            print(b)
        elif Choice2 == Def :
            print(j)
            print(c)
            print(k)
            print(i)
    elif Choice == ff8Magic :
        offMage = 'Offensive'

        supMage = 'Support'

        defMage = 'Defensive'

        Choice3 = input('What are you priortizing? >> ')

        if(Choice3 == offMage) :
            print(u)
            print(q)
            print(p)
        elif(Choice3 == supMage) :
            print(f)
            print(m)
            print(n)
        elif(Choice3 == defMage) :
            print(l)
            print(g)
            print(t)
        else :
            exit
    elif Choice == ff8Weapons :
        Cheap = 'Cheap'
        Expensive = 'Expensive'
        Choice4 = input('Cost? >> ')
        if(Choice4 == Cheap) :
            print(Q)
            print(A)
            print(E)
            print(T)
            print(P)
            print(r)
        elif(Choice4 == Expensive) :
            print(r)
            print(S)
            print(F)
            print(M)
            print(N)
            print(B)
        else:
            exit
    elif Choice == ff8Cards:
       print('This is the best card set in the game')
       print(X)
       print(Y)
       print(Z)
       print(H)
       print(D)
    else:
        print('error')
        exit
    Choice5 = input('Would u like to close? >> ')
    if(Choice5 == Yes) :
        break
    elif(Choice5 == No) :
        print('ok')
print('Goodbye!')
exit