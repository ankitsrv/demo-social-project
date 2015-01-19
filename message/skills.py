
#todo temp models for skills set C.R. by ANKIT SHRIVASTAVA

from django.db import models
from apps.smthing import Reward
from apps.organisation.models import Organisation

class SkillManager(models.Manager):

    def filter_skills_by_date(self, date_start, date_end, queryset=None, logic_operator='AND'):
        queryset = self.none() if queryset is None else queryset
        new_queryset = None
        if date_start:
            new_queryset = self.filter(created_at__gte=date_start)
        if date_end:
            new_queryset = self.filter(created_at__lte=date_end)
        if date_start and date_end:
            new_queryset = self.filter(created_at__gte=date_start, created_at__lte=date_end)

        if logic_operator == 'OR':
            return new_queryset | queryset
        else:
            return new_queryset & queryset

    def filter_skills_by_category(self, cat_type , queryset=None,  logic_operator= 'AND'):
        queryset = self.none() if queryset is None else queryset
        #new_queryset = None
        new_queryset = self.filter(skill__category=cat_type)
        if logic_operator == 'OR':
            return new_queryset | queryset
        else:
            return new_queryset & queryset

    def add_skill(self, admin_user_id, skill_name=None, cat_type='OTH'):
        admin = self.get(user_id = admin_user_id)
        if admin.super_admin != None:
            raise Exception('Not allowed to create a skill')
        if cat_type == 'OTH':
            skill = Skill.objects.create(name=skill_name, category='OTH')
        else:
            skill = Skill.objects.create(name=skill_name, category=cat_type)
        skill.save()
        return


class Skill(CommonInfo):

    CATEGORY_TYPE = (( 'MGT', 'Management'),
                     ( 'IT', 'IT Software'),
                     ( 'HR', 'Human Resource'),
                     ( 'ACC', 'Accountant'),
                     ( 'CUST', 'Customer service'),
                     ( 'RND', 'Research and Development'),
                     ( 'OTH', 'Others'),)

    category = models.CharField(max_length=5, choices=CATEGORY_TYPE)
    name = models.CharField(max_length=20, blank=False, null=False)
    creater = models.ForeignKey(OrganisationUser, null=True, default=None, blank=True, related_name='skills_created')
    history_timestamp = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    description = models.TextField(default='')
    #reward = models.ForeignKey(Reward, related_name='skill-reward')
    #organisation = models.ForeignKey(Organisation, null=True, blank=True, default=None, related_name='org_skills')

    #item = models.ManyToManyField(max_length=100, blank= False)

    objects = SkillManager()

    def clean(self):
        pass

    def __unicode__(self):
        return self.name

    """
    def get_or_create_skill(self):
        try:
            return self.skill
        except Exception:
            return self.objects.create(item_type='SKILL', skill=self)
    """

    def get_skill_name(self):
        return self.name

    def skill_subscription(self):
        return self.description

    def get_date_created(self):
        return self.created_at  # from the commonInfo mixin

    def get_date_edited(self):
        return self.last_updated

    # todo maybe useful
    def get_likes_count(self):
        return self.skill_item.likes.count()

    def get_creater(self):
        return self.creater

    def is_active(self):
        return self.active

