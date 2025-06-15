# Use official Python slim image
FROM python:3.12-slim

# Install dependencies for Chrome + Selenium
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libxshmfence1 \
    --no-install-recommends

# Set Chrome for Testing version
ENV CHROME_VERSION=137.0.7151.70

# Download Chrome for Testing and unzip it
RUN wget -q https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/linux64/chromedriver-linux64.zip -O /tmp/chromedriver-linux64.zip && \
    unzip -j /tmp/chromedriver-linux64.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver-linux64.zip && \
    chmod +x /usr/local/bin/chromedriver


# Download matching Chromedriver and unzip it to /usr/local/bin
RUN wget -q https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/linux64/chromedriver-linux64.zip -O /tmp/chromedriver-linux64.zip && \
    unzip /tmp/chromedriver-linux64.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver-linux64.zip && \
    chmod +x /usr/local/bin/chromedriver

# Add Chrome for Testing binary folder to PATH
ENV PATH="/opt/chrome-linux64:${PATH}"

# Set CHROME_BIN env variable to point to Chrome binary for Selenium
ENV CHROME_BIN=/opt/chrome-linux64/chrome

# Set working directory
WORKDIR /app

# Copy your bot script (and any other files you need)
COPY bot.py ./

# Install Python dependencies
RUN pip install --no-cache-dir selenium

# Run the bot script
CMD ["python", "bot.py"]
