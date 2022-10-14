from UI import UI

ui = UI()

print('Pandas solutions - Demo')
file_source = ui.select_file_source()
data_frame = ui.import_sample_file() if file_source == 's' else ui.import_user_file()

if data_frame is not None:
    print('Imported file structure:', end='\n')
    print(data_frame)
