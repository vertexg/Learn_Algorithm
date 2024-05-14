class Solution {
  public static int howLongToReachFundGoal(int capitalMoney, int goalMoney, int interest) {
    return howLongToReachFundGoalHelper(capitalMoney, goalMoney, interest, 0);
    // 関数を完成させてください
  }

  public static int howLongToReachFundGoalHelper(double capitalMoney, double goalMoney, double interest, int year) {
    if (capitalMoney >= goalMoney)
      return year;
    if (year >= 80)
      return 80;

    capitalMoney *= (1 + interest / 100);
    if (year % 2 == 0)
      goalMoney *= 1.02;
    else
      goalMoney *= 1.03;

    return howLongToReachFundGoalHelper(capitalMoney, goalMoney, interest, year + 1);
  }
}
