# AI-Powered Resume Screener

This project is an AI-powered resume screener that utilizes Hugging Face Transformers and Streamlit to provide a user-friendly interface for uploading and processing resumes. The application parses resumes and matches skills against job descriptions, helping recruiters and job seekers streamline the hiring process.

## Project Structure

```
ai-resume-screener
├── src
│   ├── main.py                # Entry point for the application
│   ├── ui
│   │   └── streamlit_app.py   # Streamlit user interface code
│   ├── models
│   │   └── resume_model.py     # AI model for parsing resumes
│   ├── utils
│   │   └── helpers.py          # Utility functions
│   └── data
│       └── sample_resumes.txt  # Sample resumes for testing
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .streamlit
│   └── config.toml            # Streamlit configuration
├── .gitignore                  # Files to ignore in version control
└── deployment
    ├── render.yaml            # Deployment configuration for Render
    └── vercel.json            # Deployment configuration for Vercel
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd ai-resume-screener
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application:**
   ```
   streamlit run src/main.py
   ```

2. **Upload resumes through the Streamlit interface and view the parsed results.**

## Deployment

### Streamlit Cloud

To deploy on Streamlit Cloud, follow the instructions on the [Streamlit Cloud documentation](https://docs.streamlit.io/streamlit-cloud).

### Render

To deploy on Render, use the `render.yaml` configuration file located in the `deployment` directory.

### Vercel

To deploy on Vercel, use the `vercel.json` configuration file located in the `deployment` directory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.