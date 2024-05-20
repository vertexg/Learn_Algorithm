class Solution {
  public static String fizzBuzz(int n) {
    String str = "";
    for (int i = 1; i <= n; i++) {
      if (i % 15 == 0)
        str += "-FizzBuzz";
      else if (i % 5 == 0)
        str += "-Buzz";
      else if (i % 3 == 0)
        str += "-Fizz";
      else
        str += "-" + i;
    }
    return str.substring(1);
  }
}

