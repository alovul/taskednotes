# notes/context_processors.py

def user_profile_picture(request):
    if not request.user.is_authenticated:
        return {}
    else:
        # Assuming the user profile picture is directly linked to your user model for simplicity
        # Adjust the following line according to your model structure
        profile_picture_url = request.user.userprofile.profile_picture.url if hasattr(request.user, 'user') and request.user.user.profile_picture else None
        return {'profile_picture_url': profile_picture_url}
