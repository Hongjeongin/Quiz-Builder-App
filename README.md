# Quiz-Builder-App

## Simple Description
- This is Quiz_builder_app.   
- User can make their quiz.   
- User can solve another user's quiz. and they can write solution like review for that quiz.   
- If user access to this app, they are issued token(access, refresh) with cookie.

### Settings
- Django version(latest) - 4.1.4
- Django Rest Framework version(latest) - 3.14.0
- Database: PostgreSQL version - 15.1   
ㄴ Using Louie’s docker container

### Doing history
> 
> #### 22-12-22
> - Make DRF(=Django Rest Framework) project and connect remote git
> - Database designed simply
> - Make models and make migrations and migrate for them(Database)
> - Study 'token(JWT(=JSON Web Token))' for using security measures

> #### 22-12-23
> - DRF simple jwt study and applying..

> #### 22-12-26
> - Make User CRUD with ModelViewSet, Serializer and DefaultRouter

> #### 22-12-27
> - Make Sign_in and Sign_out without token

> #### 22--12-28
> - Make Access token from refresh token   
>   ㄴ If Access token expired, it can be refresh   
>   ㄴ If Refresh token expired, it must be rejoin to app
