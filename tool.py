"""Validate simple hex frames: magic, length byte, payload, checksum."""
from __future__ import annotations
def validate(frame_hex:str,magic:str='aa55')->list[str]:
 errors=[]
 try:data=bytes.fromhex(frame_hex)
 except ValueError:return ['invalid hex']
 expected=bytes.fromhex(magic)
 if not data.startswith(expected):errors.append('wrong magic');return errors
 if len(data)<len(expected)+2:return errors+['too short']
 declared=data[len(expected)];payload=data[len(expected)+1:-1]
 if len(payload)!=declared:errors.append('length mismatch')
 if data[-1]!=(sum(data[:-1])&255):errors.append('checksum mismatch')
 return errors
if __name__=='__main__':
 import json,sys;p=json.load(sys.stdin);print(json.dumps(validate(p['frame'],p.get('magic','aa55'))))
