from common.mixins import LabelChoices


class SubscriptionPlan(LabelChoices):
    MONTHLY = 'monthly', 'Monthly'
    QUARTERLY = 'quarterly', 'Quarterly'
    HALF_YEAR = 'half_year', 'Half Year'
    YEARLY = 'yearly', 'Yearly'


class SubscriptionType(LabelChoices):
    FREE = 'free', 'Free'
    PAID = 'paid', 'Paid'


class AdType(LabelChoices):
    IMAGE = 'image', 'Image'
    VIDEO = 'video', 'Video'


class Currencies(LabelChoices):
    NGN = '₦', 'Naira'
    USD = '$', 'USD'
