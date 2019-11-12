FROM python:3.7-slim
LABEL maintainer="Perdy <perdy@perdy.io>"

ENV PATH=$HOME/.gauge:$PATH

# Create initial dir
ENV APPDIR=/srv/apps/sentiment-analysis
RUN mkdir -p $APPDIR
WORKDIR $APPDIR

# Install Prerequisites.
RUN apt-get update && apt-get install -q -y \
  apt-transport-https \
  gnupg2 \
  ca-certificates

# Install gauge
RUN apt-key adv --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys 023EDB0B && \
  echo deb https://dl.bintray.com/gauge/gauge-deb stable main | tee -a /etc/apt/sources.list

RUN apt-get update && apt-get -y install gauge

# Install gauge plugins
RUN gauge telemetry off && \
    gauge install python && \
    gauge install html-report && \
    gauge install xml-report && \
    gauge install screenshot && \
    gauge update -c && \
    gauge update -a

# Install python requirements
COPY requirements.txt $APPDIR/
RUN python -m pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy tests
COPY . $APPDIR

ENTRYPOINT ["gauge"]