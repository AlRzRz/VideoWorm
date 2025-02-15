# 🎥 VideoWorm

VideoWorm is a Python-based application that allows users to input a YouTube video URL or ID, fetches the video's transcript using the YouTube Transcript API, and then analyzes the transcript using the OpenAI API (GPT-4o model). The analysis provides a structured summary of the video's content.

## ✨ Features

- 🎯 Extracts YouTube video ID from a URL or directly uses the provided ID.
- 📜 Fetches the transcript of the video using the YouTube Transcript API.
- 🤖 Analyzes the transcript using OpenAI's GPT-4o model to provide a structured summary.
- 🖥️ Displays the analysis in a user-friendly popup window.

## 🛠️ Setup Instructions

To set up the VideoWorm project on your local machine, follow these steps:

### Prerequisites

- 🐍 Python 3.x installed on your system.
- 🔑 An OpenAI API key.

### Installation

1. **Clone the Repository**

   Clone the repository to your local machine using:

   ```bash
   git clone <repository-url>
   cd VideoWorm
   ```

2. **Create a Virtual Environment**

   Create a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   Install the required dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Environment Variables**

   Create a `.env` file in the root directory of the project and add your OpenAI API key:

   ```plaintext
   SECRETKEY=your_openai_api_key_here
   ```

### 🚀 Usage

1. Run the main script:

   ```bash
   python main.py
   ```

2. Follow the on-screen instructions to input a YouTube video URL or ID.

3. View the analyzed transcript in the popup window.

### 📂 Project Structure

- `main.py`: The main script that handles user input, fetches the transcript, and displays the analysis.
- `ai.py`: Contains the logic for interacting with the OpenAI API.
- `display.py`: Handles the display of the analysis result in a popup window.
- `prompts.py`: Contains the prompts used for the OpenAI API.
- `requirements.txt`: Lists the Python dependencies required for the project.

### 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

### 📜 License

This project is licensed under the MIT License.
