import dearpygui.dearpygui as dpg
import moviepy.editor

dpg.create_context()


def callback(sender, app_data, user_data):
    print("Sender: ", sender)
    print("App Data: ", app_data)
    file_path_n = app_data["file_path_name"]
    video = moviepy.editor.VideoFileClip(file_path_n)
    audio = video.audio
    audio.write_audiofile(file_path_n[file_path_n.rfind('\\') + 1:][:file_path_n[file_path_n.rfind('\\'):].rfind('.') - 1] + ".mp3")
    dpg.set_value(text_id, "File successfully converted")


with dpg.file_dialog(directory_selector=False, show=False, callback=callback, id='file_dialog_id',
                     width = 500, height=500):
    dpg.add_file_extension("Source files (*.mp4){.mp4}", color=(0, 255, 255, 255, 255))


with dpg.window(tag="Primary Window"):
    text_id = dpg.add_text("Information about conversion from mp4 to mp3")
    dpg.add_button(label="File Selector", callback=lambda: dpg.show_item("file_dialog_id"))


dpg.create_viewport(title="Custom title", width=700, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
