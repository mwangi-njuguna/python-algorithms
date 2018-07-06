
# coding: utf-8

# In[29]:


def insertion_sort(sequence):
#     use try except to ensure the sequence is iterable
    try:
        for i in range(1, len(sequence)):
            j = i
            while j>0 and sequence[j-1]>sequence[j]:
                sequence[j-1], sequence[j]=sequence[j],sequence[j-1]
                j-=1
        return sequence
    
    except TypeError as err:
        print("The sequence is not iterable")

def test_insertion_sort():
    my_seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]
    assert(insertion_sort(my_seq)==sorted(my_seq))
    print("Tests passed")
    
if __name__=='__main__':
    test_insertion_sort()

