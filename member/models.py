from django.db import models
from django.utils import timezone

class StudentMeta(models.Model):
    student_meta = models.CharField('学年クラス名', max_length=20)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.student_meta

class Club(models.Model):
    name = models.CharField('部活名',max_length=20)
    created_at = models.DateTimeField('日付',default=timezone.now)

    def __str__(self):
        return self.name

class Member(models.Model):
    first_name = models.CharField('名', max_length=20)
    last_name = models.CharField('姓', max_length=20)
    email = models.EmailField('メールアドレス', blank=True)
    student_meta = models.ForeignKey(
        StudentMeta, verbose_name='学年クラス', on_delete=models.PROTECT,
    )
    club = models.ManyToManyField(
        Club, verbose_name='部活',
    )
    created_at = models.DateTimeField('日付',default=timezone.now)

    def __str__(self):
        return '{0} {1} {2}'.format(self.last_name, self.first_name, self.student_meta)