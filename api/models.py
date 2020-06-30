from django.db import models

# Create your models here.
# 基表-----------------------------------
class BaseModel(models.Model):
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    class Meta:
        abstract = True
# 书表------------------------------------
class Book(BaseModel):
    book_name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pic = models.ImageField(upload_to="img", default="img/1.jpeg")
    publish = models.ForeignKey(to="Press",on_delete=models.CASCADE,db_constraint=False, related_name="books")
    authors = models.ManyToManyField(to="Author", db_constraint=False, related_name="books")
    class Meta:
        db_table = "bz_book"
        verbose_name = "图书"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.book_name
    @property
    def publish_name(self):
        return self.publish.press_name
    @property
    def press_address(self):
        return self.publish.address
    @property
    def author_list(self):
        return self.authors.values("author_name", "age", "detail__phone")

# 出版社---------------------------------------------------
class Press(BaseModel):
    press_name = models.CharField(max_length=128)
    pic = models.ImageField(upload_to="img", default="img/1.jpeg")
    address = models.CharField(max_length=256)
    class Meta:
        db_table = "bz_press"
        verbose_name = "出版社"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.press_name
# 作者---------------------------------------
class Author(BaseModel):
    author_name = models.CharField(max_length=128)
    age = models.IntegerField()
    class Meta:
        db_table = "bz_author"
        verbose_name = "作者"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.author_name

# 作者详情----------------------------------
class AuthorDetail(BaseModel):
    phone = models.CharField(max_length=11)
    author = models.OneToOneField(to="Author", on_delete=models.CASCADE, related_name="detail")
    class Meta:
        db_table = "bz_author_detail"
        verbose_name = "作者详情"
        verbose_name_plural = verbose_name
    def __str__(self):
        return "%s的详情" % self.author.author_name