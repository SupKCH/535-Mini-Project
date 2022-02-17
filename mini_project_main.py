import mini_project_half
from mini_project_half import QR_condition_control, camera_main, camera_alternative
from flask import Flask, render_template, request
import multiprocessing as mp

template_filename = "trial_1.html"
    
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('BS') == 'backwardStop':
            QR_condition_control('backwardStop')
            print("backwardStop")
        elif  request.form.get('FS') == 'forwardStop':
            QR_condition_control('forwardStop')
            print("forwardStop")
        elif  request.form.get('C') == 'center':
            QR_condition_control('center')
            print("center")
            
    elif request.method == 'GET':
        print("No Post Back Call")
        
    return render_template(template_filename)

if __name__ == '__main__':
    process_1 = mp.Process(target=camera_alternative)
    process_1.start()
    app.run(debug=True, use_reloader=False)
    #app.run(host="0.0.0.0", debug=True, use_reloader=False)
    