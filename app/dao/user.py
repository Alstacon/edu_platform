from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.models.user import User


class UserDAO:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create_user(self, first_name: str, last_name: str, email: str) -> User:
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        self.db_sesion.add(new_user)
        await self.db_sesion.flush()
        return new_user
