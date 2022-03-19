from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'auhtor': 'Mateus Alves',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'Março 19, 2022'
    },
    {
        'auhtor': 'Duda Alves',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'Março 18, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
