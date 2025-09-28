import os
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Tạo thư mục chứa file
KEY_DIR = "keys"
os.makedirs(KEY_DIR, exist_ok=True)

PRIVATE_KEY_FILE = os.path.join(KEY_DIR, "private.key")
PUBLIC_KEY_FILE = os.path.join(KEY_DIR, "public.key")
MESSAGE_FILE = os.path.join(KEY_DIR, "message.txt")
SIGNATURE_FILE = os.path.join(KEY_DIR, "signature.pem")


# 1. Tạo cặp khóa RSA
def generate_keys():
    key = RSA.generate(2048)

    with open(PRIVATE_KEY_FILE, "wb") as f:
        f.write(key.export_key())

    with open(PUBLIC_KEY_FILE, "wb") as f:
        f.write(key.publickey().export_key())

    print("✅ Đã tạo cặp khóa RSA trong thư mục 'keys/'.")

# 2. Ký thông điệp
def sign_message():
    if not os.path.exists(PRIVATE_KEY_FILE):
        print("⚠️ Chưa có private.key, hãy tạo khóa trước!")
        return

    private_key = RSA.import_key(open(PRIVATE_KEY_FILE, "rb").read())

    # Nhập thông điệp từ bàn phím
    message = input("Nhập thông điệp cần ký: ").encode()

    with open(MESSAGE_FILE, "wb") as f:
        f.write(message)

    h = SHA256.new(message)
    signature = pkcs1_15.new(private_key).sign(h)

    with open(SIGNATURE_FILE, "wb") as f:
        f.write(signature)

    print("Đã ký thông điệp và lưu chữ ký vào 'keys/signature.pem'.")


# 3. Xác minh chữ ký
def verify_signature():
    if not os.path.exists(PUBLIC_KEY_FILE):
        print("⚠️ Chưa có public.key, hãy tạo khóa trước!")
        return
    if not os.path.exists(MESSAGE_FILE) or not os.path.exists(SIGNATURE_FILE):
        print("⚠️ Chưa có message.txt hoặc signature.pem, hãy ký thông điệp trước!")
        return

    public_key = RSA.import_key(open(PUBLIC_KEY_FILE, "rb").read())
    message = open(MESSAGE_FILE, "rb").read()
    signature = open(SIGNATURE_FILE, "rb").read()

    h = SHA256.new(message)

    try:
        pkcs1_15.new(public_key).verify(h, signature)
        print("Chữ ký hợp lệ. Thông điệp chưa bị thay đổi.")
    except (ValueError, TypeError):
        print("import os
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Tạo thư mục chứa file
KEY_DIR = "keys"
os.makedirs(KEY_DIR, exist_ok=True)

PRIVATE_KEY_FILE = os.path.join(KEY_DIR, "private.key")
PUBLIC_KEY_FILE = os.path.join(KEY_DIR, "public.key")
MESSAGE_FILE = os.path.join(KEY_DIR, "message.txt")
SIGNATURE_FILE = os.path.join(KEY_DIR, "signature.pem")


# 1. Tạo cặp khóa RSA
def generate_keys():
    key = RSA.generate(2048)

    with open(PRIVATE_KEY_FILE, "wb") as f:
        f.write(key.export_key())

    with open(PUBLIC_KEY_FILE, "wb") as f:
        f.write(key.publickey().export_key())

    print("Đã tạo cặp khóa RSA trong thư mục 'keys/'.")

# 2. Ký thông điệp
def sign_message():
    if not os.path.exists(PRIVATE_KEY_FILE):
        print("⚠️ Chưa có private.key, hãy tạo khóa trước!")
        return

    private_key = RSA.import_key(open(PRIVATE_KEY_FILE, "rb").read())

    # Nhập thông điệp từ bàn phím
    message = input("Nhập thông điệp cần ký: ").encode()

    with open(MESSAGE_FILE, "wb") as f:
        f.write(message)

    h = SHA256.new(message)
    signature = pkcs1_15.new(private_key).sign(h)

    with open(SIGNATURE_FILE, "wb") as f:
        f.write(signature)

    print("Đã ký thông điệp và lưu chữ ký vào 'keys/signature.pem'.")

# 3. Xác minh chữ ký
def verify_signature():
    if not os.path.exists(PUBLIC_KEY_FILE):
        print("⚠️ Chưa có public.key, hãy tạo khóa trước!")
        return
    if not os.path.exists(MESSAGE_FILE) or not os.path.exists(SIGNATURE_FILE):
        print("⚠️ Chưa có message.txt hoặc signature.pem, hãy ký thông điệp trước!")
        return

    public_key = RSA.import_key(open(PUBLIC_KEY_FILE, "rb").read())
    message = open(MESSAGE_FILE, "rb").read()
    signature = open(SIGNATURE_FILE, "rb").read()

    h = SHA256.new(message)

    try:
        pkcs1_15.new(public_key).verify(h, signature)
        print("Chữ ký hợp lệ. Thông điệp chưa bị thay đổi.")
    except (ValueError, TypeError):
        print("Chữ ký KHÔNG hợp lệ. Thông điệp đã bị thay đổi.")

# 4. Menu lựa chọn
def menu():
    while True:
        print("\n--- MENU CHỮ KÝ SỐ RSA ---")
        print("1. Tạo cặp khóa")
        print("2. Ký thông điệp")
        print("3. Xác minh chữ ký")
        print("4. Thoát")
        choice = input("Chọn chức năng (1-4): ")

        if choice == "1":
            generate_keys()
        elif choice == "2":
            sign_message()
        elif choice == "3":
            verify_signature()
        elif choice == "4":
            print("Thoát chương trình.")
            break
        else:
            print("⚠️ Lựa chọn không hợp lệ, vui lòng nhập 1-4.")


if __name__ == "__main__":
    menu()