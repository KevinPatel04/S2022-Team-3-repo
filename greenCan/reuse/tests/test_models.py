from django.test import TestCase
from model_bakery import baker
from reuse.models import Post, Image, NGOLocation


class TestModels(TestCase):
    def test_Post_model(self):
        post = baker.make("reuse.Post")
        self.assertIsInstance(post, Post)
        self.assertEquals(str(post), str(post.id))

    def test_Image_model(self):
        image = baker.make("reuse.Image")
        self.assertIsInstance(image, Image)
        self.assertEquals(str(image), str(image.id))

    def test_NGOLocation_model(self):
        ngo_location = baker.make("reuse.NGOLocation")
        self.assertIsInstance(ngo_location, NGOLocation)
        self.assertEquals(str(ngo_location), str(ngo_location.id))
