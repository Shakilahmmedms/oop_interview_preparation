#include<bits/stdc++.h>

using namespace std;

class Car{
    public:
        int price;

    void showDetail(){
        cout<< "This is a method" <<endl;
    }


};

int main(){
    Car car1;
    car1.showDetail();
    return 0;
}