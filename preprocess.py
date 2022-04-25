def preprocess_Yes_No(col):
    return 1 if col.lower() =='yes' else 0

def preprocess_Sex(Sex):
    return 1 if Sex.lower() == 'male' else 0

def preprocess_Agecategory(AgeCategory):
    if AgeCategory== '18-24':
        return 0
    elif AgeCategory=='25-29':
        return 1
    elif AgeCategory=='30-34':
        return 2
    elif AgeCategory== '35-39':
        return 3
    elif AgeCategory== '40-44':
        return 4
    elif AgeCategory== '45-49':
        return 5
    elif AgeCategory== '50-54':
        return 6
    elif AgeCategory=='55-59':
        return 7
    elif AgeCategory== '60-64':
        return 8
    elif AgeCategory=='65-69':
        return 9
    elif AgeCategory=='70-74':
        return 10
    elif AgeCategory=='75-79':
        return 11
    elif AgeCategory=='> 80':
        return 12
    
def preprocess_Race(Race):
    if Race.lower() == 'asian':
        return [1,0,0,0,0]
    elif Race.lower() == 'black':
        return [0,1,0,0,0]
    elif Race.lower() == 'hispanic':
        return [0,0,1,0,0]
    elif Race.lower() == 'other':
        return [0,0,0,1,0]
    elif Race.lower() == 'white':
        return [0,0,0,0,1]
    elif Race.lower() == 'American Indian/Alaskan Native':
        return[0,0,0,0,0]    
    
def preprocess_Diabetic(Diabetic):
    if Diabetic.lower() == 'no, borderline diabetes':
        return [1,0,0]
    elif Diabetic.lower()== 'yes':
        return [0,1,0]
    elif Diabetic.lower() == 'yes (during pregnancy)':
        return [0,0,1]
    else:
        return [0,0,0]
    
def preprocess_Genhealth(GenHealth):
    if GenHealth.lower() == 'poor': 
        return 0
    elif GenHealth.lower() =='fair': 
        return 1
    elif GenHealth.lower()=='good': 
        return 2
    elif GenHealth.lower()== 'very good':
        return 3
    else:
        return 4


## data is ductionary contains all input from the user
def Preprocess(data):
    BMI=data['BMI']
    smoker=preprocess_Yes_No(data['Smoking'])
    Alcohol_drink=preprocess_Yes_No(data['AlcoholDrinking'])
    stroke=preprocess_Yes_No(data['Stroke'])
    physical_health=data['PhysicalHealth']
    mental_health=data['MentalHealth']
    Diff_walk=preprocess_Yes_No(data['DiffWalking'])
    sex=preprocess_Sex(data['Sex'])
    age_category=preprocess_Agecategory(data['AgeCategory'])
    race=preprocess_Race(data['Race'])
    diabetic=preprocess_Diabetic(data['Diabetic'])
    physical_activity=preprocess_Yes_No(data['PhysicalActivity'])
    general_health=preprocess_Genhealth(data['GenHealth'])
    sleep_time=data['SleepTime']
    asthma = preprocess_Yes_No(data['Asthma'])
    kidney_disease=preprocess_Yes_No(data['KidneyDisease'])
    skin_cancer=preprocess_Yes_No(data['SkinCancer'])
    
    final_data = [BMI, smoker, Alcohol_drink, stroke, physical_health, mental_health, Diff_walk, sex, age_category] + race + diabetic + [physical_activity ,general_health, sleep_time, asthma, kidney_disease, skin_cancer]
    return final_data