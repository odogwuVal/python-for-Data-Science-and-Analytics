import pandas as pd

data1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D' ,'E', 'F', 'G'],
    'value1': [1, 2, 3, 4, 5, 6, 7]
})

data2 = pd.DataFrame({
    'key': ['C', 'D', 'E', 'F' , 'G', 'H', 'I'],
    'value2': [8, 9, 10, 11, 12, 13, 14]
})

merge_inner_join = pd.merge(data1, data2, on='key', how='inner')
print(merge_inner_join)

merge_left_join = pd.merge(data1, data2, on='key', how='left')
print(merge_left_join)

merge_right_join = pd.merge(data1, data2, on='key', how='right')
print(merge_right_join)

merge_left = pd.merge(data1, data2, on='key', how='left', indicator=True)
merge_left_anti_join = merge_left[merge_left["_merge"]== "left_only"].drop("_merge", axis=1)
print(merge_left_anti_join)

merge_right = pd.merge(data1, data2, on='key', how='right', indicator=True)
merge_right_anti_join = merge_right[merge_right["_merge"]== "right_only"].drop("_merge", axis=1)
print(merge_right_anti_join)