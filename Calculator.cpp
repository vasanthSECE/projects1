#include <iostream>

int main() {
    char operation;
    double num1, num2, result;

    
    std::cout << "Enter first number: ";
    std::cin >> num1;

    std::cout << "Enter second number: ";
    std::cin >> num2;

   
    std::cout << "Choose an operation (+, -, *, /): ";
    std::cin >> operation;

 
    switch (operation) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if (num2 != 0) {
                result = num1 / num2;
            } else {
                std::cout << "Error! Division by zero." << std::endl;
                return 1;
            }
            break;
        default:
            std::cout << "Invalid operation." << std::endl;
            return 1;
    }

    std::cout << "Result: " << result << std::endl;

    return 0;
}
