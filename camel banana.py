a=int(input("Enter total number of bananas:"))                    #total bananas
l=int(input("Enter max load:"))
s=0
while(a>l):
    n=(a/l)*2-1            #no. of trips
    x=l//n                 #distance of check post trips
    s=s+x                  #storing no of bananas consumed
    a=a-l                  #next load of banana
kmleft=a-s
bananasneeded=kmleft
bananasleft=a-bananasneeded
print(bananasleft)
