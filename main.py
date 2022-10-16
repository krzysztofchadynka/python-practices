from UI import UI
from integrations.S3 import S3
from integrations.Athena import Athena

ui = UI()

functionality = ui.select_functionality()

if functionality == 1:
    print('AWS S3 using boto3 - Demo')
    s3 = S3()

    # TODO: Move this logic to UI (or another refactored class / module) and add validation
    print('[1] - Create new bucket')
    print('[2] - Upload file into bucket')
    print('[3] - Download file from bucket')
    print('[4] - Delete file from bucket')
    s3_functionality = int(input())

    if s3_functionality == 1:
        s3.create_bucket(input('Bucket name: '))
    elif s3_functionality == 2:
        s3.upload_file_to_bucket(
            input('File name: '),
            input('Bucket name: '),
            input('Key: ')
        )
    elif s3_functionality == 3:
        s3.download_file_from_bucket(
            input('Bucket name: '),
            input('File name: ')
        )
    elif s3_functionality == 4:
        s3.delete_file_from_bucket(
            input('Bucket name: '),
            input('File name: ')
        )

elif functionality == 2:
    print('Pandas solutions - Demo')
    file_source = ui.select_file_source()
    data_frame = ui.import_sample_file() if file_source == 's' else ui.import_user_file()

    if data_frame is not None:
        print('Imported file structure:', end='\n')
        print(data_frame)
        ui.interpret_file(data_frame)

elif functionality == 3:
    athena = Athena(
        input('S3 Athena output directory: '),
        input('Region name: ')
    )

    print('[1] - List available databases')
    print('[2] - List tables in the selected database')
    print('[3] - Get data from selected table')
    athena_functionality = int(input())

    if athena_functionality == 1:
        print(athena.get_databases_list())

    elif athena_functionality == 2:
        print(athena.get_tables_in_database(input('Database name: ')))

    elif athena_functionality == 3:
        database_name = input('Database name: ')
        table_name = input('Table name: ')
        selected_limit = input('Limit (optional): ')
        limit = int(selected_limit) if selected_limit else None

        data = athena.get_data_from_selected_table(database_name, table_name, limit)
        print(data)
