import java.io.*;
import java.util.*;


//Abstract class that Calculator will implement.
interface AdvancedArithmetic {
  int divisorSum(int n);
}

//Write your code here
class Calculator implements AdvancedArithmetic {
  //Fill in method for Calculator
  public int divisorSum(int n) {
    int sum = 0;
    for(int i = 1; i <= n; i++) {
      //if it is a divisor then we add it to the sum
      if (n%i == 0) {
        sum = sum + i;
      }
    }
    return sum;
  }   
}