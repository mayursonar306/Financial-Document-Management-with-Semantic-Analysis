from fastapi import APIRouter, Depends
from app.utils.auth_bearer import verify_token

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/profile")
def get_profile(
    user=Depends(verify_token)
):

    return {
        "message": "Protected Route Accessed",
        "user_data": user
    }