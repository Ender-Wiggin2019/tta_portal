import pandas as pd
def txt2Json(file):
    df = pd.read_csv('./cgeaccount-1.txt',header=None,names=['id','name'],encoding='ISO 8859-2' ,delimiter=' ',index_col='id')
    df1=df.drop_duplicates('name',keep='last')
    df1 = df1.reset_index()
    df1 = df1.set_index('name')
    df1.to_json('./data.json',orient='index')
txt2Json('./cgeaccount-1.txt')