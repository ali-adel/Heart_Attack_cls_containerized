from fastapi import FastAPI, Request, HTTPException
from tensorflow.keras.models import load_model



heart_model = load_model('ANN.h5')

app = FastAPI()

@app.get("/")
async def my_pred():
    return "Testing"


@app.post("/Heart_Prediction")
async def my_pred(request: Request):
    try:
        form_data = await request.form()
        age = float(form_data["age"])
        gender = float(form_data["gender"])  # Convert gender to float
        impulse = float(form_data["impluse"])
        pressure_high = float(form_data["pressurehight"])
        pressure_low = float(form_data["pressurelow"])
        glucose = float(form_data["glucose"])
        potassium = float(form_data["kcm"])
        troponin = float(form_data["troponin"])

        input_list = [age, gender, impulse, pressure_high, pressure_low, glucose, potassium, troponin]

        # Now you can use the input_list for predictions with your model
        predictions = heart_model.predict([input_list])

        if predictions[0] == 0:
            return "The patient does not have heart problems"
        else:
            return "The patient has heart problems"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))