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
LOGOUT_SUCCESS_MESSAGE = 'Logged out successfully, do come back for more'

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
#Profile End

# --------------------Followers_Followed-----------------------
# Follower Followed
# 1. Send Request to follow
FOLLOW_REQUEST_SUCCESS_CODE = 2000
FOLLOW_REQUEST_SUCCESS_MESSAGE = 'Request sent successfully'

FOLLOW_REQUEST_SENT_ERROR_CODE = 2001
FOLLOW_REQUEST_SENT_ERROR_MESSAGE = 'Request has already sent'

FOLLOW_REQUEST_DATA_EXCEPTION_CODE = 2002
FOLLOW_REQUEST_DATA_EXCEPTION_MESSAGE = 'User is already present in followed'

FOLLOW_REQUEST_MISSING_FIELDS_CODE = 2003
FOLLOW_REQUEST_MISSING_FIELDS_MESSAGE = 'Oops! something went wrong'

FOLLOW_REQUEST_INVALID_USERID_CODE = 2004
FOLLOW_REQUEST_INVALID_USERID_MESSAGE = 'Oops! something went wrong'

# 2. Delete Connection Request
FOLLOW_DELETE_REQUEST_SUCCESS_CODE = 2010
FOLLOW_DELETE_REQUEST_SUCCESS_MESSAGE = 'Request deleted successfully'

FOLLOW_DELETE_REQUEST_DATA_EXCEPTION_CODE = 2011
FOLLOW_DELETE_REQUEST_DATA_EXCEPTION_MESSAGE = 'Oops! something went wrong'

FOLLOW_DELETE_REQUEST_NOT_PRESENT_CODE = 2012
FOLLOW_DELETE_REQUEST_NOT_PRESENT_MESSAGE = 'Invalid request! Request in not present in your database'

FOLLOW_DELETE_REQUEST_INVALID_USERID_CODE = 2013
FOLLOW_DELETE_REQUEST_INVALID_USERID_MESSAGE = 'Oops! something went wrong'

FOLLOW_DELETE_REQUEST_MISSING_FIELDS_CODE = 2014
FOLLOW_DELETE_REQUEST_MISSING_FIELDS_MESSAGE = 'Oops! something went wrong'

# 3. Accept follower Request
FOLLOW_ACCEPT_REQUEST_SUCCESS_CODE = 2020
FOLLOW_ACCEPT_REQUEST_SUCCESS_MESSAGE = 'User added successfully'

FOLLOW_ACCEPT_REQUEST_FOLLOW_ERROR_CODE = 2021
FOLLOW_ACCEPT_REQUEST_FOLLOW_ERROR_MESSAGE = 'User is already present in followers list'

FOLLOW_ACCEPT_REQUEST_MISSING_FIELDS_CODE = 2022
FOLLOW_ACCEPT_REQUEST_MISSING_FIELDS_MESSAGE = 'Oops! something went wrong'

FOLLOW_ACCEPT_REQUEST_INVALID_USERID_CODE = 2023
FOLLOW_ACCEPT_REQUEST_INVALID_USERID_MESSAGE = 'Oops! something went wrong'

FOLLOW_ACCEPT_REQUEST_DATA_EXCEPTION_CODE = 2024
FOLLOW_ACCEPT_REQUEST_DATA_EXCEPTION_MESSAGE = 'Oops! something went wrong'

FOLLOW_ACCEPT_REQUEST_NOT_PRESENT_CODE = 2025
FOLLOW_ACCEPT_REQUEST_NOT_PRESENT_MESSAGE = 'Invalid request! Request in not present in your database'

# 4. Reject follower Request
FOLLOW_REJECT_REQUEST_SUCCESS_CODE = 2030
FOLLOW_REJECT_REQUEST_SUCCESS_MESSAGE = 'Follow request rejected successfully'

FOLLOW_REJECT_REQUEST_FOLLOW_ERROR_CODE = 2031
FOLLOW_REJECT_REQUEST_FOLLOW_ERROR_MESSAGE = 'User is already present in follower list'

FOLLOW_REJECT_REQUEST_MISSING_FIELDS_CODE = 2032
FOLLOW_REJECT_REQUEST_MISSING_FIELDS_MESSAGE = 'Oops! something went wrong'

FOLLOW_REJECT_REQUEST_INVALID_USERID_CODE = 2033
FOLLOW_REJECT_REQUEST_INVALID_USERID_MESSAGE = 'Oops! something went wrong'

FOLLOW_REJECT_REQUEST_DATA_EXCEPTION_CODE = 2034
FOLLOW_REJECT_REQUEST_DATA_EXCEPTION_MESSAGE = 'Oops! something went wrong'

FOLLOW_REJECT_REQUEST_NOT_PRESENT_CODE = 2035
FOLLOW_REJECT_REQUEST_NOT_PRESENT_MESSAGE = 'Invalid request! Request in not present in your database'

# 5. Remove from follower
FOLLOWER_DELETE_SUCCESS_CODE = 2040
FOLLOWER_DELETE_SUCCESS_MESSAGE = 'Follower removed successfully'

FOLLOWER_DELETE_FOLLOW_ERROR_CODE = 2041
FOLLOWER_DELETE_FOLLOW_ERROR_MESSAGE = 'Invalid request! Users are not connected'

FOLLOWER_DELETE_DATA_EXCEPTION_CODE = 2042
FOLLOWER_DELETE_DATA_EXCEPTION_MESSAGE = 'Oops! something went wrong'

FOLLOWER_DELETE_INVALID_USERID_CODE = 2043
FOLLOWER_DELETE_INVALID_USERID_MESSAGE = 'Oops! something went wrong'

FOLLOWER_DELETE_MISSING_FIELDS_CODE = 2044
FOLLOWER_DELETE_MISSING_FIELDS_MESSAGE = 'Oops! something went wrong'

# 6. Unfollow user
UNFOLLOW_SUCCESS_CODE = 2050
UNFOLLOW_SUCCESS_MESSAGE = 'Follower removed successfully'

UNFOLLOW_FOLLOW_ERROR_CODE = 2051
UNFOLLOW_FOLLOW_ERROR_MESSAGE = 'Invalid request! Users are not connected'

UNFOLLOW_DATA_EXCEPTION_CODE = 2052
UNFOLLOW_DATA_EXCEPTION_MESSAGE = 'Oops! something went wrong'

UNFOLLOW_INVALID_USERID_CODE = 2053
UNFOLLOW_INVALID_USERID_MESSAGE = 'Oops! something went wrong'

UNFOLLOW_MISSING_FIELDS_CODE = 2054
UNFOLLOW_MISSING_FIELDS_MESSAGE = 'Oops! something went wrong'

# 7. Search User

SEARCH_USER_SUCCESS_CODE = 2060
SEARCH_USER_SUCCESS_MESSAGE = 'Users retrieved successfully'

SEARCH_USER_DATA_EXCEPTION_CODE = 2061
SEARCH_USER_DATA_EXCEPTION_MESSAGE = 'Oops! something went wrong'

# 8. Get Followers
GET_FOLLOWER_LIST_SUCCESS_CODE = 2070
GET_FOLLOWER_LIST_SUCCESS_MESSAGE = 'Follower list retrieved successfully'

GET_FOLLOWER_LIST_INVALID_USERID_CODE = 2071
GET_FOLLOWER_LIST_INVALID_USERID_MESSAGE = 'Oops! something went wrong'

# 9. Get Followed users
GET_FOLLOWED_LIST_SUCCESS_CODE = 2080
GET_FOLLOWED_LIST_SUCCESS_MESSAGE = 'Followed list retrieved successfully'

GET_FOLLOWED_LIST_INVALID_USERID_CODE = 2081
GET_FOLLOWED_LIST_INVALID_USERID_MESSAGE = 'Oops! something went wrong'

# 8. Get other user's Followers
GET_OTHER_FOLLOWER_LIST_SUCCESS_CODE = 2090
GET_OTHER_FOLLOWER_LIST_SUCCESS_MESSAGE = 'Follower list retrieved successfully'

GET_OTHER_FOLLOWER_LIST_INVALID_USERID_CODE = 2091
GET_OTHER_FOLLOWER_LIST_INVALID_USERID_MESSAGE = 'Oops! something went wrong'

# 9. Get other user's Followed users
GET_OTHER_FOLLOWED_LIST_SUCCESS_CODE = 2100
GET_OTHER_FOLLOWED_LIST_SUCCESS_MESSAGE = 'Followed list retrieved successfully'

GET_OTHER_FOLLOWED_LIST_INVALID_USERID_CODE = 2101
GET_OTHER_FOLLOWED_LIST_INVALID_USERID_MESSAGE = 'Oops! something went wrong'

# ------------------Notifications-----------------------
# Notifications start
# 1. Get notifications
NOTIFICATIONS_GET_LIST_SUCCESS_CODE = 4000
NOTIFICATIONS_GET_LIST_SUCCESS_MESSAGE = 'Notifications retrieved successfully'

NOTIFICATIONS_GET_LIST_INVALID_USERID_CODE = 4001
NOTIFICATIONS_GET_LIST_INVALID_USERID_MESSAGE = 'Oops! something went wrong'

# 2. Update value of read_notification
NOTIFICATIONS_UPDATE_READ_STATUS_SUCCESS_CODE = 4020
NOTIFICATIONS_UPDATE_READ_STATUS_SUCCESS_MESSAGE = 'Notifications marked as read'

NOTIFICATIONS_UPDATE_READ_STATUS_INVALID_USERID_CODE = 4021
NOTIFICATIONS_UPDATE_READ_STATUS_INVALID_USERID_MESSAGE = 'Oops! something went wrong'


# 3. Get value of read_notification
NOTIFICATIONS_GET_READ_STATUS_SUCCESS_CODE = 4030
NOTIFICATIONS_GET_READ_STATUS_SUCCESS_MESSAGE = 'Notifications status retrieved successfully!'

NOTIFICATIONS_GET_READ_STATUS_INVALID_USERID_CODE = 4031
NOTIFICATIONS_GET_READ_STATUS_INVALID_USERID_MESSAGE = 'Oops! something went wrong'

# --------------------Posts-----------------------
# Posts
# 1. Create New Post
POST_CREATE_SUCCESS_CODE = 5000
POST_CREATE_SUCCESS_MESSAGE = 'New post has been created'

POST_CREATE_MISSING_FIELDS_CODE = 5001
POST_CREATE_MISSING_FIELDS_MESSAGE = 'Oops! something went wrong'

POST_CREATE_DATA_EXCEPTION_CODE = 5002
POST_CREATE_DATA_EXCEPTION_MESSAGE = 'Oops! something went wrong'

# 2. Like Post
POST_LIKE_SUCCESS_CODE = 5010
POST_LIKE_SUCCESS_MESSAGE = 'User liked the post successfully'

POST_LIKE_ALREADY_LIKED_ERROR_CODE = 5011
POST_LIKE_ALREADY_LIKED_ERROR_MESSAGE = 'User has already liked the post'

POST_LIKE_MISSING_FIELDS_CODE = 5012
POST_LIKE_MISSING_FIELDS_MESSAGE = 'Oops! something went wrong'

POST_LIKE_DATA_EXCEPTION_CODE = 5013
POST_LIKE_DATA_EXCEPTION_MESSAGE = 'Oops! something went wrong'

# 3. Unlike Post
POST_UNLIKE_SUCCESS_CODE = 5020
POST_UNLIKE_SUCCESS_MESSAGE = 'User unliked the post successfully'

POST_UNLIKE_NOT_LIKED_ERROR_CODE = 5021
POST_UNLIKE_NOT_LIKED_ERROR_MESSAGE = 'User has not liked the post'

POST_UNLIKE_MISSING_FIELDS_CODE = 5022
POST_UNLIKE_MISSING_FIELDS_MESSAGE = 'Oops! something went wrong'

POST_UNLIKE_DATA_EXCEPTION_CODE = 5023
POST_UNLIKE_DATA_EXCEPTION_MESSAGE = 'Oops! something went wrong'

# 4. Add Comment Post
POST_ADD_COMMENT_SUCCESS_CODE = 5030
POST_ADD_COMMENT_SUCCESS_MESSAGE = 'User commented the post successfully'

POST_ADD_COMMENT_NOT_ALLOWED_ERROR_CODE = 5031
POST_ADD_COMMENT_NOT_ALLOWED_ERROR_MESSAGE = 'Comments are turned off for this post'

POST_ADD_COMMENT_MISSING_FIELDS_CODE = 5032
POST_ADD_COMMENT_MISSING_FIELDS_MESSAGE = 'Oops! something went wrong'

POST_ADD_COMMENT_DATA_EXCEPTION_CODE = 5033
POST_ADD_COMMENT_DATA_EXCEPTION_MESSAGE = 'Oops! something went wrong'

# 5. Delete Comment Post
POST_DELETE_COMMENT_SUCCESS_CODE = 5040
POST_DELETE_COMMENT_SUCCESS_MESSAGE = 'User deleted commented the post successfully'

POST_DELETE_COMMENT_NOT_AUTHORISED_CODE = 5041
POST_DELETE_COMMENT_NOT_AUTHORISED_MESSAGE = 'User is not authorised to delete comment'

POST_DELETE_COMMENT_MISSING_FIELDS_CODE = 5042
POST_DELETE_COMMENT_MISSING_FIELDS_MESSAGE = 'Oops! something went wrong'

POST_DELETE_COMMENT_DATA_EXCEPTION_CODE = 5043
POST_DELETE_COMMENT_DATA_EXCEPTION_MESSAGE = 'Oops! something went wrong'

# 6. Delete Post
POST_DELETE_SUCCESS_CODE = 5050
POST_DELETE_SUCCESS_MESSAGE = 'User deleted the post successfully'

POST_DELETE_NOT_AUTHORISED_CODE = 5051
POST_DELETE_NOT_AUTHORISED_MESSAGE = 'User is not authorised to delete post'

POST_DELETE_MISSING_FIELDS_CODE = 5052
POST_DELETE_MISSING_FIELDS_MESSAGE = 'Oops! something went wrong'

POST_DELETE_DATA_EXCEPTION_CODE = 5053
POST_DELETE_DATA_EXCEPTION_MESSAGE = 'Oops! something went wrong'