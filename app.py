import numpy as np
from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

app = Flask(__name__)
# read our pickle file and label LR Ngram (1, 4) as model
model = pickle.load(open('model1_4.pkl', 'rb'))
# read our pickle file and label LR Ngram (2, 4) as model2
model2 = pickle.load(open('model2_4.pkl', 'rb'))
# # read our pickle file and label LSVM Ngram (1, 4) as model
# model = pickle.load(open('lsvmmodel1_4.pkl', 'rb'))
# # read our pickle file and label LSVM Ngram (2, 4) as model2
# model2 = pickle.load(open('lsvmmodel2_4.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/algorithms')
def algorithms():
    return render_template('algorithms.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

import os
from flask import send_from_directory

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/predict',methods=['POST','GET'])
def predict():
    
    ## Ngram (1, 4)
    prediction = model.predict(request.form.values())
    
    # Output Confidence scores
    probability_class_GO = model.predict_proba(request.form.values())[:, 0]
    probability_class_UA = model.predict_proba(request.form.values())[:, 1]
    probability_class_UC = model.predict_proba(request.form.values())[:, 2]
    
    
    ## Ngram (2, 4)
    prediction2 = model2.predict(request.form.values())
    
    # Output Confidence scores
    probability_class_GO2 = model2.predict_proba(request.form.values())[:, 0]
    probability_class_UA2 = model2.predict_proba(request.form.values())[:, 1]
    probability_class_UC2 = model2.predict_proba(request.form.values())[:, 2]
    
    try:
        # P00
        if probability_class_GO[0]==0.08765182261021813 or probability_class_UA[0]==0.1355507998162925 or probability_class_UC[0]==0.7767973775734893:
            if probability_class_GO2[0]==0.08765182261021813 or probability_class_UA2[0]==0.1355507998162925 or probability_class_UC2[0]==0.7767973775734893:
                return render_template('demo.html',
                                    inp='Input: {}'.format(request.form.to_dict(flat=True)['Safety Observation']),
                                    prediction_text='---> This is an Invalid Input. Please try again.',
                                    prediction_text2='---> This is an Invalid Input. Please try again.',
                                    )
            elif prediction2==0:
                return render_template('demo.html',
                                    inp='Input: {}'.format(request.form.to_dict(flat=True)['Safety Observation']),
                                    prediction_text='---> This is an Invalid Input. Please try again.',
                                    prediction_text2='---> This is a Good Observation!\n The Prediction Confidence for each class are-\n GO: {},\n UA: {},\n UC: {}'.format(probability_class_GO2[0], probability_class_UA2[0],probability_class_UC2[0])
                                    )
            elif prediction2==1:
                return render_template('demo.html',
                                    inp='Input: {}'.format(request.form.to_dict(flat=True)['Safety Observation']),
                                    prediction_text='---> This is an Invalid Input. Please try again.',
                                    prediction_text2='---> This is an Unsafe Act !!\nThe Prediction Confidence for each class are- \n     GO: {}, UA: {}, UC: {}'.format(probability_class_GO2[0], probability_class_UA2[0],probability_class_UC2[0])
                                    )
            elif prediction2==2:
                return render_template('demo.html',
                                    inp='Input: {}'.format(request.form.to_dict(flat=True)['Safety Observation']),
                                    prediction_text='---> This is an Invalid Input. Please try again.',
                                    prediction_text2='---> This is an Unsafe Condition !!\nThe Prediction Confidence for each class are- \n GO: {}, UA: {}, UC: {}'.format(probability_class_GO2[0], probability_class_UA2[0],probability_class_UC2[0])
                                    )
            
        # P0    
        elif prediction[0]==0:
            if probability_class_GO2[0]==0.08765182261021813 or probability_class_UA2[0]==0.1355507998162925 or probability_class_UC2[0]==0.7767973775734893:
                return render_template('demo.html',
                                    inp='Input: {}'.format(request.form.to_dict(flat=True)['Safety Observation']),
                                    prediction_text='---> This is a Good Observation!\n The Prediction Confidence for each class are-\n GO: {},\n UA: {},\n UC: {}'.format(probability_class_GO[0], probability_class_UA[0],probability_class_UC[0]),
                                    prediction_text2='---> This is an Invalid Input. Please try again.',
                                        )
            elif prediction2[0]==0:
                return render_template('demo.html',
                                    inp='Input: {}'.format(request.form.to_dict(flat=True)['Safety Observation']),
                                    prediction_text='---> This is a Good Observation!\n The Prediction Confidence for each class are-\n GO: {},\n UA: {},\n UC: {}'.format(probability_class_GO[0], probability_class_UA[0],probability_class_UC[0]),
                                    prediction_text2='---> This is a Good Observation!\n The Prediction Confidence for each class are-\n GO: {},\n UA: {},\n UC: {}'.format(probability_class_GO2[0], probability_class_UA2[0],probability_class_UC2[0])
                                    )
            elif prediction2[0]==1:
                return render_template('demo.html',
                                    inp='Input: {}'.format(request.form.to_dict(flat=True)['Safety Observation']),
                                    prediction_text='---> This is a Good Observation!\n The Prediction Confidence for each class are-\n GO: {},\n UA: {},\n UC: {}'.format(probability_class_GO[0], probability_class_UA[0],probability_class_UC[0]),
                                    prediction_text2='---> This is an Unsafe Act !!\nThe Prediction Confidence for each class are- \n     GO: {}, UA: {}, UC: {}'.format(probability_class_GO2[0], probability_class_UA2[0],probability_class_UC2[0])
                                    )
            elif prediction2[0]==2:
                return render_template('demo.html',
                                    inp='Input: {}'.format(request.form.to_dict(flat=True)['Safety Observation']),
                                    prediction_text='---> This is a Good Observation!\n The Prediction Confidence for each class are-\n GO: {},\n UA: {},\n UC: {}'.format(probability_class_GO[0], probability_class_UA[0],probability_class_UC[0]),
                                    prediction_text2='---> This is an Unsafe Condition !!\nThe Prediction Confidence for each class are- \n GO: {}, UA: {}, UC: {}'.format(probability_class_GO2[0], probability_class_UA2[0],probability_class_UC2[0])
                                    )

        
        # P1
        elif prediction[0]==1:
            if probability_class_GO2[0]==0.08765182261021813 or probability_class_UA2[0]==0.1355507998162925 or probability_class_UC2[0]==0.7767973775734893:
                return render_template('demo.html',
                                    inp='Input: {}'.format(request.form.to_dict(flat=True)['Safety Observation']),
                                    prediction_text='---> This is an Unsafe Act !!\nThe Prediction Confidence for each class are- \n     GO: {}, UA: {}, UC: {}'.format(probability_class_GO[0], probability_class_UA[0],probability_class_UC[0]),
                                    prediction_text2='---> This is an Invalid Input. Please try again.',
                                        )
            elif prediction2[0]==0:
                return render_template('demo.html',
                                    inp='Input: {}'.format(request.form.to_dict(flat=True)['Safety Observation']),
                                    prediction_text='---> This is an Unsafe Act !!\nThe Prediction Confidence for each class are- \n     GO: {}, UA: {}, UC: {}'.format(probability_class_GO[0], probability_class_UA[0],probability_class_UC[0]),
                                    prediction_text2='---> This is a Good Observation!\n The Prediction Confidence for each class are-\n GO: {},\n UA: {},\n UC: {}'.format(probability_class_GO2[0], probability_class_UA2[0],probability_class_UC2[0])
                                    )
            elif prediction2[0]==1:
                return render_template('demo.html',
                                    inp='Input: {}'.format(request.form.to_dict(flat=True)['Safety Observation']),
                                    prediction_text='---> This is an Unsafe Act !!\nThe Prediction Confidence for each class are- \n     GO: {}, UA: {}, UC: {}'.format(probability_class_GO[0], probability_class_UA[0],probability_class_UC[0]),
                                    prediction_text2='---> This is an Unsafe Act !!\nThe Prediction Confidence for each class are- \n     GO: {}, UA: {}, UC: {}'.format(probability_class_GO2[0], probability_class_UA2[0],probability_class_UC2[0])
                                    )
            elif prediction2[0]==2:
                return render_template('demo.html',
                                    inp='Input: {}'.format(request.form.to_dict(flat=True)['Safety Observation']),
                                    prediction_text='---> This is an Unsafe Act !!\nThe Prediction Confidence for each class are- \n     GO: {}, UA: {}, UC: {}'.format(probability_class_GO[0], probability_class_UA[0],probability_class_UC[0]),
                                    prediction_text2='---> This is an Unsafe Condition !!\nThe Prediction Confidence for each class are- \n GO: {}, UA: {}, UC: {}'.format(probability_class_GO2[0], probability_class_UA2[0],probability_class_UC2[0])
                                    )

        
        # P2
        elif prediction[0]==2:
            if probability_class_GO2[0]==0.08765182261021813 or probability_class_UA2[0]==0.1355507998162925 or probability_class_UC2[0]==0.7767973775734893:
                return render_template('demo.html',
                                    inp='Input: {}'.format(request.form.to_dict(flat=True)['Safety Observation']),
                                    prediction_text='---> This is an Unsafe Condition !!\nThe Prediction Confidence for each class are- \n GO: {}, UA: {}, UC: {}'.format(probability_class_GO[0], probability_class_UA[0],probability_class_UC[0]),
                                    prediction_text2='---> This is an Invalid Input. Please try again.',
                                        )
            elif prediction2[0]==0:
                return render_template('demo.html',
                                    inp='Input: {}'.format(request.form.to_dict(flat=True)['Safety Observation']),
                                    prediction_text='---> This is an Unsafe Condition !!\nThe Prediction Confidence for each class are- \n GO: {}, UA: {}, UC: {}'.format(probability_class_GO[0], probability_class_UA[0],probability_class_UC[0]),
                                    prediction_text2='---> This is a Good Observation!\n The Prediction Confidence for each class are-\n GO: {},\n UA: {},\n UC: {}'.format(probability_class_GO2[0], probability_class_UA2[0],probability_class_UC2[0])
                                    )
            elif prediction2[0]==1:
                return render_template('demo.html',
                                    inp='Input: {}'.format(request.form.to_dict(flat=True)['Safety Observation']),
                                    prediction_text='---> This is an Unsafe Condition !!\nThe Prediction Confidence for each class are- \n GO: {}, UA: {}, UC: {}'.format(probability_class_GO[0], probability_class_UA[0],probability_class_UC[0]),
                                    prediction_text2='---> This is an Unsafe Act !!\nThe Prediction Confidence for each class are- \n     GO: {}, UA: {}, UC: {}'.format(probability_class_GO2[0], probability_class_UA2[0],probability_class_UC2[0])
                                    )
            elif prediction2[0]==2:
                return render_template('demo.html',
                                    inp='Input: {}'.format(request.form.to_dict(flat=True)['Safety Observation']),
                                    prediction_text='---> This is an Unsafe Condition !!\nThe Prediction Confidence for each class are- \n GO: {}, UA: {}, UC: {}'.format(probability_class_GO[0], probability_class_UA[0],probability_class_UC[0]),
                                    prediction_text2='---> This is an Unsafe Condition !!\nThe Prediction Confidence for each class are- \n GO: {}, UA: {}, UC: {}'.format(probability_class_GO2[0], probability_class_UA2[0],probability_class_UC2[0])
                                    )
    except:
        return render_template('demo.html',
                                    inp='Input: {}'.format(request.form.to_dict(flat=True)['Safety Observation']),
                                    prediction_text='---> This is an Invalid Input. Please try again.',
                                    prediction_text2='---> This is an Invalid Input. Please try again.',
                                    )

        

if __name__ == "__main__":
    app.run(debug=True)
