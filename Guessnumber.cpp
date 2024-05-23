#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
 
    std::srand(std::time(0));
    
    
    int randomNumber = std::rand() % 100 + 1;
    int guess = 0;

    std::cout << "Guess the number (between 1 and 100):" << std::endl;

    
    while (true) {
        std::cout << "Enter your guess: ";
        std::cin >> guess;

        if (guess < randomNumber) {
            std::cout << "Too low! Try again." << std::endl;
        } else if (guess > randomNumber) {
            std::cout << "Too high! Try again." << std::endl;
        } else {
            std::cout << "Congratulations! You guessed the correct number: " << randomNumber << std::endl;
            break;
        }
    }

    return 0;
}
