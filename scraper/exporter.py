import pandas as pd

def export_to_excel(data, filename="output/trendyol_products.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)