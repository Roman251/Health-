from flask import Flask,request
import numpy as np
import pickle
import flasgger
from flasgger import Swagger


app=Flask(__name__)
Swagger(app)

#Loading all pickel files(models)
model_diabetes=pickle.load(open('pickle_files/diabetes/model_diabetes.pkl','rb'))
model_liver=pickle.load(open('pickle_files/liver/model_liver.pkl','rb'))
model_cancer=pickle.load(open('pickle_files/cancer/model_cancer.pkl','rb'))
model_heart=pickle.load(open('pickle_files/heart/model_heart.pkl','rb'))
model_kidney=pickle.load(open('pickle_files/kidney/model_kidney.pkl','rb'))

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict_diab',methods=["Get"])
def predict_diabetes():
    
    """Let's check if the client has diabetes 
    Input the necessary parameters.
    ---
    parameters:  
      - name: Pregnancies
        in: query
        type: number
        required: true
      - name: Glucose
        in: query
        type: number
        required: true
      - name: BloodPressure
        in: query
        type: number
        required: true
      - name: SkinThickness
        in: query
        type: number
        required: true
      - name: Insulin
        in: query
        type: number
        required: true
      - name: BMI
        in: query
        type: number
        required: true
      - name: DiabetesPedigreeFunction
        in: query
        type: number
        required: true 
      - name: Age
        in: query
        type: number
        required: true  
    responses:
        100:
            description: Your Health
        
    """
    Pregnancies=request.args.get("Pregnancies")
    Glucose=request.args.get("Glucose")
    BloodPressure=request.args.get("BloodPressure")
    SkinThickness=request.args.get("SkinThickness") 
    Insulin=request.args.get("Insulin")
    BMI=request.args.get("BMI")
    DiabetesPedigreeFunction=request.args.get("DiabetesPedigreeFunction")
    Age=request.args.get("Age")  
    prediction=model_diabetes.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])[0]
   
    return str(prediction)


@app.route('/predict_liv',methods=["Get"])
def predict_liver():
    
    """Let's check if the client has liver problems 
    Input the necessary parameters.
    ---
    parameters:  
      - name: Total_Bilirubin
        in: query
        type: number
        required: true
      - name: Alkaline_Phosphotase
        in: query
        type: number
        required: true
      - name: Alamine_Aminotransferase
        in: query
        type: number
        required: true
      - name: Aspartate_Aminotransferase
        in: query
        type: number
        required: true
      - name: Total_Protiens
        in: query
        type: number
        required: true
      - name: Albumin
        in: query
        type: number
        required: true 
      - name: Albumin_and_Globulin_Ratio
        in: query
        type: number
        required: true  
    responses:
        100:
            description: Your Health
        
    """
    Total_Bilirubin=request.args.get("Total_Bilirubin")
    Alkaline_Phosphotase=request.args.get("Alkaline_Phosphotase")
    Alamine_Aminotransferase=request.args.get("Alamine_Aminotransferase") 
    Aspartate_Aminotransferase=request.args.get("Aspartate_Aminotransferase")
    Total_Protiens=request.args.get("Total_Protiens")
    Albumin=request.args.get("Albumin")  
    Albumin_and_Globulin_Ratio=request.args.get("Albumin_and_Globulin_Ratio")
    prediction=model_liver.predict([[ Total_Bilirubin,
       Alkaline_Phosphotase, Alamine_Aminotransferase,
       Aspartate_Aminotransferase, Total_Protiens, Albumin,
       Albumin_and_Globulin_Ratio]])[0]
   
    return str(prediction)



@app.route('/predict_canc',methods=["Get"])
def predict_cancer():
    
    """The diagnosis of breast tissues (M = malignant, B = benign) 
    Input the necessary parameters.
    ---
    parameters:
      - name: radius_mean
        in: query
        type: number
        required: true
      - name: texture_mean
        in: query
        type: number
        required: true
      - name: perimeter_mean
        in: query
        type: number
        required: true
      - name: area_mean
        in: query
        type: number
        required: true
      - name: smoothness_mean
        in: query
        type: number
        required: true
      - name: compactness_mean
        in: query
        type: number
        required: true
      - name: concavity_mean
        in: query
        type: number
        required: true
      - name: concave points_mean
        in: query
        type: number
        required: true
      - name: symmetry_mean
        in: query
        type: number
        required: true
      - name: fractal_dimension_mean
        in: query
        type: number
        required: true
      - name: radius_se
        in: query
        type: number
        required: true
      - name: texture_se
        in: query
        type: number
        required: true
      - name: perimeter_se
        in: query
        type: number
        required: true
      - name: area_se
        in: query
        type: number
        required: true
      - name: smoothness_se
        in: query
        type: number
        required: true
      - name: compactness_se
        in: query
        type: number
        required: true
      - name: concavity_se
        in: query
        type: number
        required: true
      - name: concave points_se
        in: query
        type: number
        required: true
      - name: symmetry_se
        in: query
        type: number
        required: true
    responses:
        100:
            description: Your Health
        
    """
    radius_mean=request.args.get("radius_mean")
    texture_mean=request.args.get("texture_mean")
    perimeter_mean=request.args.get("perimeter_mean")
    area_mean=request.args.get("area_mean")
    smoothness_mean=request.args.get("smoothness_mean")
    compactness_mean=request.args.get("compactness_mean")
    concavity_mean=request.args.get("concavity_mean")
    concavepoints_mean=request.args.get("concavepoints_mean")
    symmetry_mean=request.args.get("symmetry_mean")
    fractal_dimension_mean=request.args.get("fractal_dimension_mean")
    radius_se=request.args.get("radius_se")
    texture_se=request.args.get("texture_se")
    perimeter_se=request.args.get("perimeter_se")
    area_se=request.args.get("area_se")
    smoothness_se=request.args.get("smoothness_se")
    compactness_se=request.args.get("compactness_se")
    concavity_se=request.args.get("concavity_se")
    concavepoints_se=request.args.get("concavepoints_se")
    symmetry_se=request.args.get("symmetry_se")
    fractal_dimension_se=request.args.get("fractal_dimension_se")
    radius_worst=request.args.get("radius_worst")
    texture_worst=request.args.get("texture_worst")
    perimeter_worst=request.args.get("perimeter_worst")
    area_worst=request.args.get("area_worst")
    smoothness_worst=request.args.get("smoothness_worst")
    compactness_worst=request.args.get("compactness_worst")
    concavity_worst=request.args.get("concavity_worst")
    concavepoints_worst=request.args.get("concavepoints_worst")
    symmetry_worst=request.args.get("symmetry_worst")
    fractal_dimension_worst=request.args.get("fractal_dimension_worst")
    prediction=model_cancer.predict([[ radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concavepoints_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concavepoints_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concavepoints_worst,symmetry_worst,fractal_dimension_worst]])[0]
   
    return str(prediction)


@app.route('/predict_kid',methods=["Get"])
def predict_kidney():
    
    """Let's check if the client is healthy 
    Input the necessary parameters.
    ---
    parameters:
      - name: age
        in: query
        type: number
        required: true
      - name: bp
        in: query
        type: number
        required: true
      - name: sg
        in: query
        type: number
        required: true
      - name: al
        in: query
        type: number
        required: true
      - name: su
        in: query
        type: number
        required: true
      - name: pcc
        in: query
        type: number
        required: true
      - name: ba
        in: query
        type: number
        required: true
      - name: bgr
        in: query
        type: number
        required: true
      - name: bu
        in: query
        type: number
        required: true
      - name: sc
        in: query
        type: number
        required: true
      - name: sod
        in: query
        type: number
        required: true
      - name: pot
        in: query
        type: number
        required: true
      - name: hemo
        in: query
        type: number
        required: true
      - name: pcv
        in: query
        type: number
        required: true
      - name: wc
        in: query
        type: number
        required: true
      - name: rc
        in: query
        type: number
        required: true
      - name: dm
        in: query
        type: number
        required: true
      - name: cad
        in: query
        type: number
        required: true
      - name: pe
        in: query
        type: number
        required: true
    responses:
        100:
            description: Your Health
        
    """
    age=request.args.get("age")
    bp=request.args.get("bp")
    sg=request.args.get("sg") 
    al=request.args.get("al")
    su=request.args.get("su")
    pcc=request.args.get("pcc")  
    ba=request.args.get("ba")
    bgr=request.args.get("bgr")
    bu=request.args.get("bu")
    sc=request.args.get("sc")  
    sod=request.args.get("sod")
    pot=request.args.get("pot")
    hemo=request.args.get("hemo")
    pcv=request.args.get("pcv")  
    wc=request.args.get("wc")
    rc=request.args.get("rc")
    dm=request.args.get("dm")
    cad=request.args.get("cad")  
    pe=request.args.get("pe")

    prediction=model_kidney.predict([[ age, bp, sg, al, su, pcc, ba, bgr, bu, sc, sod,
       pot, hemo, pcv, wc, rc, dm, cad, pe]])[0]
   
    return str(prediction)

@app.route('/predict_heart',methods=["Get"])
def predict_heart():
    
    """Let's check if the client is healthy 
    Input the necessary parameters.
    ---
    parameters:
      - name: age
        in: query
        type: number
        required: true
      - name: sex
        in: query
        type: number
        required: true
      - name: cp
        in: query
        type: number
        required: true
      - name: restbp
        in: query
        type: number
        required: true
      - name: chol
        in: query
        type: number
        required: true
      - name: fbs
        in: query
        type: number
        required: true
      - name: restecg
        in: query
        type: number
        required: true
      - name: thalach
        in: query
        type: number
        required: true
      - name: examg
        in: query
        type: number
        required: true
      - name: oldpeak
        in: query
        type: number
        required: true
      - name: slope
        in: query
        type: number
        required: true
      - name: ca
        in: query
        type: number
        required: true
      - name: thal
        in: query
        type: number
        required: true 
    responses:
        100:
            description: Your Health
        
    """
    age=request.args.get("age")
    sex=request.args.get("sex")
    cp=request.args.get("cp")
    restbp=request.args.get("restbp")
    chol=request.args.get("chol")
    fbs=request.args.get("fbs")
    restecg=request.args.get("restecg")
    thalach=request.args.get("thalach")
    examg=request.args.get("examg")
    oldpeak=request.args.get("oldpeak")
    slope=request.args.get("slope")
    ca=request.args.get("ca")
    thal=request.args.get("thal") 
    prediction=model_heart.predict([[age,sex,cp,restbp,chol,fbs,restecg,thalach,examg,oldpeak,slope,ca,thal]])[0]
   
    return str(prediction)


if __name__=='__main__':
    app.run()


#http://127.0.0.1:5000/apidocs/