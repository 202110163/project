int fibIter(int n)
{
    if(n < 2) return n;
    else {
        int i, tmp, current=1, last=0;
        for(i=2;i<=n;i++){
            tmp = current;
            current += last;
            last = tmp;
        }
        return current;
    }
}