# AI Resume Skill Gap Analyzer

A Day-1 mini project that uses AI to analyze resumes and identify skill gaps for target job roles.

## Problem Statement

Job seekers often struggle to identify which skills they're missing for their target roles. This tool leverages AI to:
- Analyze resume content semantically (not just keyword matching)
- Extract existing skills from the resume
- Identify missing or weak skills for a specific job role
- Provide actionable suggestions for improvement

This helps candidates understand their gaps and take concrete steps to improve their competitiveness.

## AI Tool Used

**Google Gemini AI** (`gemini-1.5-flash`)

We use Google's Gemini AI model through the `google-generativeai` SDK. The AI performs:
- Semantic understanding of resume content
- Intelligent skill extraction (technical and soft skills)
- Role-specific skill requirement analysis
- Contextual gap identification
- Personalized improvement recommendations

The AI goes beyond simple keyword matching by understanding context, implied skills, and industry standards.

## How It Works

1. **User Input**
   - Paste resume text into the text area
   - Enter target job role (e.g., "Machine Learning Engineer")

2. **AI Processing**
   - Resume and job role are sent to Google Gemini via API
   - Gemini analyzes the resume using semantic understanding
   - AI extracts skills mentioned or implied in the resume
   - AI identifies expected skills for the target role
   - AI compares both and finds gaps

3. **Structured Output**
   - **Extracted Skills**: All technical skills, soft skills, tools, and frameworks found
   - **Missing/Weak Skills**: Critical skills absent or underdeveloped for the role
   - **Suggestions**: Actionable recommendations to improve

4. **Download Results**
   - Analysis can be downloaded as a text file for future reference

## Sample Input / Output

### Sample Input

**Resume Text:**
```
John Doe
Software Developer

Experience:
- Built web applications using React and Node.js
- Worked with MongoDB databases
- Developed REST APIs
- Collaborated with cross-functional teams

Skills: JavaScript, HTML, CSS, Git
```

**Target Job Role:** `Machine Learning Engineer`

### Sample Output

```markdown
## 1. Extracted Skills

Technical Skills:
- JavaScript (React, Node.js)
- HTML/CSS
- MongoDB (NoSQL databases)
- REST API development
- Git version control

Soft Skills:
- Team collaboration
- Cross-functional communication

## 2. Missing / Weak Skills

Critical Missing Skills:
- Python programming (essential for ML)
- Machine Learning frameworks (TensorFlow, PyTorch, Scikit-learn)
- Data processing libraries (Pandas, NumPy)
- Statistical analysis and mathematics
- Model training and evaluation
- Deep learning concepts
- ML deployment and MLOps
- Cloud platforms (AWS/GCP/Azure) for ML

Weak Areas:
- No data science or ML project experience mentioned
- No exposure to ML algorithms or model development
- Limited mathematical/statistical background shown

## 3. Suggestions

Immediate Actions:
1. Learn Python - it's the primary language for ML
2. Complete ML courses (Coursera, fast.ai, deeplearning.ai)
3. Build 2-3 ML projects (start with Kaggle competitions)
4. Study key algorithms: regression, classification, clustering, neural networks
5. Get familiar with Jupyter notebooks and data visualization
6. Learn Scikit-learn for classical ML and TensorFlow/PyTorch for deep learning
7. Add ML projects to your resume with clear problem statements and results
8. Consider a nanodegree or certification in Machine Learning
9. Highlight any transferable skills from software development (API building could relate to ML model deployment)

Long-term Development:
- Deepen mathematical foundations (linear algebra, calculus, statistics)
- Explore MLOps and model deployment pipelines
- Learn about experiment tracking and model versioning
```

## Tech Stack

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.8+ |
| **UI Framework** | Streamlit |
| **AI Model** | Google Gemini (gemini-1.5-flash) |
| **AI SDK** | google-generativeai |
| **Environment** | python-dotenv |
| **Deployment** | Local (can be deployed to Streamlit Cloud) |

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key

### Steps

1. **Clone or download the project**
   ```bash
   cd AI_Resume_Gap_Analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the app**
   
   Open your browser and go to `http://localhost:8501`

## Usage

1. Open the application in your browser
2. Paste your complete resume text in the left text area
3. Enter your target job role in the right input field
4. Click "Analyze Resume" button
5. Wait for AI analysis (takes a few seconds)
6. Review the structured results
7. Optionally download the analysis for future reference

## Project Structure

```
AI_Resume_Gap_Analyzer/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── .env               # Environment variables (create this)
```

## Features

✅ Text-based resume input  
✅ AI-powered semantic analysis  
✅ Structured output with clear sections  
✅ Downloadable results  
✅ Input validation and error handling  
✅ Clean, professional UI  
✅ No database or authentication needed  

## Limitations

- Text-only input (no PDF upload)
- No resume storage or history
- Requires active internet connection for Gemini API
- Analysis quality depends on resume detail and clarity

## Future Enhancements (Out of Scope for Day-1)

- PDF resume upload support
- Multiple resume comparison
- Skill trend analysis
- Learning resource recommendations
- User accounts and history

## License

This is a mini-project for learning purposes.

## Author

Built as a Day-1 AIML Engineering Project
