// Just a code snippet to test out how memory addresses behave

#include <stdio.h>

void test(int k);

int main() {
    int i = 0;
    int b = 130383727203;
    
    printf("The address of i is %x\n", &i);
    printf("The address of b is %x\n", &b);
    test(i);
    printf("The address of i is %x\n", &i);
    test(b);
    
    printf("\n\n==========\nConclusion: variables i and b have each their own address and so does the local variable k of the test() function. The address of the local variable k is independent of the other 2 variables. It doesn't change whether you put i or b as the argument of the test() function; k had the same memory address in both cases, showing that k is independent of these variables and k has its own place in memory.\n==========");

    return 0;
}

void test(int k) {
    static int num_calls = 0;
    ++num_calls;
    printf("The %dth address of k is %x\n", num_calls, &k);
} 
