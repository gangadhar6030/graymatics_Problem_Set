def knapsack_recursion(m,w,v,n):
    if n==0 or m<=0:
        return 0
    if w[n-1]>m:
        return knapsack_recursion(m,w,v,n-1)
    else:
        return max(v[n-1]+knapsack_recursion(m-w[n-1],w,v,n-1),knapsack_recursion(m,w,v,n-1))


name="name"
weight="weight"
value="value"
my_dict1 = [{ name:'map', weight:9, value:150 }, { name:'compass', weight:13, value:35 }, { name:'water', weight:153, value:200 }, { name:'sandwich', weight:50, value:160 }, { name:'glucose', weight:15, value:60 }, { name:'tin', weight:68, value:45 }, { name:'banana', weight:27, value:60 }, { name:'apple', weight:39, value:40 }]
my_dict2= [{ name:'map', weight:9, value:150 }, { name:'compass', weight:13, value:35 }, { name:'water', weight:153, value:200 }, { name:'sandwich', weight:50, value:160 }, { name:'glucose', weight:15, value:60 }, { name:'tin', weight:68, value:45 }, { name:'banana', weight:27, value:60 }, { name:'apple', weight:39, value:40 }]
my_dict3= [{ name:'cheese', weight:23, value:30 }, { name:'beer', weight:52, value:10 }, { name:'suntan cream', weight:11, value:70 }, { name:'camera', weight:32, value:30 }, { name:'T-shirt', weight:24, value:15 }, { name:'trousers', weight:48, value:10 }, { name:'umbrella', weight:73, value:40 }]
my_dict4 = [{ name:'cheese', weight:23, value:30 }, { name:'beer', weight:52, value:10 }, { name:'suntan cream', weight:11, value:70 }, { name:'camera', weight:32, value:30 }, { name:'T-shirt', weight:24, value:15 }, { name:'trousers', weight:48, value:10 }, { name:'umbrella', weight:73, value:40 }]
my_dict5 = [{ name:'waterproof trousers', weight:42, value:70 }, { name:'waterproof overclothes', weight:43, value:75 }, { name:'note-case', weight:22, value:80 }, { name:'sunglasses', weight:7, value:20 }, { name:'towel', weight:18, value:12 }, { name:'socks', weight:4, value:50 }, { name:'book', weight:30, value:10 }]
my_dict6 = [{ name:'waterproof trousers', weight:42, value:70 }, { name:'waterproof overclothes', weight:43, value:75 }, { name:'note-case', weight:22, value:80 }, { name:'sunglasses', weight:7, value:20 }, { name:'towel', weight:18, value:12 }, { name:'socks', weight:4, value:50 }, { name:'book', weight:30, value:10 }]

my_list = [my_dict1,my_dict2,my_dict3,my_dict4,my_dict5,my_dict6]

max_weight = [100,200, 100,200,100,200]

for i in range(len(max_weight)):
    w=[]
    v=[]
    m=max_weight[i]
    for i in my_list[i]:
        w+=[i["weight"]]
        v+=[i["value"]]
    print(knapsack_recursion(m,w,v,len(w)))