import pickle
pickle_out=open('file.pkl','wb') # make and open file in write byter mode
pickle.dump(model,pickle_out) # dump the model into pickle file
pickle_out.close()# must close write mode
