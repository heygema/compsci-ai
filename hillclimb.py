def calc_cost(arr, n):
    c = 0
    for i in range(n):
        for j in range(n):
            if arr[j] < arr[i]:
                c+=1
    return c

def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]

def main():
    print("hill climbing method")
    N = int(input("masukan panjang array> "))
    arr = []
    swaps = 0 
    for i in range(0,N):
        arr.append(int(input("input ke array > ")))
    best_cost = calc_cost(arr, N)
    while(best_cost > 0):
        for i in range(N):
            print(arr)
            print("lagi di index {}".format(i))
            print("swapping array...")
            swap(arr, i, (-N)+i)
            swaps +=1
            new_cost = calc_cost(arr, N)
            if best_cost > new_cost:
                print("after swaps terjadi {}".format(swaps))
                best_cost = new_cost
            else:
                swap(arr, i, (-N)+i)
    
    print("final aswer to this\n-----------------\n")
    for i in arr:
        print(i)

if __name__ == "__main__":
    main()
