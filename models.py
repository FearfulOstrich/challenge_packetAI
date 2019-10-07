""" The predictions should be divided into two category:
        1. Predict the best solution/answer to the problem/question.
        2. Predict the cause of the problem if there is one.

    1. To predict the solution/answer, we can use a supervised approach.
        To begin with, we suppose the accepted answer is the one with the most upvotes
        in order to create a traning set and a validation set (later on, those posts
        could be preprocessed to only select one or a set of sentences). We take as
        input the initial post containing the question (eventually we could take as
        input the title of the post).
        The model used will use LSTM layers and an attention layer.


    2. To predict a cause, we first need to assess the probability that a cause is exposed,
        and if the probability is high enough, we predict the cause of the problem.
        To build the dataset, we need to manually build the training set by labelling the
        cause, when available.
        We can train a first model to predict a probability that there will be a cause from a querry.
         In a second part, we can predict the cause using a similar layer as above. 

"""
