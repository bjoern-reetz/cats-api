from fastapi import APIRouter

router = APIRouter(tags=["cats"])


@router.get("/")
def root():
    return "hello world!"
