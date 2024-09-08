# syntax=docker/dockerfile:1
FROM python:3.9
#RUN pip3 install --upgrade pip

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#COPY  static/ /Image_Encrypter/static/
#COPY templates/ /Image_Encrypter/templates

COPY . .
EXPOSE 5000
CMD ["python", "views.py"]