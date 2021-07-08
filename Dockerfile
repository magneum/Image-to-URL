FROM python:latest
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"
RUN apt-get update && apt-get upgrade -y

RUN python -m pip install --upgrade pip
RUN git clone https://github.com/HypeVoidSoul/Image-to-URL.git
RUN cd Image-to-URL
WORKDIR /Image-to-URL
RUN pip3 install -U -r requirements.txt
CMD python3 -m ıɱąɠɛ2ųཞƖ
