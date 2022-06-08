from django.http import HttpResponse
from django.shortcuts import render
import pickle
import pandas as pd
import numpy as np


def home(request):
    return render(request, "home.html")


def result(request):
    with open('model.pkl', 'rb') as f:
        reg = pickle.load(f)
    lis=[]
    lis.append(request.GET['LIMIT_BAL'])
    lis.append(request.GET['SEX'])
    lis.append(request.GET['EDUCATION'])
    lis.append(request.GET['MARRIAGE'])
    lis.append(request.GET['AGE'])
    lis.append(request.GET['PAY_0'])
    lis.append(request.GET['PAY_2'])
    lis.append(request.GET['PAY_3'])
    lis.append(request.GET['PAY_4'])
    lis.append(request.GET['PAY_5'])
    lis.append(request.GET['PAY_6'])
    lis.append(request.GET['BILL_AMT1'])
    lis.append(request.GET['BILL_AMT2'])
    lis.append(request.GET['BILL_AMT3'])
    lis.append(request.GET['BILL_AMT4'])
    lis.append(request.GET['BILL_AMT5'])
    lis.append(request.GET['BILL_AMT6'])
    lis.append(request.GET['PAY_AMT1'])
    lis.append(request.GET['PAY_AMT2'])
    lis.append(request.GET['PAY_AMT3'])
    lis.append(request.GET['PAY_AMT4'])
    lis.append(request.GET['PAY_AMT5'])
    lis.append(request.GET['PAY_AMT6'])




    payornot = reg.predict(pd.DataFrame(columns=['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0',
       'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1',
       'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6',
       'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5',
       'PAY_AMT6'],data=np.array(lis).reshape(1,23)))




    return render(request, "result.html",{'price' : payornot})


