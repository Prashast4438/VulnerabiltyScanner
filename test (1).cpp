#include <iostream>
#include <cstring>
#include <fstream>
#include <cstdlib>

using namespace std;

int main() {
    // Buffer overflow vulnerability
    char buffer[10];
    cin >> buffer; // Unchecked input vulnerability
    strcpy(buffer, "test"); // Vulnerability

    // Hardcoded credential
    string password = "1234"; // Hardcoded password vulnerability
    cout << "Password: " << password << endl;

    // Use of unsafe string functions
    char source[20], destination[20];
    strcpy(source, "Vulnerable Code");
    strcat(destination, source); // Buffer overflow vulnerability

    // Use of gets (deprecated and unsafe)
    gets(buffer); // Unsafe function usage

    // Command injection vulnerability
    string command;
    cin >> command; // Unchecked input
    system(command.c_str()); // Command injection vulnerability

    // File handling without validation
    ifstream file("config.txt");
    if (!file) {
        cerr << "Error opening file" << endl;
    }

    // Integer overflow/underflow
    int largeNumber = 2147483647; // Max value for 32-bit int
    int result = largeNumber + 1; // Overflow vulnerability
    cout << "Result: " << result << endl;

    // Use of deprecated malloc without checking return value
    int *arr = (int *)malloc(100 * sizeof(int));
    if (arr == nullptr) {
        cerr << "Memory allocation failed" << endl;
    }

    // Null pointer dereference
    int *ptr = nullptr;
    *ptr = 42; // Null pointer dereference vulnerability

    // Insecure random number generation
    int insecureRandom = rand(); // Insecure RNG

    // Potential use-after-free
    int *freePtr = (int *)malloc(sizeof(int));
    free(freePtr); // Free memory
    *freePtr = 42; // Use-after-free vulnerability

    // Unchecked dynamic memory allocation
    char *dynamicBuffer = new char[100];
    // No check for successful allocation
    delete[] dynamicBuffer;

    return 0;
}

