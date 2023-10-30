#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
import pycodestyle
from models.base_model import BaseModel
from models import storage
import os


class test_dbStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """instance for testing"""
        self.storage = DBStorage()

    def tearDown(self):
        """clean up after testing"""
        if os.path.exists(DBStorage.__file_path):
            os.remove(DBStorage.__file_path)

    def test_pycode(self):
        style = pycodestyle.StyleGuide(quiet=True)
        files = [
            'models/engine/db_storage.py'
            'tests/test_models/test_engine/test_db_storage.py'
        ]
        result = style.check_files(files)
        self.assertEqual(
            result.total_errors, 0, "PEP 8 style issues found"
        )

    def test_documentation(self):
        check_class = [DBStorage]
        for cls in check_class:
            self.assertTrue(
                cls.__doc__ is not None and len(cls.__doc__strip()) > 0,
                f"Missing docstring in {cls.__name__}"
            )

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ DBStorage object storage created """
        from models.engine.file_storage import DBStorage
        print(type(storage))
        self.assertEqual(type(storage), DBStorage)


if __name__ == '__main__':
    unittest.main()
