from django.db import models

class Table1(models.Model):
    objects = models.Manager() # vs code 오류 제거용

    no      = models.AutoField(primary_key=True)
    title   = models.CharField(max_length=200)
    content = models.TextField()
    writer  = models.CharField(max_length=50)
    hit     = models.IntegerField() # 조회수
    img     = models.BinaryField(null=True) # 바이너리 필드
    regdate = models.DateTimeField(auto_now_add=True)