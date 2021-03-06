""" This file contains the models expected for the API """

#Third party imports 
from flask_restplus import fields, Namespace 

class MeetupsModel:
    """
    Meetup input data

    """
    api = Namespace('Meetups', description = 'Meetups Routes')
    meetups = api.model('Meetup', {
        'm_id':fields.Integer(required=False, description='The unique identifier of the meetup'),
        'createdOn': fields.String(required=False, description='This time the meetup was created'),
        'location': fields.String(required=True, description='The meetup location'),
        'images': fields.String(required=True, description='The images attached to a meetup'),
        'topic': fields.String(required=True, description='The meetup topic'),
        'happeningOn': fields.String(required=True, description='The date the meetup is happening'),
    })

class QuestionModel:
    """
    Question input data

    """
    api = Namespace('Questions', description='Questions Routes')
    questions = api.model('Question', {
        'qsn_id':fields.Integer(required=True, description='The unique identifier of the question'),
        'body': fields.String(required=True, description='The body of the question'),
        'meetup_id': fields.Integer(required=True, description='The meetup unique identifier'),
        'createdOn': fields.String(required=True, description='The time the question was posted'),
        'title': fields.String(required=True, description='The title of the question'),
        'votes': fields.Integer(required=True, description='The number of votes a question contains'),
    })

class ResponseModel:
    """
    Response input data

    """
    api = Namespace('Responds', description = 'Responses Routes')
    responses = api.model('Response', {
        'r_id':fields.Integer(required=True, description='The unique identifier of the comment'),
        'meetup_id': fields.Integer(required=True, description='Meetup unique identifier'),
        'topic': fields.String(required=True, description='The topic of the meetup'),
        'status': fields.String(required=True, description='The response status'),
    })

class VotesModel:
    """
    Upvote/Downvote input data

    """
    api = Namespace('Question_Votes', description='Question_Votes Route')
    nvotes = api.model('Question', {
        'votes': fields.Integer(required=True, description='The number of votes a question contains'),
        })


class UserModel:
    """
    User input data

    """
    api = Namespace('Users', description = 'User Routes')
    users = api.model('User', {
        'user_id':fields.Integer(required=False, description='This is the user firstname'),
        'fname': fields.String(required=True, description='This is the user firstname'),
        'lname': fields.String(required=True, description='This is the user lastname'),
        'email': fields.String(required=True, description='The user email'),
        'username': fields.String(required=True, description='The username of the user'),
        'password': fields.String(required=True, description='The password of the user'),
        'registered': fields.String(required=False, description='The time the user was registered'),
        'isAdmin': fields.Boolean(required=False, description='The role of the user'),
    })