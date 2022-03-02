Flask-Blog
===

## Installation
- option 1
```shell
pip install -r requirements.txt
flask run  # or python app.py
```
- option 2
```shell=
docker-compose up -d [--build]
```
- Note : Remember add env variable in Dockerfile, like:
```dockerfile=
ENV EMAIL_USER=YOUR_EMAIL
ENV EMAIL_PASS=YOUR_EMAIL_PASSWORD
# ENV SCERET_KEY=0
ENV SQL_DB_URL=sqlite:///site.db
ENV MAIL_SERVER=smtp.googlemail.com
```
## Enjoy  
- Open your Browser and type `http://localhost:5000/home`
- if you need, please create database table struction `db.create_all()`
## Note
- blog/static put somthing like image, css 
- blog/template put html file

## TODO
devlop to 

[reference](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=1)

- use docker to build blod, cannot send register validation email


## UI
![](/blog/static/Home.png)
![](/blog/static/account.png)
> 可上傳大頭貼

![](/blog/static/post.png)
> 支持markdown 語法