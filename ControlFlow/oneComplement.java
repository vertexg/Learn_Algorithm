class Solution {
  public static String oneComplement(String bits) {
    String output = "";
    for (int i = 0; i < bits.length(); i++) {
      output += bits.charAt(i) == '0' ? "1" : "0";
    }
    return output;
  }
}
