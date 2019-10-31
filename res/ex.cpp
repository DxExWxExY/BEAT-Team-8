#include <stdlib.h>
#include <iostream>


int multiply(int x, int y){


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
   int x=0;
   int y=0;
   char s[100]="Hello world!\n";
   printf("%s", s);

//   printf("insert number to multiply\n");
   printf("insert number to print\n");
   std::cin >> x;
//   int value = multiply(x,y);
   printNum(x);
//   printf("Result is: %d\n",value);

   return 0;
}
