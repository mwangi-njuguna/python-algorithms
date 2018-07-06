
# coding: utf-8

# In[9]:


def quick_sort(sequence):
    #Use median as pivot
    try:
        if len(sequence)<2: return sequence
        mid = len(sequence)//2
        #partition index = pi
        pi = sequence[mid] #value partitioning index of the sequence
        sequence = sequence[:mid] + sequence[mid+1:]
        lower_elements =  [element for element in sequence if element<=pi]
        higher_elements = [element for element in sequence if element>pi]

        return quick_sort(lower_elements) + [pi] + quick_sort(higher_elements)
        
    except TypeError:
        print("Sequence not iterable")
        
def test_quick_sort():
    
    my_seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]
    assert(quick_sort(my_seq)==sorted(my_seq))
    print("Gotcha!")
    
if __name__=='__main__':
    test_quick_sort()
        

