#include <stdio.h>

/************
Dynamically declaring variables in C with the token paste operator: ##
************/

#define VAR(name, num) name##num

int main() {
  for (int i = 0; i < 100; i++) {
      int VAR(x, i) = i * 2;
      printf("%d\t", VAR(x, i));
  }
  
  return 0;
}
