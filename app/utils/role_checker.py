from fastapi import HTTPException, Depends
from app.utils.auth_bearer import verify_token

class RoleChecker:

    def __init__(self, allowed_roles: list):
        self.allowed_roles = allowed_roles

    def __call__(
        self,
        user=Depends(verify_token)
    ):

        user_role = user.get("role")

        if user_role not in self.allowed_roles:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return user