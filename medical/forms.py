from django import forms
from .models import MedicalData


class ContactForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-md', 'id': 'first_name'}))
    second_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-md', 'id': 'second_name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control input-md', 'id': 'email'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-md', 'id': 'phone_number'}))


class MedicalForm(forms.ModelForm):
    class Meta:
        model = MedicalData
        exclude = ['user']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control', 'id': 'age', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'id': 'gender'}),
            'WBC': forms.TextInput(attrs={'class': 'form-control', 'id': 'wbc', 'placeholder': 'WBC'}),
            'RBC': forms.TextInput(attrs={'class': 'form-control', 'id': 'rbc', 'placeholder': 'RBC'}),
            'HGB': forms.TextInput(attrs={'class': 'form-control', 'id': 'hgb', 'placeholder': 'HGB'}),
            'HCT': forms.TextInput(attrs={'class': 'form-control', 'id': 'hct', 'placeholder': 'HCT'}),
            'MCV': forms.TextInput(attrs={'class': 'form-control', 'id': 'mcv', 'placeholder': 'MCV'}),
            'MCH': forms.TextInput(attrs={'class': 'form-control', 'id': 'mch', 'placeholder': 'MCH'}),
            'MCHC': forms.TextInput(attrs={'class': 'form-control', 'id': 'mchc', 'placeholder': 'MCHC'}),
            'RDW': forms.TextInput(attrs={'class': 'form-control', 'id': 'rdw', 'placeholder': 'RDW'}),
            'PLT': forms.NumberInput(attrs={'class': 'form-control', 'id': 'plt', 'placeholder': 'PLT'}),
            'MPV': forms.TextInput(attrs={'class': 'form-control', 'id': 'mpv', 'placeholder': 'MPV'}),
            'Neutrophils': forms.TextInput(attrs={'class': 'form-control', 'id': 'neutrophils', 'placeholder': 'Neutrophils'}),
            'Lymphocytes': forms.TextInput(attrs={'class': 'form-control', 'id': 'lymphocytes', 'placeholder': 'Lymphocytes'}),
            'Monocytes': forms.TextInput(attrs={'class': 'form-control', 'id': 'monocytes', 'placeholder': 'Monocytes'}),
            'Eosinophils': forms.TextInput(attrs={'class': 'form-control', 'id': 'eosinophils', 'placeholder': 'Eosinophils'}),
            'Basophils': forms.TextInput(attrs={'class': 'form-control', 'id': 'basophils', 'placeholder': 'Basophils'}),
            'Glucose': forms.NumberInput(attrs={'class': 'form-control', 'id': 'glucose', 'placeholder': 'Glucose'}),
            'Urea': forms.NumberInput(attrs={'class': 'form-control', 'id': 'urea', 'placeholder': 'Urea'}),
            'Creatinine': forms.TextInput(attrs={'class': 'form-control', 'id': 'creatinine', 'placeholder': 'Creatinine'}),
            'Cholesterol': forms.NumberInput(attrs={'class': 'form-control', 'id': 'cholesterol', 'placeholder': 'Cholesterol'}),
            'HDL': forms.NumberInput(attrs={'class': 'form-control', 'id': 'hdl', 'placeholder': 'HDL'}),
            'LDL': forms.NumberInput(attrs={'class': 'form-control', 'id': 'ldl', 'placeholder': 'LDL'}),
            'Triglycerides': forms.NumberInput(attrs={'class': 'form-control', 'id': 'triglycerides', 'placeholder': 'Triglycerides'}),
            'ALT': forms.NumberInput(attrs={'class': 'form-control', 'id': 'alt', 'placeholder': 'ALT'}),
            'AST': forms.NumberInput(attrs={'class': 'form-control', 'id': 'ast', 'placeholder': 'AST'}),
            'Bilirubin': forms.TextInput(attrs={'class': 'form-control', 'id': 'bilirubin', 'placeholder': 'Bilirubin'}),
            'Total_Protein': forms.TextInput(attrs={'class': 'form-control', 'id': 'total_protein', 'placeholder': 'Total Protein'}),
            'Albumin': forms.TextInput(attrs={'class': 'form-control', 'id': 'albumin', 'placeholder': 'Albumin'}),
            'Globulin': forms.TextInput(attrs={'class': 'form-control', 'id': 'globulin', 'placeholder': 'Globulin'}),
            'Calcium': forms.TextInput(attrs={'class': 'form-control', 'id': 'calcium', 'placeholder': 'Calcium'}),
            'Phosphorus': forms.TextInput(attrs={'class': 'form-control', 'id': 'phosphorus', 'placeholder': 'Phosphorus'}),
            'Magnesium': forms.TextInput(attrs={'class': 'form-control', 'id': 'magnesium', 'placeholder': 'Magnesium'}),
            'Sodium': forms.NumberInput(attrs={'class': 'form-control', 'id': 'sodium', 'placeholder': 'Sodium'}),
            'Potassium': forms.TextInput(attrs={'class': 'form-control', 'id': 'potassium', 'placeholder': 'Potassium'}),
            'Chloride': forms.NumberInput(attrs={'class': 'form-control', 'id': 'chloride', 'placeholder': 'Chloride'}),
            'Continent': forms.Select(attrs={'class': 'form-control', 'id': 'continent'}),
            'Capital': forms.TextInput(attrs={'class': 'form-control', 'id': 'capital', 'placeholder': 'Capital'}),
        }
