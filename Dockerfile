ARG DJANGO_CONTAINER_VERSION=2.0.1

FROM us-docker.pkg.dev/uwit-mci-axdd/containers/django-container:${DJANGO_CONTAINER_VERSION} as app-container

USER acait

COPY --chown=acait:acait ./docker /app/
COPY --chown=acait:acait ./setup.py /app/
COPY --chown=acait:acait ./uw_spotseeker/ /app/uw_spotseeker

COPY --chown=acait:acait ./conf/urls.py /app/project/urls.py
COPY --chown=acait:acait ./conf/settings.py /app/project/settings.py
COPY --chown=acait:acait ./conf/test.sh /app/test.sh

WORKDIR /app/

RUN . /app/bin/activate && pip install --no-cache-dir .
RUN /app/bin/python manage.py migrate
