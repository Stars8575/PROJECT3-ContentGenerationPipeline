"""
optimizer.py

Automatically improves generated content
if the evaluation score is below the
desired threshold.
"""

from google.genai import types

from config import (
    client,
    MODEL_NAME,
    GENERATION_CONFIG
)


QUALITY_THRESHOLD = 8.5


def optimize_content(
    content: str,
    evaluation: dict
):
    """
    Optimizes content if the overall score
    is below QUALITY_THRESHOLD.

    Returns:
        optimized_content,
        optimized(bool)
    """

    overall_score = evaluation.get("overall", 0)

    if overall_score >= QUALITY_THRESHOLD:
        return content, False

    prompt = f"""
You are a senior content editor.

The following content received a quality score
of {overall_score}/10.

Improve it significantly.

Focus on:

- Grammar
- Readability
- Professional tone
- Flow
- Clarity
- Engagement
- Remove repetition
- Improve transitions
- Keep all important information

Do NOT shorten the article.

Return ONLY the improved version.

Content:

{content}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.5,
            top_p=0.9,
            max_output_tokens=GENERATION_CONFIG["max_output_tokens"],
        ),
    )

    return response.text.strip(), True


def should_optimize(
    evaluation: dict
):
    """
    Returns True if optimization is required.
    """

    return evaluation.get("overall", 0) < QUALITY_THRESHOLD