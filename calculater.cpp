#include<iostream>
using namespace std;
int main(){
    int n1,n2;
    char sign;
    cin>>n1>>sign>>n2;
    switch (sign)
    {
        case '+':
            cout<<n1+n2;
            break;

        case '-':
            cout<<n1-n2;
            break;

        case '/':
            
            cout<<n1/n2;
            break;

        case '*':
            cout<<n1*n2;
            break;


        default:
            cout<<"nothing";
            break;
    }

    

    return 0;
}
