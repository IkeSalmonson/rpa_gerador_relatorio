FROM python:3.12.3-alpine3.19
#python_playground


WORKDIR /usr/share/gerador_relatorios
COPY ./requirements.txt ../requirements.txt
RUN  pip install -r ../requirements.txt

COPY ./tests ../tests
COPY ./data_example ../data_example
COPY ./setup.py ../

COPY ./pyproject.toml ../



COPY ./gerador_relatorios ./

RUN pip install -e ../ 
