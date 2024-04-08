# from django.shortcuts import render
# from django.http import HttpResponse
# import pickle
# import pandas as pd
#
# def home(request):
#     return render(request, 'home.html')
#
# def predict_result(request):
#     if request.method == 'POST':
#         age = int(request.POST['age'])
#         sex = request.POST['sex']
#         bp = request.POST['bp']
#         cholesterol = request.POST['cholesterol']
#         na_to_k = float(request.POST['na_to_k'])
#         na_to_k = round(na_to_k, 2)
#
#
#         # Convert user inputs into a DataFrame similar to X_train
#         user_data = pd.DataFrame({
#             'Age': [age],
#             'Sex': [sex],
#             'BP': [bp],
#             'Cholesterol': [cholesterol],
#             'Na_to_K': [na_to_k]
#         })
#
#         # Perform one-hot encoding for categorical variables
#         user_data = pd.get_dummies(user_data, drop_first=True)
#
#         # Ensure all columns present in user data
#         expected_columns = ['Age', 'Na_to_K', 'Sex_M', 'BP_LOW', 'BP_NORMAL', 'Cholesterol_NORMAL']
#         for col in expected_columns:
#             if col not in user_data.columns:
#                 user_data[col] = 0
#
#         # Rearrange columns to match X_train
#         user_data = user_data[expected_columns]
#
#         # Load the trained model
#         with open('logistic_model2.pkl', 'rb') as f:
#             model = pickle.load(f)
#
#         # Make predictions
#         prediction = model.predict(user_data)
#
#         return render(request, 'result.html', {'prediction': prediction[0]})
#     else:
#         return HttpResponse('Invalid request method')


from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import pickle
from django import forms

# Define your form class
from django.shortcuts import render
from .forms import YourForm
import pandas as pd
import pickle

def home(request):
    if request.method == 'POST':
        form = YourForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            bp = form.cleaned_data['bp']
            cholesterol = form.cleaned_data['cholesterol']
            na_to_k = form.cleaned_data['na_to_k']

            user_data = pd.DataFrame({
                'Age': [age],
                'Sex': [sex],
                'BP': [bp],
                'Cholesterol': [cholesterol],
                'Na_to_K': [na_to_k]
            })

            user_data = pd.get_dummies(user_data, drop_first=True)

            expected_columns = ['Age', 'Na_to_K', 'Sex_M', 'BP_LOW', 'BP_NORMAL', 'Cholesterol_NORMAL']
            for col in expected_columns:
                if col not in user_data.columns:
                    user_data[col] = 0

            user_data = user_data[expected_columns]

            with open('logistic_model2.pkl', 'rb') as f:
                model = pickle.load(f)

            prediction = model.predict(user_data)

            return render(request, 'result.html', {'prediction': prediction[0]})
    else:
        form = YourForm()

    return render(request, 'home.html', {'form': form})

def predict_result(request):
    if request.method == 'POST':
        form = YourForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            bp = form.cleaned_data['bp']
            cholesterol = form.cleaned_data['cholesterol']
            na_to_k = form.cleaned_data['na_to_k']

            user_data = pd.DataFrame({
                'Age': [age],
                'Sex': [sex],
                'BP': [bp],
                'Cholesterol': [cholesterol],
                'Na_to_K': [na_to_k]
            })

            user_data = pd.get_dummies(user_data, drop_first=True)

            expected_columns = ['Age', 'Na_to_K', 'Sex_M', 'BP_LOW', 'BP_NORMAL', 'Cholesterol_NORMAL']
            for col in expected_columns:
                if col not in user_data.columns:
                    user_data[col] = 0

            user_data = user_data[expected_columns]

            with open('logistic_model2.pkl', 'rb') as f:
                model = pickle.load(f)

            prediction = model.predict(user_data)

            return render(request, 'result.html', {'prediction': prediction[0]})
    else:
        form = YourForm()

    return render(request, 'home.html', {'form': form})
