import pandas as pd

def get_summary_stats(df):
    summary_stats = df.describe()
    
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    if len(cat_cols) > 0:
        group_col = cat_cols[0]
        grouped_stats = df.groupby(group_col).mean(numeric_only=True)
    else:
        grouped_stats = pd.DataFrame()
        
    return summary_stats, grouped_stats