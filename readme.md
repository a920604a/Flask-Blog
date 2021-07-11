<!--
 * @Author: yuan
 * @Date: 2021-05-23 13:27:07
 * @LastEditTime: 2021-05-25 13:47:02
 * @FilePath: /python-flask/readme.md
-->

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
docker-compose -d [--build]
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
- use docker to build blod, cannot send register validation email