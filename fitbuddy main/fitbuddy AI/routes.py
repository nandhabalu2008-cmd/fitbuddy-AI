from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session

from .database import get_db
from .models import UserPlan
from .gemini_generator import generate_workout_gemini
from .gemini_flash_generator import generate_nutrition_tip_with_flash
from .updated_plan import update_workout_plan

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return request.app.state.templates.TemplateResponse(
        request, "index.html", {"request": request}
    )

@router.post("/generate-workout", response_class=HTMLResponse)
def generate_workout(
    request: Request,
    user_id: str = Form(...),
    name: str = Form(...),
    age: int = Form(...),
    weight: str = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...),
    db: Session = Depends(get_db),
):
    workout = generate_workout_gemini(user_id, name, age, weight, goal, intensity)
    nutrition = generate_nutrition_tip_with_flash(goal, weight)

    record = UserPlan(
        user_id=user_id,
        name=name,
        age=age,
        weight=weight,
        goal=goal,
        intensity=intensity,
        workout_plan=workout,
        nutrition_tip=nutrition,
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    return request.app.state.templates.TemplateResponse(
        request,
        "result.html",
        {
            "request": request,
            "plan": record,
        },
    )

@router.post("/submit-feedback", response_class=HTMLResponse)
def submit_feedback(
    request: Request,
    record_id: int = Form(...),
    feedback: str = Form(...),
    db: Session = Depends(get_db),
):
    record = db.query(UserPlan).filter(UserPlan.id == record_id).first()
    if not record:
        return HTMLResponse("Plan not found.", status_code=404)

    record.feedback = feedback
    record.updated_plan = update_workout_plan(record.workout_plan, feedback)
    db.commit()
    db.refresh(record)

    return request.app.state.templates.TemplateResponse(
        request,
        "result.html",
        {"request": request, "plan": record},
    )

@router.get("/view-all-users", response_class=HTMLResponse)
def view_all_users(request: Request, db: Session = Depends(get_db)):
    records = db.query(UserPlan).order_by(UserPlan.id.desc()).all()
    return request.app.state.templates.TemplateResponse(
        request,
        "all_users.html",
        {"request": request, "users": records},
    )
