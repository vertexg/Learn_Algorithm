def numberOfDots(x):
    if x <= 1:
        return 1
      
    return numberOfDots(x - 1) + x


``` java
class Solution{
    public static int numberOfDots(int x){
        if (x <= 0) return 0;
       return x + numberOfDots(x-1);
        
    }
}
```
