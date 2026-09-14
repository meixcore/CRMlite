FROM python:3.13

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV USER=django_web
ENV GROUP=maintenance
ENV WORK_DIR=/usr/src/app

RUN mkdir -p ${WORK_DIR}

WORKDIR ${WORK_DIR}

RUN addgroup --system ${GROUP} && \
    adduser --system --ingroup ${GROUP} ${USER}

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-root --no-interaction --no-ansi

COPY . ${WORK_DIR}

RUN mkdir -p ${WORK_DIR}/app/static && \
    chown -R ${USER}:${GROUP} ${WORK_DIR}

WORKDIR ${WORK_DIR}/app

USER ${USER}

ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]