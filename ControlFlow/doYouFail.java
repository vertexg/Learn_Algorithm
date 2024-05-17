class Solution {

  public static String doYouFail(String string) {
    int count = 0;
    for (int i = 0; i < string.length(); i++) {
      if (string.charAt(i) == 'A')
        count += 1;
      if (count >= 3) {
        return "fail";
      }
    }
    return "pass";
    // 関数を完成させてください
  }
}


class Solution {

  public static String doYouFail(String string) {
    int count = 0;
    for (int i = 0; i < string.length(); i++) {
      if (string.charAt(i) == 'A')
      count += 1;

    }
    if (count >= 3) {
      return "fail";
    } else {
      return "pass";
    }

    // 関数を完成させてください
  }
}
早期終了の欠如: 'A' が3つ以上出てきた時点でループを終了するロジックがないため出力に問題があった。
