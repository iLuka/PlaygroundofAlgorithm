class InsertionSort:


    def __init__(self, target:list):

        self.sort(target)

    def sort(self, target):

        ##insertion sort core: compare and swap util last one
        for j in range(1,len(target)):

            #key value storage
            key = target[j]

            i=j-1;

            while i>=0 and target[i]>key:
                target[i+1]=target[i]
                i=i-1

            target[i+1]=key

        print(target)

target = [5,2,3,6,4,1]

insertionSort = InsertionSort(target)
