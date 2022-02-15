
def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        changed = False
        for j in range(arr_len-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                change = True
        if change == False:
            break
    return arr
    

def main():
    arr = [3,4,5,623,8, 17, 20, 44, 50, 60]
    print(bubble_sort(arr))


if __name__ == "__main__":
    main()
