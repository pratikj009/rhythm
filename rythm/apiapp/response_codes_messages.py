# -----------------Account-------------------
# Account Start
# 1. Login
LOGIN_SUCCESS_CODE = 1000
LOGIN_SUCCESS_MESSAGE = 'Welcome, '

LOGIN_WRONG_CREDENTIALS_CODE = 1001
LOGIN_WRONG_CREDENTIALS_MESSAGE = 'Wrong credentials'

LOGIN_MISSING_FIELDS_CODE = 1002
LOGIN_MISSING_FIELDS_MESSAGE = 'Please enter missing fields'

LOGIN_DATA_EXCEPTION_CODE = 1003
LOGIN_DATA_EXCEPTION_MESSAGE = 'The user name you have entered is invalid'

# 2. Register
REGISTER_SUCCESS_CODE = 1010
REGISTER_SUCCESS_MESSAGE ='You have been successfully registered! Please login to continue!'

REGISTER_MISSING_PASSWORD_CODE = 1012
REGISTER_MISSING_PASSWORD_MESSAGE = 'Please enter missing fields'

REGISTER_MISSING_FIELD_CODE = 1011
REGISTER_MISSING_FIELD_MESSAGE = 'Please enter missing fields'

# 3. Logout
LOGOUT_SUCCESS_CODE = 1020
LOGOUT_SUCCESS_MESSAGE = 'Hope you made memories, do come back for more'

LOGOUT_INVALID_USERID_CODE = 1021
LOGOUT_INVALID_USERID_SUCCESS = 'Oops! something went wrong'

LOGOUT_GCMDEVICE_ERROR_CODE = 1022
LOGOUT_GCMDEVICE_ERROR_MESSAGE = 'Logged out but the GCMDevice does not exists'

LOGOUT_MISSING_FIELD_CODE = 1023
lOGOUT_MISSING_FIELD_MESSAGE = 'Oops! something went wrong'

# 4. Forgot Password
FORGOT_PASSWORD_EMAIL_SUCCESS_CODE = 1030
FORGOT_PASSWORD_EMAIL_SUCCESS_MESSAGE = 'New password has been sent to the registered Email ID'

FORGOT_PASSWORD_EMAIL_INVALID_CODE = 1031
FORGOT_PASSWORD_EMAIL_INVALID_MESSAGE = 'The Email ID you have entered is invalid'

FORGOT_PASSWORD_MISSING_FIELD_CODE = 1032
FORGOT_PASSWORD_MISSING_FIELD_MESSAGE = 'Please enter missing fields'

#5. Update GCM Token
UPDATE_GCM_TOKEN_SUCCESS_CODE = 1040
UPDATE_GCM_TOKEN_SUCCESS_MESSAGE = 'GCM token updated successfully!'

UPDATE_GCM_TOKEN_NEW_DEVICE_CODE = 1041
UPDATE_GCM_TOKEN_NEW_DEVICE_MESSAGE = 'New GCMDevice registered for the user successfully'

UPDATE_GCM_TOKEN_MISSING_FIELD_CODE = 1042
UPDATE_GCM_TOKEN_MISSING_FIELD_MESSAGE = 'Oops! something went wrong'

# 6. Username Availability (Pre login)
USERNAME_AVAILABLE_CODE = 1050
USERNAME_AVAILABLE_MESSAGE = 'Username is available'

USERNAME_NOT_AVAILABLE_CODE= 1051
USERNAME_NOT_AVAILABLE_MESSAGE = 'User name is already taken'

USERNAME_AVAILABILITIY_DATA_EXCEPTION_CODE = 1052
USERNAME_AVAILABILITIY_DATA_EXCEPTION_MESSAGE = 'Oops! something went wrong'

# 7. Login with Facebook
LOGIN_WITH_FB_SUCCESS_CODE = 1060
LOGIN_WITH_FB_SUCCESS_MESSAGE = 'Welcome, '

LOGIN_WITH_FB_NEW_USER_CODE = 1061
LOGIN_WITH_FB_NEW_USER_MESSAGE = 'Welcome, '

LOGIN_WITH_FB_DATA_EXCEPTION_CODE = 1062
LOGIN_WITH_FB_DATA_EXCEPTION_MESSAGE = 'Oops! something went wrong'

LOGIN_WITH_FB_MISSING_FIELDS_CODE = 1063
LOGIN_WITH_FB_MISSING_FIELDS_MESSAGE = 'Oops! something went wrong'

# 8. Login with Google
LOGIN_WITH_GOOGLE_SUCCESS_CODE = 1070
LOGIN_WITH_GOOGLE_SUCCESS_MESSAGE = 'Welcome, '

LOGIN_WITH_GOOGLE_NEW_USER_CODE = 1071
LOGIN_WITH_GOOGLE_NEW_USER_MESSAGE = 'Welcome, '

LOGIN_WITH_GOOGLE_DATA_EXCEPTION_CODE = 1072
LOGIN_WITH_GOOGLE_DATA_EXCEPTION_MESSAGE = 'Oops! something went wrong'

LOGIN_WITH_GOOGLE_MISSING_FIELDS_CODE = 1073
LOGIN_WITH_GOOGLE_MISSING_FIELDS_MESSAGE = 'Oops! something went wrong'


#----------------- Profile -----------------------------------
# Profile start
# 1. Get Profile Details
PROFILE_GET_DETAILS_SUCCESS_CODE = 3000
PROFILE_GET_DETAILS_SUCCESS_MESSAGE = 'User Profile retrieved successfully'

PROFILE_GET_DETAILS_INVALID_USERID_CODE = 3001
PROFILE_GET_DETAILS_INVALID_USERID_MESSAGE = 'Oops! something went wrong'

PROFILE_GET_DETAILS_MISSING_FIELDS_CODE = 3002
PROFILE_GET_DETAILS_MISSING_FIELDS_MESSAGE = 'Oops! something went wrong'

# 2. Profile Update
PROFILE_UPDATE_SUCCESS_CODE = 3010
PROFILE_UPDATE_SUCCESS_MESSAGE = 'Profile Udpated'

PROFILE_UPDATE_INVALID_USERID_CODE = 3011
PROFILE_UPDATE_INVALID_USERID_MESSAGE = 'Oops! something went wrong'

PROFILE_UPDATE_MISSING_FIELDS_CODE = 3012
PROFILE_UPDATE_MISSING_FIELDS_MESSAGE = 'Oops! something went wrong'

# 3. Username Availability (Post Login)
PROFILE_USERNAME_AVAILABLE_CODE = 3020
PROFILE_USERNAME_AVAILABLE_MESSAGE = 'User name is available'

PROFILE_USERNAME_NOT_AVAILABLE_CODE= 3021
PROFILE_USERNAME_NOT_AVAILABLE_MESSAGE = 'User name is already taken'

PROFILE_USERNAME_DATA_EXCEPTION_CODE = 3022
PROFILE_USERNAME_DATA_EXCEPTION_MESSAGE = 'Oops! something went wrong'

# 4. Get Other User's Profile Details
PROFILE_GET_OTHER_USER_DETAILS_SUCCESS_CODE = 3030
PROFILE_GET_OTHER_USER_DETAILS_SUCCESS_MESSAGE = 'User Profile retrieved successfully'

PROFILE_GET_OTHER_USER_DETAILS_INVALID_USERID_CODE = 3031
PROFILE_GET_OTHER_USER_DETAILS_INVALID_USERID_MESSAGE = 'Oops! something went wrong'
#Profile End