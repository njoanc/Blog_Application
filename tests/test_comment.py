from app.models import Writer,Comment,Blog
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.writer_Wecode = Writer(username = 'Wecode',password = 'kazuba1', email = 'wecode@gmail.com')
        self.new_blog = Blog(id=1,blog_title='Test',blog_content='This is a test blog',category="happiness", writer= self.writer_Wecode,likes=0,dislikes=0)
        self.new_comment = Comment(id=1,comment='Test comment',writer=self.writer_Wecode,blog=self.new_blog)

    def tearDown(self):
        Blog.query.delete()
        Writer.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.writer,self.writer_WEcode)
        self.assertEquals(self.new_comment.blog,self.new_blog)
