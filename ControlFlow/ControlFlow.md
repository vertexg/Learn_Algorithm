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
## 条件付き三項演算子
公式
``` python
op1 ? op2 : op3
```

``` javascript

const age = 20;
const result = age >= 20 ? "成人です" : "未成年です";
console.log(result); // "成人です"
```
