from app.models import Comment,User,Blog
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_jeanne = User(username = 'jeanne',password = 'kazubajoanna', email = 'njoanc@gmail.com')
        self.new_blog = Blog(id=1,blog_title='Test',blog_content='This is a test blog',category="interview",user = self.user_jeanne,likes=0,dislikes=0)
        self.new_comment = Comment(id=1,comment='Test comment',user=self.user_jeanne,blog=self.new_blog)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_jeanne)
        self.assertEquals(self.new_comment.blog,self.new_blog)
