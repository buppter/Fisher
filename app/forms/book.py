from wtforms import Form, StringField


class SearchForm(Form):
    q = StringField()
