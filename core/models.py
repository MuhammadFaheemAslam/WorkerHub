from django.db import models
from accounts.models import CustomUser
from django.core.exceptions import ValidationError



class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.first_name} on {self.created_at}"

class PostMedia(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('document', 'Document'),
    )
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='media')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    file = models.FileField(upload_to='post_media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.media_type.capitalize()} for Post ID {self.post.id}"
    
    def clean(self):
        """Ensure the file is of the correct type based on media_type."""
        if self.media_type == 'image' and not self.file.name.endswith(('.jpg', '.jpeg', '.png')):
            raise ValidationError('Only .jpg, .jpeg, and .png files are allowed for images.')
        elif self.media_type == 'video' and not self.file.name.endswith(('.mp4', '.mov', '.avi')):
            raise ValidationError('Only .mp4, .mov, and .avi files are allowed for videos.')
        elif self.media_type == 'document' and not self.file.name.endswith(('.pdf', '.doc', '.docx')):
            raise ValidationError('Only .pdf, .doc, and .docx files are allowed for documents.')


    
class PostReaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')
    is_like = models.BooleanField()

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} liked/disliked {self.post.id}"


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"


# Share model for tracking post shares
class PostShare(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='shares')  
    shared_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.user.username} shared post {self.post.id}"
