def hello():
   print("Hello from inside a file!") 

def pack(a,b,c):
    return ["red","blue","green"]

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("My lunchbox is empty!")
    else: 
        for i in range(len(my_list)):
            if i == 0:
                print(f"first I eat {my_list[0]}")
            else:
                print(f"Next I eat {my_list[i]}")

hello()
print(pack(1,2,3))
eat_lunch(["salad","sandwich","cola","fruit"])
eat_lunch([])