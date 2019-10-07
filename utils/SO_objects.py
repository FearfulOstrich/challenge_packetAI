""" File containing the Stack Overflow API objects:
        - Question/Querry
        - posts
        - comments
        - Topics (Querry + posts + comments) """

import nltk

class Post(object):
    """ Post class to create the stack-overflow post entity.
    Contains attributes:
        - Id
        - Body
        - Score
        - Tags"""

    def __init__(self, id, body, score, tags, comments):
        self.body = body
        self.id = id
        self.score = score
        self.tags = tags
        self.comments = []

    def encode_body(self):
        "Function to encode the body of the post."

    def add_comment(self, comm):
        self.comments.append(comm)

class Querry(Post):
    """Querry class, inherits from the post object, to create the initial post.
    Contains extra attribute:
        - title"""

    def __init__(self, id, body, score, tags, title, answerId):
        self.title = title
        self.answerId = answerId
        Post.__init__(id, body, score, tags)


    def encode_title(self):
        "Function to encode the body of the post."


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


class Page(object):
    """Page class to group together the Querry, the posts and the comments."""

    def __init__(self, querry):
        self.querry = querry
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
