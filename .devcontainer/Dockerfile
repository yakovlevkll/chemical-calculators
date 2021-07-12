# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.187.0/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3.9"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends curl

# Poetry package manager
USER vscode
ARG INSTALL_POETRY="true"
ARG POETRY_VERSION="1.1.6"
RUN if [ "${INSTALL_POETRY}" = "true" ]; then curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - --version ${POETRY_VERSION}; fi
ENV PATH "/home/vscode/.poetry/bin:$PATH"

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp
