#include<iostream>
#include<cmath>

using namespace std;

int countDigits(int number) {
    int count = 0;
    while (number > 0) {
    number /= 10;
    count++;
    }
    return count;
} 

int  isArmstrong(int number) {
    int originalNumber = number;
    int sum = 0;
    int power = countDigits(number);

    while (number > 0) {
    int digit = number % 10;
    sum += pow(digit, power);
    number /= 10;
    }

    return (sum == originalNumber);
}

int main() {
    int num;

    cout << "Enter a number: ";
    cin >> num;

    if (isArmstrong(num)) {
    cout << num << " is an Armstrong number." << endl;
    } else {
    cout << num << " is not an Armstrong number." << endl;
    }

    return 0;
}

