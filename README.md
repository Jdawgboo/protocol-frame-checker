# Protocol Frame Checker

Validate a small hex frame format with magic bytes, one-byte declared payload length, and additive checksum.

```bash
cat frame.json | python tool.py
python -m unittest -v
```

The supported format is intentionally narrow; adapt framing, byte order, and checksums for your actual protocol.
