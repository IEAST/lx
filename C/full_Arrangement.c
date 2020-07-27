int num[];
void main()
{
    int a,b;
    scanf("%d", &a);
    
    for(int i=1;i<=a;i++){
        num[i-1]=i;
    }
    for(int i=1;i<=a;i++){
        printf("%d ",num[i-1]);
    }
}