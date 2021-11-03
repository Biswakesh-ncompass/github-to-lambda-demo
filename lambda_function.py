import pandas as pd
import numpy as np


def lambda_handler(event, context):
    d={'col1':[1,2],'col2':[3,4],'col3':[5,6]}
    a=[[1,2]]
    b=[[3,4]]
    matrix=np.add(a,b)
    df=pd.DataFrame(data=d)
    print(df)
    print('Done X1.2')
    print(matrix)
