# agg 调用的时候要指定字段，apply 默认传入的是整个dataframe
import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 1, 2, 2],'B': [1, 2, 3, 4],'C': np.random.randn(4)})

df.groupby('A',as_index=False).agg({'B':{'B_S':sum}})

df.groupby('A',as_index=False).apply(lambda x:sum(x['B'])).reset_index()
print(df)

# agg 方法将一个函数使用在一个数列上，然后返回一个标量的值。也就是说agg每次传入的是一列数据，对其聚合后返回标量。

# 对于apply采用自定义函数时，可以之间在函数后面，加上参数