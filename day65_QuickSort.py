# Enter your code here. Read input from STDIN. Print output to STDOUT


def QuickSort(p, arr):
    
    if len(arr) == 1:
        return arr
    
    left = list(filter(lambda x: x < p, arr))
    middle = list(filter(lambda x: x == p, arr))
    right = list(filter(lambda x: x > p, arr))
    
    if left :
        left = QuickSort(left[0], left)
        
    if right:
        right = QuickSort(right[0], right)
    
    print(*left, *middle, *right)
    return left + middle + right
    

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = QuickSort(arr[0], arr)
    
    
if __name__ == '__main__':
    main()

