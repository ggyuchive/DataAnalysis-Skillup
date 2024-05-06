import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(left=employee, right=employee, how='inner', left_on='managerId', right_on='id')
    result = df[df['salary_x'] > df['salary_y']]
    return pd.DataFrame({'Employee': result['name_x']})