import pandas as pd

class Transformer:
    def __init__(self, data: pd.DataFrame):
        self.raw_data = data
        self.cleaned_data = pd.DataFrame()

    def type_fix(self): 
        # Travailler sur une copie pour éviter de modifier l'original
        self.cleaned_data = self.raw_data.copy()
        # Convertir 'InvoiceDate' en datetime
        self.cleaned_data['InvoiceDate'] = pd.to_datetime(self.cleaned_data['InvoiceDate'], errors='coerce')

    def customerid_fix(self): 
        # Restaurer les CustomerID par InvoiceNo
        restored_id = self.cleaned_data.groupby('InvoiceNo').agg({
            'CustomerID': lambda x: x[x.notnull()].iloc[0] if x.notnull().any() else None
        }).reset_index()

        # Créer un mapping depuis le DataFrame agrégé
        customerids = restored_id.set_index('InvoiceNo')['CustomerID'].to_dict()

        # Mapper les CustomerID restaurés
        self.cleaned_data['CustomerID'] = self.cleaned_data['InvoiceNo'].map(customerids)

        # Supprimer les lignes où CustomerID est toujours manquant
        self.cleaned_data = self.cleaned_data.dropna(subset=['CustomerID'])

    def transform(self):
        self.type_fix()
        self.customerid_fix()
        return self.cleaned_data
