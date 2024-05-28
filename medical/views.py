from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from . import forms

from . import models
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Agg')
import numpy as np
import io
import base64
from threading import Thread


def generate_explanation(row):
    explanations = []

    if "High Risk of Cardiovascular Diseases" in row["Diseases"]:
        explanations.append("The patient is over 60 years old, which indicates a high risk of cardiovascular diseases.")
    if "Prostate Health Concerns" in row["Diseases"]:
        explanations.append("The patient is a male over 50 years old, indicating potential prostate health concerns.")

    if "Diabetes" in row["Diseases"]:
        explanations.append(f"The patient's glucose level is {row['Glucose']}, which indicates diabetes.")

    if "Anemia" in row["Diseases"]:
        explanations.append(f"The patient's hemoglobin level is {row['HGB']}, which indicates anemia.")

    if "Hypercholesterolemia" in row["Diseases"]:
        explanations.append(
            f"The patient's cholesterol level is {row['Cholesterol']}, which indicates hypercholesterolemia.")

    if "Infection or Inflammation" in row["Diseases"]:
        explanations.append(
            f"The patient's white blood cell count is {row['WBC']}, which indicates infection or inflammation.")

    if "Thrombocytopenia" in row["Diseases"]:
        explanations.append(f"The patient's platelet count is {row['PLT']}, which indicates thrombocytopenia.")

    if "Neutropenia" in row["Diseases"]:
        explanations.append(
            f"The patient's neutrophil percentage is {row['Neutrophils']}, which indicates neutropenia.")

    if "Lymphocytosis" in row["Diseases"]:
        explanations.append(
            f"The patient's lymphocyte percentage is {row['Lymphocytes']}, which indicates lymphocytosis.")

    if "Monocytosis" in row["Diseases"]:
        explanations.append(f"The patient's monocyte percentage is {row['Monocytes']}, which indicates monocytosis.")

    if "Eosinophilia" in row["Diseases"]:
        explanations.append(
            f"The patient's eosinophil percentage is {row['Eosinophils']}, which indicates eosinophilia.")

    if "Basophilia" in row["Diseases"]:
        explanations.append(f"The patient's basophil percentage is {row['Basophils']}, which indicates basophilia.")

    if "Liver Dysfunction" in row["Diseases"]:
        explanations.append(f"The patient's bilirubin level is {row['Bilirubin']}, which indicates liver dysfunction.")

    if "Kidney Dysfunction" in row["Diseases"]:
        explanations.append(
            f"The patient's creatinine level is {row['Creatinine']}, which indicates kidney dysfunction.")

    if "Liver Disease" in row["Diseases"]:
        explanations.append(
            f"The patient's ALT level is {row['ALT']} and/or AST level is {row['AST']}, which indicates liver disease.")

    if "Hypernatremia" in row["Diseases"]:
        explanations.append(f"The patient's sodium level is {row['Sodium']}, which indicates hypernatremia.")
    elif "Hyponatremia" in row["Diseases"]:
        explanations.append(f"The patient's sodium level is {row['Sodium']}, which indicates hyponatremia.")

    if "Hyperkalemia" in row["Diseases"]:
        explanations.append(f"The patient's potassium level is {row['Potassium']}, which indicates hyperkalemia.")
    elif "Hypokalemia" in row["Diseases"]:
        explanations.append(f"The patient's potassium level is {row['Potassium']}, which indicates hypokalemia.")

    if "Hypercalcemia" in row["Diseases"]:
        explanations.append(f"The patient's calcium level is {row['Calcium']}, which indicates hypercalcemia.")
    elif "Hypocalcemia" in row["Diseases"]:
        explanations.append(f"The patient's calcium level is {row['Calcium']}, which indicates hypocalcemia.")

    if "Hypoalbuminemia" in row["Diseases"]:
        explanations.append(f"The patient's albumin level is {row['Albumin']}, which indicates hypoalbuminemia.")

    if "Hyperphosphatemia" in row["Diseases"]:
        explanations.append(
            f"The patient's phosphorus level is {row['Phosphorus']}, which indicates hyperphosphatemia.")
    elif "Hypophosphatemia" in row["Diseases"]:
        explanations.append(f"The patient's phosphorus level is {row['Phosphorus']}, which indicates hypophosphatemia.")

    if "Hypermagnesemia" in row["Diseases"]:
        explanations.append(f"The patient's magnesium level is {row['Magnesium']}, which indicates hypermagnesemia.")
    elif "Hypomagnesemia" in row["Diseases"]:
        explanations.append(f"The patient's magnesium level is {row['Magnesium']}, which indicates hypomagnesemia.")

    if "Hyperchloremia" in row["Diseases"]:
        explanations.append(f"The patient's chloride level is {row['Chloride']}, which indicates hyperchloremia.")
    elif "Hypochloremia" in row["Diseases"]:
        explanations.append(f"The patient's chloride level is {row['Chloride']}, which indicates hypochloremia.")

    return explanations

def determine_disease(row):
    diseases = []

    # Определяем заболевания на основе возраста и пола
    if row["age"] > 60:
        diseases.append("High Risk of Cardiovascular Diseases")
    if row["gender"] == "Male" and row["age"] > 50:
        diseases.append("Prostate Health Concerns")

    # Определяем заболевания на основе анализа крови
    if not (70 <= row["Glucose"] <= 99):
        if row["Glucose"] > 126:
            diseases.append("Diabetes")

    if row["HGB"] < 12:
        diseases.append("Anemia")

    if row["Cholesterol"] > 200:
        diseases.append("Hypercholesterolemia")

    if not (4.0 <= row["WBC"] <= 11.0):
        diseases.append("Infection or Inflammation")

    if not (4.0 <= row["RBC"] <= 5.9):
        diseases.append("Anemia")

    if not (150 <= row["PLT"] <= 450):
        diseases.append("Thrombocytopenia")

    if not (40 <= row["Neutrophils"] <= 70):
        diseases.append("Neutropenia")

    if not (20 <= row["Lymphocytes"] <= 40):
        diseases.append("Lymphocytosis")
    if not (2 <= row["Monocytes"] <= 10):
        diseases.append("Monocytosis")

    if not (1 <= row["Eosinophils"] <= 5):
        diseases.append("Eosinophilia")

    if row["Basophils"] > 1.0:
        diseases.append("Basophilia")

    if row["Bilirubin"] > 1.2:
        diseases.append("Liver Dysfunction")

    if row["Creatinine"] > 1.2:
        diseases.append("Kidney Dysfunction")

    if row["ALT"] > 40:
        diseases.append("Liver Disease")

    if row["AST"] > 40:
        diseases.append("Liver Disease")

    if not (135 <= row["Sodium"] <= 145):
        if row["Sodium"] > 145:
            diseases.append("Hypernatremia")
        else:
            diseases.append("Hyponatremia")

    if not (3.5 <= row["Potassium"] <= 5.0):
        if row["Potassium"] > 5.0:
            diseases.append("Hyperkalemia")
        else:
            diseases.append("Hypokalemia")
    if not (8.5 <= row["Calcium"] <= 10.5):
        if row["Calcium"] > 10.5:
            diseases.append("Hypercalcemia")
        else:
            diseases.append("Hypocalcemia")

    if row["Albumin"] < 3.5:
        diseases.append("Hypoalbuminemia")

    if not (2.5 <= row["Phosphorus"] <= 4.5):
        if row["Phosphorus"] > 4.5:
            diseases.append("Hyperphosphatemia")
        else:
            diseases.append("Hypophosphatemia")

    if not (1.5 <= row["Magnesium"] <= 2.5):
        if row["Magnesium"] > 2.5:
            diseases.append("Hypermagnesemia")
        else:
            diseases.append("Hypomagnesemia")

    if not (98 <= row["Chloride"] <= 108):
        if row["Chloride"] > 108:
            diseases.append("Hyperchloremia")
        else:
            diseases.append("Hypochloremia")

    return diseases

def generate_base_ordered_values(gender, age, continent):
    # Примерные базовые значения для показателей
    base_values = {
        'WBC': 7.0,  # 10^3/µL
        'RBC': 5.0,  # 10^6/µL
        'HGB': 15.0, # g/dL
        'HCT': 44.0, # %
        'MCV': 90.0, # fL
        'MCH': 29.5, # pg
        'MCHC': 34.0, # g/dL
        'RDW': 13.0, # %
        'PLT': 300,  # 10^3/µL
        'MPV': 9.5,  # fL
        'Neutrophils': 55.0, # %
        'Lymphocytes': 30.0, # %
        'Monocytes': 5.0,   # %
        'Eosinophils': 2.5,  # %
        'Basophils': 0.75,  # %
        'Glucose': 85.0,   # mg/dL
        'Urea': 13.5,      # mg/dL
        'Creatinine': 1.0, # mg/dL
        'Cholesterol': 160.0, # mg/dL
        'HDL': 50.0,       # mg/dL
        'LDL': 95.0,       # mg/dL
        'Triglycerides': 100.0, # mg/dL
        'ALT': 30.0,       # U/L
        'AST': 25.0,       # U/L
        'Bilirubin': 0.65, # mg/dL
        'Total_Protein': 7.2, # g/dL
        'Albumin': 4.2,    # g/dL
        'Globulin': 3.0,   # g/dL
        'Calcium': 9.5,    # mg/dL
        'Phosphorus': 3.5, # mg/dL
        'Magnesium': 1.95, # mg/dL
        'Sodium': 140.0,   # mEq/L
        'Potassium': 4.3,  # mEq/L
        'Chloride': 102.5  # mEq/L
    }

    # Пример закономерностей
    if gender == 'Male':
        base_values['RBC'] += 0.5
        base_values['HGB'] += 1.0
        base_values['Creatinine'] += 0.2
        base_values['Cholesterol'] += 10
    else:
        base_values['HDL'] += 10

    # Изменения в зависимости от возраста
    for key in base_values.keys():
        if key in ['WBC', 'RBC', 'HGB', 'HCT', 'MCV', 'MCH', 'MCHC', 'RDW', 'PLT', 'MPV']:
            base_values[key] -= age * 0.01
        elif key in ['Glucose', 'Cholesterol', 'Creatinine', 'Urea', 'Triglycerides']:
            base_values[key] += age * 0.2

    df = pd.DataFrame([base_values])

    return df
def generate_ordered_values(data):
    # Примерные базовые значения для показателей
    base_values = data.copy()
    gender = base_values['gender']
    age = base_values['age']

    # Пример закономерностей
    if gender == 'male':
        base_values['RBC'] += 0.5
        base_values['HGB'] += 1.0
        base_values['Creatinine'] += 0.2
        base_values['Cholesterol'] += 10
    else:
        base_values['HDL'] += 10

    # Изменения в зависимости от возраста
    for key in base_values.keys():
        if key in ['WBC', 'RBC', 'HGB', 'HCT', 'MCV', 'MCH', 'MCHC', 'RDW', 'PLT', 'MPV']:
            base_values[key] -= age * 0.01
        elif key in ['Glucose', 'Cholesterol', 'Creatinine', 'Urea', 'Triglycerides']:
            base_values[key] += age * 0.2

    df = pd.DataFrame([base_values])

    return df


def plot_ordered_values(df, title):
    # Convert the DataFrame to long-form format
    df_long = df.melt(var_name='Indicator', value_name='Value')

    # Ensure all values in 'Value' column are numeric
    df_long['Value'] = pd.to_numeric(df_long['Value'], errors='coerce')

    # Drop any rows where 'Value' is NaN
    df_long.dropna(subset=['Value'], inplace=True)

    sns.set(style="whitegrid")

    fig, ax = plt.subplots(figsize=(8, 6))

    try:
        bars = sns.barplot(x='Value', y='Indicator', data=df_long, palette="viridis", orient='h', ax=ax)
    except Exception as e:
        print(f"Error plotting barplot: {e}")
        return None

    ax.set_title(title, fontsize=16, weight='bold')
    ax.set_xlabel('Values', fontsize=12)
    ax.set_ylabel('Indicators', fontsize=12)

    for bar in bars.patches:
        ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{bar.get_width():.2f}', va='center', ha='left', fontsize=10, color='black')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graph = base64.b64encode(image_png).decode('utf-8')

    return graph


def post_contacts(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            first_name = cd.get('first_name')
            second_name = cd.get('second_name')
            email = cd.get('email')
            phone_number = cd.get('phone_number')

            user = models.CustomUser()

            data = {'first_name': first_name, 'second_name': second_name, 'email': email,
                    'phone_number': phone_number}

            user.save(data=data)

            request.session['user_code'] = user.user_code

            print(user.user_code)

            return redirect('medical:medicals')
    else:

        form = forms.ContactForm()

    return render(request, 'medical/contacts.html', {'form': form})


def post_medicals(request):
    if request.method == 'POST':
        form = forms.MedicalForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            user_code = request.session.get('user_code')
            print(user_code, 1)
            if user_code:
                try:
                    user = models.CustomUser.objects.get(user_code=user_code)
                    form.user = user
                except models.CustomUser.DoesNotExist:
                    pass
            form.user_code = user_code

            print(form)

            form.save()
            return redirect('medical:analysis')
        else:
            print(form.errors)
    else:
        form = forms.MedicalForm()

    return render(request, 'medical/medicals.html', {'form': form})


def get_user_medical_data(request, user_code):
    # Step 1: Fetch the user
    user = get_object_or_404(models.CustomUser, user_code=user_code)

    # Step 2: Access the related MedicalData instance
    try:
        medical_data_instance = user.medical_data  # Access the related MedicalData instance
    except models.MedicalData.DoesNotExist:
        medical_data_instance = None  # Handle the case where no related MedicalData exists

    # Step 3: Manually create a dictionary of fields and their values
    if medical_data_instance:
        medical_data_dict = {field.name: getattr(medical_data_instance, field.name) for field in
                             medical_data_instance._meta.fields}
    else:
        medical_data_dict = {}

    # Now medical_data_dict contains all the fields and their values
    return medical_data_dict


def get_analysis(request):
    user_code = request.session.get('user_code')

    medical_data_dict = get_user_medical_data(request, user_code)

    df = generate_base_ordered_values(medical_data_dict['gender'], medical_data_dict['age'], medical_data_dict['Continent'])
    graph_default = plot_ordered_values(df, 'Normal Blood Test Values')

    df1 = generate_ordered_values(medical_data_dict)
    graph_users = plot_ordered_values(df1, 'Your Blood Test Values')

    print(medical_data_dict)

    diseases = determine_disease(medical_data_dict)

    medical_data_dict['Diseases'] = diseases

    explanations = generate_explanation(medical_data_dict)

    return render(request, 'medical/analysis.html', {'graph_users': graph_users,'graph_default':graph_default, 'explanations': explanations,'diseases':diseases})
