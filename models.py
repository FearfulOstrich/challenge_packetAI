""" The predictions should be divided into two category:
        1. Predict the best solution/answer to the problem/question.
        2. Predict the cause of the problem if there is one.

    1. To predict the solution/answer, A model like the one presented in this paper
        (https://www.aclweb.org/anthology/W18-5035.pdf) could be used. The output
        of the prediction is a sentence Using the following input:
            - Embedded post title.
            - Embedded main post body. (sentence wise)
            - Embedded AcceptedAnswer (using corresponding ID) post body. (sentence wise)
            - Score and other 


    Supposing we get a dataset containing the following:
    - Embedded post title.
    - Embedded main post body (body of the question).
    We can train a first model to predict a probability that there will be a
