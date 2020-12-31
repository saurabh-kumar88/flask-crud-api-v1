from locust import HttpUser, TaskSet, task

nodejs_api = 'http://mern-crud-app-back-end-v1.herokuapp.com/api/todo/'
nodejs_api_local = 'http://localhost:3000/api/todo/'
json_place_holder = 'https://jsonplaceholder.typicode.com/posts'


class QuickStartUser(HttpUser):

    @task
    def index(self):
        self.client.get(json_place_holder)
