
# coding: utf-8

# In[20]:


def selection_sort(sequence):
    try:
        for i in range(len(sequence)-1, 0, -1):
            max_index = i
            for j in range(max_index):
                if sequence[j]>sequence[max_index]:
                    max_index = j
            sequence[i], sequence[max_index] = sequence[max_index], sequence[i]
        return sequence

    except TypeError:
        print("Sequence not iterable")

def test_selection_sort():
    my_seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]
    assert(selection_sort(my_seq)==sorted(my_seq))
    print("Algorithm ok")
    
if __name__=='__main__':
    test_selection_sort()

