class Solution {
  public static boolean isPalindromeInteger(int n) {
    String s = String.valueOf(n);
    int l = s.length();
    int midle = (int) Math.floor(l / 2);

    for (int i = 0; i < midle; i++) {
      if (s.charAt(i) != s.charAt(l - 1 - i)) {
        return false;
      }
    }

    return true;
  }
}
