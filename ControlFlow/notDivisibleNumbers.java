class Solution {
  public static String notDivisibleNumbers(int x, int y) {
    String output = "";
    for (int i = 0; i > x; i++) {
      if (x % y != 0)
        output += i + "-";
    }
    return output.substring(0, output.length() - 1);
  }
}
