from locust import HttpUser, task, between


class TriviaUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_root(self):
        self.client.get("/")
