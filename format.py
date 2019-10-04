import pandas as pd
import xml.etree.ElementTree as ET

def build_posts_df(xml):
    """Function to create a Series from the xml posts object."""

    root = xml.getroot()
    cols = ['PostTypeId', 'acceptedAnswerId', 'Text', 'Title', 'CommentCount', 'AnswerCount'] #Columns selected
    main_posts = pd.DataFrame(columns=cols)
    other_posts = pd.Dataframe(columns=['ParentId', 'Score', 'Body'])
    for p in root:
        if p.attrib.get("PostTypeId")=="1":
            id = p.attrib.get("Id")
            row = dict(zip(cols, [p.attrib.get(a) for a in cols]))
            row_s = pd.Series(row)
            row_s.name = id
            posts = posts.append(row_s)

    return main_posts, other_posts

def append_comments(xml, posts):
    """Function to append comments to the posts df.
    Selects accepted answer to a separate column."""

    root = xml.getroot()
    cols = ['']
    comments = pd.DataFrame(columns=cols)


def build_data(dirname):
    """Function to build the data from stack overflow xml files.
    Takes posts and matches all comments corresponding to the post id."""

    fposts = dirname+'/Posts.xml'
    fcomments = dirname+'/Comments.xml'
    xml_posts = ET.parse(fposts)
    xml_comments = ET.parse(fcomments)

    posts_df = build_posts_df(xml_posts)
    comments_df = append_comments(xml_comments, posts_df)
