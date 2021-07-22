### 300 points

### you get a source.c file so let's check it :

[*] most important lines of code :

`int account_balance = 1100; `

main options :

```
        printf("\n1. Check Account Balance\n");
        printf("\n2. Buy Flags\n");
        printf("\n3. Exit\n");

```

option 2 has another choices inside it :
```
else if(menu == 2){
            printf("Currently for sale\n");
            printf("1. Defintely not the flag Flag\n");
            printf("2. 1337 Flag\n");


```
we can see that we can read the flag if we take choice 2 
but there is a problem :

"1337 flags cost 100000 dollars" , and we got only 1100 in balance 

so our goal is to figure out a way increases our balance then try buy "1337 flag" .

let's check this block :

```
if(auction_choice == 1){
                printf("These knockoff Flags cost 900 each, enter desired quantity\n");
                int number_flags = 0;
                fflush(stdin);
                scanf("%d", &number_flags);
                if(number_flags > 0){
                    int total_cost = 0;
                    total_cost = 900*number_flags;
                    printf("\nThe final cost is: %d\n", total_cost);
                    if(total_cost <= account_balance){
                        account_balance = account_balance - total_cost;
                        printf("\nYour current balance after transaction: %d\n\n", account_balance);
                    }
```
as we can see our balance can be modified at this block , we msut inter +ve number of flags and it will be multiplied by 900 and

"if total cost <= balance" this will be subtract from  our balance .
## intger overflow :
integer range is -2147483647 : +2147483648 

But what if we increase max+1  ? 

it will wrap around and = -2147483647 .

we can use this at our situation !

exploit 
=======
we will enter number of flags = (2147483648/900)+n ;where n >=1  , so this number will wrap around and be in the -ve side 

this will satisfy conditions
[*]no.flags >0 

[*]total cost <=  balance ; hence it will be -ve 

[*] account_balance = account_balance - total_cost ;will get executed and will make our balance large 

compile the source.c file by

`gcc source.c` 

you can create your dummy flag under the name of flag.txt to check the process .

![1-2](https://user-images.githubusercontent.com/67979878/126600967-b5239347-7546-4ffc-b94b-de0863de7ef1.PNG)

now we can read the flag !

![2-2](https://user-images.githubusercontent.com/67979878/126601072-21453a5e-1f3f-4d5e-93a4-1f984f41a412.PNG)



