class InsertionSort:


    def __init__(self, target:list):

        self.sort(target)

    def sort(self, target):

        #insertion sort: start with i and j
        #

        for j in range(1,len(target)):

            #record value for later swap
            key = target[j]

            #compare the elements before list[j] with key/target[j]
            i=j-1;

            #if target[i]>key them swap with target[i+1], which is target[j]
            #use i+1 is because use for later swap when iterating backwards
            #swap i with i+1 if target[i] greater than key
            #util index reaches the head or value is not greater than key
            while i>=0 and target[i]>key:

                target[i+1]=target[i]
                #index moves towards head
                i=i-1
            #the element greator than key has been swaped, the key should be moved to the place where i ends.
            #if  nothing happends, this keeps the element unchanged
            target[i+1]=key

        print(target)

target = [5,2,3,6,4,1]

insertionSort = InsertionSort(target)
