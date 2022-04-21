from flask import Flask,request #get and post
import pandas as pd
import numpy as np
import pickle


#start of the app
app=Flask(__name__)

pickle_in=open('classifier.pkl','rb') #open pickle file in read byte mode
classifier=pickle.load(pickle_in) #load classifier from pickle file


@app.route('/')
def welcome():
    return 'Is your bank note fake? Lets find out'

@app.route('/predict')
def predictnote():
    #variance 	skewness 	curtosis 	entropy
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return'predicted value'+str(prediction) 

@app.route('/predict_file',methods=['POST'])
def predictnote_file():
    df=pd.read_csv(request.files.get('file'))
    prediction=classifier.predict(df)
    
    #variance 	skewness 	curtosis 	entropy
    # variance=request.args.get('variance')
    # skewness=request.args.get('skewness')
    # curtosis=request.args.get('curtosis')
    # entropy=request.args.get('entropy')
    # prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return'predicted value'+str([prediction]) 




if __name__=='__main__':
    app.run()