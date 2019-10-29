import unittest
from app.model import Sources,Articles


class TestArticles(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''
    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_article = Articles(1,'tumaa','he becomes the best','Kipchoge breaks the world record on 2 hour marathon','https://techtoday.com','https://marathons.com/images','2019-010-21T14:50:05Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.author,'mzinge')
        self.assertEquals(self.new_article.title,'hussein takes part in hackerthon')
        self.assertEquals(self.new_article.description,'he becomes the best')
        self.assertEquals(self.new_article.url,'https://techtoday.com')
        self.assertEquals(self.new_article.urlToImage,'https://marathons.com/images')
        self.assertEquals(self.new_article.publishedAt,'2019-010-21T14:50:05Z')


class SourceTest(unittest.TestCase):
   '''
   Test case to test the behavior of the NewsSource class
   '''
   def setUp(self):
       '''
       Setup function that will run before every test
       '''
       self.new_source = Sources('gsu','kbbs','Latest news','https://newscenteer.com','games','msa')
   def test_instance(self):
       self.assertTrue(isinstance(self.new_source,Sources))
   def test_to_check_instance_variables(self):
       '''
       Test function to check instance variables
       '''
       self.assertEquals(self.new_source.id,'gsu')
       self.assertEquals(self.new_source.name,'kbbs')
       self.assertEquals(self.new_source.description,'Latest newsy')
       self.assertEquals(self.new_source.url,'https://newscenteer.com')
       self.assertEquals(self.new_source.category,'games')
       self.assertEquals(self.new_source.country,'msa')


if __name__ == '__main__':
    unittest.main()
