from news.models import *

User1 = User.objects.create_user(username='Vladislav')
User2 = User.objects.create_user(username='Vladimir')
A1= Author.objects.create(authorUser=User1)
A2= Author.objects.create(authorUser=User2)
cat1 = Category.objects.create(name='Bisnes')
cat2 = Category.objects.create(name='Music')
cat3 = Category.objects.create(name='Film')
cat4 = Category.objects.create(name='World')
p1 = Post.objects.create(author=A1, categoryType='NW', tittle='News', text='Курс доллара вырос!')
p2 = Post.objects.create(author=A2, categoryType='AR', tittle='Новый фильм!', text='Вышел фильм Аватар!')
p3 = Post.objects.create(author=A2, categoryType='AR', tittle='Новый альбом!', text='Вышел новый альбом!')
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=2))
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=4))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=4))
com1 = Comment.objects.create(commentPost=p1, commentUser=User1, text='Nice')
com2 = Comment.objects.create(commentPost=p2, commentUser=User2, text='Cool film')
com3 = Comment.objects.create(commentPost=p3, commentUser=User1, text='Bad')
com4 = Comment.objects.create(commentPost=p1, commentUser=User2, text='Bad news')
Comment.objects.get(id=1).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).like()
Post.objects.get(id=1).like()
Post.objects.get(id=2).dislike()
Post.objects.get(id=3).dislike()
Post.objects.get(id=3).like()
Post.objects.get(id=2).like()

A1.update_rating()
A2.update_rating()
A1.ratingAuthor
A2.ratingAuthor
rat= Author.objects.order_by('-ratingAuthor')[:1]

for ret in rat:
    ret.ratingAuthor
    ret.authorUser.username

Post.objects.all().order_by('-rating').values("author","dateCreation", "rating", "tittle", "text")
Comment.objects.all().order_by('-rating').values("commentUser", "rating", "text", "dateCreation")