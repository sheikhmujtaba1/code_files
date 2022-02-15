
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    arr = [3,4,6,1]
    bubble_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
