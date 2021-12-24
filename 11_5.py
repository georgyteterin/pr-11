list1=[]
list2=[]
out=[]
i=j=0

def finding_out(list1, list2, out, i, j):
    while i<len(list1) and j<len(list2):
        if list1[i]<list2[j]:
            out.append(list1[i])
            i+=1
        else:
            out.append(list2[j])
            j+=1

    while i<len(list1):
        out.append(list1[i])
        i+=1

    while j<len(list2):
        out.append(list2[j])
        j+=1

    return(out)