import json, random, requests, shutil

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, View
from random_word import RandomWords

from .models import *

r = RandomWords()

# Create your views here.
class Lounge(View):

    def get(self, request):
        return render(request, 'create_avatar.html', status=200)

    def post(self, request):
        return HttpResponse('congrats!', status=200)

class Play(View):

    def get(self, request):
        return render(request, 'create_avatar.html', status=200)

    def post(self, request):
        return HttpResponse('congrats!', status=200)

class Create(View):

    def get(self, request):
        return render(request, 'create_avatar.html', status=200)

    def post(self, request):

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        # apply the public apis
        bname = body['name']
        _name = bname.replace(' ', '_')
        name = _name.lower()

        sprites = [
            'male',
            'female',
            'human',
            'identicon',
            'initials',
            'bottts',
            'avataaars',
            'jdenticon',
            'gridy',
            'code',
        ]
        
        autogen_name = r.get_random_words(limit=2)
        #autogen_name = requests.get('https://random-word-api.herokuapp.com/word?number=2')
        name_set = ' '.join(autogen_name)

        profile_name = name
        avatar_url = 'https://avatars.dicebear.com/api/{}/{}.svg'.format(random.choice(sprites), name)
        avatar_autogenerated_name = name_set.title()
        atk = self.randomize_atk()
        strength = self.randomize_str()
        agi = self.randomize_agi()
        intelligence = self.randomize_int()
        base_armor = self.randomize_base_armor()
        base_hp = (self.randomize_base_hp() + 12 * int(strength))
        base_mana = (self.randomize_base_mana() + 12 * int(intelligence))
        base_atk_spd = round(agi * .05, 2)
        skill_one = SkillOne.objects.order_by("?").first()
        skill_two = SkillTwo.objects.order_by("?").first()
        skill_three = SkillThree.objects.order_by("?").first()
        skill_ultimate = SkillUlt.objects.order_by("?").first()
        skill_passive = SkillPassive.objects.order_by("?").first()
        hidden_skill_potential = HiddenSkillPotential.objects.order_by("?").first()

        data = {
            'profile_name': bname,
            'avatar_url': avatar_url,
            'avatar_autogenerated_name': avatar_autogenerated_name,
            'base_stats': {
                'atk': atk,
                'str': strength,
                'agi': agi,
                'int': intelligence,
                'base_armor': base_armor,
                'base_hp': base_hp,
                'base_mana': base_mana,
                'base_atk_spd': base_atk_spd,
            },
            'base_skills': {
                'skill_one': {
                    'skill_name': skill_one.skill_name,
                    'skill_damage': skill_one.skill_damage,
                    'skill_effect': skill_one.skill_effect,
                },
                'skill_two': {
                    'skill_name': skill_two.skill_name,
                    'skill_damage': skill_two.skill_damage,
                    'skill_effect': skill_two.skill_effect,
                },
                'skill_three': {
                    'skill_name': skill_three.skill_name,
                    'skill_damage': skill_three.skill_damage,
                    'skill_effect': skill_three.skill_effect,
                },
                'skill_ultimate': {
                    'skill_name': skill_ultimate.skill_name,
                    'skill_damage': skill_ultimate.skill_damage,
                    'skill_effect': skill_ultimate.skill_effect,
                },
                'skill_passive': {
                    'skill_name': skill_passive.skill_name,
                    'skill_damage': skill_passive.skill_damage,
                    'skill_effect': skill_passive.skill_effect,
                },
                'hidden_skill_potential': {
                    'skill_name': hidden_skill_potential.skill_name,
                    'skill_damage': hidden_skill_potential.skill_damage,
                    'skill_effect': hidden_skill_potential.skill_effect,
                },
            }
        }
        
        return JsonResponse(data, safe=False)

    def randomize_atk(self):
        value = random.randrange(40, 70)
        return int(value)

    def randomize_str(self):
        value = random.randrange(15, 35)
        return int(value)

    def randomize_agi(self):
        value = random.randrange(18, 30)
        return int(value)
    
    def randomize_int(self):
        value = random.randrange(16, 35)
        return int(value)

    def randomize_base_armor(self):
        value = random.randrange(5, 15)
        return int(value)

    def randomize_base_hp(self):
        value = random.randrange(350, 550)
        return int(value)

    def randomize_base_mana(self):
        value = random.randrange(225, 475)
        return int(value)
