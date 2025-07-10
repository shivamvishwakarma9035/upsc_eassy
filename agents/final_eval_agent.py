
async def final_score(c: int, d: int, l: int) -> dict:
    total = c + d + l
    if total >= 110:
        return {"score": total, "status": "pass"}
    return {"score": total, "status": "fail", "message": "Needs improvement"}
