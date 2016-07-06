Things to change in actual cbt app:
Note that in settings you would have to modify media_url to a more generalised form when merging. (in your directory structure you just have avatarimages folder as media url. It would be better to change it to some other name with images present in a subdirectory with an apt name as per the app )
Views need to be modified for handling the user playing the game. User should be identified by session login at the starting instead of the url as in the current state of things.
Look at comments on line 26 in views.py and line 11 in models.py