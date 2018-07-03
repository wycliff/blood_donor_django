from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

# Doing a Q lookup
from django.db.models import Q


from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )


User = get_user_model() # Now i will be using my custom user model , yeeey




#==================================  REGISTRATION  ======================================

class UserCreateSerializer(ModelSerializer):
    email = EmailField(label = "Email Address")
    # email2 = EmailField(label = "Confirm email")
    class Meta:
        model = User
        fields = [
             
             #'active',
             #'admin',
             #'staff', 
             'email',
             'full_name',
             'password',
             'blood_type', 
             'rhesus_factor', 
             'age',
             'current_location',  
             'gender',   
             'weight',
             #'first_time_donor', 
        ]

        #Setting the password to write only
        extra_kwargs = { "password": 
                        { "write_only":True }
                                             }

    #checking if email exists, General validation
    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email = email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered")
        return data

    #validating email1
    def validate_email(self, value):
        data = self.get_initial()
        email = data.get("email")
        # email2 = value
        # if email1 != email2:
        #     raise ValidationError("Emails must match.")
        # Checking if email exists
        user_qs = User.objects.filter(email = email)
        if user_qs.exists():
            raise ValidationError("This user has already registered")  
        return value    

    # def validate_email2(self, value):
    #     data = self.get_initial()
    #     email1 = data.get("email")
    #     email2 = value
    #     if email1 != email2:
    #         raise ValidationError("Emails must match.")
    #     return value

    #overwrite the create_user() method
    def create_user(self, validated_data):
        print (validated_data) #a dictionary

       # username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        blood_type = validated_data['blood_type']
        rhesus_factor = validated_data['rhesus_factor']
        age = validated_data['age']
        current_location = validated_data['current_location']
        gender = validated_data['gender']
        weight = validated_data['weight']

        #create an isntance of the object and save it
        user_obj = User(            
           # username = username,
            email = normalize_email(email),
            full_name = full_name,
            blood_type =  blood_type,
            rhesus_factor = rhesus_factor,
            age = age,
            current_location = current_location,
            gender =  gender,
            weight = weight,
        )
        
        user_obj.set_password(password)
        user_obj.save()
        return validated_data



#=============================== LOGIN =================================================

class UserLoginSerializer(ModelSerializer):
    #token = CharField(allow_blank = True, read_only = True)
    #username = CharField(required=False, allow_blank = True)
    email = EmailField(label = "Email Address",required=False, allow_blank = True)
    class Meta:
        model = User 
        fields = [
             
             'email',   
             'password',
             #'token',

        ]
        
        #Setting the password to write only
        extra_kwargs = {"password": 
                        {"write_only":True}
                                  }

    #checking if email exists, General validation
    def validate(self, data):
        user_obj = None
        email = data.get("email", None) #dont need to use None though, its the default
        #username = data.get("username", None)
        full_name = data.get("full_name", None)
        password = data["password"]

        if not email:
            raise ValidationError("email is required to login")

        #getting user object from this (all the details you want to get back will be obtained from this)
        user = User.objects.filter(
            Q(email=email) #|
            #Q(full_name = full_name)  
            #Q(username=username)
            ).distinct()

        user = user.exclude(email__isnull=True).exclude(email__iexact='') #excludes from the above filtered those without email
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This email is not valid")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials, please try again.")

        data["token"] =  "SOME RANDOM TOKEN"
        #data["full_name"]= full_name
        return data


#============================ Getting user data for populating dataset(filtered by rhesus and blood type) =================
# Will be authenticated using the returned web token.
# Make a serializer for the read op, or do it directly from the views. Remember CRUD? 


  # user = User.objects.filter(
  #           Q(rhesus_factor=rhesus_factor) | 
  #           Q(blood_type = 'A')          # 'A' or a variable
  #           ).distinct()




