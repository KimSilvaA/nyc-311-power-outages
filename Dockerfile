FROM continuumio/miniconda3:latest

WORKDIR /app

COPY environment.yml /app/environment.yml
COPY requirements.txt /app/requirements.txt

RUN conda install -n base -c conda-forge mamba -y && conda clean -afy
RUN mamba env update -n base -f /app/environment.yml && conda clean -afy

COPY . /app

EXPOSE 8501
CMD ["python", "-m", "streamlit", "run", "src/analysis/dashboard_app.py", "--server.address=0.0.0.0", "--server.port=8501"]