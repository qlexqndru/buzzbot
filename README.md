# 🚀 BuzzBot: Intelligent Chat Assistant with Web Search Integration

## 🧠 About BuzzBot

BuzzBot is an intelligent chatbot built with [Streamlit](https://streamlit.io/) and [Langchain](https://www.langchain.com/) that leverages web search capabilities to provide up-to-date and accurate information. Whether you're seeking the latest trends in artificial intelligence or need concise summaries from reputable sources, BuzzBot is here to assist!

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Docker Setup](#docker-setup)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🌟 Features

- **Intelligent Conversations:** Engage in natural, human-like dialogue.
- **Web Search Integration:** Fetch and summarize the latest information from the web.
- **Customizable Search Parameters:** Tailor your searches with options like site, filetype, intitle, and exclusion keywords.
- **Streamlit Interface:** User-friendly and interactive web interface.
- **Docker Support:** Easily deployable using Docker containers.
- **Traceable Interactions:** Utilize Langsmith for monitoring and tracing chatbot interactions.

## 🛠 Installation

### Prerequisites

- [Python 3.11](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Docker](https://www.docker.com/get-started) (optional, for Docker setup)

### Clone the Repository

```bash
git clone https://github.com/yourusername/buzzbot.git
cd buzzbot
```

### Install Dependencies

```bash
pip install --no-cache-dir -r requirements.txt
```

## 🔧 Configuration

Create a `.env` file in the root directory and add your API keys:
```env
SERPAPI_API_KEY=your_actual_serpapi_api_key
GROQ_API_KEY=your_actual_groq_api_key
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=your_actual_langchain_api_key
LANGCHAIN_PROJECT=bdf_chatbot
LANGCHAIN_TRACING_V2=true
```
**Note:** Replace the placeholder values with your actual API keys.

## 🚀 Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

Open your browser and navigate to `http://localhost:8501` to interact with BuzzBot.

## 🐳 Docker Setup

### Build the Docker Image

```bash
docker build -t buzzbot .
```

### Run the Docker Container

```bash
docker run -d -p 8501:8501 --env-file .env buzzbot
```

Access the application at `http://localhost:8501`.

## 📁 Project Structure

```bash
buzzbot/
│
├── app.py                  # Streamlit application
├── web_search.py           # Web search functionality using SerpAPI
├── langchain_handler.py    # Langchain handler for processing inputs
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── .env                    # Environment variables
├── README.md               # This README file
└── assets/                 # Images and other assets
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "Add YourFeature"`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request.

For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 📬 Contact

- qlexqndru – alexqndru@xandru.co
- GitHub: https://github.com/qlexqndru/buzzbot

Made with ❤️ by qlexqndru
