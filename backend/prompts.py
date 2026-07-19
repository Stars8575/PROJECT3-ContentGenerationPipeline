"""
All prompt templates for the Content Generation Pipeline.
Each function returns a prompt string that will be sent to Gemini.
"""


def research_prompt(topic: str):
    return f"""
You are an expert researcher.

Research the following topic:

Topic:
{topic}

Provide:

1. Key concepts
2. Important facts
3. Latest trends
4. Benefits
5. Challenges
6. Real-world examples

Return everything as clean bullet points.
"""


def outline_prompt(topic: str, research: str):
    return f"""
You are a professional content strategist.

Topic:
{topic}

Research:
{research}

Create a detailed outline.

Requirements:
- Catchy title
- Introduction
- 4–6 main sections
- Subpoints
- Conclusion

Return only the outline.
"""


def content_prompt(
    topic: str,
    outline: str,
    tone: str,
    word_count: int,
    content_type: str,
):
    return f"""
You are a professional writer.

Write a {content_type}.

Topic:
{topic}

Tone:
{tone}

Word Count:
Approximately {word_count} words

Outline:
{outline}

Requirements:

- Follow the outline
- Proper headings
- Smooth transitions
- Professional language
- Original content
- Easy to read
- No markdown
- No explanations

Return only the final content.
"""


def refine_prompt(content: str):
    return f"""
You are an expert editor.

Improve the following content.

Focus on:

- Grammar
- Readability
- Sentence flow
- Clarity
- Engagement
- Remove repetition
- Keep original meaning

Content:

{content}

Return only the improved version.
"""


def seo_prompt(content: str):
    return f"""
You are an SEO expert.

Based on the content below generate:

1. SEO Title
2. Meta Description
3. Focus Keyword
4. Five Related Keywords
5. Five Tags

Content:

{content}

Return in this format:

Title:
Meta Description:
Focus Keyword:
Related Keywords:
Tags:
"""


def evaluation_prompt(content: str):
    return f"""
You are a professional content evaluator.

Evaluate this content.

Score from 1 to 10.

Categories:

Grammar

Readability

Professionalism

SEO Friendliness

Originality

Overall Quality

Also provide:

Strengths

Weaknesses

Suggestions for improvement

Content:

{content}

Return ONLY valid JSON.

Example:

{{
    "grammar": 9,
    "readability": 8,
    "professionalism": 9,
    "seo": 8,
    "originality": 9,
    "overall": 9,
    "strengths": [
        "...",
        "..."
    ],
    "weaknesses": [
        "...",
        "..."
    ],
    "suggestions": [
        "...",
        "..."
    ]
}}
"""