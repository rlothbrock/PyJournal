import random


def unique_id_creator(self):
    date__ = self.date_session.replace('-','')
    return '{}{:X}'.format(date__,int(random.random()*10**17))