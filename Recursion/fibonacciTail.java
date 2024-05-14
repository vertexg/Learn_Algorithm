class Main{
　　　　　　　　　//再帰
    public static int fibonacci(int n){
        if (n == 0) return 0;
        if (n == 1) return 1;
        return fibonacci(n-1) + fibonacci(n-2);
    }

    // 末尾再帰
    public static int fibonacciTail(int n){
        return fibonacciTailHelper(0,1,n);
    }

    public static int fibonacciTailHelper(int f1, int f2, int n) {
        if (n == 0) return f1;
        return fibonacciTailHelper(f2,f1+f2,n-1);
    }
