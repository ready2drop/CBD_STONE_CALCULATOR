# Gradio
examples = [
    [
        [['100.0','38.2', '72', '1.0','10.6','171.0','14.54','236.0','548.0','182.0','3.2']],
        "PT_NO = 10001862, VISIBLE_STONE_CT = True, REAL_STONE = True",
    ],

    [
        [['81.0', '36.1','58','1.0','13.6','388.0','21.13','196.0','70.0','118.0','2.7']],
        "PT_NO = 10007376, VISIBLE_STONE_CT = True, REAL_STONE = True",
    ],
    [
        [['80.0','36.6','63','0.0','9.3','103.0','8.45','440.0','199.0','100.0','4.5',]],
        "PT_NO = 10040285, VISIBLE_STONE_CT = False, REAL_STONE = True",
    ],
    [
        [['83.0','36.7','57','1.0', '12.1','192.0','8.63','47.0','32.0','59.0','0.4']],
        "PT_NO = 10005545, VISIBLE_STONE_CT = False, REAL_STONE = False",
    ],
]

tabular_header = ['HR', 'BT','AGE', 'DUCT_DILIATATION_10MM', 'Hb','PLT','WBC', 'ALP', 'ALT', 'AST','TOTAL_BILIRUBIN']

description = """
Due to GPU resource constraints, the online demo is running on 2 vCPUs and 16 GB of RAM. \n
**Note**: This model is specifically designed for the diagnosis and prediction of common bile duct(CBD) stones and provides accurate and reliable results. \n 
The input data consists of the following **discrete** and **continuous** variables, all of which play a significant role in the model's performance \n
- Discrete Variables:
- DUCT_DILIATATION_10MM (Presence of common bile duct dilation (≥10mm))
- Continuous Variables:
- HR: Initial heart rate (Float)
- BT: Initial body temperature (Float)
- AGE: Age (Int)
- Hb: Hemoglobin level (Float)
- PLT: Platelet count (Float)
- WBC: White blood cell count (Float)
- ALP: Alkaline phosphatase (Float)
- ALT: Alanine aminotransferase (Float)
- AST: Aspartate aminotransferase (Float)
- BILIRUBIN: Bilirubin level (Float)
**Important**: Changes to the structure of the input data (e.g., adding, removing columns) may affect the model's predictions. \n 
Therefore, it is essential to retrain or revalidate the model if any modifications are made to the input data structure. \n
"""

title_markdown = ("""
## Development of a Common Bile Duct Stone Prediction Model Using Machine Learning Based on Clinical Data
[📖[Learn more about Common Bile Duct Stones (https://namu.wiki/w/%EC%B4%9D%EB%8B%B4%EA%B4%80%EA%B2%B0%EC%84%9D%EC%A6%9D)] 
### Copyright © 2024 Dongguk University (DGU) and Dongguk University Medical Center (DUMC). All rights reserved.
""")