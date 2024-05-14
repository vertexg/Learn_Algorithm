class Solution{
    public static int recursiveDigitsAdded(long digits){
        long current = splitAndAdd(digits);

        if (current < 10)
            return (int) current;

        return (int) current + recursiveDigitsAdded(current);
        // 関数を完成させてください
    }
    public static long splitAndAdd(long digits) {

    if (digits < 10)
      return digits;
    return (digits % 10) + splitAndAdd(digits / 10);

  }
}

