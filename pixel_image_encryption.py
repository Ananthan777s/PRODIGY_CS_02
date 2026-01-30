from PIL import Image
import sys


def encrypt_decrypt_image(input_image, output_image, key):
    try:
        img = Image.open(input_image)
        img = img.convert("RGB")  # Ensure RGB mode
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]

                pixels[x, y] = (
                    r ^ key,
                    g ^ key,
                    b ^ key
                )

        img.save(output_image)
        print(f"[✔] Operation completed! Saved as '{output_image}'")

    except FileNotFoundError:
        print("[✘] Error: Image file not found.")
    except Exception as e:
        print(f"[✘] Unexpected error: {e}")


def main():
    print("=== Image Encryption / Decryption Tool ===")
    print("1. Encrypt Image")
    print("2. Decrypt Image")

    choice = input("Choose an option (1/2): ").strip()

    if choice not in ("1", "2"):
        print("[✘] Invalid choice!")
        sys.exit()

    input_image = input("Enter input image file (with extension): ").strip()
    output_image = input("Enter output image file name: ").strip()

    try:
        key = int(input("Enter encryption key (0–255): "))
        if not (0 <= key <= 255):
            raise ValueError
    except ValueError:
        print("[✘] Key must be an integer between 0 and 255.")
        sys.exit()

    encrypt_decrypt_image(input_image, output_image, key)


if __name__ == "__main__":
    main()
