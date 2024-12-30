import pandas as pd

class DataAnalyzer:
    def __init__(self, data : pd.DataFrame):
        self.data = data
    
    def display_summary(self):
        """
        Analyse sommaire des données 
        """
        print("Vue globale des données : ")
        print(self.data.info())
    

    def count_missing_values(self):
        """
        Affiche un tableau avec le nombre de données manquantes (NaN, None) par colonne.
        """
        missing_counts = self.data.isnull().sum().reset_index()
        missing_counts.columns = ['Column', 'Missing Values']
        return missing_counts
    
    def product_id_consistency(self):
        """Vérifie la consistance entre StockCode et Description"""
        # Grouper par StockCode et vérifier les descriptions uniques
        product_desc = self.data.groupby('StockCode')['Description'].agg(['nunique', 'unique'])
            
        # Identifier les incohérences
        inconsistent_products = product_desc[product_desc['nunique'] > 1]
            
        # Créer un DataFrame détaillé des inconsistances
        detailed_inconsistencies = []
        for stock_code in inconsistent_products.index:
            descriptions = self.data[self.data['StockCode'] == stock_code]['Description'].unique()
            detailed_inconsistencies.append({
                'StockCode': stock_code,
                'Description_Count': len(descriptions),
                'Descriptions': descriptions
            })
                
        return pd.DataFrame(detailed_inconsistencies)