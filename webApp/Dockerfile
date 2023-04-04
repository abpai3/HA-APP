FROM python:3
WORKDIR /usr/src/app
COPY . . 
RUN pip install --upgrade pip 
RUN pip install -r requirement.txt
ENV DB_HOST postgres
ENV DB_USER postgres
ENV DB_PASS app@12345
ENV DB_NAME UserDetails
ENV DB_PORT 5432
EXPOSE 8080
CMD ["python","app.py"]
