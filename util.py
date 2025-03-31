import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import os
from imblearn.over_sampling import SMOTE
import warnings
warnings.filterwarnings("ignore")


def load_data(data_dir : str, 
              excel_file : str,
                mode : str = "train",
                scale = bool,
                smote = bool,
                ):
    
    
    print("--------------Load RawData--------------")
    df = pd.read_csv(os.path.join(data_dir, excel_file))
    
    #Inclusion
    print("--------------Inclusion--------------")
    print('Total : ', len(df))

    print("--------------fillNA--------------")
    # data = data.dropna()
    df.fillna(0.0,inplace=True)
    print(df['REAL_STONE'].value_counts())

    #Column rename
    df.rename(columns={'ID': 'patient_id', 'REAL_STONE':'target'}, inplace=True)

   # df_all = ['SEX', 'SBP', 'DBP', 'HR', 'RR', 'BT',
    #    'AGE', 'VISIBLE_STONE_CT', 'PANCREATITIS', 'DUCT_DILIATATION_10MM',
    #    'DUCT_DILIATATION_8MM', 'Hb', 'PLT', 'WBC', 'ALP', 'ALT', 'AST', 'CRP',
    #    'BILIRUBIN', 'HR_100', 'GGT', 'BUN', 'CREATININE', 'BT_38', 'target']

    # Forward (n=13)
    columns = ['patient_id',  'HR', 'BT', 'AGE','DUCT_DILIATATION_10MM', 'Hb','PLT','WBC','ALP', 'ALT', 'AST', 'TOTAL_BILIRUBIN',  'target']
    
    # # VISIBLE_STONE_CT (n=1)
    # columns = ['patient_id','VISIBLE_STONE_CT', 'target']

 
    data = df[columns]
    
    if scale:
        print("--------------Scaling--------------")
        columns_to_scale = ['SEX',  'AGE', 'DUCT_DILIATATION_10MM', 'DUCT_DILIATATION_8MM', 'Hb', 'PLT', 'WBC', 'ALP', 'ALT', 'AST',  'GGT', 'BUN', 'CREATININE']

        columns_to_scale_existing = [col for col in columns_to_scale if col in data.columns]

        if columns_to_scale_existing:
            scaler = MinMaxScaler()
            data[columns_to_scale_existing] = scaler.fit_transform(data[columns_to_scale_existing])
        else:
            print("No columns to scale.")
            
    if mode == 'train' or mode == 'test':
        if smote:  # Apply SMOTE if the flag is set
            print(data['target'].value_counts())
            print("Applying SMOTE...")
            smote = SMOTE(sampling_strategy='all', random_state=42)
            X_data = data.drop(columns=['target'])
            y_data = data['target']
            X_data_res, y_data_res = smote.fit_resample(X_data, y_data)
            data_resampled = pd.DataFrame(X_data_res, columns=X_data.columns)
            data_resampled['target'] = y_data_res
            data = data_resampled  # Update train_data with resampled data
            print(data['target'].value_counts())
            
        train_data, test_data = train_test_split(data, test_size=0.3, stratify=data['target'], random_state=123)
        valid_data, test_data = train_test_split(test_data, test_size=0.4, stratify=test_data['target'], random_state=123)
        
        if mode == 'train':
            print("Train set shape:", train_data.shape)
            print("Validation set shape:", valid_data.shape)
            return train_data, valid_data

        elif mode == 'test':
            print("Test set shape:", test_data.shape)
            return test_data
    
    else:
        raise ValueError("Choose mode!")
    
    
def load_data_and_prepare(data_dir, excel_file, mode, scale, smote):
    # Load train, validation, and test data
    train_df,val_df = load_data(data_dir, excel_file, mode, scale, smote)
    
    train_df.drop(columns=['patient_id','target'],inplace = True)
    val_df.drop(columns=['patient_id','target'],inplace = True)
    
    train = pd.concat([train_df,val_df],axis=0)
    
    return train