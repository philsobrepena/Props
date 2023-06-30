from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Props(models.Model):
    ###is viewed to signify if new prop has been seen
    is_viewed = models.BooleanField(default=False)

    EMOJIS = [
    ("\U0001F600", "\U0001F600 smile"),  # 😄
    ("\U0001F920", "\U0001F920 cowboy"),  # 🤠
    ("\U0001F33B", "\U0001F33B sunflower"),  # 🌻
    ("\U0001F4B0", "\U0001F4B0 moneybagz"),  # 💰
    ("\U0001F480", "\U0001F480 skull"),  # 💀
    ("\U00002764", "\U00002764 heart"),  # ❤️
    ("\U00002728", "\U00002728 starz"),  # ✨
    ("\U0001F44D", "\U0001F44D thumby"),  # 👍
    ("\U0001F4C8", "\U0001F4C8 stonkchart"),  # 📈
    ("\U0001F973", "\U0001F973 celebrah"),  # 🥳
]

    item = models.CharField(max_length=15, choices=EMOJIS)
    date = models.DateField(default=timezone.now)
    description = models.TextField()
    recipient = models.ForeignKey(
        User,
        related_name="props",
        on_delete=models.CASCADE,
        null=True
    )

#####sender id and user to show at recipient props list

    sender_id = models.PositiveIntegerField(null=True, editable=False)
    sender_username = models.CharField(max_length=150, null=True, editable=False)

    def save(self, *args, **kwargs):
        if self.sender_id is None:
            self.sender_id = self.recipient.id if self.recipient else None
        if self.sender_username is None:
            self.sender_username = self.recipient.username if self.recipient else None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.item
