from operator import itemgetter
import cv2
import numpy
import os
from base64 import b64encode

class Predict:
    def __init__(self, classesDict, model, dictionar):
        self.classesDict = classesDict
        self.model = model
        self.dictionar = dictionar
        self.surf = cv2.xfeatures2d.SURF_create()
        self.bowDiction = cv2.BOWImgDescriptorExtractor(self.surf, cv2.BFMatcher(cv2.NORM_L2))
        self.bowDiction.setVocabulary(self.dictionar)

    def adjust_size(self, image, size=1.0):
        return cv2.resize(image, (0, 0), fx=size, fy=size)

    def feature_extract(self, img):
        return self.bowDiction.compute(img, self.surf.detect(img))

    def predictionIMG_proba(self, x_test):
        return self.model.predict_proba(numpy.reshape(x_test, (1, len(x_test[0]))))

    def getClassName(self, cl):
        for cls in self.classesDict:
            if self.classesDict[cls] == cl:
                return cls
        return 'no-logo'

    def get_img_match(self, img1, img2_path, matches_number):
        image1 = img1
        image2 = cv2.imread(img2_path)
        try:
            height1, width1 = image1.shape
            height2, width2 = image2.shape
        except Exception:
            height1, width1, _ = image1.shape
            height2, width2, _ = image2.shape

        if height1 < 400 or height2 < 400:
            if height1 < height2:
                width2 = int(width2 * height1 / height2)
                height2 = height1
                image2 = cv2.resize(image2, (int(width2), int(height2)))
            else:
                width1 = int(width1 * height2 / height1)
                height1 = height2
                image1 = cv2.resize(image1, (int(width1), int(height1)))
        else:
            width1 = 400 * width1 / height1
            width2 = 400 * width2 / height2
            image1 = cv2.resize(image1, (int(width1), 400))
            image2 = cv2.resize(image2, (int(width2), 400))

        def to_gray(color_img):
            gray = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
            return gray

        image1_gray = to_gray(image1)
        image2_gray = to_gray(image2)

        def gen_surf_features(gray_img):
            surf = cv2.xfeatures2d.SURF_create()
            kp, desc = surf.detectAndCompute(gray_img, None)
            return kp, desc

        # generate SURF keypoints and descriptors
        image1_kp, image1_desc = gen_surf_features(image1_gray)
        image2_kp, image2_desc = gen_surf_features(image2_gray)

        bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

        matches = bf.match(image2_desc, image1_desc)

        # Sort the matches in the order of their distance.
        matches = sorted(matches, key=lambda x: x.distance)

        # draw the top N matches
        N_MATCHES = matches_number

        match_img = cv2.drawMatches(
            image2, image2_kp,
            image1, image1_kp,
            matches[:N_MATCHES], image1.copy(), flags=2)

        return match_img, len(image1_desc), len(matches)

    def showPrediction(self):
        for i in range(len(self.classesDict)):
            self.prediction_prob[i] = [self.prediction_prob[i], self.getClassName(i)]
        top4 = sorted(self.prediction_prob, key=itemgetter(0), reverse=True)[:4]
        return top4

    def getJson(self, img):
        features = self.feature_extract(img)
        prediction_prob = self.predictionIMG_proba(features)
        self.prediction_prob = [int(float('{0:.20f}'.format(prediction_prob[0][i]))*100) for i in range(len(prediction_prob[0]))]
        toppredicts = self.showPrediction()
        predict_json = {}
        index = 0
        for predict in toppredicts:
            index += 1
            predict_json[index] = [predict[1], predict[0]]
            path = os.path.join('static\\img\\dataset\\'+predict[1], predict[1]+'.png')
            predict_json[index].append(path)
            img_match, img_desc, match_desc = self.get_img_match(img, path, 10)
            img_match = self.adjust_size(img_match, 2.0)
            img_match = b64encode(cv2.imencode(img=img_match, ext='.png')[1].reshape((len(cv2.imencode(img=img_match, ext='.png')[1]))).tobytes()).decode('utf-8')
            predict_json[index].append(img_match)
            predict_json[index].append(img_desc)
            predict_json[index].append(match_desc)
        return predict_json