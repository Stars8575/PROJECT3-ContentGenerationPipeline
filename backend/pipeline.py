import json

from google.genai import types

from config import (
    client,
    MODEL_NAME,
    GENERATION_CONFIG
)

from prompts import (
    research_prompt,
    outline_prompt,
    content_prompt,
    refine_prompt,
    seo_prompt,
    evaluation_prompt
)

from templates import get_template


def generate_response(prompt: str) -> str:
    """
    Sends a prompt to Gemini and returns the response text.
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=GENERATION_CONFIG["temperature"],
            top_p=GENERATION_CONFIG["top_p"],
            max_output_tokens=GENERATION_CONFIG["max_output_tokens"],
        ),
    )

    return response.text.strip()


def safe_json(text: str):
    """
    Converts Gemini JSON response into a Python dictionary.
    Falls back gracefully if parsing fails.
    """

    try:
        text = text.replace("```json", "")
        text = text.replace("```", "")
        return json.loads(text)

    except Exception:
        return {
            "grammar": 0,
            "readability": 0,
            "professionalism": 0,
            "seo": 0,
            "originality": 0,
            "overall": 0,
            "strengths": [],
            "weaknesses": [],
            "suggestions": ["Unable to evaluate content."]
        }


def generate_content_pipeline(
    topic: str,
    content_type: str,
    tone: str,
    word_count: int
):
    """
    Complete prompt engineering pipeline.
    """

    template = get_template(content_type)

    # -------------------------------------------------
    # STEP 1
    # Research
    # -------------------------------------------------

    research = generate_response(
        research_prompt(topic)
    )

    # -------------------------------------------------
    # STEP 2
    # Outline
    # -------------------------------------------------

    outline = generate_response(
        outline_prompt(
            topic,
            research
        )
    )

    # -------------------------------------------------
    # STEP 3
    # Generate Content
    # -------------------------------------------------

    writer_prompt = content_prompt(
        topic=topic,
        outline=outline + "\n\n" + template["instructions"],
        tone=tone,
        word_count=word_count,
        content_type=content_type
    )

    content = generate_response(writer_prompt)

    # -------------------------------------------------
    # STEP 4
    # Refine
    # -------------------------------------------------

    refined_content = generate_response(
        refine_prompt(content)
    )

    # -------------------------------------------------
    # STEP 5
    # SEO
    # -------------------------------------------------

    seo = generate_response(
        seo_prompt(refined_content)
    )

    # -------------------------------------------------
    # STEP 6
    # Evaluation
    # -------------------------------------------------

    evaluation_text = generate_response(
        evaluation_prompt(refined_content)
    )

    evaluation = safe_json(
        evaluation_text
    )

    # -------------------------------------------------
    # Return Everything
    # -------------------------------------------------

    return {

        "topic": topic,

        "content_type": content_type,

        "tone": tone,

        "word_count": word_count,

        "research": research,

        "outline": outline,

        "content": refined_content,

        "seo": seo,

        "evaluation": evaluation
    }