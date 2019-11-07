#include <stdlib.h>
#include <stdio.h>
//#include <iostream>

struct Test {
  int a;
  char b;
  char c;
};

int multiply(int x, int y){

  int result=0;
  printf("multiplying numbers!");
  result =x*y;

  return result;
}

int main(void)
{
   // printf() displays the string inside quotation
   struct Test struct_example = {0,'a','b'};
   int x=0;
   int y=0;
   char s[100]="Hello world!\n";
   printf("%s", s);

   printf("insert numbers to multiply\n");
   //std::cin >> x >> y;
   int value = multiply(x,y);
   printf("Result is: %d\n",value);

   return 0;
}
