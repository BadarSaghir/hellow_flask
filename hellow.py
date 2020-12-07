from flask import Flask

app = Flask(__name__)
print(__name__)


def make_bold(func):
    def decorate(*args):
        return "<b>" + func() + "</b>"

    return decorate


def make_ittlaic(func):
    def decorate(*args):
        return "<i>" + func() + "</i>"

    return decorate


def make_emphais(func):
    def decorate(*args):
        return "<em>" + func() + "</em>"

    return decorate


def make_underline(func):
    def decorate():
        return "<u>" + func() + "</u>"
    return decorate


@app.route('/')
@make_bold
@make_ittlaic
@make_emphais
@make_underline
def hello_world():
    return 'hello World'
#
#
# @app.route('/bye')
# @make_bold
# @make_ittlaic
# @make_emphais
# @make_underline
# def Goodbye():
#     return 'Good bye'


# @make_bold
# @app.route('/<username>')
# def greeting(username):
#     return f"Welcome {username}"


if __name__ == "__main__":
    app.run(debug=True)
