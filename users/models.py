from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #第一个参数关联模型名，第二个表示级联（即关联数据表删除后，UserProfile内数据也删除），修改外键名称

    org = models.CharField('Organization', max_length = 128, blank = True)

    telephone = models.CharField('Telephone', max_length = 50, blank = True)

    mod_date = models.DateTimeField('Last modified', auto_now=True)

    class Meta:
        verbose_name = 'User Profile'
    #更改对象名

    def __str__(self):
        return self.user._str_()



