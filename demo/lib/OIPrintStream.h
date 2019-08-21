#import <Foundation/Foundation.h>

@interface OIPrintStream: NSObject

- (nonnull instancetype)initWithFileHandle:(nonnull NSFileHandle *)fileHandle;

- (void)printString:(nonnull NSString *)message;

@end
