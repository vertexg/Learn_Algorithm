# Listとは
データを箱に並べて、中に入っている値には番号（インデックス）が割り当てられている。たとえば、動物のリストがあるとき、
インデックスを使用してリストから特定の名前を取得したり、追加、削除したりすることができる。

## 例
```python
str = "Hello World!";

for i in range(0, len(str)):
    print(str[i])

```
配列は、連続した形でメモリに保存され、その位置はデータサイズとインデックスに基づく簡単な数式で計算できるため、配列内を高速にアクセスすることができる。

## 配列の注意点

1. 配列は固定されており、配列に格納されたデータは置き換えることはできるが、宣言された項目は削除できない
2. 配列のサイズ以上に要素を追加する場合、大きなサイズである新しい配列を追加し、新しい配列にコピーする必要があるため、O（n）の時間がかかる
3. 配列は連続したメモリ構造を持っているため、配列の値の取得にはO（1）の時間がかかる。ベースアドレス +（インデックス × データサイズ）の式を使うことで、インデックスはメモリから直接値を取得することができる。このように、要素に同じ時間でアクセスできることを、ランダムアクセス、またはダイレクトアクセスと呼ぶ。
4. 配列内では、一種類のデータ型のみをしようすることができる。コンパイラがデータをメモリに格納するためには、同じサイズのデータである必要があるため。


