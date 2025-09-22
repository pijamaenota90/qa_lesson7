import os
import zipfile
import pytest


@pytest.fixture(scope="session")
def create_archive():
    resources_dir = 'resources'
    os.makedirs(resources_dir, exist_ok=True)
    archive_path = os.path.join(resources_dir, 'test_archive.zip')

    with zipfile.ZipFile(archive_path, 'w') as zipf:
        files_to_add = ['test1.pdf', 'test2.xlsx', 'test3.csv']

        for file in files_to_add:
            source_file_path = os.path.join('files', file)
            zipf.write(source_file_path, file)

    return archive_path