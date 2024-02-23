from robot.api.deco import keyword, not_keyword

class FileStorage:
    def __init__(self) -> None:
        pass

    @keyword("Upload File", types={'file': 'str', 'file_name': 'str', 'folder_path': 'str'})
    def upload_file(self, file, file_name, folder_path):
        pass

    @keyword("Download File", types={'file_path': 'str'})
    def download_file(self, file_path):
        pass