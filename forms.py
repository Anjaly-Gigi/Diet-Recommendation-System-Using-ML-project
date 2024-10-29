from flask_wtf import FlaskForm # type: ignore
from wtforms import SelectField, SubmitField # type: ignore

class NutrientForm(FlaskForm):
    calories = SelectField('Calories', choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('very high', 'Very High')])
    fat_content = SelectField('Fat Content', choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('very high', 'Very High')])
    cholesterol_content = SelectField('Cholesterol Content', choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('very high', 'Very High')])
    sodium_content = SelectField('Sodium Content', choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('very high', 'Very High')])
    carbohydrate_content = SelectField('Carbohydrate Content', choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('very high', 'Very High')])
    fiber_content = SelectField('Fiber Content', choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('very high', 'Very High')])
    sugar_content = SelectField('Sugar Content', choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('very high', 'Very High')])
    protein_content = SelectField('Protein Content', choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('very high', 'Very High')])
    
    submit = SubmitField('Submit')


