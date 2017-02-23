FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD ./requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install nodejs -y
RUN apt-get install npm -y
RUN apt-get install node -y
RUN npm install --save-dev react webpack webpack-bundle-tracker babel babel-loader
RUN mkdir -p assets/js
RUN touch webpack.config.js
RUN touch assets/js/index.js
