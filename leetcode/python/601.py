import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    l, r = 0, 0
    result = pd.DataFrame(columns=['id', 'visit_date', 'people'])
    for i in range(stadium.shape[0]):
        ppl = stadium['people'][i]
        if ppl >= 100:
            r = i
        else:
            if r-l >= 2:
                for j in range(l, r+1):
                    result.loc[len(result)] = stadium.loc[j]
            l, r = i+1, i+1
    if r-l >= 2:
        for j in range(l, r+1):
            result.loc[len(result)] = stadium.loc[j]
    return result