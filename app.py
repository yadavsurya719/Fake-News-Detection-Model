import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the ML model using pickle
model_path = r'C:/Users/achin/Desktop/real and fake/data.ipynb'
with open('C:/Users/achin/Desktop/real and fake/data.ipynb', 'wb') as model_file:
    pickle.dump(model_path, model_file)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    input_choice = request.form.get('inputChoice')

    if input_choice == 'file':
        # Handle file upload
        uploaded_file = request.files['file']

        # Process the file and make predictions using the ML model
        if uploaded_file:
            # Placeholder code: Read the content of the file
            file_content = uploaded_file.read()

            # Placeholder code: Use your model for prediction
            prediction_result = model.predict([file_content])

            # Return the result to the user (you might want to render a new page or show results on the same page)
            return f"File Upload Result: {prediction_result}"

    elif input_choice == 'manual':
        # Handle manual entry
        news_article = request.form.get('newsArticle')

        # Placeholder code: Use your model for prediction
        prediction_result = model_file.predict([news_article])

        # Return the result to the user (you might want to render a new page or show results on the same page)
        if prediction_result[0] == 0:
            result_message = "The news is likely to be true."
        else:
            result_message = "The news is likely to be fake."

        return f"Manual Entry Result: {result_message}"


if __name__ == '__main__':
    app.run(debug=True)