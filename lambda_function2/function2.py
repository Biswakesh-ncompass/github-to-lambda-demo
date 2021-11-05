import pandas as pd
import numpy as np


def lambda_handler(event, context):
    a=[[1,2]]
    b=[[3,4]]
    matrix=np.add(a,b)
    print(matrix)
