#include <iostream>

int main() {

    std::cout << "Hello world!" << std::endl;
    std::cout << "What is your name?" << std::endl;
    std::string userName;
    std::cin >> userName;
    std::cout << "Hello " << userName;
    return 0;
    
}