import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame()
    result['score'] = scores['score'].sort_values(ascending=False)
    result['rank'] = result['score'].rank(method='dense', ascending=False)
    return result