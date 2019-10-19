import pandas as pd
import xml.etree.ElementTree as ET
import utils.SO_objects as SO

def buildPostsDf(xml):
    """Function to create a DataFrames from the xml posts object.
    One DataFrame for querries (with title) and one for posts."""

    root = xml.getroot()
    querry_cols = ['PostTypeId', 'acceptedAnswerId', 'Body', 'Title', 'Tags', 'AnswerCount', 'Score', 'CommentCount'] #Columns selected
    posts_cols = ['ParentId', 'Score', 'Body', 'Tags']
    querry_df = pd.DataFrame(columns=querry_cols)
    posts_df = pd.DataFrame(columns=posts_cols)

    for p in root:
        if p.attrib.get("PostTypeId")=="1":
            id = p.attrib.get("Id")
            row = dict(zip(querry_cols, [p.attrib.get(a) for a in querry_cols]))
            row_s = pd.Series(row)
            row_s.name = id
            querry_df = querry_df.append(row_s)

        elif p.attrib.get("PostTypeId")=="2":
            id = p.attrib.get("Id")
            row = dict(zip(posts_cols, [p.attrib.get(a) for a in posts_cols]))
            row_s = pd.Series(row)
            row_s.name = id
            posts_df = querry_df.append(row_s)

    return querry_df, posts_df

def buildCommentsDf(xml):
    """Function to create a Dataframe from the xml comments objects."""

    root = xml.getroot()
    cols = ['PostId', 'Score', 'Text']
    comments_df = pd.DataFrame(columns=cols)

    for c in root:
        id = c.attrib.get("Id")
        row = dict(zip(cols, [c.attrib.get(a) for a in cols]))
        row_s = pd.Series(row)
        row_s.name = id
        comments_df.append(row_s)

    return comments_df


def buildData(dirname):
    """Function to build the data from stack overflow xml files.
    Takes posts and matches all comments corresponding to the post id."""

    fposts = dirname+'/Posts.xml'
    fcomments = dirname+'/Comments.xml'
    xml_posts = ET.parse(fposts)
    xml_comments = ET.parse(fcomments)

    querry_df, posts_df = build_posts_df(xml_posts)
    comments_df = append_comments(xml_comments, posts_df)

    return querry_df, posts_df, comments_df
