#include <stdio.h>

/*
An example of pointers in C.

If someone is watching this code:
Run the program first and see the output alongside the source code. it will make it easier for you to understand it.

This program is just me trying some things out to understand pointers a little. I do not know much about them, that's why I try a bunch of things and see what the output will be.
*/

int main() {
    
    /* First trying out some basic pointers syntax and definitions. */
    
    char c = 'Z';
    char *ptr = NULL;
    char **ptrr = NULL;
    ptr = &c;
    ptrr = &ptr;
    
    printf("- The address of variable c is: %x\n", &c);
    printf("- ptr stores the address of variable c: %x\n", ptr);
    printf("- c has the value: %c\n", c);
    printf("- Dereferencing ptr to see that it points to the value of c: %c\n", *ptr);
    printf("- The address of ptr is: %x\n", &ptr);
    printf("- ptrr stores the address of ptr: %x\n", ptrr);
    printf("- ptrr points to ptr, which in turn points to the value of c. So dereferencing ptrr should also give us the value of c: %c\n", **ptrr);
    printf("- I don't know what will happen here: %x\n", *ptrr);
    printf("Apparently dereferincing ptrr only once gives the value of ptr, which is the memory location of the variable c.\n");
    
    printf("\n");
    
    /* Trying arhitmetic with pointers and addresses. */
    
    int x = 45;
    int y = 20;
    int *p = NULL;
    p = &x;
    
    printf("x = %d; y = %d\n&x = %x\n", x, y, &x);
    printf("- Dereferending p to see that it points to the value of x: %d\n", *p);
    printf("- Adding dereferenced p to y: %d\n", y + *p);
    printf("- Trying to see if we can dereference the address of x to yield its value and add it to y: %d\n", y + *&x);
    
    *p = 34;
    printf("Changing the value of *p will change the value of x as well: x = %d\n&x = %x and p = %x\n", x, &x, p);
    
    printf("\nInteresting results!\n");
    
    return 0;
}
