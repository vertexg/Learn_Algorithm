# 制御フロー
ステートメントや関数、式がどのような順序で評価されるかには一定のルールがあり、これらは制御フローと呼ばれる。

## 例
``` python
age = 20
if age < 20:
    print("あなたは未成年です")
elif age >= 20 and age < 65:
    print("あなたは成人です")
else:
    print("あなたは高齢者です")

```

if文の他に三項演算子でも書ける
## 条件付き三項演算子

公式
``` javascript
op1 ? op2 : op3
```

``` javascript

const age = 20;
const result = age >= 20 ? "成人です" : "未成年です";
console.log(result); // "成人です"
```
# for文
公式
``` python
for(初期化; 条件; ループの最後に評価される式){
   ステートメント
}
```
また、for文にはfor文の中にfor文を持つことができる
```python
for(let i = 1; i <= 2; i++) {
   for (let j = 1; j <= 3; j++) {
        console.log(i,j);
   }
}

// 1 1
// 1 2
// 1 3
// 2 1
// 2 2
....
```


# while文
for文の他にwhile文を使い反復することができる

```python
    while(i){
        処理
    }
```
# break continue
制御フローで breakが処理されると、反復ループから抜け出すことができ、continueを実行するとループは次のループに進む
``` python
def findLetter(s, letter):
    found = False

    for i in range(0, len(s)):
        if(s[i] == letter[0]):
            found = True
            break

    return True if found else False

print(findLetter("It is a sunny day.", "a"))
print(findLetter("It is a sunny day.", "z"))


```








