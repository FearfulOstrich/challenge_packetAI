# main file

import nltk
from format import buildData
from utils import SO_objects as SO
from nltk.tokenize import word_tokenize


""" 1. Import and clean training data """

domain = 'health'
querry, posts, comments = builData('data/{}.stackexchange.com'.format(domain))

dataset = []

for q in querry:
    page = SO.Page()
    page.addQuerry(SO.Querry(q.index, q.Body, q.Score, q.Tags, q.Title, q.acceptedAnswerId))
    # Select posts corresponding to the querry
    in_posts = posts[posts.ParentId==q.index]
    if len(in_posts)>0:
        for p in in_posts:
            new_post = SO.Post(p.index, p.Body, p.Tags, p.Score)
            in_comments = comments[comments.PostId == p.index]
            if len(in_comments)>0:
                for c in in_comments:
                    new_comment = SO.Comment(c.Text, c.PostId, c.Score)
    page.cleanPage()
    dataset.append(page)

""" 2. Get all words in this particular domain """

all_words = []
for p in dataset:
    all_words.extend(p.bagOfWords())

all_words = nltk.FreqDist(all_words) #get the frequency distribution of all used words.

n_features = 2000
features = list(all_words.keys())[:2000]
