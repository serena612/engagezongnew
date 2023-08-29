from pyexpat.errors import messages
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from engage.account.models import UserGameLinkedAccount
from jet.admin import CompactInline
from . import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models import Subquery, OuterRef, TextField
from django.db.models.functions import Cast
from django.db.models import F, Q
from django.contrib import messages as messagesss
from django.forms.widgets import HiddenInput


class TournamentPrizeInline(CompactInline):
    model = models.TournamentPrize
    min_num = 1
    tournament = None
    extra = 0 
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if not obj:
            fields.remove('winner')
        return fields

    def get_formset(self, request, obj=None, **kwargs):
        if obj:
            self.tournament = obj
        return super().get_formset(request, obj, **kwargs)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        formfield = super().formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'winner':
            # get last round
            ha = models.TournamentMatch.objects.filter(tournament=self.tournament).order_by('-round_number').first()
            if ha:
                lastround = ha.round_number
                winners = models.TournamentMatch.objects.filter(tournament=self.tournament).filter(round_number=lastround).values_list('winners',flat=True)
                # winners = ha.winners
            # print("last round", lastround)
                formfield.queryset = formfield.queryset.filter(
                    tournamentparticipant__tournament=self.tournament
                ).filter(
                    tournamentmatch__round_number=lastround
                ).filter(is_staff=False).filter(pk__in=winners)
            else:
                formfield.queryset = formfield.queryset.filter(
                    tournamentparticipant__tournament=self.tournament
                ).filter(is_staff=False)
           
            subquery = UserGameLinkedAccount.objects.filter(user=OuterRef('id'), tournament=self.tournament)
            combined_query = formfield.queryset.annotate(
                    # tourn = Cast(Subquery(subquery.values('tournament')[:1]), output_field=TextField()),
                    gnickname = Cast(Subquery(subquery.values('account')[:1]), output_field=TextField())
                ).filter(is_staff=False)
            formfield.queryset = combined_query.distinct()
        return formfield

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        formfield = super().formfield_for_dbfield(
            db_field, request, **kwargs)
        if db_field.name == 'winner':
            formfield.widget.can_add_related = False
            formfield.widget.can_change_related = False
            formfield.widget.can_delete_related = False
        return formfield
   

class TournamentParticipantInline(CompactInline):
    model = models.TournamentParticipant
    # readonly_fields = ('points', 'rank')
    exclude = ('notify_before_game', 'prize','points', 'rank')
    min_num = 0
    extra = 0
    tournament = None
#     def get_fields(self, request, obj=None):
#         fields = list(super().get_fields(request, obj=obj))
#         if obj is None:
#             fields.remove('participant')
#         return fields
    def get_formset(self, request, obj=None, **kwargs):
        if obj:
            self.tournament = obj
            
        return super().get_formset(request, obj, **kwargs)
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        formfield = super().formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == 'participant':
            subquery = UserGameLinkedAccount.objects.filter(user=OuterRef('id'), tournament=self.tournament)
            combined_query = formfield.queryset.annotate(
                    # tourn = Cast(Subquery(subquery.values('tournament')[:1]), output_field=TextField()),
                    gnickname = Cast(Subquery(subquery.values('account')[:1]), output_field=TextField())
                ).filter(is_staff=False)
            formfield.queryset = combined_query
        return formfield


    def formfield_for_dbfield(self, db_field, request, **kwargs):
        formfield = super().formfield_for_dbfield(
            db_field, request, **kwargs)
        if self.tournament and self.tournament.starts_in_full == "In Progress" and formfield is not None:
            formfield.disabled = True
        
        if db_field.name == 'participant':
            formfield.widget.can_add_related = False
            formfield.widget.can_change_related = False
            formfield.widget.can_delete_related = False
        return formfield
    
    def has_add_permission(self, request, obj=None):
        if obj and obj.starts_in_full == "In Progress":
            return False
        else:
            return True
    
    def has_delete_permission(self, request, obj=None):
        if obj and obj.starts_in_full == "In Progress":
            return False
        else:
            return True

    # def has_change_permission(self, request, obj=None):
    #     if not obj:
    #         return False
    #     elif obj.state != "upcoming":
    #         return False
    #     else:
    #         return True
    


class TournamentMatchInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TournamentMatchInlineForm, self).__init__(*args, **kwargs)
        
        if 'winners' in self.fields and 'instance' in kwargs:
            if kwargs['instance'].round_number >1:
                match_winners = models.TournamentMatch.objects.filter(tournament=kwargs['instance'].tournament).filter(round_number=int(kwargs['instance'].round_number)-1).values_list('winners',flat=True)
                
                # print("previous matches winners:", match_winners)
                self.fields['participants'].queryset = self.fields['participants'].queryset.filter(pk__in=match_winners)
                self.fields['winners'].queryset = self.fields['winners'].queryset.filter(pk__in=match_winners)
                # print("query", self.fields['participants'].queryset.query)
            #print('before',self.fields['participants'].queryset)
            part_round = self.fields['participants'].queryset.filter(Q(participanto__round_number=kwargs['instance'].round_number) & Q(participanto__tournament=kwargs['instance'].tournament)).values_list('pk', flat=True)
            part_match = self.fields['participants'].queryset.filter(participanto=kwargs['instance'].id)
            #print("participants in same round",part_round)
            #print("participants in this match", part_match.values_list('pk', flat=True))
            self.fields['participants'].queryset = self.fields['participants'].queryset.exclude(pk__in=part_round)
            self.fields['participants'].queryset = self.fields['participants'].queryset | part_match
            # self.fields['participants'].queryset = self.fields['participants'].queryset.exclude((Q(participanto__round_number=kwargs['instance'].round_number) & Q(participanto__tournament=kwargs['instance'].tournament)) & ~Q(participanto=kwargs['instance'].id)).distinct()
            #print("final participants",self.fields['participants'].queryset)
            self.fields['winners'].queryset = self.fields['winners'].queryset.filter(participanto=kwargs['instance'].id).distinct()
           
        elif 'winners' in self.fields:
            self.fields['participants'].queryset = self.fields['participants'].queryset.none() # self.fields['participants'].queryset.distinct()
            self.fields['winners'].queryset = self.fields['winners'].queryset.none() # self.fields['winners'].queryset.distinct()
            self.fields["participants"].widget = HiddenInput()
            self.fields["winners"].widget = HiddenInput()
            
            
            

            
            
    # class Meta:
    #     model = models.TournamentMatch
    #     fields = "__all__"
    #     widgets = {
    #         "participants": ParticipantsWidget,  # (attrs={'style': 'width: 100% !important', 'class':'multiselect dropdown-toggle mt-multiselect',})
    #         "winners": ParticipantsWidget,  # (attrs={'style': 'width: 100% !important', 'class':'multiselect dropdown-toggle mt-multiselect',})
    #     }


class TournamentMatchInline(CompactInline):
    model = models.TournamentMatch
    min_num = 0
    form = TournamentMatchInlineForm
    # readonly_fields = ('id',)
    exclude = ('match_data', 'id',)
    tournament = None
    extra = 0



    def get_fields(self, request, obj=None):
        fields = list(super().get_fields(request, obj=obj))
        if obj is None:
            fields.remove('winners')
            fields.remove('participants')
        return fields
    
    def get_formset(self, request, obj=None, *args, **kwargs):
        if obj:
             self.tournament = obj
        return super().get_formset(request, obj, *args, **kwargs)
   

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        formfield = super().formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.name == "participants" or db_field.name == "winners":
            # print('instance', kwargs['instance'])
            if self.tournament:
                subquery = UserGameLinkedAccount.objects.filter(user=OuterRef('id'), tournament=self.tournament)
                
                # matches = models.TournamentMatch.objects.filter(tournament=self.tournament.id).values_list('pk', flat=True)
                # formfield.queryset = formfield.queryset.filter(participanto__in=matches)
                #print("values before=",formfield.queryset.values_list('pk', flat=True))
                formfield.queryset = formfield.queryset.filter(tournamentparticipant__tournament=self.tournament.id) \
                .filter(tournamentparticipant__status="accepted").filter(is_staff=False).filter(tournamentparticipant__is_waiting_list=False)
                combined_query = formfield.queryset.annotate(
                    # tourn = Cast(Subquery(subquery.values('tournament')[:1]), output_field=TextField()),
                    gnickname = Cast(Subquery(subquery.values('account')[:1]), output_field=TextField())
                )
                formfield.queryset = combined_query.distinct()
                # print(formfield.queryset.values_list())
                #print("values=",formfield.queryset.values_list('pk', flat=True))
                # formfield.queryset = formfield.queryset# .filter(Q(usergamelinkedaccount__tournament_id=self.tournament.id) & Q(tournamentparticipant__status="accepted")) # .select_related('usergamelinkedaccount')
                # print(queryset)
        return formfield
    
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        formfield = super().formfield_for_dbfield(
            db_field, request, **kwargs)
        if self.tournament and db_field.name == "round_number":
            rounds = self.tournament.rounds_number
            formfield.choices = formfield.choices[:rounds+1]
        return formfield


@admin.register(models.Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'start','close')
    exclude = ('slug', 'job_id', 'created_by','format')
    inlines = [TournamentMatchInline, TournamentPrizeInline,
               TournamentParticipantInline]
        

    def start(self, obj):
        now = timezone.now()
        if obj.started_on and obj.end_date > now and not obj.closed_on:
            return mark_safe('<span>ongoing</span>')
        elif obj.end_date > now and not  obj.started_on:
            return mark_safe(
                f'<a class="grp-state-focus addlink a_start" data-link="/api/tournaments/{obj.slug}/start/" style="cursor:pointer">Start</a>'
            )
    start.short_description = ''
    start.allow_tags = True

    def close(self, obj):
        now = timezone.now()
        if obj.started_on and obj.end_date > now and not obj.closed_on:
            return mark_safe(
                f'<a class="grp-state-focus addlink a_close"  data-link="/api/tournaments/{obj.slug}/close/" style="cursor:pointer">End</a>'
            )
        elif  obj.started_on and  obj.closed_on:
            return mark_safe('<span>closed</span>')  

    close.short_description = ''
    close.allow_tags = True
    
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        formfield = super().formfield_for_dbfield(
            db_field, request, **kwargs)
        # if self.tournament is not None and self.tournament.state != "upcoming" and formfield is not None:
        #     formfield.disabled = True
        
        if db_field.name == 'game':
            formfield.widget.can_add_related = False
            formfield.widget.can_change_related = False
            formfield.widget.can_delete_related = False
        return formfield

    class Media:
        css = { 'all': ('admin/tournament/bootstrap-4.5.2.min.css', 'css/bootstrap-multiselect.css', 'css/tournament.css')} # 
        js = ('admin/tournament/select2.min.js', 'admin/tournament/bootstrap-multiselect.js', 'admin/tournament/base.js','admin/tournament/moment.min.js', ) # 'admin/tournament/select2.min.js', # 'js/bootstrap-multiselect.js', , 'admin/tournament/select2.multi-checkboxes.js'

        
