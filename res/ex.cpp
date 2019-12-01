#include <stdlib.h>
#include <iostream>


int multiply(int x, int y,int ){


  int result=0;
  printf("multiplying numbers!");
  result =x*y;

  return result;
}

void printNum(int x){

  printf("Your number is: %d",x);

}


int main(void)
{
   // printf() displays the string inside quotation
   int x=3;
   int y=2;
   char s[100]="Hello world!\n";
   printf("%s", s);

//   printf("insert number to multiply\n");
   printf("insert number to print\n");
//   std::cin >> x;
   int value = multiply(x,y,9);
   printNum(x);
//   printf("Result is: %d\n",value);

   return 0;
}
