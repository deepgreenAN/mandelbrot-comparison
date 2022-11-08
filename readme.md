# マンデルブロ集合を描画
複数言語でマンデルブロ集合の描画と比較
## 言語
- rust
- python

## ビルド
[nushell](https://github.com/nushell/nushell)と[poetry](https://github.com/python-poetry/poetry)をインストール
```
〉nu build.nu
```

## ベンチマーク計測
`bench`コマンドを読み込み
```
〉source utils.nu
```
### rust
```
cd mandelbrot_rs
bench {target/release/mandelbrot} 10
cd ..
```
`target/release/mandelbrot_multi_thread`とすればマルチスレッドで実行される．

### python
```
cd mandelbrot_py
bench {poetry run python scripts/mandelbrot_full_jit.py} 10
cd ..
```
`poetry run python scripts/mandelbrot_pure.py`とすればpure python実装を実行する．