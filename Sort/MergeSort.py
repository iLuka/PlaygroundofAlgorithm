class MergeSort:

    def __init__(self, target:list):
        self.result = self.sort(target)

    #idea of merge sort is "divide and conquor"
    #first, divide
    #second, conquor which is sort here
    #divide the element to pairs of two and reversely merge
    def sort(self, target:list):
        if len(target)<=1:
            return target

        #find the mid of list
        mid = int(len(target)/2)

        #divide to left and right
        left = target[:mid]
        right = target[mid:]

        #continue divide and MergeSort
        left = self.sort(left)
        right = self.sort(right)

        #
        result = self.merge(left,right)

        return result

    #merge with left and right
    def merge(self, left, right):
        #an extra space is needed to store the result of conquor
        res = list()

        i = 0
        j = 0

        while(i<len(left) and j<len(right)):
            if(left[i]<right[j]):
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1

        if(i<len(left)):res+=left[i:]

        if(j<len(right)):res+=right[j:]


        return res

target = [5,1,3,2,6,8,7,0]
ms = MergeSort(target)
print(ms.result)
print(ms.sort(target))
