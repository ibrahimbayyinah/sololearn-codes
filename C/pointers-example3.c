#include <stdio.h>

void swap (int *num1, int *num2);

int main() {
    int x = 25;
    int y = 100;

    printf("x is %d, y is %d\n&x is %p, &y is %p\n", x, y, (void*)&x, (void*)&y); 
    swap(&x, &y);
    printf("x is %d, y is %d\n&x is %p, &y is %p\n", x, y, (void*)&x, (void*)&y);
    
    printf("\nConclusion: the memory addresses stay the same, the values got swapped.\n");

    return 0;
}
 
void swap (int *num1, int *num2) {
    int temp;
    printf("\n\nWe are in the swap function now.\n&temp = %p.\n", (void*)&temp);
    temp = *num1;
    *num1 = *num2;
    *num2 = temp;
    printf("num1 = %p, &temp = %p, num2 = %p.\n", (void*)num1, (void*)&temp, (void*)num2);
    printf("End of the swap function.\n\n");
}
