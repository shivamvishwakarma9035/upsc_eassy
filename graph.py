
from agents.clarity_agent import evaluate_clarity
from agents.depth_agent import evaluate_depth
from agents.language_agent import evaluate_language
from agents.final_eval_agent import final_score
from agents.congrats_agent import get_congrats
from agents.improvement_agent import get_suggestions

async def run_evaluation(essay: str) -> dict:
    clarity = await evaluate_clarity(essay)
    depth = await evaluate_depth(essay)
    language = await evaluate_language(essay)

    final = await final_score(
        c=clarity["score"],
        d=depth["score"],
        l=language["score"]
    )

    if final["status"] == "pass":
        message = await get_congrats()
        return {
            "score": final["score"],
            "message": message,
            "feedback": f"Clarity: {clarity['reason']}\n\nDepth: {depth['reason']}\n\nLanguage: {language['reason']}",
            "suggestions": []
        }
    else:
        tips = await get_suggestions(essay)
        return {
            "score": final["score"],
            "message": final["message"],
            "feedback": f"Clarity: {clarity['reason']}\n\nDepth: {depth['reason']}\n\nLanguage: {language['reason']}",
            "suggestions": tips
        }
