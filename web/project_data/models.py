from django.db import models


class Project(models.Model):
    kickstarter_id = models.IntegerField()
    name = models.CharField(max_length=1024)
    category = models.CharField(max_length=1024)
    main_category = models.CharField(max_length=1024)
    currency = models.CharField(max_length=1024)
    deadline = models.CharField(max_length=1024)
    goal = models.IntegerField()
    launched = models.CharField(max_length=1024)
    pledged = models.IntegerField()
    state = models.CharField(max_length=1024)
    backers = models.IntegerField()
    country = models.CharField(max_length=1024)
    usd_pledged = models.IntegerField()
    usd_pledged_real = models.IntegerField()
    usd_goal_real = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)