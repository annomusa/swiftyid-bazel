#import "lib/OIPrintStream.h"

@implementation OIPrintStream {
  NSFileHandle *_fileHandle;
}

- (instancetype)initWithFileHandle:(nonnull NSFileHandle *)fileHandle {
  if (self = [super init]) {
    _fileHandle = fileHandle;
  }
  return self;
}

- (void)printString:(nonnull NSString *)message {
  NSData *data = [message dataUsingEncoding:NSUTF8StringEncoding];
  [_fileHandle writeData:data];
  NSData *newline = [NSData dataWithBytes:"\n" length:1];
  [_fileHandle writeData:newline];
}


@end
