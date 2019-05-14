def fixdown(a,k,n):
    """
    不断调整序列，使得序列成为大根堆
    """
    N=n-1
    while 2*k<=N:
        j=2*k#j是k节点的子节点
        if j<N and a[j]<a[j+1]:#j不是最后一个节点,则两个子节点比较大小,a[j]是最大的子节点
            j+=1
        if a[k]<a[j]:#比较较大子节点a[j]和父节点的值
            a[k],a[j]=a[j],a[k]#交换
            k=j#交换后，开始继续往下检查子节点大小
        else:
            break
def heapsort(l):
    """
    堆排序python实现
    """
    n=len(l)-1
    for i in range(n//2,0,-1):#i的范围为5,4,3,2,1没有0
        fixdown(l,i,len(l))#执行到这里后，最大值77已经最后了
    while n>1:
        l[1],l[n]=l[n],l[1]#把序列尾部的元素放到堆顶位置，
        fixdown(l,1,n)#将序列从新排列成大根堆
        n=n-1#不断将堆订元素取出
    return l[1:]#返回排序后的序列


if __name__=="__main__":  
    l=[-1,26,5,77,1,61,11,59,15,48,19]#第一个元素不用，占位  
    print (l)
    res=heapsort(l)
    print( res )