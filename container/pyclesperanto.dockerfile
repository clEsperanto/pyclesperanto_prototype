#FROM continuumio/anaconda3
#
#ENV WRK /run
#WORKDIR $WRK
#COPY . $WRK
#
#RUN conda init bash \
#    && . ~/.bashrc \
#    && conda env create -p $WRK/env -f ./environment.yaml
#
#ENTRYPOINT ["/run/runner.sh"]

FROM nvidia/cuda:11.3.1-base-ubuntu20.04

RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    sudo \
    git \
    bzip2 \
    libx11-6 \
 && rm -rf /var/lib/apt/lists/*

# Create a working directory
RUN mkdir /app
WORKDIR /app
ENV APP /app

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' --shell /bin/bash user && chown -R user:user /app
RUN echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-user
USER user

# All users can use /home/user as their home directory
ENV HOME=/home/user
RUN chmod 777 /home/user

# Set up the Conda environment
ENV CONDA_AUTO_UPDATE_CONDA=false \
    PATH=/home/user/miniconda/bin:$PATH
COPY . $APP
RUN curl -sLo ~/miniconda.sh https://repo.continuum.io/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh \
 && chmod +x ~/miniconda.sh \
 && ~/miniconda.sh -b -p ~/miniconda \
 && rm ~/miniconda.sh \
 && conda env create -p $APP/env -f $APP/environment.yaml \
 && conda clean -ya

# Custom runner that autoloads the environment - python support only
ENTRYPOINT ["/run/runner.sh"]
