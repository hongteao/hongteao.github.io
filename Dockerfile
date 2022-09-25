ARG FROM_TAG=3.7-slim-buster
FROM python:${FROM_TAG}

# Install python dependencies
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt --no-cache-dir && \
    rm -rf /root/.cache/

COPY policy_sentry /tmp/policy_sentry
RUN pip install /tmp/policy_sentry --no-cache-dir && \
    rm -rf /root/.cache/

RUN mkdir /workspace

COPY app.py /workspace

WORKDIR /workspace

CMD python -m uvicorn app:app --host 0.0.0.0 --port 8000
