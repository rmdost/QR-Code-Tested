import csv
import qrcode

# Read the CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Generate QR codes for each data cell
for row in data:
    for cell in row:
        # Create a QR code instance
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(cell)
        qr.make(fit=True)

        # Generate the QR code image
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image with the data cell number
        qr_image.save(f'qr_code_{cell}.png')
