import unittest
from fixtures.docs import documents
from fixtures.dirs import directories
import document_directory
from unittest.mock import patch


class FuncsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.directories = directories
        self.documents = documents
        with patch('document_directory.input', return_value='e'):
            document_directory.runner()

    def test_get_doc_info(self):
        doc_return = document_directory.document_number_info('11-2')
        self.assertEqual(doc_return, 'invoice "11-2" "Геннадий Покемонов"')

    def test_add_doc(self):
        user_input = ['11', 'pass', 'dan', '3']
        with patch('document_directory.input', side_effect=user_input):
            document_directory.add_document()
        self.assertEqual(directories['3'], ['11'])

    def test_del_doc(self):
        doc_return = document_directory.delete_document('10006')
        self.assertEqual(doc_return, 0)