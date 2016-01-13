from django_mako_plus.controller.router import get_renderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django import forms
from django.contrib.auth import authenticate, login, logout
import homepage.models as hmod
import hashlib, datetime, random, string
from django.core.mail import send_mail, EmailMessage
# ldap plugins
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO, SEARCH_SCOPE_WHOLE_SUBTREE

templater = get_renderer('homepage')

'''
    index:

        Handles
        - Loads landing page
        - Logging in users (our system, active directory)
        - Logging out user
        - Forgot my password modal
        - Password recovery email

'''

@view_function
def process_request(request):
    '''
        process_request: Loads landing page

    '''

    params = {}

    return templater.render_to_response(request, 'index.html', params)


def get_username(request):
    '''
        get_username: Returns the username of the user logged in

    '''
    username = {}

    if request.user.username != "":

        username = {
            'first_name': request.user.first_name
        }

    return JsonResponse(username)


@view_function
def loginform(request):
    '''
        loginform: returns html for login modal, validates form, logs in users

    '''

    params = {}

    form = LoginForm()

    # check form
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            #Authenicate and Login
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)

            # reload page to close modal
            return HttpResponse('''
                <script>
                    window.location.href = window.location.href
                </script>

            ''')

    # pass form
    params['form'] = form

    return templater.render_to_response(request, 'index.loginform.html', params)


@view_function
def logout_view(request):
    '''
        logout_view: logs out signed in user, return to homepage

    '''
    logout(request)
    return HttpResponseRedirect('/homepage/index/')

def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    '''
        random_generator: returns random string to use for temp_password

    '''
    return ''.join(random.choice(chars) for x in range(size))

@view_function
def forgot_password(request):
    '''
        forgot_password: loads forgot_password modal, validates form, generates password recovery email

    '''

    params = {}

    form = ForgotPasswordForm()

    # validate form
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():

            # get user
            user = hmod.User.objects.get(username=form.cleaned_data['username'], email=form.cleaned_data['email'])

            # create temp password
            temp_password = random_generator()
            user.temp_password = temp_password

            # create activation key
            random_string = str(random.random()).encode('utf8')
            salt = hashlib.sha1(random_string).hexdigest()[:5]
            salted = (salt + user.email).encode('utf8')
            activation_key = hashlib.sha1(salted).hexdigest()
            user.activation_key = activation_key

            # expiration date
            user.expiration_date = datetime.date.today() + datetime.timedelta(days=1)
            user.save()

            # email password link embedded with key,
            subject = "CHF- Password Recovery"
            to = [user.email]
            from_email = 'do-not-reply@cheritagefoundation.com'

            params = {
                'activation_link': 'http://127.0.0.1:8000/homepage/index.recover_password/' + activation_key,
                'temp_password': temp_password
            }

            message = templater.render(request, 'recover_password_email.html', params)

            msg = EmailMessage(subject, message, to=to, from_email=from_email)
            msg.content_subtype = 'html'
            msg.send()

            return HttpResponse('''
                <script>
                    window.location.href = window.location.href
                </script>

            '''
            )

            # user clicks link and it reset's password to temp password IF within 24 hours

    params['form'] = form
    return templater.render_to_response(request, 'index.forgot_password.html', params)

@view_function
def recover_password(request):
    '''
        recover_password:

            - user clickes recovery link in email, calls this function
            - reset password to temp_password if link not expired
    '''

    params = {}

    # user clicked link

    # get activation key
    activation_key = request.urlparams[0]

    # lookup user
    user = hmod.User.objects.get(activation_key=activation_key)
    print('user:', user)

    # check if expiration date has passed
    expiration_date = user.expiration_date

    if expiration_date > datetime.date.today():

        # change password
        saved_username = user.username
        temp_password = user.temp_password
        user.set_password(user.temp_password)
        user.save()

        # login user
        user = authenticate(username = saved_username, password = temp_password)
        login(request, user)


    return templater.render_to_response(request, 'index.html', params)

class LoginForm(forms.Form):
    '''
        LoginForm:

            - collects username and password
            - checks if user exists in Active Directory
            - ensures unique username

    '''
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput)


    def clean(self):

        if self.is_valid():
            # check ldap
            try:
                # create server, make connection change server to cheritagefoundation.com later
                s = Server('www.cheritagefoundation.com', port=12345, get_info=GET_ALL_INFO)
                c = Connection(
                      s,
                      auto_bind = True,
                      user = self.cleaned_data['username'] + '@cheritagefoundation.local',
                      password= self.cleaned_data['password'],
                      authentication=AUTH_SIMPLE,
                      client_strategy=STRATEGY_SYNC
                    )

                # search for user in Active Directory
                search_results = c.search(
                  search_base = 'CN=Users,DC=cheritagefoundation,DC=local',
                  search_filter = '(samAccountName=' + self.cleaned_data['username'] + ')',
                  search_scope = SEARCH_SCOPE_WHOLE_SUBTREE,
                  attributes = [
                    'givenName',
                    'sn',
                    'l',
                    'streetAddress',
                    'postalCode',
                    'st',
                    'mobile',
                    'info',
                  ])

                # if user exists
                if search_results:

                    # get info from active directory
                    user_info = c.response[0]['attributes']

                    # update chf user
                    user = hmod.User.objects.get_or_create(
                        username=self.cleaned_data['username'],
                        first_name = user_info['givenName'],
                        last_name = user_info['sn'],
                        phone = user_info['mobile'],
                        email = user_info['info'],
                        )

                    user = hmod.User.objects.get(username = self.cleaned_data['username'])

                    # set user password
                    user.set_password(self.cleaned_data['password'])
                    user.save()

            except:

                # user does not exist in Active Directory

                # try to log user in
                user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])

                if user is None:

                    # report invalid user
                    raise forms.ValidationError("Incorrect username and password")
                    return self.cleaned_data

        return self.cleaned_data

class ForgotPasswordForm(forms.Form):
    '''
        ForgotPasswordForm:

            - collects username and recovery email
            - checks if they match
            - return validation error if they don't
    '''
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'dan@gmail.com'}))

    def clean(self):
        '''
            clean: check if username and email match
        '''
        if self.is_valid():
            try:
                user = hmod.User.objects.get(username=self.cleaned_data['username'], email=self.cleaned_data['email'])
            except hmod.User.DoesNotExist:
                raise forms.ValidationError("Username and email did not match")

        return self.cleaned_data
