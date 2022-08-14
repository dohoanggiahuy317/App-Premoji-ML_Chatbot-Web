import re
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer


class MLEmoPredict:
    emotions = ["joy", 'fear', "anger", "sadness", "disgust", "shame", "guilt"]
    emoji_dict = {"joy": "😂", "fear": "😱", "anger": "😠", "sadness": "😢", "disgust": "😒", "shame": "😳",
                  "guilt": "😳"}

    clifs = []
    highestModel = None
    vectorizer = None

    def __init__(self):
        file = 'MLEmojiDetectionBot/dataEmojiBot.txt'
        data = self.read_data(file)
        self.trainingModel(data)

    def read_data(self, file):
        data = []
        with open(file, 'r') as f:
            for line in f:
                line = line.strip()
                label = ' '.join(line[1:line.find("]")].strip().split())
                text = line[line.find("]") + 1:].strip()
                data.append([label, text])
        return data

    def ngram(self, token, n):
        output = []
        for i in range(n - 1, len(token)):
            ngram = ' '.join(token[i - n + 1:i + 1])
            output.append(ngram)
        return output

    def create_feature(self, text, nrange=(1, 1)):
        text_features = []
        text = text.lower()
        text_alphanum = re.sub('[^a-z0-9#]', ' ', text)
        for n in range(nrange[0], nrange[1] + 1):
            text_features += self.ngram(text_alphanum.split(), n)
        text_punc = re.sub('[a-z0-9]', ' ', text)
        text_features += self.ngram(text_punc.split(), 1)
        return Counter(text_features)

    def convert_label(self, item, name):
        items = list(map(float, item.split()))
        label = ""
        for idx in range(len(items)):
            if items[idx] == 1:
                label += name[idx] + " "

        return label.strip()

    def train_test(self, clf, X_train, X_test, y_train, y_test):
        clf.fit(X_train, y_train)
        train_acc = accuracy_score(y_train, clf.predict(X_train))
        test_acc = accuracy_score(y_test, clf.predict(X_test))
        return train_acc, test_acc

    def trainingModel(self, data):
        X_all = []
        y_all = []

        for label, text in data:
            y_all.append(self.convert_label(label, self.emotions))
            X_all.append(self.create_feature(text, nrange=(1, 4)))

        X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size=0.2, random_state=123)

        vectorizer = DictVectorizer(sparse=True)

        X_train = vectorizer.fit_transform(X_train)
        X_test = vectorizer.transform(X_test)
        self.vectorizer = vectorizer

        # ---------------------------------------------------------------------------------------------------------------
        svc = SVC()
        lsvc = LinearSVC(random_state=123)
        rforest = RandomForestClassifier(random_state=123)
        dtree = DecisionTreeClassifier()

        self.clifs = [svc, lsvc, rforest, dtree]
        # self.clifs = [dtree]
        # ---------------------------------------------------------------------------------------------------------------

        print("Training.....")
        highestAcc = 0
        for clf in self.clifs:
            clf_name = clf.__class__.__name__
            train_acc, test_acc = self.train_test(clf, X_train, X_test, y_train, y_test)
            # Iprint(clf_name, test_acc)
            if test_acc > highestAcc:
                highestAcc = test_acc
                self.highestModel = clf

        # print(self.highestModel)
        l = ["joy", 'fear', "anger", "sadness", "disgust", "shame", "guilt"]
        l.sort()
        label_freq = {}
        for label, _ in data:
            label_freq[label] = label_freq.get(label, 0) + 1

    def predictResponse(self, text):
        features = self.create_feature(text, nrange=(1, 4))
        features = self.vectorizer.transform(features)
        prediction = self.highestModel.predict(features)[0]

        emoji = self.emoji_dict[prediction]
        return {"emoji": emoji, "feeling": prediction}

    def getResponse(self, text):
        ans = self.predictResponse(text)
        return str("<div class='botText'><div>I think your feeling is: " + ans["feeling"] + " " + ans["emoji"]+"</div></div>")

