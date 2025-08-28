import gradio as gr
import numpy as np
import pickle

model = pickle.load(open('model.pkl','rb'))

label_map = {0:'No Rain',1:'Rain'}

def predict_rain(Temperature,Humidity,Wind_Speed,Pressure):
    input_data=np.array([[Temperature,Humidity,Wind_Speed,Pressure]])
    pred_num=model.predict(input_data)[0]
    return label_map[pred_num]
iface = gr.Interface(
    fn=predict_rain,
    inputs=[
        gr.Number(label='Temperature'),
        gr.Number(label='Humidity'),
        gr.Number(label='Wind Speed'),
        gr.Number(label='Pressure')
    ],
    outputs=gr.Textbox(label="Predicted Tomorrow Rain or Not:"),
    title="Rain Prediction",
)

iface.launch()
