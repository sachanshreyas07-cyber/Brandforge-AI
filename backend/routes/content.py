from fastapi import APIRouter

from models.content_request import ContentRequest
from prompts.content_prompts import generate_ideas_prompt
from services.gemini_service import generate

router = APIRouter()

@router.post("/generate-ideas")
def generate_ideas(req: ContentRequest):

    try:
        prompt = generate_ideas_prompt(
            req.niche,
            req.goal,
            req.content_type
        )

        response = generate(prompt)

        print("Gemini Response:")
        print(response)

        return response

    except Exception as e:
        print("ERROR:", e)
        raise e