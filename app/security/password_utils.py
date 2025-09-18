from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])



def hash_password(password):
    return str(pwd_context.hash(password))

def verifiy_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

parol = "salom123 "
print(verifiy_password(parol,"$2b$12$DUDXaztIQWXLWSW4rrmCyOrw2HIlgTmeeMUJOtAK7Es5alOnc4.Gm"))