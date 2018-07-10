from django.db import models
from hashids import Hashids

from eventex.subscriptions.validators import validate_cpf

hashids = Hashids(salt='Welcome to the Django', min_length=11)



class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    email = models.EmailField('e-mail', blank=True)
    phone = models.CharField('telefone', max_length=20, blank=True)
    created_at = models.DateTimeField('criado em', auto_now=True)
    hashid = models.CharField(max_length=11, primary_key=True)
    paid = models.BooleanField('pago', default=False)

    class Meta:
        verbose_name_plural = 'inscrições'
        verbose_name = 'inscrição'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.hashid = hashids.encode(int(self.cpf))
        super(Subscription, self).save(*args, **kwargs)