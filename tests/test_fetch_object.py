import biocframe
import collaboratordb


def test_fetch_object():
    id = "dssc-test_basic-2023:my_first_df@2023-07-28"
    obj = collaboratordb.fetch_object(id)
    assert isinstance(obj, biocframe.BiocFrame)

