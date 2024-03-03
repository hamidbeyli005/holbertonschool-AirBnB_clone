import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None

    def test_help_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help quit")
            self.assertEqual(f.getvalue().strip(), "Quit command to exit the program")

    def test_do_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.do_EOF(""))

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.emptyline()
            self.assertEqual(f.getvalue(), '')

    def test_do_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) == 36)  # Check if UUID is generated

    def test_do_show(self):
        obj = BaseModel()
        obj.save()
        obj_id = obj.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {}".format(obj_id))
            self.assertIn(obj_id, f.getvalue().strip())

    def test_do_destroy(self):
        obj = BaseModel()
        obj.save()
        obj_id = obj.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel {}".format(obj_id))
            self.assertNotIn(obj_id, storage.all())

    def test_do_all(self):
        obj1 = BaseModel()
        obj1.save()
        obj2 = BaseModel()
        obj2.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertIn(obj1.id, f.getvalue().strip())
            self.assertIn(obj2.id, f.getvalue().strip())

    def test_do_update(self):
        obj = BaseModel()
        obj.save()
        obj_id = obj.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('update BaseModel {} name "test"'.format(obj_id))
            self.assertEqual(obj.name, '"test"')

    def test_do_count(self):
        obj1 = BaseModel()
        obj1.save()
        obj2 = BaseModel()
        obj2.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count BaseModel")
            self.assertEqual(f.getvalue().strip(), "4")

if __name__ == '__main__':
    unittest.main()
