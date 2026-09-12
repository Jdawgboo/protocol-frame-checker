import unittest
from tool import validate
class FrameTests(unittest.TestCase):
 def test_frame(self):
  raw=bytes.fromhex('aa55')+bytes([2,1,2]);frame=(raw+bytes([sum(raw)&255])).hex();self.assertEqual(validate(frame),[]);self.assertIn('checksum mismatch',validate(frame[:-2]+'00'))
if __name__=='__main__':unittest.main()
