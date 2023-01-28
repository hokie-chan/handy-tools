import sys
import base64
src_file_content = open(sys.argv[1],'rb').read()
dst_file = open(sys.argv[2], "wb")
eee = base64.b64encode(src_file_content)
eee_len = len(eee)
cur_pos = 0
while cur_pos < eee_len:
    dst_file.write(eee[cur_pos:cur_pos+76] + ('\r\n').encode('utf-8'))
    cur_pos += 76
dst_file.write('\r\n\r\n'.encode('utf-8'))
dst_file.close()