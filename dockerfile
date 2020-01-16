FROM python:3
RUN mkdir /code
COPY requirements.txt /code/
RUN pip3 install -r /code/requirements.txt
COPY title_scrape.py /code/
CMD ["python","/code/title_scrape.py"]