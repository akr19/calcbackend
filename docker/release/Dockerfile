FROM akr19/calcbackend-base:latest

# Copy application artifacts
COPY target /wheelhouse

# Install application
RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse calcbackend
# && \
#    rm -rf /wheelhouse
