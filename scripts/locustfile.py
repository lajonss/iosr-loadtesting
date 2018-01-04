from locust import HttpLocust, TaskSet, task


class HelloWorldTaksSet(TaskSet):
    @task
    def my_task(self):
        self.client.get('/greeting')


class HelloWorldLocust(HttpLocust):
    task_set = HelloWorldTaksSet
