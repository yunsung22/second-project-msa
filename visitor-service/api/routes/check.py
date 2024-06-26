from fastapi import APIRouter,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.params import Form
from api.services.visitors import VisitorsService

check_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')


@check_router.get('/', response_class=HTMLResponse)
def check(req: Request):
    return templates.TemplateResponse('check/check.html', {'request': req})

@check_router.get('/checkok', response_class=HTMLResponse)
def checkok(req: Request):
    return templates.TemplateResponse('check/checkok.html', {'request': req})



@check_router.post("/checkok")
async def search_visitor(req: Request, name: str = Form(), phone_number: str = Form()):
    visitor_info = VisitorsService.search_visitor(name, phone_number)

    visitor_list = [
        {
            "name": visitor.name,
            "company_name": visitor.company_name,
            "email": visitor.email,
            "department_name": visitor.department_name,
            "job_position": visitor.job_position,
            "phone_number": visitor.phone_number,
            "employee_id": visitor.employee_id,
            "purpose": visitor.purpose,
            "location_id": visitor.location_id,
            "visit_date": visitor.visit_date,
            "status": visitor.status,
            "location": visitor.location
        } for visitor in visitor_info
    ]
    return visitor_list


