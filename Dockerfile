FROM continuumio/miniconda3:latest

WORKDIR /app

COPY environment.yml /app/environment.yml
COPY requirements.txt /app/requirements.txt

COPY data/runtime /app/data/runtime
COPY src/analysis /app/src/analysis

# Install mamba in base
RUN conda install -n base -c conda-forge mamba -y && conda clean -afy

# Create the environment using the name in environment.yml
RUN mamba env create -f /app/environment.yml && conda clean -afy

# Use the new environment
SHELL ["conda", "run", "-n", "nyc-311-power-outages", "/bin/bash", "-c"]

EXPOSE 8501