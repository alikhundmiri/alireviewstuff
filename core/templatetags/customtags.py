'''

Very simple filter that returns one of the following by default:

# days ago
yesterday
today
January 01, 2007
Example template code:

This thread was started {{ post.date_created|dayssince }}.
This thread was started today.

E-mail sent: {{ email.date_sent|dayssince|capfirst }}
E-mail sent: Yesterday

Object created: {{ obj.date_created|dayssince|upper }}
Object created: 12 DAYS AGO

User's bogus birthday: {{ user.get_profile.bday|dayssince }}
User's bogus birthday: April 20, 3030

ref : https://www.djangosnippets.org/snippets/116/
'''
from django import template
import datetime

register = template.Library()

def dayssince(value):
    "Returns number of days between today and value."
    today = datetime.date.today()
    diff  = today - value
    if diff.days > 1:
        return '%s days ago' % diff.days
    elif diff.days == 1:
        return 'yesterday'
    elif diff.days == 0:
        return 'today'
    else:
        # Date is in the future; return formatted date.
        return value.strftime("%B %d, %Y")

register.filter('dayssince', dayssince)