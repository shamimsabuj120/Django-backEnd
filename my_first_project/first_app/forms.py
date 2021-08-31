from django import forms

class user_form(forms.Form):

    user_name = forms.CharField(required=False, label="Full Name",
                                widget=forms.TextInput(attrs={'placeholder':'enter your full name',
                                                              'style':'width:300px'}))

    user_email = forms.EmailField(label="Email ID",required=False)

    user_date = forms.DateField(label="Date of birth", widget=forms.TextInput(attrs={'type':'date'}),required=False)

    user_phone = forms.IntegerField(label="Phone Number",required=False)
    boolean_field = forms.BooleanField(label="Boolean Field", required=False)
    char_field = forms.CharField(max_length=15, min_length=5, required=False)
    choice_field = forms.ChoiceField(choices=(('','--SELECT OPTION--'),('1','first'),('2','second'),('3','third')))
    choice=(('A','A'),('B','B'),('C','C'),('D','D'))
    radio_choice = forms.ChoiceField(choices=choice, widget=forms.RadioSelect)
    # password = forms.PasswordInput()
    multiple_choice=(('', '--SELECT OPTION--'), ('1', 'first'), ('2', 'second'), ('3', 'third'))
    multiple_field = forms.MultipleChoiceField(choices=multiple_choice, widget=forms.CheckboxSelectMultiple)
