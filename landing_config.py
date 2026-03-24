# Landing Page Configuration

## Site Configuration
SITE_NAME = "AI Resume Skill Gap Analyzer"
TAGLINE = "Discover Your Skill Gaps Powered by AI"

## URLs
STREAMLIT_APP_URL = "http://localhost:8501"  # Change for production
GITHUB_REPO = "https://github.com/Mrvatsan/Ai_Resume_Skill_Gap_Analyzer"

## Social Media
GITHUB_URL = "https://github.com"
LINKEDIN_URL = "https://linkedin.com"
TWITTER_URL = "https://twitter.com"

## SEO Metadata
META_DESCRIPTION = "AI-powered resume skill gap analyzer. Identify missing skills for your target job role with instant AI analysis. Download detailed recommendations."
META_KEYWORDS = "resume, skills, gap analysis, AI, job seeker, career development"

## Email Configuration (for future use)
CONTACT_EMAIL = "contact@example.com"
SUPPORT_EMAIL = "support@example.com"

## Analytics (optional)
# Uncomment and configure if using Google Analytics
# GOOGLE_ANALYTICS_ID = "UA-XXXXXXXXX-X"

## Feature Flags
FEATURES = {
    "demo_video": False,  # Set to True when demo video is ready
    "newsletter_signup": False,  # Set to True to enable newsletter
    "contact_form": False,  # Set to True to enable contact form
    "testimonials": False,  # Set to True to show testimonials
    "pricing": False,  # Set to True to show pricing section
}

## Theme Colors (matches CSS variables)
COLORS = {
    "primary": "#6366f1",
    "primary_dark": "#4f46e5",
    "secondary": "#ec4899",
    "accent": "#f59e0b",
    "text_dark": "#1f2937",
    "text_light": "#6b7280",
    "bg_light": "#f9fafb",
    "bg_lighter": "#ffffff",
}

## Content Sections
SECTIONS = {
    "hero": {
        "title": "Discover Your Skill Gaps",
        "subtitle": "Get instant, AI-powered insights on what skills you need to land your dream job.",
        "cta_primary": "Launch App",
        "cta_secondary": "Learn More"
    },
    "features": [
        {
            "title": "Semantic Analysis",
            "description": "Advanced AI understanding that goes beyond keyword matching",
            "icon": "fa-magic"
        },
        {
            "title": "Skill Extraction",
            "description": "Automatically extracts all technical and soft skills",
            "icon": "fa-crosshairs"
        },
        {
            "title": "Gap Identification",
            "description": "Identifies missing or underdeveloped skills",
            "icon": "fa-chart-line"
        },
        {
            "title": "Smart Recommendations",
            "description": "Receive personalized improvement suggestions",
            "icon": "fa-lightbulb"
        },
        {
            "title": "Download Results",
            "description": "Export analysis as a text file",
            "icon": "fa-download"
        },
        {
            "title": "Lightning Fast",
            "description": "Get results in seconds",
            "icon": "fa-zap"
        }
    ]
}

## Deployment Environments
ENVIRONMENTS = {
    "development": {
        "url": "http://localhost:8000",
        "api_url": "http://localhost:8501",
        "debug": True
    },
    "staging": {
        "url": "https://staging.example.com",
        "api_url": "https://api-staging.example.com",
        "debug": False
    },
    "production": {
        "url": "https://example.com",
        "api_url": "https://api.example.com",
        "debug": False
    }
}

## Build & Deployment
BUILD_COMMAND = "echo 'No build needed for static landing page'"
DEPLOY_COMMAND = "git push origin main"

## Future Enhancement Ideas
TODO = [
    "Add email subscription form",
    "Implement demo video tutorial",
    "Add user testimonials section",
    "Create FAQ section",
    "Add comparison with competitors",
    "Implement user authentication",
    "Add payment integration",
    "Create blog/resources section",
    "Add API documentation",
    "Implement chatbot support",
    "Add accessibility testing",
    "Performance optimization",
    "Dark mode toggle",
    "Multi-language support",
    "Mobile app link"
]
