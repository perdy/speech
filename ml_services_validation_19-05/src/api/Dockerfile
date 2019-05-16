FROM python:3.7-slim
LABEL maintainer="Perdy <perdy@perdy.io>"

# Create initial dir
ENV APPDIR=/srv/apps/sentiment-analysis
RUN mkdir -p $APPDIR
WORKDIR $APPDIR

# Install python requirements
ENV RUNTIME_PACKAGES libhdf5-serial-dev
ENV BUILD_PACKAGES build-essential
COPY requirements.txt $APPDIR/
RUN apt-get update && \
    apt-get install -q -y $BUILD_PACKAGES $RUNTIME_PACKAGES && \
    python -m pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y --auto-remove $BUILD_PACKAGES && \
    apt-get clean && \
    rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/*

# Copy application
COPY . $APPDIR

ENTRYPOINT ["python"]
