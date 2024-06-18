from fastapi import APIRouter, HTTPException, status, Depends
from database import ENGINE, session
from models import Product, User
from fastapi.encoders import jsonable_encoder
from schemas import ProductM
from fastapi_jwt_auth import AuthJWT


session = session(bind=ENGINE)
product_router = APIRouter(prefix="/product")


@product_router.get("/")
def get_products(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="create a new token")
    products = session.query(Product).all()
    context = [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "count": product.count,
            "price_type": product.price_type,
            "slug": product.slug,
            "image": product.image
        }
        for product in products
    ]

    return jsonable_encoder(context)


@product_router.post("/create")
def create_product(product: ProductM, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="create a new token")

    exist_user = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="this user does not exist")

    if exist_user.is_staff:
        new_product = Product(
            name=product.name,
            description=product.description,
            price=product.price,
            count=product.count,
            price_type=product.price_type,
            slug=product.slug,
            image=product.image
        )

        session.add(new_product)
        session.commit()

        context = {
            "status_code": status.HTTP_201_CREATED,
            "msg": "Product created",
            "data": {
                "id": new_product.id,
                "name": new_product.name,
                "description": new_product.description,
                "price": new_product.price,
                "count": new_product.count,
                "price_type": new_product.price_type,
                "slug": new_product.slug,
                "image": new_product.image
            }
        }
        return context
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="permission not")


@product_router.get("/{id}")
async def get_product(id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="create a new token")
    check_product = session.query(Product).filter(Product.id == id).first()
    if check_product:
        context = [
            {
                "id": check_product.id,
                "name": check_product.name,
                "description": check_product.description,
                "price": check_product.price,
                "count": check_product.count,
                "price_type": check_product.price_type,
                "slug": check_product.slug,
                "image": check_product.image
            }
        ]
        return jsonable_encoder(context)
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="product not found")


@product_router.put("/{id}", status_code=status.HTTP_200_OK)
def update_product(id: int, data: ProductM, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="create a new token")
    exist_users = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    if exist_users.is_staff:
        product = session.query(Product).filter(Product.id == id).first()
        if product:

            for key, value in data.dict(exclude_unset=True).items():
                setattr(product, key, value)

            session.commit()
            context = {
                    "status_code": 200,
                    "msg": "Product updated"
                }
            return jsonable_encoder(context)
        else:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Failed!")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="not possible to update product data for you")


@product_router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_product(id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="create a new token")
    exist_users = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")
    if exist_users.is_staff:
        product = session.query(Product).filter(Product.id == id).first()
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="product not found")

        session.delete(product)
        session.commit()

        context = {
            "status_code": 200,
            "msg": "Product deleted"
        }
        return jsonable_encoder(context)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="not possible to delete product data for you")