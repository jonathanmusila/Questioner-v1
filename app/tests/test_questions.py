import unittest
import json

#local imports
from app.apps import create_app
from .base_test import Settings

class TestQuestions(Settings):

    def test_post_question(self):
        """Test API can post a question to a meetup"""
        res = self.client.post('/api/v1/meetups/upcoming', content_type='application/json', data=json.dumps(self.meetup))
        res1 = self.client.post('/api/v1/meetups/1/questions', content_type='application/json', data=json.dumps(self.question))
        self.assertEqual(res1.status_code, 201)

    def test_get_question_meetup_id_that_doesnt_exist(self):
        res = self.client.post('/api/v1/meetups/upcoming', data=json.dumps(self.meetup), content_type='application/json')
        rv = self.client.post('/api/v1/meetups/1/questions', data=json.dumps(self.question), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        res1 = self.client.get('/api/v1/meetups/1/questions/8')
        data = json.loads(res1.data.decode())
        self.assertEqual(res1.status_code, 404)

    def test_upvote_a_question(self):
        res = self.client.post('/api/v1/meetups/upcoming', data=json.dumps(self.meetup), content_type='application/json')
        rv = self.client.post('/api/v1/meetups/1/upvote', data=json.dumps(self.upvote), content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_downvote_a_question(self):
        res = self.client.post('/api/v1/meetups/upcoming', data=json.dumps(self.meetup), content_type='application/json')
        rv = self.client.post('/api/v1/meetups/1/downvote', data=json.dumps(self.downvote), content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_get_single_question(self):
        """Test API can get a single question by using it's id."""
        res = self.client.post('/api/v1/meetups/upcoming', content_type='application/json', data=json.dumps(self.meetup))
        rv = self.client.post('/api/v1/meetups/1/questions', data=json.dumps(self.question), content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        rv1 = self.client.get('/api/v1/meetups/1/questions/1')
        data = json.loads(rv1.data.decode())
        self.assertEqual(rv1.status_code, 200)
        self.assertIn('The question body', str(rv1.data))

    def test_update_question(self):
        """Test API can update an existing question. (PUT request)."""
        rs = self.client.post('/api/v1/meetups/upcoming', data=json.dumps(self.meetup), content_type='application/json')
        rv = self.client.post('/api/v1/meetups/1/questions', data=json.dumps(self.question), content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        rv1 = self.client.put('/api/v1/meetups/1/questions/1', data=json.dumps(self.question), content_type='application/json')
        self.assertEqual(rv1.status_code, 201)
        results = self.client.get('/api/v1/meetups/1/questions/1')
        self.assertIn("0", str(results.data))
        