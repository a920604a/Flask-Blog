#! /bin/bash
###
 # @Author: yuan
 # @Date: 2021-05-22 10:54:07
 # @LastEditTime: 2021-05-24 17:07:48
 # @FilePath: /python-flask/build.sh
### 

docker build -t app-flask:1.0.0 .

<<<<<<< HEAD
# docker run -d -ti --name app-flask -p 5000:5000 app-flask:1.0.0 
=======
# docker run -d -ti --name app-flask -p 5000:5000 app-flask:1.0.0
>>>>>>> 1d482ab3e4f67d9383fe79392e8247647e748ceb
# docker exec -ti app-flask /bin/bash  