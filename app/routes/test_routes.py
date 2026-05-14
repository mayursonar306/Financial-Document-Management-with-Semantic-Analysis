from fastapi import APIRouter, Depends

from app.utils.role_checker import RoleChecker

router = APIRouter(
    prefix="/test",
    tags=["RBAC Test"]
)

admin_only = RoleChecker(["Admin"])

analyst_only = RoleChecker([
    "Admin",
    "Analyst"
])

auditor_only = RoleChecker([
    "Admin",
    "Auditor"
])

@router.get("/admin")
def admin_route(
    user=Depends(admin_only)
):

    return {
        "message": "Welcome Admin"
    }

@router.get("/analyst")
def analyst_route(
    user=Depends(analyst_only)
):

    return {
        "message": "Welcome Analyst"
    }

@router.get("/auditor")
def auditor_route(
    user=Depends(auditor_only)
):

    return {
        "message": "Welcome Auditor"
    }