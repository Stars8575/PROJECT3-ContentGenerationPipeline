import json

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


def generate_response(prompt: str):
    """
    Sends prompt to Groq and returns the generated response.
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=GENERATION_CONFIG["temperature"],
        max_tokens=GENERATION_CONFIG["max_tokens"]
    )

    return response.choices[0].message.content.strip()


def safe_json(text: str):
    """
    Converts model JSON response into a Python dictionary.
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
            "suggestions": [
                "Unable to evaluate content."
            ]
        }


def generate_content_pipeline(
    topic: str,
    content_type: str,
    tone: str,
    word_count: int
):
    """
    Complete AI content generation pipeline.
    """

    template = get_template(content_type)

    # Step 1: Research
    research = generate_response(
        research_prompt(topic)
    )

    # Step 2: Outline
    outline = generate_response(
        outline_prompt(
            topic,
            research
        )
    )

    # Step 3: Generate Content
    writer_prompt = content_prompt(
        topic=topic,
        outline=outline + "\n\n" + template["instructions"],
        tone=tone,
        word_count=word_count,
        content_type=content_type
    )

    content = generate_response(writer_prompt)

    # Step 4: Refine
    refined_content = generate_response(
        refine_prompt(content)
    )

    # Step 5: SEO Suggestions
    seo = generate_response(
        seo_prompt(refined_content)
    )

    # Step 6: Evaluation
    evaluation_text = generate_response(
        evaluation_prompt(refined_content)
    )

    evaluation = safe_json(
        evaluation_text
    )

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