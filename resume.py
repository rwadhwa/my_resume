from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/courses')
def courses():
    courses = [
        ['Misy350', 'Web Application Development',
           'Learning web development, using full stack coding'],
        ['MISY330', 'Database Design & Implementation',
            'Learning access and sql databases'],
        ['BUAD306', 'Intro to Marketing',
           'Learn Fundamental Marketing Concepts'],
        ['Buad309', 'Intro to Organizational Behavior',
            'Examines individual, group, and organizational determinants of work behavior in organizations.']
    ]
    return render_template('courses.html', courses=courses)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
