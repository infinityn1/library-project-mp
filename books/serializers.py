from rest_framework import serializers
from .models import Book
from rest_framework.exceptions import ValidationError


class BookSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price',)
        

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        if not title.isalpha():
            raise ValidationError(
                {'status': False,
                 'messagse': 'Faqat harf kiriting'}
            )
            
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {'status': False,
                 'messagse': 'Kitob hamda sarlavha bir xil bolmasligi kerak'}                
            )
        
        return data
    
