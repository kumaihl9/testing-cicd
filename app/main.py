from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import models

# Set up DB
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("form.htl", {"request": request})

@app.post("/submit")
def submit_form(
    name: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db)
    ):
    existing = db.query(models.User).filter(models.User.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists.")

    new_user = models.User(name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return RedirectResponse("/", status_code=303)
