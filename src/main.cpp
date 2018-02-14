/// Application entry point.
///
#include <cstdlib>
#include <iostream>
#include <string>


using namespace std;


/// Execute the application.
///
int main() {
    extern string greeting();  // greeting.cpp
    cout << greeting() << endl;
    return EXIT_SUCCESS;
}
