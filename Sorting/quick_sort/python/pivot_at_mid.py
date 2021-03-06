from typing import MutableSequence


def quicksort_middle_pivot(arr: MutableSequence, left: int, right: int) -> None:
    pl = left
    pr = right
    pivot = arr[(pl + pr) // 2]
    while pl <= pr:
        while arr[pl] < pivot:
            pl += 1
        while arr[pr] > pivot:
            pr -= 1
        if pl <= pr:
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1
            
     
    # pl이 pr과 같거나 pr을 역전해야 끝나므로, pr이 왼쪽 부분의 끝, pl이 오른쪽 부분의 시작이 된다.
    if left < pr:
        quicksort_middle_pivot(arr, left, pr)
    if pl < right:
        quicksort_middle_pivot(arr, pl, right)

if __name__ == "__main__":
    a = [5, 8, 4, 2, 6, 1, 3, 9, 7]
    quicksort_middle_pivot(a, 0, len(a) - 1)
