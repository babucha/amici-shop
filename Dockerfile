### Build and install packages
FROM python:3.9 as build-python

RUN apt-get -y update \
  && apt-get install -y gettext \
  # Cleanup apt cache
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

### Final image
FROM python:3.9-slim

RUN groupadd -r saleor && useradd -r -g saleor saleor

RUN apt-get update \
  && apt-get install -y \
  libcairo2 \
  libgdk-pixbuf2.0-0 \
  liblcms2-2 \
  libopenjp2-7 \
  libpango-1.0-0 \
  libpangocairo-1.0-0 \
  libssl3 \
  libtiff6 \
  libwebp7 \
  libxml2 \
  libpq5 \
  shared-mime-info \
  mime-support \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN echo 'image/webp webp' >> /etc/mime.types

RUN mkdir -p /app/media /app/static \
  && chown -R saleor:saleor /app/

COPY --from=build-python /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/
COPY . /app
WORKDIR /app

ARG ALLOWED_CLIENT_HOSTS
ENV ALLOWED_CLIENT_HOSTS ${ALLOWED_CLIENT_HOSTS:-amicisarti.ru}

ARG STATIC_URL
ENV STATIC_URL ${STATIC_URL:-/static/}
ARG SECRET_KEY
ENV SECRET_KEY ${SECRET_KEY:-%r@-$ad2p21m%hb^woxl^-k^xf6!^#^f+a^91pxd#%c1mefmf!k}

RUN chmod -R 755 /app/ && \
  SECRET_KEY=${SECRET_KEY} STATIC_URL=${STATIC_URL} python3 manage.py collectstatic --no-input

EXPOSE 8000
ENV PYTHONUNBUFFERED 1

CMD ["gunicorn", "--bind", ":8000", "--workers", "4", "--worker-class", "saleor.asgi.gunicorn_worker.UvicornWorker", "saleor.asgi:application"]
