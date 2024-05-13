class Main {

  public static String divisor(int n) {
    return divisorHelper(n, 1);
  }

  public static String divisorHelper(int n, int i) {
    if (n <= i)
      return String.valueOf(n);
    if (n % i == 0)
      return String.valueOf(i) + '-' + divisorHelper(n, i + 1);
    else
      return divisorHelper(n, i + 1);

  }
