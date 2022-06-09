from django.test import TestCase
from .models import Image, Comment, Profile, User

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.comment = Comment(name="This is great")
        self.comment.save_comment()

        self.image = Image(name='Anniversary', caption='The best way to have today', comment=self.comment)
        self.image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        self.image.delete_image()

    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)

class ProfileTestCase(TestCase):
    def setUp(self):
        current_user='current_user'
        self.profile= Profile(profile_photo='uploads/img.jpg', bio='bio', user=current_user)
        self.profile.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

class CommentTestClass(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='Robert',password='12356')
        self.comment = Comment(comment='This is great',user=self.new_user,post=1)
        self.comment.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def tearDown(self):
        Comment.objects.all().delete()
