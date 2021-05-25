#! /bin/bash
###
 # @Author: yuan
 # @Date: 2021-05-22 10:54:07
 # @LastEditTime: 2021-05-24 17:07:48
 # @FilePath: /python-flask/build.sh
### 

docker build -t app-flask:1.0.0 .

# docker run -ti --name app-flask -p 5000:5000 app-flask:1.0.0
# docker exec -ti app-flask /bin/bash  