FROM ubuntu:latest
############################## HEADER ##########################################
#
# Galantelab Development Team <bioinfo@mochsl.org.br>
#
# Some useful commands:
#    $ docker build . -t galantelab/base:latest -t galantelab/base:2.0.0
#    $ docker run --rm -it galantelab/base:latest /bin/bash
#    $ docker push galantelab/base:latest
#
################################################################################



############################## PREAMBLE ########################################

MAINTAINER Galantelab Development Team <bioinfo@mochsl.org.br>
LABEL architecture="x86_64" name="galantelab/base"


ENV CONTAINER galantelab/base
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


# The default user at container's startup: lion.
RUN groupadd -f -g 9999 docker
RUN useradd -d /home/lion -ms /bin/bash -u 1000 -g 9999 -p lion lion


# Basic installations.
RUN apt-get -y update --fix-missing
RUN apt-get -y upgrade
RUN apt-get -y install \
	locales \
	ca-certificates \
	curl \
	wget \
	git \
	libcurl4-openssl-dev \
	libncurses5-dev \
	libtbb-dev \
	libssl-dev \
	libbz2-dev \
	liblzma-dev \
	zlib1g-dev \
	tzdata \
	pigz \
	gcc \
	#gfortran \
	#ninja-build \
	#build-essential \
	#pkg-config \
	make \
	less \
	nano
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV PATH ./.local/bin:/home/lion/.local/bin:$PATH


WORKDIR /home
USER lion

# Finishing.
CMD [ "/bin/bash" ]
