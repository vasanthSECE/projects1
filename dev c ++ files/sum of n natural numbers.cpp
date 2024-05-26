#include <iostream>
using namespace std;
int main() {
    int n;
    
    
    cout << "Enter the value of n: ";
    cin >> n;

  
    int sum = 0;
    for (int i = 1; i <= n; ++i) {
        sum += i;
    }

   
    std::cout << "The sum of the first " << n << " natural numbers is: " << sum << std::endl;

    return 0;
}

