#include<bits/stdc++.h>

using namespace std;

class A{
    int value; // private here

    public:
        string name;
        A(string name){
            this->name = name;

        }
};

int main(){

    A obj("shakil");
    obj.value = 10;
    cout<<obj.value<<" "<<obj.name<<endl; 

    return 0;
}