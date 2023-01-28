import sys
import base64
src_file_content = open(sys.argv[1],'rb').read()
dst_file = open(sys.argv[2], "wb")
dst_file.write(base64.b64decode(src_file_content))
dst_file.close()