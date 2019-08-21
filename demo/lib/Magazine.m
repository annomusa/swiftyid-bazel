#import "lib/Printer-Swift.h"
#import "lib/Article-Swift.h"

int main(int argc, char **argv) {
  @autoreleasepool {
    OIPrinter *printer = [[OIPrinter alloc] initWithPrefix:@"Magazine: "];

    ObjcArticle *article = [[ObjcArticle alloc] initWithTitle:@"Bazel" content:@"An open-source build and test tool"];
    [printer print:@"Tech Magazine"];

    [article print];
  }
  return 0;
}
