import pandas as pd
import matplotlib.pyplot as plt

data = {'team': ['A', 'B', 'C'], 'score': [10, 15, 7]}
df = pd.DataFrame(data)
df.plot(kind='bar', x='team', y='score', title='Team Score')
plt.savefig("output.png")

print("[INFO] 分析完成，已儲存圖表 output.png")