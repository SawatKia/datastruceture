bid = input("Enter All Bid : ")
bid = bid.split(' ')
for i in range(0, len(bid)):
    bid[i] = int(bid[i])
bid.sort()


if len(bid)==1:
    print("not enough bidder")
elif bid[-1]==bid[-2]:
    print("error : have more than one highest bid")
else :
    bid.sort()
    print("winner bid is",end = ' ')
    print(bid[-1],end = ' ')
    print("need to pay",end = ' ')
    print(bid[-2])



