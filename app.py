import argparse
import os
import matplotlib.pyplot as plt
import sys
import gradio as gr
import torch
import pandas as pd
import numpy as np
import io
import base64
from lime.lime_tabular import LimeTabularExplainer
from pycaret.classification import *
import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="torch.storage")

from util import load_data_and_prepare
import view


       
def parse_args(args):
    parser = argparse.ArgumentParser(description="CBD Classification")
    parser.add_argument('--data_dir', type=str, default="./data/")
    parser.add_argument('--excel_file', type=str, default="DUMC_final.csv")
    parser.add_argument('--mode', type=str, default="train")
    parser.add_argument('--scale', type=bool, default=True)
    parser.add_argument('--smote', type=bool, default=True)
    parser.add_argument('--model_name_or_path', type=str, default="./data/model", choices=[])

    return parser.parse_args(args)



# Inference function
def classify(tabular_data):
    
    try:
        # Ensure tabular_data is a 2D list and extract the first row
        if isinstance(tabular_data, list) and isinstance(tabular_data[0], list):
            tabular_data = tabular_data[0] # Extract the first row
        else:
            raise ValueError("Input data is not in the expected 2D list format.")
 
        # Convert input data to a pandas DataFrame
        input_data = pd.DataFrame([tabular_data], columns= tabular_header)
        print(f"Original Input DataFrame:\n{input_data}")

        # Use PyCaret's predict_model to make predictions
        prediction = predict_model(model, data=input_data)
 
        # Extract predicted class and probability
        predicted_class = prediction.loc[0, "prediction_label"]
        class_probability = prediction.loc[0, "prediction_score"]

        # Generate appropriate output based on the prediction and probability
        if class_probability < 0.34:
            result = (
                f"This analysis estimates a low probability ({class_probability:.2f}) of a common bile duct stone. "
                 "Please consult a medical professional for final diagnosis."
            )
        elif 0.34 <= class_probability < 0.67:
            result = (
                f"Based on the provided data, this tool estimates an intermediate probability ({class_probability:.2f}) "
                "of a common bile duct stone. Further medical review is recommended."
            )
        else: # class_probability >= 0.67
            result = (
                f"Based on the provided data, this tool estimates a high probability ({class_probability:.2f}) "
                "of a common bile duct stone. Further medical review is necessary."
            )

        return result

    except Exception as e:
        return f"An error occurred during classification: {str(e)}"

# Inference function
def predict_proba_fn(instance):
    """
    PyCaret의 predict_model을 활용한 확률 예측 함수.
    """
    # 2D 형태로 변환
    if instance.ndim == 1:
        instance = instance.reshape(1, -1)
    
    # DataFrame으로 변환
    instance_df = pd.DataFrame(instance, columns=train.columns)
    
    # predict_model을 통해 예측 수행
    predictions = predict_model(model, data=instance_df)
    
    # prediction_label이 1이면 prediction_score, 0이면 1-prediction_score
    predictions['class_1_prob'] = np.where(predictions['prediction_label'] == 1, 
                                            predictions['prediction_score'], 
                                            0)
    
    predictions['class_0_prob'] = np.where(predictions['prediction_label'] == 0, 
                                            predictions['prediction_score'], 
                                            0)
    
    # class_0_prob와 class_1_prob 반환
    return predictions[['class_0_prob', 'class_1_prob']].values


# def explain_with_lime(tabular_data):
#     instance = np.array(tabular_data[0],dtype='float')
    
#     # Create an explainer instance for classification
#     explainer = LimeTabularExplainer(
#         training_data=train.values,  # Use your training data
#         feature_names=tabular_header,
#         class_names=['intermediate', 'High'],  # Replace with actual class names
#         mode='classification'
#     )

#     # LIME expects a 2D numpy array or DataFrame for input, and we need to provide the correct number of features
#     explanation = explainer.explain_instance(
#         instance,  # Single instance (first row of the tabular data)
#         predict_proba_fn,  # The prediction function
#         num_features=len(tabular_header)  # Number of features to display in the explanation
#     )
    
#     # Plot LIME explanation
#     fig = explanation.as_pyplot_figure()
#     fig.set_size_inches(25, 8) 
#     buf = io.BytesIO()
#     fig.savefig(buf, format='png')
#     buf.seek(0)
#     encoded_image = base64.b64encode(buf.read()).decode('utf-8')
#     buf.close()
#     plt.close(fig)
    
#     return f"<img src='data:image/png;base64,{encoded_image}'/>"

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    train = load_data_and_prepare(args.data_dir, args.excel_file, args.mode, args.scale, args.smote)
    model = load_model(args.model_name_or_path)
    examples = view.examples
    description = view.description
    title_markdown = view.title_markdown
    tabular_header = view.tabular_header
    tabular_dtype = ['number'] * len(tabular_header)


    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown(title_markdown)
        gr.Markdown(description)
        with gr.Row():
            with gr.Column():
                tabular_input = gr.Dataframe(headers= tabular_header, datatype= tabular_dtype, label="Tabular Input", type="array", interactive=True, row_count=1, col_count=11)
                info = gr.Textbox(lines=1, label="Patient info", visible = False)

                with gr.Accordion("Parameters", open=False) as parameter_row:
                    temperature = gr.Slider(minimum=0.0, maximum=1.0, value=0.2, step=0.1, interactive=True,
                                            label="Temperature", )
                    top_p = gr.Slider(minimum=0.0, maximum=1.0, value=0.4, step=0.1, interactive=True, label="Top P", )
                    
                with gr.Row():
                    # btn_c = gr.ClearButton([tabular_input])
                    btn_c = gr.Button("Clear")
                    btn = gr.Button("Run")
                    
    

        
        result_output = gr.Textbox(lines=2, label="Classification Result")
        lime_output = gr.HTML(label="LIME Explanation")
        gr.Examples(examples=examples, inputs=[tabular_input, info])
        btn.click(fn=classify, inputs=tabular_input, outputs=result_output)
        # btn.click(fn=explain_with_lime, inputs=tabular_input, outputs=lime_output)  # Add LIME button    
    
        # Clear functionality: resets inputs and outputs
        def clear_fields():
            return None, None, [[None] * len(tabular_header)]

        btn_c.click(fn=clear_fields, inputs=[], outputs=[result_output, lime_output, tabular_input])


    demo.queue()
    demo.launch(share=True)

