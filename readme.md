# TCGA cancer prediction Machine Learning Models and API
This project is developed with [Django Rest Framework](https://www.django-rest-framework.org/) \
The dataset and KNN algorithm inspired by [tumor-origin github](https://github.com/programmingprincess/tumor-origin/) \
API inspired by [Heart Disease Machine Learning API](https://github.com/HaomingJue/heart-disease-ml-api/)
### To install the dpendencies
<code>pip install -r requirements.txt</code>
### To start the server locally (localhost:8000)
<code>python manage.py runserver</code>

## API
API URL Pattern \
<code>[post] <deploy_url>/ml/<model_name></code> \
If you run the project locally, the default url should be http://localhost:8000

**Current Deploy Link:** https://tcgacancerapi.herokuapp.com \
eg: To apply ml prediction with KNN model, use <code>Post</code> method to call <code>https://tcgacancerapi.herokuapp.com/ml/knn_model</code> \
Please  include the Request Body following below guidance.

### Valid <model_name>
knn_model\
mlp_model

**Note:** The <model_name> parameter should be consistent with one of the models in saved_models directory

### Request Body (knn_model)
parameter **input:** a 2403*1 array representing lists of data input by user \
take a look at <code>test_data_knn.json</code> as an example.

### Request Body (mlp_model)
parameter **input:** a 154*1 array representing lists of data input by user \
take a look at <code>test_data_mlp.json</code> as an example.

### Response
A JSON indicating the probability of each cancer type in %:
```json
{
    "Bladder": 0.0,
    "Breast": 0.0,
    "Bile duct": 0.0,
    "Colon": 0.0,
    "Esophagus": 0.0,
    "Head and neck": 0.0,
    "Kidney chromophobe": 0.0,
    "Kidney renal clear cell": 0.0,
    "Liver": 0.0,
    "Lung": 0.0,
    "Ovary": 0.0,
    "Pancreas": 0.0,
    "Prostate": 100.0,
    "Skin melanoma": 0.0,
    "Stomach": 0.0,
    "Thyroid": 0.0,
    "Uterus": 0.0
}
```
### How to update the trained models
Use <code>knn_tcga_training.ipynb</code> to train a new knn model. \
Use <code>mlp_tcga_training.ipynb</code> to train a new deep mlp model. \
Replace compressed pickle model files in <code>saved_models</code> directory

