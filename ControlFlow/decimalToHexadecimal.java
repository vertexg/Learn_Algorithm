class Solution{
    public static String decimalToHexadecimal(int decNumber){
      
    int currentBinary = 0;
    String hexadecimal = "0123456789ABCDEF";
    String str = "";

    while (decNumber >= 0) {
      currentBinary = decNumber % 16;
      str = hexadecimal.charAt(currentBinary) + str; 
      decNumber = decNumber /= 16;
      if (decNumber == 0)
        break;

    }
    return str;
  }
    
}

