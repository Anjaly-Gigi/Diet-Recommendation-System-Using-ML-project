from flask import Flask, render_template
from forms import NutrientForm  # Ensure the module name is correct
import secrets  # Import the secrets module
import pandas as pd
import joblib  # type: ignore
import sys

# Print the Python path to check if it includes the directory with 'threadpoolctl'
print("Python Path:", sys.path)

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Generates a random secret key

# Load the pre-trained KMeans model and scaler
kmeans_model = joblib.load('kmeans_model_diet.pkl')
scaler = joblib.load('scaler_diet.pkl')


# Load the recipes DataFrame
df = pd.read_csv('recipes_clusters_diet.csv')

def recommend_recipes(nutrient_ranges):
    # Define a mapping for nutrient ranges to numerical values
    nutrient_mapping = {
        'low': 1,
        'medium': 2,
        'high': 3,
        'very high': 4
    }

    # Extract nutrient values from nutrient_ranges dictionary and map to numerical values
    user_nutrients = {
        'Calories': nutrient_mapping.get(nutrient_ranges['Calories']),
        'FatContent': nutrient_mapping.get(nutrient_ranges['FatContent']),
        'CholesterolContent': nutrient_mapping.get(nutrient_ranges['CholesterolContent']),
        'SodiumContent': nutrient_mapping.get(nutrient_ranges['SodiumContent']),
        'CarbohydrateContent': nutrient_mapping.get(nutrient_ranges['CarbohydrateContent']),
        'FiberContent': nutrient_mapping.get(nutrient_ranges['FiberContent']),
        'SugarContent': nutrient_mapping.get(nutrient_ranges['SugarContent']),
        'ProteinContent': nutrient_mapping.get(nutrient_ranges['ProteinContent'])
    }

    # Convert user nutrients to DataFrame with correct column names
    user_nutrients_df = pd.DataFrame([user_nutrients])

    # Scale the user nutrient data
    user_nutrients_scaled = scaler.transform(user_nutrients_df)

    # Predict the cluster for the user input
    cluster_label = kmeans_model.predict(user_nutrients_scaled)[0]

    # Recommend recipes from the predicted cluster
    recommended_recipes = df[df['Cluster'] == cluster_label].sample(n=3)
    return recommended_recipes[['Name', 'Cluster']]

@app.route('/', methods=['GET', 'POST'])
def home():
    form = NutrientForm()  # Create an instance of the form

    if form.validate_on_submit():  # Check if form is submitted and validated
        # Retrieve form data if form is submitted
        nutrient_ranges = {
            'Calories': form.calories.data,
            'FatContent': form.fat_content.data,
            'CholesterolContent': form.cholesterol_content.data,
            'SodiumContent': form.sodium_content.data,
            'CarbohydrateContent': form.carbohydrate_content.data,
            'FiberContent': form.fiber_content.data,
            'SugarContent': form.sugar_content.data,
            'ProteinContent': form.protein_content.data,
        }

        # Recommend recipes based on the nutrient ranges
        recommended_recipes = recommend_recipes(nutrient_ranges)

        # Redirect or process nutrient_ranges further here
        return render_template('recommendation.html', nutrient_ranges=nutrient_ranges, recommended_recipes=recommended_recipes)

    # Pass 'form' to the template context for rendering the form on 'index.html'
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)  # Run the application