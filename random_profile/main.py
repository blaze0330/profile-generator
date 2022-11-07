'''
python Random Profile generator module
author : codeperfectplus
language : python 3.0 ++
github : codeperfectplus
'''

import os
import sys
import uuid
import random
from typing import List, Tuple

sys.path.append('.')

from random_profile.enums.gender import Gender
from random_profile.utils import *

VERSION = '2.0.1'

lname_txt = os.path.join(ASSETS_DIR, "lnames.txt")
fname_male_txt = os.path.join(ASSETS_DIR, "fnames_male.txt")
fname_female_txt = os.path.join(ASSETS_DIR, "fnames_female.txt")
hair_colors_txt = os.path.join(ASSETS_DIR, "hair_colors.txt")
blood_types_txt = os.path.join(ASSETS_DIR, "blood_types.txt")
street_names_txt = os.path.join(ASSETS_DIR, "street_names.txt")
cities_name_txt = os.path.join(ASSETS_DIR, "cities_name.txt")
states_names_txt = os.path.join(ASSETS_DIR, "states_names.txt")
job_titles_txt = os.path.join(ASSETS_DIR, "job_titles.txt")
job_levels_txt = os.path.join(ASSETS_DIR, "job_levels.txt")

# loading data from txt files
lname = load_txt_file(lname_txt)
fname_male = load_txt_file(fname_male_txt)
fname_female = load_txt_file(fname_female_txt)
hair_colors = load_txt_file(hair_colors_txt)
blood_types = load_txt_file(blood_types_txt)
states_names = load_txt_file(states_names_txt)
cities_name = load_txt_file(cities_name_txt)
street_names = load_txt_file(street_names_txt)
job_titles = load_txt_file(job_titles_txt)
job_levels = load_txt_file(job_levels_txt)

class RandomProfile(object):
    def __init__(self, num: int = 1, gender: Gender = None):
        """
        num = Total No. of Name You Want To Print
        default is 1
        To Print More Than one Name Change value of num
        """
        self.num = num
        self.gender = gender

    def __str__(self) -> str:
        return f'Random Profile Generator version {VERSION}'

    def __repr__(self) -> str:
        return f'RandomProfile(num={self.num})'

    def __call__(self, num: int = None) -> List[dict]:
        return self.full_profile(num)

    def __iter__(self):
        yield self.full_profile()

    def __next__(self):
        yield self.full_profile()

    def __len__(self):
        return self.num

    def __getitem__(self, index):
        return self.full_profile()[index]

    def ip_address(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return ipv4_gen()
        return [ipv4_gen() for _ in range(num)]

    def job_title(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return random.choice(job_titles)
        return random.choices(job_titles, k=num)

    def blood_type(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return random.choice(blood_types)
        return random.choices(blood_types, k=num)

    def hair_color(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return random.choice(hair_colors)
        return random.choices(hair_colors, k=num)

    def dob_age(self, num: int = None) -> List[Tuple[str, int]]:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return generate_dob_age()
        return [generate_dob_age() for _ in range(num)]

    def height_weight(self, num: int = None) -> List[Tuple[int, int]]:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return generate_random_height_weight()
        return [generate_random_height_weight() for _ in range(num)]

    def generate_address(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        address_list = []
        for _ in range(num):
            street_num = random.randint(100, 999)
            street = random.choice(street_names)
            city = random.choice(cities_name)
            state = random.choice(states_names)
            zip_code = random.randint(10000, 99999)

            address = {
                'street_num': street_num,
                'street': street,
                'city': city,
                'state': state,
                'zip_code': zip_code
            }
            address_list.append(address)

        return address_list
    
    def first_names(self, num: int = None, gender: Gender = None) -> list:
        num = self.num if num is None else num
        if gender is None:
            gender = self.gender
        if gender is None:
            names = fname_female + fname_male
        elif gender.value == Gender.MALE.value:
            names = fname_male
        else:
            names = fname_female
            
        if num == 1 or num is None:
            return random.choice(names)
        
        return random.choices(names, k=num)

    def last_names(self, num: int = None) -> list:
        num = self.num if num is None else num
        if num is None:
            num = self.num
        if num == 1 or num is None:
            return random.choice(lname)
        return random.choices(lname, k=num)
        
    def full_names(self, num: int = None, gender: Gender = None) -> list:
        num = self.num if num is None else num

        if gender is None:
            gender = self.gender

        if gender is None:
            names = fname_female + fname_male
        elif gender.value == Gender.MALE.value:
            names = fname_male
        else:
            names = fname_female
        
        if num == 1 or num is None:
            return random.choice(names) + ' ' + random.choice(lname)

        return [random.choice(names) + ' ' + random.choice(lname) for _ in range(num)]
        
    def full_profiles(self, num: int = None, gender: Gender = None) -> list:
        num = self.num if num is None else num

        profile_list = []

        for _ in range(num):

            # random gender for every profile in list
            this_gender = generate_random_gender() if gender is None else gender
            first = random.choice(fname_male if this_gender.value == Gender.MALE.value else fname_female)
            last = random.choice(lname)
            full_name = first + ' ' + last
            
            hair_color = random.choice(hair_colors)
            blood_type = random.choice(blood_types)
            
            phone_number = f'+1-{random.randint(300, 500)}-{random.randint(800, 999)}-{random.randint(1000,9999)}'

            

            dob, age = generate_dob_age()
            height, weight = generate_random_height_weight()

            job_title = random.choice(job_titles)
            job_experience = generate_random_job_level(age, job_levels)

            street_num = random.randint(100, 999)
            street = random.choice(street_names)
            city, coords = generate_random_city_coords(cities_name)
            coords_pretty = coords_string(coords)
            state = random.choice(states_names)
            zip_code = random.randint(10000, 99999)

            address = {
                'street_num': street_num,
                'street': street,
                'city': city,
                'state': state,
                'zip_code': zip_code
            }
            
            full_address = f'{street_num} {street}, {city}, {state} {zip_code}'
            
            mother = self.first_names(1, Gender.FEMALE)[0] + ' ' + last
            father = self.first_names(1, Gender.MALE)[0] + ' ' + last

            card = generate_random_card()

            profile = {}
            profile['id'] = str(uuid.uuid4())
            profile['gender'] = this_gender.value

            profile['first_name'] = first
            profile['last_name'] = last
            profile['hair_color'] = hair_color
            profile['blood_type'] = blood_type
            profile['full_name'] = full_name

            profile['job_title'] = self.job_title(num=1)
            profile['dob'] = dob
            profile['age'] = age
            profile['phone_number'] = phone_number
            profile['email'] = profile['first_name'].lower() + profile['last_name'].lower() + '@example.com'
            
            
            profile['blood_type'] = self.blood_type(num=1)
            profile['height'] = height
            profile['weight'] = weight
            profile['hair_color'] = self.hair_color(num=1)
            profile['ip_address'] = self.ip_address(num=1)


            profile['address'] = address
            profile['full_address'] = full_address
            profile['job_job_experience'] = job_experience
            profile['mother'] = mother
            profile['father'] = father
            profile['payment_card'] = card

            profile_list.append(profile)

        return profile_list
