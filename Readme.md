# Cold Email Generator

A GenAI-powered Streamlit application that leverages Large Language Models to automatically generate personalized cold emails for job applications. It intelligently analyzes job postings, matches them with your portfolio, and creates tailored professional emails using advanced natural language processing.

## Features

- **URL-based Job Analysis**: Extracts job details from provided career page URLs
- **Portfolio Matching**: Automatically matches your skills and projects with job requirements
- **Customized Email Generation**: Creates professional, personalized cold emails using Groq LLM
- **Portfolio Management**: Maintains a database of your projects and skills for relevant examples

## Tech Stack

### Core Technologies
- **Frontend**: Streamlit
- **Backend**: Python

### AI/ML Components
- **LLM Integration**: Groq API (llama-3.3-70b-versatile)
- **AI Framework**: LangChain for composable AI applications
- **Vector Database**: ChromaDB for semantic search and skill matching

### Additional Libraries
- langchain_groq for LLM integration
- pandas for data processing
- chromadb for vector storage
- python-dotenv for environment management
- dnspython for URL processing

## Setup

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd cold-email-generator
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**
   - Create a `.env` file in the root directory
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_api_key_here
     or use TEMP api key provided in the files
     ```

4. **Portfolio Setup**
   use Portfolio generator.ipynb to generate your portfolio which includes links to your github. It will generate the my_portfolio.csv uing your Resume.
   - Place your `my_portfolio.csv` in the `resource` folder
   - CSV format:
     ```
     Techstack,Links
     "Python, ML, AI","https://github.com/..."
     ```

5. **Run the Application**
   ```bash
   streamlit run main.py
   ```

## Usage

1. Launch the application
2. Enter the job posting URL in the input field
3. Click "Generate email"
4. Review and copy the generated email

## Project Structure

```
cold-email-generator/
│
├── main.py           # Main Streamlit application
├── chains.py         # LLM chain configurations
├── portfolio.py      # Portfolio management
├── utils.py          # Utility functions
│
├── resource/
│   └── my_portfolio.csv  # Your portfolio data
│
└── requirements.txt  # Project dependencies
```

## Features Breakdown

### AI-Powered Job Analysis
- Uses LLM to extract and understand key information from job postings
- Employs natural language processing to identify required skills and experience
- Intelligent processing of role descriptions and requirements
- Semantic understanding of job context and company needs

### AI-Enhanced Portfolio Matching
- Vector database with semantic search capabilities
- Intelligent mapping of skills to job requirements using embeddings
- Context-aware project recommendation system
- Dynamic relevance scoring of portfolio items

### LLM-Powered Email Generation
- AI-driven professional email structure and tone
- Context-aware personalization based on job details and company background
- Intelligent integration of relevant portfolio links and experiences
- Natural language generation for compelling and authentic emails

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.
