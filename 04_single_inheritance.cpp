#include <iostream>
#include <string>
using namespace std;

class Animal {
public:
    string name;
    void eat() {
        cout << name << " can eat" << endl;
    }
};

class Cat : public Animal {
public:
    Cat(string name) {
        this->name = name;
    }
};

int main() {
    Cat obj("Cat");
    obj.eat();

    return 0;
}
