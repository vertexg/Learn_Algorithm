class Solution{
    public static boolean isPrime(int number){
        for(int i = 2; i < number; i++ ){
            if(number % i == 0)
            return False;
        }
        return number > 1;
    }
}

