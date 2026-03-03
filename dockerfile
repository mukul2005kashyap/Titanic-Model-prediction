# Base image 
FROM python:3.10-slim

# set working dir
WORKDIR /app

# copy
COPY r.txt .

# Run
RUN pip install --no-cache-dir -r r.txt

COPY . .

EXPOSE 8501

CMD ["streamlit" , "run" , "main.py" , "--server.port=8501", "--server.address=0.0.0.0"]
