from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField, RadioField
from wtforms.validators import InputRequired, Email

class AddSnackForm(FlaskForm):
    email = StringField("Email", validators=[Email()])
    name = StringField("Snack Name", validators=[InputRequired(message="Snack Name cant be blank")])
    price = FloatField("Price in USD")
    quantity = IntegerField("How many?")
    is_healthy = BooleanField("This is a healthy snack")

    category = SelectField("Category", choices=[
                            ('ic','Ice Cream'), ('chips','Potato Chips'), ('candy','Candy/Sweets')])


class EmployeeForm(FlaskForm):
    name = StringField("Employee Name", validators=[InputRequired("Name cannot be blank")])
    state = StringField("State")
    dept_code = SelectField("Department Code")