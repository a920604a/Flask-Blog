'''
Author: yuan
Date: 2021-05-22 19:59:11
LastEditTime: 2021-05-25 13:40:21
FilePath: /python-flask/app.py
'''
from blog import create_app

app = create_app()
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
    # app.run(debug=True, host='0.0.0.0', port=5000)


