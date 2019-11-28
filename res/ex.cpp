#include <stdlib.h>
#include <iostream>


int multiply(int x, int y){


  int result=0;
  printf("multiplying numbers!");
  result =x*y;

  return result;
}

void printing(char charArray[]){

  printf("Your number is: %s\n",charArray);

}


int main(void)
{
   // printf() displays the string inside quotation
   int x=3;
   int y=4  ;
   char s[100]="Hello adrian!\n";
//   printf("%s", s);

//   printf("insert number to multiply\n");
   printf("insert number to print\n");
   std::cin >> x;
   int value = multiply(x,x);
   printing(s);
   printf("Result is: %d\n",value);

   return 0;
}
