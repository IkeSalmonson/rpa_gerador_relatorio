FROM python:3.12.3-alpine3.19
#python_playground


WORKDIR /usr/share/rpa_projeto_relatorio
COPY ./requirements.txt ./requirements.txt
RUN  pip install -r ./requirements.txt

# Modificado para montar o volume completo do projeto para o container de desenvolvimento 
COPY ./tests ./tests
COPY ./data_example ./data_example
COPY ./setup.py ./
COPY ./pyproject.toml ./
COPY ./gerador_relatorio ./gerador_relatorio

RUN pip install -e ./ 
