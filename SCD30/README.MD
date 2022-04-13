※これらのファイルはツクレル㈱の教材向けのファイルです。

# ファイルについて

これらのファイルは、CO2センサーSCD30をM5StackのUIFlowで制御するためのプログラムです。
SCD30の制御は https://github.com/agners の SCD30.py https://github.com/agners/micropython-scd30/ を利用して行います。
SCD30.pyをM5Stack本体に書き込んでからプログラムを実行します。
実行環境はUIFlowです。
対象とするはハードはM5Stack Basic,Gray,Fire,Go,Core2,Core2 AWSです。

## SCD30mod.m5b
SCD30.pyの関数を扱うためのカスタムブロックです。

## LineGraph.m5b
UIFlow上で線グラフを描画するカスタムブロックです。

## SCD30simpleDemo.m5f
SCD30.pyとSCD30mod.m5bを利用してSCD30の測定データを表示します。

## SCD30noCustom.m5f
SCD30.pyとSCD30mod.m5bを利用してSCD30の測定データをグラフ表示します。
グラフ表示はUIFlowの標準ブロックで行います。

## SCD30GraphDemo.m5f
SCD30.pyとSCD30mod.m5b、LinGraph.m5bを利用してSCD30をの測定データをグラフ表示します。
グラフ表示にはLinGraph.m5bに含まれるカスタムブロックで行います。
