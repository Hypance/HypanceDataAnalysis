<div align="center">
  <img src=https://avatars.githubusercontent.com/u/113800422?s=200&v=4"><br>
</div>

-----------------
# HyTa - テクニカルアナリシスライブラリー

 ![](https://img.shields.io/badge/python-3.8-blue.svg) ![](https://img.shields.io/badge/python-3.9-blue.svg) ![](https://img.shields.io/badge/python-3.10-blue.svg) ![](https://img.shields.io/badge/python-3.11-blue.svg) ![unit tests](https://github.com/Hypance/HypanceDataAnalysis/blob/read.me/readme_docs/unittest.svg) 



<p align="center">
    <a href="/readme_docs/readme_fr.md">Français </a>
    ·
    <a href="/readme_docs/readme_cn.md">简体中文</a>
    ·
    <a href="/readme_docs/readme_es.md">Español</a>
    ·
    <a href="/readme_docs/readme_de.md">Deutsch</a>
    ·
    <a href="/readme_docs/readme_ja.md">日本語</a>
    ·
    <a href="/readme_docs/readme_pt-BR.md">Português Brasileiro</a>
    ·
    <a href="/readme_docs/readme_it.md">Italiano</a>
    ·
    <a href="/readme_docs/readme_kr.md">한국어</a>
    .
    <a href="/readme_docs/readme_nl.md">Nederlands</a>
    .
    <a href="/readme_docs/readme_np.md">नेपाली</a>
    .
    <a href="/readme_docs/readme_tr.md">Türkçe</a>
  </p>

-----------------

「Hytaは、テクニカル分析のための金融指標を提供する新しいPythonライブラリで、特にインクリメンタルな計算に重点を置いているのが特徴です。このライブラリは、インクリメンタルな計算を特徴とするため、リアルタイムアプリケーションや反復的な入力を伴う他のアプリケーションに特に適しています。

比較的新しいプロジェクトである「hyta」は、ユーザーからのフィードバックや、ユーザー独自のニーズを満たすためにAPIを改善するための提案を強く受け入れています。

---

### 指標一覧

hyta」の現在のバージョンは、包括的な指標セットを含んでいます。しかし、好みの指標が含まれていない場合、GitHub Issuesからチケットを作成すれば、将来のバージョンのライブラリに組み込まれる可能性が高いです。

- [Average Directional Index (ADX)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/adx.py)
- [Aroon](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/aroon.py)
- [Average True Range (ATR)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/atr.py)
- [Bollinger Bands](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/bollinger.py)
- [Commodity Channel Index (CCI)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/cci.py)
- [Chaikin Money Flow (CMF)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/cmf.py)
- [Chande Momentum Oscillator (CMO)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/cmo.py)
- [Detrended Price Oscillator (DPO)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/dpo.py)
- [Directional Movement Index (DX)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/dx.py)
- [Exponential Moving Average (EMA)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/ema.py)
- [Hull Moving Average (HMA)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/hma.py)
- [Ichimoku Cloud](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/ichimoku_cloud.py)
- [Kaufman Adaptive Moving Average (KAMA)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/kama.py)
- [Moving Average Convergence Divergence (MACD)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/macd.py)
- [Money Flow Index (MFI)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/mfi.py)
- [Momentum](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/momentum.py)
- [Moving Average](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/movingaverage.py)
- [On Balance Volume (OBV)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/on_balance_volume.py)
- [Percentage Price Oscillator (PPO)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/ppo.py)
- [Parabolic SAR (PSAR)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/psar.py)
- [Rate of Change (ROC)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/roc.py)
- [Relative Strength Index (RSI)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/rsi.py)
- [Simple Moving Average (SMA)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/SMA.py)
- [Stochastic Oscillator](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/Stochastic_Oscillator.py)
- [Triangular Moving Average (TMA)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/tma.py)
- [True Strength Index (TSI)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/tsi.py)
- [Ultimate Oscillator (UO)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/uo.py)
- [Williams %R](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/williams_r.py)
- [Weighted Moving Average (WMA)](https://github.com/Hypance/HypanceDataAnalysis/blob/main/hyta/wma.py)



### インストール
```bash
pip install hyta
```

### お問い合わせ先

- 問題、バグ、修正の報告や新機能の提案を最も効率的に行うには、[GitHub Issues](https://github.com/Hypance/HypanceDataAnalysis/issues)の活用を強くお勧めします。