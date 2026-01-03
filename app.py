"""
AI Resume Skill Gap Analyzer
A Streamlit application that uses Groq AI to analyze resumes
and identify skill gaps for target job roles.
"""

import streamlit as st
from groq import Groq
import os
import sys
import traceback
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Groq API
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

print("=" * 60)
print("🔍 CHECKING API KEY CONFIGURATION")
print("=" * 60)

if not GROQ_API_KEY:
    error_msg = "⚠️ GROQ_API_KEY not found in environment variables!"
    print(f"ERROR: {error_msg}", file=sys.stderr)
    st.error(error_msg + " Please set it in your .env file.")
    st.stop()
else:
    print(f"✓ API Key found: {GROQ_API_KEY[:20]}...{GROQ_API_KEY[-4:]}")
    print(f"✓ API Key length: {len(GROQ_API_KEY)} characters")

try:
    client = Groq(api_key=GROQ_API_KEY)
    print("✓ Groq API configured successfully")
except Exception as e:
    error_msg = f"Failed to configure Groq API: {str(e)}"
    print(f"ERROR: {error_msg}", file=sys.stderr)
    traceback.print_exc()
    st.error(error_msg)
    st.stop()

print("=" * 60)
print()


def analyze_resume(resume_text: str, job_role: str) -> str:
    """
    Analyze resume using Groq AI.
    
    Args:
        resume_text: The resume content as plain text
        job_role: Target job role for analysis
        
    Returns:
        Structured analysis from Groq AI
    """
    
    # Create the prompt for Groq
    prompt = f"""
You are an AI hiring evaluator, not a resume summarizer.

Your task is to STRICTLY compare a candidate's resume against a target job role and identify gaps.

Follow these rules:
- You MUST identify missing or weak skills.
- If a skill required for the role is not clearly mentioned or demonstrated in the resume, treat it as MISSING.
- Do NOT only list present skills.
- Do NOT generalize.
- Do NOT skip any section.
- If no skills are missing (very rare), explicitly write: "None – resume strongly matches the role."

Steps to follow:
1. Infer the core skill requirements for the given job role based on current industry standards.
2. Extract the skills explicitly or implicitly present in the resume.
3. Compare both lists.
4. Identify skills that are missing, weak, or insufficiently demonstrated.
5. Provide concrete improvement suggestions.

Resume:
{resume_text}

Target Job Role:
{job_role}

OUTPUT FORMAT (MANDATORY — DO NOT CHANGE):

Extracted Skills:
- (list only skills found in the resume)

Missing / Weak Skills:
- (list skills REQUIRED for the role but missing or weak in the resume)

Suggestions:
- (actionable steps to close the gaps)
"""
    
    try:
        # Initialize Groq API
        print(f"\n{'='*60}")
        print(f"🤖 STARTING RESUME ANALYSIS")
        print(f"{'='*60}")
        print(f"Job Role: {job_role}")
        print(f"Resume Length: {len(resume_text)} characters")
        
        print("✓ Using model: llama-3.1-8b-instant")
        
        # Generate response using Groq
        print("⏳ Sending request to Groq API...")
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional AI resume analysis assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        
        result = completion.choices[0].message.content
        print("✓ Response received successfully")
        print(f"Response Length: {len(result)} characters")
        print(f"{'='*60}\n")
        
        return result
    
    except Exception as e:
        error_msg = f"Error analyzing resume: {str(e)}"
        print(f"\n{'='*60}", file=sys.stderr)
        print(f"❌ ERROR OCCURRED", file=sys.stderr)
        print(f"{'='*60}", file=sys.stderr)
        print(f"Error Type: {type(e).__name__}", file=sys.stderr)
        print(f"Error Message: {str(e)}", file=sys.stderr)
        print(f"\nFull Traceback:", file=sys.stderr)
        traceback.print_exc()
        print(f"{'='*60}\n", file=sys.stderr)
        return error_msg


def main():
    """
    Main Streamlit application.
    """
    
    # Page configuration
    st.set_page_config(
        page_title="AI Resume Skill Gap Analyzer",
        page_icon="📄",
        layout="wide"
    )
    
    # Title and description
    st.title("📄 AI Resume Skill Gap Analyzer")
    st.markdown("""
    Powered by **Groq AI** 🚀
    
    This tool analyzes your resume against a target job role and identifies skill gaps using advanced AI reasoning.
    """)
    
    st.divider()
    
    # Create two columns for input
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📝 Resume Text")
        resume_text = st.text_area(
            label="Paste your resume here",
            height=300,
            placeholder="Paste your complete resume text here...\n\nInclude your experience, projects, skills, education, etc.",
            label_visibility="collapsed"
        )
    
    with col2:
        st.subheader("🎯 Target Job Role")
        job_role = st.text_input(
            label="Enter the job role you're targeting",
            placeholder="e.g., Machine Learning Engineer",
            label_visibility="collapsed"
        )
        
        st.markdown("#### Examples:")
        st.markdown("""
        - Machine Learning Engineer
        - Full Stack Developer
        - Data Scientist
        - DevOps Engineer
        - Product Manager
        """)
    
    st.divider()
    
    # Analyze button
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
    with col_btn2:
        analyze_button = st.button("🔍 Analyze Resume", type="primary", use_container_width=True)
    
    # Analysis logic
    if analyze_button:
        # Input validation
        if not resume_text.strip():
            st.warning("⚠️ Please paste your resume text before analyzing.")
            return
        
        if not job_role.strip():
            st.warning("⚠️ Please enter a target job role before analyzing.")
            return
        
        # Show loading spinner
        with st.spinner("🤖 AI is analyzing your resume... This may take a few seconds."):
            analysis_result = analyze_resume(resume_text, job_role)
        
        # Display results
        st.divider()
        st.subheader("📊 Analysis Results")
        
        # Check if there was an error
        if analysis_result.startswith("Error"):
            st.error(analysis_result)
        else:
            st.markdown(analysis_result)
            
            # Download option
            st.divider()
            st.download_button(
                label="📥 Download Analysis",
                data=analysis_result,
                file_name=f"resume_analysis_{job_role.replace(' ', '_')}.txt",
                mime="text/plain"
            )
    
    # Footer
    st.divider()
    st.markdown("""
    <div style='text-align: center; color: gray; padding: 20px;'>
        <small>Built with Streamlit and Groq AI | AI Resume Skill Gap Analyzer</small>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
