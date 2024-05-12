わからなかったためもう一度復習
class Solution {
  public static String sheeps(int count) {
    return sheepsHelper(count, "");
  }

  public static String sheepsHelper(int count, String string) {
    if (count <= 0)
      return string;
    return sheepsHelper(count - 1, String.valueOf(count) + " sheep ~ " + string);
  }
}
