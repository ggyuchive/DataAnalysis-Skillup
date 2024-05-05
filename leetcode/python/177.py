import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salary = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    attribute = 'getNthHighestSalary('+str(N)+')'
    if len(salary) < N or N <= 0:
        return pd.DataFrame({attribute: [None]})
    return pd.DataFrame({attribute: [salary[N-1]]})