学習していたプリミティブ型だが、車、国などをデータとして表すときに限界があり、プリミティブ型以外のものをオブジェクトと呼ばれる。

# クラスとは
クラスは、オブジェクトの設計図やテンプレートとして機能し、オブジェクトが持つべき属性（プロパティ）と操作（メソッド）を定義される。
クラスの属性にはオブジェクトの状態を表し、メソッドはオブジェクトの動作や振る舞いを定義します。
しかし、クラス自体は具体的なデータを持たず、あくまでもオブジェクトを生成するための設計図としての役割を果たす。

# インスタンスとは
インスタンスは、クラスに基づいて生成された具体的なオブジェクトで、クラスが設計図なら、インスタンスは設計図に基づいて実際に作成された実体、つまり「製品」に相当する。
インスタンス化によりクラスから新しいオブジェクトを生成するプロセスを指し、プロセスを通じて、クラスで定義された属性に具体的な値が割り当てられ、メソッドが実際に動作するようになる。
また、インスタンスごとに属性の値は異なることができ、それぞれ独立した状態を持つことができる

# コンストラクタ

メンバ変数オブジェクトが持つデータを「状態」と呼び,オブジェクトの状態は、クラス内で定義されるメンバ変数という変数に保存される。
メンバ変数は、クラス内で定義され、メソッドからアクセスできる変数です。

クラスからインスタンスを生成する際に自動的に実行される特別なメソッドです。メソッドは、インスタンスの初期化を目的としており、インスタンスが持つべき属性の初期値を設定したり、
インスタンス生成時に必要な処理を行うために使用される。

# オブジェクトの振る舞い
振る舞いとは、オブジェクトの状態を読み取り、変更、更新する処理を指す。オブジェクトの振る舞いは、そのクラスのメソッド内で定義され、オブジェクトが行うことができるアクションを「動詞」として記述し、
状態はオブジェクトの属性や状況を「名詞」として表す。

# 文字列とオブジェクト
文字列はプリミティブ型ではなく、オブジェクトとして扱われる。これは、文字列は可変長であり、任意の長さのテキストデータを格納できるため
また、プリミティブ型は、固定サイズであり、通常は数値データを表現するのに適している。

## オブジェクト参照
オブジェクトは含まれるデータによってサイズが変わる.例えば、文字列オブジェクトは、保持している文字の数に応じてサイズが変わるため、文字列が長ければ長いほど格納するために必要なメモリの量も増える
このような可変長のデータは、サイズを予測することが難しいためモリの中で動的に管理される必要がある。

オブジェクトは、ヒープと呼ばれるメモリの領域に格納され、ヒープは動的に割り当てられるメモリで、プログラムの実行中にサイズが変わるデータを扱うのに適している。
一方で、プリミティブ型のデータはスタックと呼ばれるメモリ領域に格納されることが多く、これはサイズが固定されていて、コンパイル時にメモリの量が決定される。