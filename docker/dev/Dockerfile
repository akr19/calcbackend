FROM akr19/calcbackend-base:latest
MAINTAINER akr19 <akr19@akr19.akr19>

ENV TERM=xterm-256color

# Install dev/build dependencies
RUN apt-get update && \
    apt-get install -qy python-dev && \
    apt-get install -qy libmysqlclient-dev && \
    apt-get install -qy ipython

# Activate virtual environment and install wheel support
RUN . /appenv/bin/activate && \
    pip install wheel --upgrade 

# PIP environment variables (NOTE: must be set after installing wheels)
ENV WHEELHOUSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache

# OUTPUT: Build artefacts (Wheels)
VOLUME /wheelhouse

# OUTPUT: Build cache
VOLUME /build

# OUTPUT: Test reports 
VOLUME /reports

COPY scripts/test.sh /usr/local/bin/test.sh
RUN chmod +x /usr/local/bin/test.sh

# Set defaults for entrypoint and command string
ENTRYPOINT ["test.sh"]
CMD ["nosetests","--rednose","--with-coverage","--cover-package=calculator","--verbosity=2"]

# Add application source
COPY src /application
WORKDIR /application

