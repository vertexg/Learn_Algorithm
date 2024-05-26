class Main {
  public static String decimalToBinary(int decNumber) {
    String str = "";
    int currentBinary = 0;

    while (decNumber >= 0) {
      currentBinary = decNumber % 2;
      str = currentBinary + str; // 計算した2進数の桁を文字列の先頭に追加
      
      decNumber /= 2;
      if (decNumber == 0)
        break;

    }
    return str;
  }

}
