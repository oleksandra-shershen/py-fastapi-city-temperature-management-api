from fastapi import HTTPException


def city_already_exists_exception():
    raise HTTPException(
        status_code=400, detail="Such name for Temperature already exists"
    )


def city_not_found_exception():
    raise HTTPException(status_code=404, detail="Temperature not found")
