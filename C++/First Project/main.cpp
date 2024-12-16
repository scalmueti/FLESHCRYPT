#include <iostream>

int main() {
    using namespace std;

    cout << "Hello world!" << endl;
    cout << "What is your name?" << endl;
    string userName;
    cin >> userName;
    cout << "Hello " << userName;
    for (int a=2;a<=10;a+=3) {
        cout << a << endl;
    }
    cout << "Break" << endl;
    for(int i=2;i<=10;i+=3) {
        cout << i << endl;
    }
    return 0;
    
}