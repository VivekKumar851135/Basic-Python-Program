#include<stdio.h>
/*int b;
int my_function(int a){
if(a==0){
    return b;
}else{
    b=b+(a%10);
    a=a/10;
   return my_function(a);
}
}

int main(){
    int a,c;
    printf("Enter a number\n");
    scanf("%d",&a);
   c=my_function(a);
   printf("%d\n",c);
}*/

int main(){
    int m,n,i,j;
    printf("enter m");
    scanf("%d",&m);
    for(n=1;n<=m;n++,n++){
        for(i=1;i<=3;i++){
            for(j=1;j<=(n-i);j++)
                printf(" ");
            printf("\n");
        }
         for(i=1;i<=3;i++){
            for(j=1;j<=n;j++)
                printf("O");
            printf("\n");
        } 
    }  
    return 0;
}