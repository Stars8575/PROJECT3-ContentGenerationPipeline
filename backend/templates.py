"""
Content Templates

Each template contains instructions that guide the AI
to generate content in a format appropriate for the
selected content type.
"""

CONTENT_TEMPLATES = {

    "Blog": {
        "description": "Professional long-form blog article",
        "instructions": """
- Create an engaging title
- Write an introduction
- Use clear headings
- Explain concepts thoroughly
- Include examples where appropriate
- Finish with a conclusion
"""
    },

    "LinkedIn Post": {
        "description": "Professional LinkedIn content",
        "instructions": """
- Strong opening hook
- Professional tone
- Short paragraphs
- Actionable insights
- End with a discussion question
- Include relevant hashtags
"""
    },

    "Instagram Caption": {
        "description": "Social media caption",
        "instructions": """
- Short and engaging
- Conversational tone
- Use emojis where appropriate
- Include a call to action
- Include hashtags
"""
    },

    "Email": {
        "description": "Professional email",
        "instructions": """
- Subject line
- Greeting
- Professional body
- Clear closing
- Polite signature
"""
    },

    "Product Description": {
        "description": "Marketing product description",
        "instructions": """
- Product headline
- Key features
- Benefits
- Persuasive language
- Call to action
"""
    },

    "YouTube Script": {
        "description": "Video narration script",
        "instructions": """
- Attention-grabbing intro
- Smooth transitions
- Clear sections
- Viewer engagement
- Ending with CTA
"""
    },

    "Technical Documentation": {
        "description": "Developer documentation",
        "instructions": """
- Clear title
- Overview
- Requirements
- Step-by-step explanation
- Examples
- Best practices
"""
    },

    "News Article": {
        "description": "Professional news report",
        "instructions": """
- Headline
- Summary
- Main story
- Supporting facts
- Neutral tone
"""
    }

}


def get_template(content_type: str):
    """
    Returns the selected template.

    Falls back to Blog if content type
    is not found.
    """

    return CONTENT_TEMPLATES.get(
        content_type,
        CONTENT_TEMPLATES["Blog"]
    )


def list_templates():
    """
    Returns all available content types.
    """

    return list(CONTENT_TEMPLATES.keys())