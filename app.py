from flask import Flask, render_template, redirect, url_for
from forms import CompanyForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'FLASK0COMPUTER1PROGRAMMING'


# courses_list = [{
#     'title': 'Python 101',
#     'description': 'Learn Python basics',
#     'price': 34,
#     'available': True,
#     'level': 'Beginner'
#     }]
@app.route('/', methods=('GET', 'POST'))
def index():
    form = CompanyForm()
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()
