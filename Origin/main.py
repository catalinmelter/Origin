from flask import Flask, render_template, request, jsonify
import cv2, numpy, DataManage, ClassManage, PredictLogo

#init
app = Flask(__name__)
#classes
clmng = ClassManage.Classes()
#data manage
datamng = DataManage.DataManage()

#first page
@app.route('/')
def index():
    return render_template('index.html', images=clmng.classes)

#upload page
@app.route('/upload', methods = ['POST'])
def upload():
    try:
        image = request.files['image'].read()
        image = numpy.fromstring(image, numpy.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)
        try:
            height, width = image.shape
        except Exception:
            height, width, _ = image.shape
        if height > 280 or width > 280:
            if height > width:
                width = int(280 * width / height)
                image = cv2.resize(image, (int(width), 280))
            else:
                height = int(280 * height / width)
                image = cv2.resize(image, (280, int(height)))

        result = predictImg(image)
        return jsonify(result=result)
    except Exception:
        return jsonify(result=False)

#predict function with NN
def predictImg(img):
    model = datamng.loadModel('static\\model\\model.h5')
    dictionar = datamng.loadDataNp('static\\data\\dictionar.npy')

    prediction = PredictLogo.Predict(classesDict=clmng.classesDictionar, model=model, dictionar=dictionar)
    result = prediction.getJson(img=img)
    return result

#run at port 4500
if __name__ == '__main__':
    app.run(port=4500, debug=True)
