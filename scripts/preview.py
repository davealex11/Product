from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
from functools import partial
import os,re,argparse
from pathlib import Path
class Handler(SimpleHTTPRequestHandler):
 def send_head(self):
  self.byte_range=None
  path=self.translate_path(self.path)
  if os.path.isfile(path) and path.endswith('.mp4'):
   size=os.path.getsize(path);start=0;end=size-1
   value=self.headers.get('Range')
   if value:
    m=re.fullmatch(r'bytes=(\d*)-(\d*)',value.strip())
    if not m:
     self.send_error(416);return None
    a,b=m.groups()
    if a:start=int(a);end=min(int(b),size-1) if b else size-1
    elif b:start=max(0,size-int(b))
    if start>=size or start>end:
     self.send_response(416);self.send_header('Content-Range',f'bytes */{size}');self.end_headers();return None
   f=open(path,'rb');f.seek(start);self.byte_range=end-start+1
   self.send_response(206 if value else 200)
   self.send_header('Content-Type','video/mp4');self.send_header('Accept-Ranges','bytes');self.send_header('Content-Length',str(end-start+1))
   if value:self.send_header('Content-Range',f'bytes {start}-{end}/{size}')
   self.end_headers();return f
  return super().send_head()
 def copyfile(self,source,outputfile):
  if self.byte_range is None:return super().copyfile(source,outputfile)
  remain=self.byte_range
  try:
   while remain:
    data=source.read(min(remain,65536))
    if not data:break
    outputfile.write(data);remain-=len(data)
  except (BrokenPipeError,ConnectionResetError):pass
if __name__ == '__main__':
 parser=argparse.ArgumentParser(description='Preview the product page with video seeking support.')
 parser.add_argument('--port',type=int,default=8766)
 args=parser.parse_args()
 root=Path(__file__).resolve().parent.parent / 'outputs'
 print(f'Preview: http://127.0.0.1:{args.port}/netradyne-products.html',flush=True)
 ThreadingHTTPServer(('127.0.0.1',args.port),partial(Handler,directory=str(root))).serve_forever()
