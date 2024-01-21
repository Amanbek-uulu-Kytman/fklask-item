from flask_wtf import FlaskForm
from wtforms import (SubmitField, StringField, IntegerField,
                     SelectField, DateField, validators)
from wtforms.validators import DataRequired, ValidationError

from .models import Item


class DeleteItemForm(FlaskForm):
    submit = SubmitField('Delete')

class ItemForm(FlaskForm):
    name = StringField(label='Название товара', validators=[DataRequired()])
    price = IntegerField(label='Цена товара', validators=[DataRequired()])
    submit = SubmitField(label='Сохранить товар')

    def validate_price(self, price):
        if price.data < 100:
            raise ValidationError('Товар неможет стоить менее 100 едениц ')


class PurchaseForm(FlaskForm):
    name = StringField(label='Имя клиента')
    age = IntegerField(label='возраст')
    item_id = SelectField(label='Что купил')
    date_purchase = DateField('Дата')
    submit = SubmitField(label='Сохранить покупку')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        result = []
        for item in Item.query.all():
            result.append((item.id, item.name))
        self.item_id.choices = result

    def validate_age(self, age):
        if age.data < 18:
            raise ValidationError('Лицам младше 18 лет, продажа запрещена!')
