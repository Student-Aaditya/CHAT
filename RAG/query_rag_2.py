import os ,sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))  

from RAG.router.club_router import club_router
from RAG.router.about_course_router import about_course_router
from RAG.router.admission_router import admission_router
from RAG.router.faq_router import keyword_faq_router
from Ollama.llm_client import ask_ollama_raw
from RAG.router.course_router import course_router
from RAG.router.btech_course import btech_router
from RAG.router.mtech_course_router import mtech_router
from RAG.router.ug_pg_router import ug_pg_router
from RAG.router.facilities_router import facilities_router
from RAG.router.event_router import event_router
from RAG.router.niet_overview import about_niet_router
from RAG.router.placement_router import placement_record_router

def answer_rag(query: str):
    q = query.lower().strip()

    # ---------- EVENTS ----------
    if any(w in q for w in ["event", "events", "hackathon", "conference"]):
        res = event_router(q)
        if res:
            return res
    
    # ---------- ADMISSION ----------
    if any(w in q for w in ["admission", "admissions", "counselling", "jee", "direct admission", "fee", "documents"]):
        res = about_niet_router(q)
        if res:
            return res
        return "For more information visit:\nhttps://www.niet.co.in/admissions/eligibility-admission-process"

    # ---------- FACILITIES ----------
    res = facilities_router(q)
    if res:
        return res

    # ---------- UG / PG ----------
    res = ug_pg_router(q)
    if res:
        return res

    # ---------- BTECH ----------
    res = btech_router(q)
    if res:
        return res

    # ---------- MTECH ----------
    res = mtech_router(q)
    if res:
        return res

    # ---------- COURSE OVERVIEW ----------
    if any(w in q for w in ["why choose", "seats", "duration", "benefit"]):
        res = course_router(q)
        if res:
            return res
        return "Please visit:\nhttps://www.niet.co.in/courses"

    # ---------- CLUBS ----------
    if "club" in q or "clubs" in q:
        res = club_router(q)
        if res:
            return res
        return "Visit:\nhttps://niet.co.in/students-life/student-clubs-societies"

    if any(w in q for w in ["niet", "about", "overview", "research""non veg","wifi"]):
        res = keyword_faq_router(q)
        if res:
            return res
        return "More info:\nhttps://www.niet.co.in/about"

    # # ---------- FAQ ----------
    # res = keyword_faq_router(q)
    # if res:
    #     return res

    # ---------- FINAL FALLBACK (LLM) ----------
    return ask_ollama_raw(
        f"Answer strictly about NIET institute. Query: {query}"
    )


if __name__=="__main__":
    print(answer_rag("why choose iot"))