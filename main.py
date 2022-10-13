from validators.FileFormatValidator import FileFormatValidator
from validators.FilePathValidator import FilePathValidator

print('DataFrame - Demo')
print('File format: [c]sv, [j]son, [x]ml')
file_format_validator = FileFormatValidator()

while True:
    file_format = input()
    if not file_format_validator.validate(file_format):
        print(file_format_validator.get_error_message_content())
        continue
    else:
        break

print('File path:')
file_path = input()
file_path_validator = FilePathValidator()
if not file_path_validator.validate(file_path):
    print(file_path_validator.get_error_message_content())
