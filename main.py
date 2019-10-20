# main file

import nltk
from format import buildData
from utils import SO_objects as SO
import numpy as np
import utils.transform as transform
from sklearn import model_selection
from sklearn.linear_model import LinearRegression as LR
from nltk.classify.naivebayes import NaiveBayesClassifier
from nltk.classify import accuracy
import pickle


""" 1. Import and clean training data """

domain = 'cooking'
querry, posts, comments = buildData('data/{}.stackexchange.com'.format(domain))

pickle.dump(querry, open('pickles/querry.p', 'wb'))
pickle.dump(posts, open('pickles/posts.p', 'wb'))
pickle.dump(comments, open('pickles/comments.p', 'wb'))

querry = pickle.load(open('pickles/querry.p', 'rb'))
posts = pickle.load(open('pickles/posts.p', 'rb'))
comments = pickle.load(open('pickles/comments.p', 'rb'))

dataset = []

for _,q in querry.iterrows():
    page = SO.Page()
    page.addQuerry(SO.Querry(q.name, q.Body, q.Score, q.Tags, q.Title, q.acceptedAnswerId))
    # Select posts corresponding to the querry
    in_posts = posts[posts.ParentId==q.name]
    if len(in_posts)>0:
        for _,p in in_posts.iterrows():
            new_post = SO.Post(p.name, p.Body, p.Tags, p.Score)
            in_comments = comments[comments.PostId == p.name]
            if len(in_comments)>0:
                for c in in_comments:
                    new_comment = SO.Comment(c.Text, c.PostId, c.Score)
                    new_post.addComment(new_comment)
            page.addPost(new_post)

    page.cleanPage()
    dataset.append(page)

""" 2. Get all words in all querries in this particular domain """

p.querry.clean_body

all_words = []
for p in dataset:
    all_words.extend(p.querry.querry_post.bagOfWords())

all_words = nltk.FreqDist(all_words) #get the frequency distribution of all used words.

n_features = 2000
features = list(all_words.keys())[:n_features]


""" 3. Get all words in all answers in this particular domain """

Y_words = []

for p in dataset:
    if p.answer_flag:
        Y_words.extend(p.clean_answer.split())

Y_words = nltk.FreqDist(Y_words) #get the frequency distribution of all used words.

n_y_features = 250

y_features = list(Y_words.keys())[:n_y_features]


""" 4. Extract dataset X & Y """

X = []
Y = []

for p in dataset:
    if p.answer_flag:
        X.append(transform.WordsToVec(features, p.querry.clean_body))
        Y.append(transform.WordsToVec(y_features, p.clean_answer))

data = zip(X, Y)
data = np.random.shuffle(data)

training, testing = model_selection.train_test_split(data, test_size=0.2)


""" 5. Train a model """

nltk_model = NaiveBayesClassifier.train(training)
print(accuracy(nltk_model, testing))
