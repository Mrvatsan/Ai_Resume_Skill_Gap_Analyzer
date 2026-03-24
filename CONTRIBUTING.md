# Contributing to AI Resume Skill Gap Analyzer

Thank you for your interest in contributing to the AI Resume Skill Gap Analyzer project!

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a feature branch (`git checkout -b feature/your-feature`)
4. Make your changes
5. Commit your changes (`git commit -m 'feat: add your feature'`)
6. Push to the branch (`git push origin feature/your-feature`)
7. Open a Pull Request

## Development Setup

### Prerequisites
- Python 3.8+
- Node.js 14+ (for frontend development)
- Git

### Local Development

```bash
# Clone the repository
git clone https://github.com/Mrvatsan/Ai_Resume_Skill_Gap_Analyzer.git
cd Ai_Resume_Skill_Gap_Analyzer

# Create virtual environment (Python)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Run the application
python -m http.server 8000  # Landing page
streamlit run app.py        # Streamlit app
```

## Code Style

### Python
- Follow PEP 8
- Use type hints
- Write docstrings for functions

### JavaScript
- Use consistent naming conventions
- Add comments for complex logic
- Format with 4 spaces

### HTML/CSS
- Use semantic HTML
- Follow BEM naming for CSS classes
- Keep styles organized

## Testing

Before submitting a PR, please:
- Test the landing page on desktop and mobile
- Verify all links work correctly
- Check browser console for errors
- Test keyboard navigation

## Commit Message Format

```
<type>: <subject>

<body>

<footer>
```

### Types
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes
- `refactor:` - Code refactoring
- `perf:` - Performance improvements
- `test:` - Test additions/changes
- `chore:` - Build/dependency updates
- `a11y:` - Accessibility improvements
- `security:` - Security-related changes

### Examples
```
feat: Add dark mode toggle to landing page

fix: Correct hero section alignment on mobile

docs: Update deployment instructions

a11y: Improve keyboard navigation support
```

## Pull Request Process

1. Update documentation if needed
2. Add tests for new features
3. Ensure all tests pass
4. Provide a clear description of changes
5. Link any related issues

## Reporting Bugs

Please use the GitHub Issues page to report bugs. Include:
- Description of the bug
- Steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots/videos if applicable
- Browser/environment information

## Feature Requests

We welcome feature suggestions! Please create an issue with:
- Clear description of the feature
- Use cases
- Suggested implementation (optional)

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Report inappropriate behavior

## Questions?

Feel free to open an issue or contact the maintainers.

Thank you for contributing! 🎉
