import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 日本語対応のフォントを設定
plt.rcParams['font.family'] = 'MS Gothic'  
plt.rcParams['font.size'] = 12

# データの読み込み
df = pd.read_csv("C:\\source\\mu-psd-03\\AI\\weather(1).csv", encoding='shift_jis')
df["date"]=pd.to_datetime(df["date"])
df = pd.get_dummies(df)

# 相関行列
correlation_coefficients = df.corr()  # 相関行列の計算

# 相関行列のヒートマップ (相関係数の値あり)
plt.figure(figsize=(12, 8))  # この段階で画像のサイズを指定する
sns.heatmap(correlation_coefficients, cmap='seismic', annot=True)

# ヒートマップを表示
plt.show()
