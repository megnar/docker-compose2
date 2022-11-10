FROM python:3.9

COPY ./Hello_world.py ./

CMD ["python3", "Hello_world.py"]