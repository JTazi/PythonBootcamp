#write function for n coins where every x coin is flipped where x = 2 through n
'''create a dictionary where each key is a coin and the value is heads or tails'''
'''even = heads, odd = tails'''
'''coins start on heads up'''
def coin_flip(n):
    head_list=[]
    coins = []
    coin_count = 0
    x=1
    while x<=n: 
        coins.append(0)
        x+=1
    for y in range(2,n+1):
        for val in range(y-1,n,y):
            coins[val]+=1
    for coin in coins:
        coin_count +=1
        if coin%2==0:
            head_list.append(coin_count)
    return head_list
