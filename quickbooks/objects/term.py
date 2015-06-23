from base import QuickbooksBaseObject


'''
QBO definition: The Term entity represents the terms under which a sale is made, typically expressed in the
form of days due after the goods are received. Optionally, a discount of the total amount may be applied if
payment is made within a stipulated time. For example, net 30 indicates that payment is due within 30 days.
A term of 2%/15 net 60 indicates that payment is due within 60 days, with a discount of 2% if payment is made
within 15 days. This entity also supports: -An absolute due date -A number of days from a start
date -A percent discount -An absolute discount
'''
class Term(QuickbooksBaseObject):
    class_dict = {}

    qbo_object_name = "Term"

    Name = ""
    Type = ""
    DiscountPercent = 0
    DayOfMonthDue = 0
    DueNextMonthDays = 0
    DiscountDayOfMonth = 0
    Active = True

    def __unicode__(self):
        return self.Name
