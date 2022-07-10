from django.db import models
from categories.models import Category
from users.models import User
from django.core.validators import FileExtensionValidator
# from apps.movies.models import Reviews

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    main_movie_image = models.ImageField(upload_to = 'main_movie_image', blank = True, null = True)
    year_of_issue = models.DateField()
    GENRE_CHOICES = (
        ('Драма/мелодрама', 'Драма/мелодрама'),
        ('Комедия', 'Комедия'),
        ('Фантастика', 'Фантастика'),
        ('Боевики', 'Боевики'),
        ('Ужасы', 'Ужасы'),
        ('Мультфильмы', 'Мультфильмы'),
        ('Аниме', 'Аниме'),
        ('Триллер', 'Триллер'),
        ('Детектив', 'Детектив'),
        ('Исторические', 'Исторические'),
        ('Документальные', 'Документальные'),
        ('Криминал', 'Криминал'),

    )
    genre = models.CharField(choices=GENRE_CHOICES, default='Боевики', max_length=250)
    rating = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='movie_category')
    slug = models.SlugField()
    movie_trailer = models.FileField(upload_to='movie',null=True,
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class MovieImage(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_image", null=True)
    movie_image = models.FileField(upload_to='videos_trailers',null=True )

    class Meta:
        verbose_name = "Картинка фильма"
        verbose_name_plural = "Картинки фильмов"

class MovieComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_movie")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_comment" )
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"

    
class RatingStar(models.Model): 
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model): 
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, related_name= "star_rating", verbose_name="звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name = "movie_rating", verbose_name="фильм")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model): 
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name="фильм", on_delete=models.CASCADE, related_name="movie_reviews")

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"