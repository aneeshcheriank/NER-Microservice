FROM python:3.12-slim

# create an app directory in the container
RUN mkdir -p /app

# copy the required files to the container
COPY app.py /app/
COPY src/. /app/src/
COPY requirements.txt /app/

# set the working directory
WORKDIR /app

# install the dependencies
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt &&\
    python -m spacy download en_core_web_sm

# Specify the port 
EXPOSE 8080

# Commad to run the applciation
CMD ["app.py"]
ENTRYPOINT ["python"]