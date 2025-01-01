import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
        """
        Vérifie la consistance entre StockCode et Description
        """
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
    
    def country_distrib(self):
        """
        Affiche et retourne le nombre de transactions par pays
        """
        transactions = self.data ['Country'].value_counts()
        plt.figure(figsize=(10, 6))
        transactions.plot(kind='barh', color='skyblue', edgecolor='black')
        plt.title("Nombre de transactions par pays", fontsize=16)
        plt.xlabel("Pays", fontsize=14)
        plt.ylabel("Nombre de transactions", fontsize=14)
        plt.xticks(rotation=45, fontsize=12)
        plt.xticks(rotation=45, fontsize=12)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.show()

    def stat_analitics(self):
        """
        Affiche la distribution des quantités et prix unitaires
        """
        # Analyse de la distribution des données numériques
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))
        sns.boxplot(y=self.data['Quantity'], ax=ax1)
        sns.boxplot(y=self.data['UnitPrice'], ax=ax2)
        ax1.set_title('Distribution Quantity')
        ax2.set_title('Distribution UnitPrice')
        plt.show()