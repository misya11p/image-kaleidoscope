from flask import Flask, render_template, request
import sys; sys.path.insert(0, './modules')
from write_image import write_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kaleidoscope', methods=['POST'])
def kaleidoscope():
    if 'file' in request.files:
        file = request.files['file']
        output_dir = 'static/tmp/'
        filepath = output_dir + 'base.' + file.filename.split('.')[-1]
        file.save(filepath)
        write_image(filepath, output_dir=output_dir)
        name = '1'    
    else:
        name = request.form['name']

    return render_template('kaleidoscope.html', name=name)

if __name__ == '__main__':
    app.run()