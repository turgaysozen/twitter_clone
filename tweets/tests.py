from django.test import TestCase
from rest_framework.test import APIClient
from .models import Tweet
from django.contrib.auth import get_user_model

User = get_user_model()

class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_user", password="123")
        self.user2 = User.objects.create_user(username="test_user2", password="123")
        Tweet.objects.create(content="tweet_1", user=self.user)
        Tweet.objects.create(content="tweet_2", user=self.user2)
        self.tweet_count = Tweet.objects.all().count()      

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='123')
        return client

    def test_create(self):
        created_tweet = Tweet.objects.create(content="test_tweet", user=self.user)
        self.assertEqual(created_tweet.user, self.user)
        self.assertEqual(created_tweet.id, 10)

    def test_tweet_list(self):
        tweet_list = Tweet.objects.all()
        self.assertEqual(tweet_list.count(), 2)

    def test_tweet_list_by_api(self):
        client = self.get_client()
        response = client.get("/api/tweets/")
        self.assertEqual(response.status_code, 200)

    def test_action_like(self):
        # tweet_list = Tweet.objects.all()
        # print('*************** -- like -- *************************')
        # for tweet in tweet_list:
        #     print(tweet.id)
        # print('*************** -- like -- *************************')
        client = self.get_client()
        response = client.post("/api/tweets/action", {"id": 2, "action": "like"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get('likes')
        self.assertEqual(like_count, 1)

    def test_action_unlike(self):
        # tweet_list = Tweet.objects.all()
        # print('*************** -- unlike -- *************************')
        # for tweet in tweet_list:
        #     print(tweet.id)
        # print('*************** -- unlike -- *************************')
        client = self.get_client()
        response = client.post("/api/tweets/action", {"id": 6, "action": "like"})
        self.assertEqual(response.status_code, 200)
        response = client.post("/api/tweets/action", {"id": 6, "action": "unlike"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get('likes')
        self.assertEqual(like_count, 0)

    def test_action_retweet(self):
        # tweet_list = Tweet.objects.all()
        # print('*************** -- retweet -- *************************')
        # for tweet in tweet_list:
        #     print(tweet.id)
        # print('*************** -- retweet -- *************************')
        client = self.get_client()
        response = client.post("/api/tweets/action", {"id": 4, "action": "retweet"})
        self.assertEqual(response.status_code, 201)
        retweet_id = response.json().get('id')
        # print('*************** -- retweet id -- *************************')
        # print(retweet_id)
        # print('*************** -- retweet id -- *************************')
        new_tweet_list = Tweet.objects.all()
        self.assertEqual(retweet_id, 5)
        self.assertEqual(self.tweet_count + 1, new_tweet_list.count())

    def test_tweet_create(self):
        client = self.get_client()
        data = {
            "content": "This is a test tweet",
            "user": self.user
        }
        response = client.post('/api/tweets/create', data)
        self.assertEqual(response.status_code, 201)

    def test_tweet_detail_view(self):
        # tweet_list = Tweet.objects.all()
        # print('*************** -- detail -- *************************')
        # for tweet in tweet_list:
        #     print(tweet.id)
        # print('*************** -- detail -- *************************')
        client = self.get_client()
        response = client.get('/api/tweets/17')
        data = response.json()
        tweet_id = data.get('id')
        self.assertEqual(17, tweet_id)

    def test_tweet_delete(self):
        # tweet_list = Tweet.objects.all()
        # print('*************** -- delete -- *************************')
        # for tweet in tweet_list:
        #     print(tweet.user, tweet.id)
        # print('*************** -- delete -- *************************')
        client = self.get_client()
        response = client.delete('/api/tweets/15/delete')
        self.assertEqual(response.status_code, 401)
        response = client.delete('/api/tweets/14/delete')
        response = client.get('/api/tweets/14')
        status_code = response.status_code
        self.assertEqual(status_code, 404)
    
