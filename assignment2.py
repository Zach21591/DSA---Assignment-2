import winsound
import time

def playSound():
    winsound.Beep(1000, 500)

def displayArray(array):
    print(", ".join(map(str, array)))

def merge(array):
    if len(array) <= 1:
        return array
    
    middleElement = len(array) // 2
    rightSide = array[middleElement:]
    leftSide = array[:middleElement]

    print("Split:", array)

    rightSide = merge(rightSide)
    leftSide = merge(leftSide)

    return sortWithSound(leftSide, rightSide)

def sortWithSound(left, right):
    mergedList = []
    rightIndex = 0
    leftIndex = 0

    while rightIndex < len(right) and leftIndex < len(left):
        if right[rightIndex] > left[leftIndex]:
            mergedList.append(left[leftIndex])
            leftIndex = leftIndex + 1
        else:
            mergedList.append(right[rightIndex])
            rightIndex = rightIndex + 1

        displayArray(mergedList)

        playSound()
        time.sleep(0.5)

    mergedList.extend(right[rightIndex:])
    mergedList.extend(left[leftIndex:])

    print("Merge:", mergedList)
    
    return mergedList

def main():
    arrayLength = int(input("Please enter the length of the array: "))

    array = []
    print("Please enter all the elements that will be in the oringal array (input a number, then press enter, input another number, enter, repeat):")
    for i in range(arrayLength):
        array.append(int(input()))

    print("\nThe Original Array:")
    displayArray(array)

    print("\nImplementing the Merge Sort Algorithm:")
    sortedArray = merge(array)
    print("\nThe Sorted Array:")
    displayArray(sortedArray)
    print("\nSorting Complete!")

main()