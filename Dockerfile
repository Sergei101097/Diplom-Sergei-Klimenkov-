FROM python:3.9.9-buster as base

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.7

# Install Google Chrome.
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# Install Chromedriver.
RUN apt-get install -yqq unzip
RUN export chrome_version=$(google-chrome --version | grep -P -o --regexp='\d+\.\d+\.\d+') && \
    wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE_$chrome_version`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Install poetry.
RUN pip install "poetry==$POETRY_VERSION"
RUN pip install --upgrade pip
# Copy the poetry files to speed up builds.
WORKDIR /home/sergei/python-ui-framework
COPY poetry.lock pyproject.toml ./

# Install dependencies via Poetry.
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi
RUN pip install Faker
RUN pip install webdriver_manager
RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
  && tar xzvf docker-17.04.0-ce.tgz \
  && mv docker/docker /usr/local/bin \
  && rm -r docker docker-17.04.0-ce.tgz
# Copy the source code into the image.
#COPY framework ./framework
COPY BaseApp ./BaseApp
COPY PageObject ./PageObject
COPY tests ./tests
#COPY poetry.lock .
