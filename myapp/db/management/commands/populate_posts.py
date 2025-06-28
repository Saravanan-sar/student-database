from typing import Any
from django.core.management.base import BaseCommand
from django.core.files import File
from db.models import Post  # change 'db' to your actual app name

class Command(BaseCommand):
    help = 'Populate the Post model with initial data'

    def handle(self, *args: Any, **options: Any):
        titles = [
            'CapStone',
            'Symposium',
            'Pongal Celebration',
            'Regatta',
            'Archivers Day',
        ]

        contents = [
            'CapStone is annual celebration on AVS it is Largest event of the year, The Special DAy of AVSEC thus The Cinema ceelbrities are been as chief guest, Student are been perform their dance and music and other culural acts The Blast ends with DJ and Fireworks It gennerally happen in tHe Month of Feb Last week or  March  First Week thus the Award winner are been get prices by the hands of chief guest. IN 2025 the chief guest was Kayadu Lohar The Heroiene Of dragon movie and also the Movie promotipon for the Sweet Heart movie also occured oNthis year Actor Rio and Actress Kayadu Lohar were the chief guests of the event.',
            'Symposium is a event where the students are been given a chance to present their ideas and projects in front of the audience, The Symposium is been held in the month of January and February, The students are been given a chance to present their ideas and projects in front of the audience, The Symposium is been held in the month of January and February, The students are been given a chance to present their ideas and projects in front of the audience.',
            'Pongal Celebration is a event where the students are been given a chance to celebrate the Pongal festival, The Pongal Celebration is been held in the month of January, The students are been given a chance to celebrate the Pongal festival, The Pongal Celebration is been held in the month of January.',
            "regatta is Ride Fest event that is first celebration on AVSEC every years ffirst celebrations was it.The rides like coloumbus ,Giannt wheel, and cup and sauscer ,spin to hell are the events .The unride games also been conduct like kabaddi,foot ball, throw ball,balooon blasts etc are beem occur The event is been held in the month of August and September, The students are been given a chance to celebrate the Regatta festival, The Regatta Celebration is been held in the month of August and September.",  
            'ARchivers days is givving the Offer letter to the students who are been placed in the companies, The Archivers Day is been held in the month of April and May, The students are been given a chance to celebrate the Archivers Day festival, The Archivers Day Celebration is been held in the month of April and May.',
        ]

        image_paths = [
            'media/profile_photos/cap 2025.jpeg',
            'media/profile_photos/sym 2025.jpg',
            'media/profile_photos/pongal.jpg',
            'media/profile_photos/Ragata (10).jpeg',
            'media/profile_photos/archviwrs.jpg',
        ]

        for title, content, image_path in zip(titles, contents, image_paths):
            post = Post(title=title, content=content)
            with open(image_path, 'rb') as img_file:
                post.img.save(image_path.split('/')[-1], File(img_file), save=True)

        self.stdout.write(self.style.SUCCESS('✅ Successfully populated the Post model with initial data'))