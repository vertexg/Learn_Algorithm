class Solution{
    public static int totalSquareArea(int x){
        if (x <= 0) return 0;
        return (int)Math.pow(x,3) + totalSquareArea(x -1);
    }
}

