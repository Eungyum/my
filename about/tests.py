from django.test import TestCase
from django.urls import reverse
from .models import About, RAG, AIConvHistory

class AboutModelTest(TestCase):
    def test_str_method(self):
        about = About(title="About Test Title")
        self.assertEqual(str(about), "About Test Title")
        
class RAGModelTest(TestCase):
    def test_str_method(self):
        rag = About(title="RAG Test Title")
        self.assertEqual(str(rag), "RAG Test Title")
        
class AIConvHistoryModelTest(TestCase):
    def test_str_method(self):
        aiconvhistory = About(title="AIConvHistory Test Title")
        self.assertEqual(str(aiconvhistory), "AIConvHistory Test Title")