from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user_model import User

from app.utils.auth_bearer import verify_token
from app.utils.role_checker import RoleChecker

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)

admin_only = RoleChecker(["Admin"])

@router.put("/assign-role/{user_id}")
def assign_role(
    user_id: int,
    role: str,
    db: Session = Depends(get_db),
    admin=Depends(admin_only)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.role = role

    db.commit()

    return {
        "message": f"Role updated to {role}"
    }