class Solution{
    public static int divideBy3Count(int n){
        return divideBy3CountHelper(n, 0);
    }
    public static int divideBy3CountHelper(int n, int count ){
        if (n/3 < 1) return count;
        else return divideBy3CountHelper(n/3, count+1);

    } 
        // 関数を完成させてください
    }


