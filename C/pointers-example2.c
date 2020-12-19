#include <stdio.h>

/* Heavily modified from the code that was initially written by "Ajinkya Jadhav" (account on SoloLearn), to expand it and learn more about pointers. */

int main() {
    int x = 5;
    int y;
    int *p = NULL;
    p = &x;
    
   printf("x is initially: %d, and address of x is: %x\nThe address of y is: %x\n\n", x, p, &y); 
    
    y = *p + 2; /* y is assigned 7 */
    y += *p;     /* y is assigned 12 */
    *p = y;       /* x is assigned 12 */
    (*p)++;      /* x is incremented to 13 */

    printf("p is pointing to the value %d\n", *p);
    printf("value of x is now: %d\n", x); 
    printf("address of x is still %x\n",p);
    p++;    /* incrementing p */
    printf("when we increment p, address of x is still %x\n",&x);
    printf("and p holds now the following address: %x (which is 4 more than &x)\n", p);
    printf("p now points to the following integer value: %d, and the following floating point value: %f\n", *p, *p);
    x = 3;  /* setting a new value for x */
    printf("new value of x = %d, and &x = %x\n", x, &x);
    printf("p still points to the following integer value: %d, and the following floating point value: %f\n", *p, *p);
    p--;    /* decrementing p */
    printf("p now holds the address of x again %x\n", p);
    printf("p now points to the new value of x: %d\n", *p);
    
    printf("\nInteresting finds!\n");
}
