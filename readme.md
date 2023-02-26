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
knn_model

**Note:** The <model_name> parameter should be consistent with one of the models in saved_models directory

### Request Body
parameter **input:** a 2403*1 array representing lists of data input by user \
take a look at <code>test_data.json</code> as an example.

### Response
A JSON indicating the probability of each cancer type in %

### How to update the trained models
Use <code>knn_tcga_training.ipynb</code> to train a new knn model. \
Replace compressed pickle model files in <code>saved_models</code> directory

