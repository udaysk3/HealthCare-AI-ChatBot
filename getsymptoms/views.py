from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .newPythonCodeOfAlgorithm import randomforest
from .diagnosis import diag

# import joblib
# import numpy as np
# import pandas as pd
# from scipy.stats import mode
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.svm import SVC
# from sklearn.naive_bayes import GaussianNB
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, confusion_matrix

# DATA_PATH = "getsymptoms/dataset/Training.csv"
# data = pd.read_csv(DATA_PATH).dropna(axis = 1)

# X = data.iloc[:,:-1]


# symptoms = X.columns.values

# # load the models
# final_rf_model = joblib.load("final_rf_model.joblib")
# final_nb_model = joblib.load("final_nb_model.joblib")
# final_svm_model = joblib.load("final_svm_model.joblib")

# encoder = LabelEncoder()
# data["prognosis"] = encoder.fit_transform(data["prognosis"])

# # load the data_dict
# # data_dict = joblib.load("data_dict.joblib")
# # Creating a symptom index dictionary to encode the
# # input symptoms into numerical form
# symptom_index = {}
# for index, value in enumerate(symptoms):
# 	symptom = " ".join([i.capitalize() for i in value.split("_")])
# 	symptom_index[symptom] = index

# data_dict = {
# 	"symptom_index":symptom_index,
# 	"predictions_classes":encoder.classes_
# }

# # Defining the Function
# # Input: string containing symptoms separated by commas
# # Output: Generated predictions by models
# def predictDisease(symptoms):
# 	symptoms = symptoms.split(",")
	
# 	# creating input data for the models
# 	input_data = [0] * len(data_dict["symptom_index"])
# 	for symptom in symptoms:
# 		index = data_dict["symptom_index"][symptom]
# 		input_data[index] = 1
		
# 	# reshaping the input data and converting it
# 	# into suitable format for model predictions
# 	input_data = np.array(input_data).reshape(1,-1)
	
# 	# generating individual outputs
# 	rf_prediction = data_dict["predictions_classes"][final_rf_model.predict(input_data)[0]]
# 	nb_prediction = data_dict["predictions_classes"][final_nb_model.predict(input_data)[0]]
# 	svm_prediction = data_dict["predictions_classes"][final_svm_model.predict(input_data)[0]]
	
# 	# making final prediction by taking mode of all predictions
# 	final_prediction = mode([rf_prediction, nb_prediction, svm_prediction])[0][0]
# 	predictions = {
# 		"rf_model_prediction": rf_prediction,
# 		"naive_bayes_prediction": nb_prediction,
# 		"svm_model_prediction": svm_prediction,
# 		"final_prediction":final_prediction
# 	}
# 	return predictions

# Testing the function
# print(predictDisease("Itching,Muscle Wasting"))


@csrf_exempt
def getsymptoms(req):
    if req.method=='POST':
        print(req)
        received_json_data=json.loads(req.body)
        print(received_json_data)
        feeling  =  received_json_data['queryResult']['parameters']['feeling']
        symptoms =  received_json_data['queryResult']['parameters']['symptoms']
        print(symptoms)
        res = ''
        if len(symptoms) == 1:
            res = randomforest(symptoms[0])
        elif len(symptoms) == 2:
            res = randomforest(symptoms[0], symptoms[1])
        elif len(symptoms) == 3:
            res = randomforest(symptoms[0], symptoms[1], symptoms[2])
        elif len(symptoms) == 4:
            res = randomforest(symptoms[0], symptoms[1], symptoms[2], symptoms[3])
        elif len(symptoms) == 5:
            res = randomforest(symptoms[0], symptoms[1], symptoms[2], symptoms[3], symptoms[4])
        print(res)
        # for symptom in symptoms:
        #     if '_' in symptom:
        #         symptom = " ".join([i for i in symptom.split("_")])
        #         print(symptom)
        #     else:
        #         l.append(" ".join([i for i in symptom.split()]))
        # res = ','.join(l)
        # print(res)
        # disease = predictDisease(res)
 
        return JsonResponse(
           {
  "fulfillmentMessages": [
    {
      "text": {
        "text": [
          f"Hi, You may be suffering with {res}."
        ]
      }
    },
    {
      "text": {
        "text": [
          f'''You are advised to take these steps: \n
          {diag(res)}
          ''' 
        ]
      }
    },
    {
      "text": {
        "text": [
          "Your health and well-being are important to me. If you're experiencing serious issues or pain, I highly recommend seeking medical attention from a doctor or hospital."
        ]
      }
    }
  ]
}
  
                       )
    # print('disease is',randomforest('headache','neck_pain','back_pain'))
    return render(req, 'getsymptoms/index.html')
        # "You may be suffering with "+ disease + "You are adviced to take these medicines :"
        # +
        # medicines.lilst
        # +
        # "And Consult doctor after "+ these.days + "If still you feel same symptoms"