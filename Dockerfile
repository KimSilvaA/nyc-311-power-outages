FROM continuumio/miniconda3:latest

WORKDIR /app

COPY environment.yml /app/environment.yml
RUN conda env update -n base -f /app/environment.yml && conda clean -afy

COPY . /app

EXPOSE 8501
CMD ["streamlit", "run", "src/analysis/dashboard_app.py", "--server.address=0.0.0.0", "--server.port=8501"]