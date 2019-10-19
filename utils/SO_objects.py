""" File containing the Stack Overflow API objects:
        - Question/Querry
        - posts
        - comments
        - Topics (Querry + posts + comments) """

import nltk
# nltk.download()
from nltk.corpus import stopwords
import re

"""---___---___---___---___---___---__---__---___---___---___---___---___---__---__---___---___---___---___---___---__---__"""

def regexReplacement(_string):
    """Function to replace regular expression (e.g: email, numbers...) by keyword."""

    assert(type(_string)==type('a string'))

    # Change email addresses by emailaddr
    _string = re.sub('([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', 'emailaddr', _string)

    # Change url addresses by urladdr
    _string = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', 'urladdr', _string)

    # Change numbers by numbr
    _string = re.sub('\d+((\.|\,)\d+)?', 'numbr', _string)

    # Remove punctuation
    _string = re.sub('[^\w\d\s]', '', _string)

    # Make all white spaces single spaces
    _string = re.sub('\s+', ' ', _string)

    # Remove leading and trailing spaces.
    _string = re.sub('^\s+|\s+?$', '', _string)

    # Make all letters lower cases
    _string = _string.lower()

    return _string

def stopWordsStemming(_string):
    """Function to remove stopwords and to stem remaining words."""

    # Remove stopwords
    stop_words = set(stopwords.words('english')) #or english #or using a different stopwords library.
    _string = ' '.join(word for word in _string.split() if word not in stop_words)

    # Stem remaining words
    stemmer = nltk.PorterStemmer()
    _string = ' '.join(stemmer.stem(word) for word in _string.split())

    return _string

"""---___---___---___---___---___---__---__---___---___---___---___---___---__---__---___---___---___---___---___---__---__"""


class Post(object):
    """ Post class to create the stack-overflow post entity.
    Contains attributes:
        - Id
        - Body
        - Score
        - Tags"""

    def __init__(self, id, body, tags, score):
        self.body = body
        self.id = id
        self.score = score
        self.tags = tags
        self.comments = []

    def cleanBody(self):
        "Function to clean the text body of the post."
        self.clean_body = stopWordsStemming(regexReplacement(self.body))

    def cleanComments(self):
        "Function to clean the comments of each post"
        for comm in self.comments:
            comm.cleanComment()

    def addComment(self, comm):
        self.comments.append(comm)

    def cleanPost(self):
        """Function to clean the entire post (body + comments)"""
        self.cleanBody()
        self.cleanComments()

    def bagOfWords(self):
        "Get all the words that appear in a post."
        self.bow = self.clean_body.split()

        for comm in self.comments:
            self.bow.extend(comm.bagOfWords)

        return self.bow


class Querry(Post):
    """Querry class, inherits from the post object, to create the initial post.
    Contains extra attribute:
        - title"""

    def __init__(self, id, body, score, tags, title, answerId):
        self.title = title
        self.answer_id = answerId
        self.querry_post = Post.__init__(id, body, tags, score)


    def cleanTitle(self):
        "Function to clean the body of the post."
        self.clean_title = stopWordsStemming(regexReplacement(self.title))

    # def cleanBody(self):
    #     "Function to clean the body of the querry"
    #     self.clean_body = stopWordsStemming(regexReplacement(self.body))

    def cleanQuerry(self):
        """Function to clean the entire querry (title+body)"""
        self.cleanBody()
        self.cleanTitle()

    def bagOfWords(self):
        """Get all the words that appear in a querry."""
        self.bow = self.clean_title.split()

        return self.bow.extend(self.querry_post.bagOfWords())


class Comment(object):
    """Comment class to create the stack-overflow comment entity.
    Contains attributes:
        - Body
        - postId
        - score"""

    def __init__(self, body, postId, score):
        self.body = body
        self.postId = postId
        self.score = score

    def cleanComment(self):
        "Function to clean the text body of the post."
        self.clean_body = stopWordsStemming(regexReplacement(self.body))

    def bagOfWords(self):
        "Get all the words that appear in a comment."
        return self.clean_body.split()


class Page(object):
    """Page class to group together the Querry, the posts and the comments."""

    def __init__(self):
        self.posts = []

    def addPost(self, post):
        self.posts.append(post)

    def addQuerry(self, querry):
        self.querry = querry

    def cleanPosts(self):
        "Function to clean all posts"
        for post in self.posts:
            post.cleanPost()

    def cleanPage(self):
        """Function to clean the entire page (querry (title + body) + posts (body + comments))"""
        self.querry.cleanQuerry()
        self.cleanPosts()

    def bagOfWords(self):
        """Get all the words that appear in a clean page."""
        self.bow = []
        self.bow.append(self.querry.bagOfWords())
        for post in self.posts:
            self.bow.extend(post.bagOfWords())

        return self.bow
