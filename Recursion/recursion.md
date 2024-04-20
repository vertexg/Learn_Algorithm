# 再帰（recursion）とは
関数が処理の中で自分自身を呼び出すことを指す

## ベースケース（base case）とは

1. 再帰呼び出しを行わずに関数の戻り値を直接返す
2. 再帰の終了条件を明確に定義する

ベースケースは関数内で再帰呼び出しを行わずに処理を完了できる最も単純なケースを指し、
ベースケースを定義することで、再帰呼び出しを無限に続くことを防ぎ、関数が終了を保証することを指す

``` python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # 55
```
## 総和

「1 から 5 までの総和」 = 「1 から 4 までの総和」 + 5と表現できる
``` python
# 1 から n までの総和を計算する関数s
def summation(n):
    if n <= 0:
        return 0
    return summation(n-1) + n

# 1 から 5 までの総和を計算
print(summation(5))
```
## 階乗
「1 から 5 までの整数の掛け算」 = 「1 から 4 までの整数の掛け算」 × 5　と表現できる
```python
# 1 から n までの整数の積を計算する関数
def factorial(n):
    if n <= 0:
        return 1
    return factorial(n-1) * n

```
