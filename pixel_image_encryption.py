def encrypt_decrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # XOR operation with key
            pixels[x, y] = (
                r ^ key,
                g ^ key,
                b ^ key
            )

    img.save(output_image)
    print(f"Operation completed! Saved as {output_image}")


def main():
    print("=== Image Encryption Tool ===")
    print("1. Encrypt Image")
    print("2. Decrypt Image")

    choice = input("Choose an option (1/2): ")

    input_image = input("Enter image file name (with extension): ")
    output_image = input("Enter output image name: ")
    key = int(input("Enter encryption key (0–255): "))

    if choice in ["1", "2"]:
        encrypt_decrypt_image(input_image, output_image, key)
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
