from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt

import pickle
import numpy
import pandas as pd
import os
import bz2

base_dir = os.path.dirname(__file__)

cancer_names = {
    "blca": "Bladder",
    "brca": "Breast",
    "chol": "Bile duct",
    "coad": "Colon",
    "esca": "Esophagus",
    "hnsc": "Head and neck",
    "kich": "Kidney chromophobe",
    "kirc": "Kidney renal clear cell",
    "lich": "Liver",
    "luad": "Lung",
    "prad": "Prostate",
    "stad": "Stomach",
    "thca": "Thyroid",
    "ucec": "Uterus",
    "paad": "Pancreas",
    "skcm": "Skin melanoma",
    "ov": "Ovary"
}

# Create your views here.
@csrf_exempt
@api_view(['POST'])
def predict(request, model_name):
    data = numpy.array(request.data["input"]).reshape(1,-1)
    ifile = bz2.BZ2File(base_dir + "/saved_models/" + model_name + ".pk.bz2",'rb')
    load_model = pickle.load(ifile)
    ifile.close()
    # replace class labels with full names
    class_labels = load_model.classes_
    class_labels_name = [cancer_names.get(item, item) for item in class_labels]
    # Get the prediction for each cancer type in %
    result = load_model.predict_proba(data)*100
    pred = pd.DataFrame(result, columns=class_labels_name)
    return JsonResponse(pred.to_dict('records')[0], safe=True)
