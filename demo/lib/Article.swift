import Foundation
import lib_Printer

@objc(ObjcArticle)
public class Article: NSObject {

  private let stream: Printer
  private let title: String
  private let content: String
  private var lastResult: Int?

  @objc public init(title: String, content: String) {
    let prefixPrint = "Article \(title): " as NSString
    self.stream = Printer(prefix: prefixPrint)
    self.title = title
    self.content = content
  }

  @objc public func print() {
    stream.print(content as NSString)
  }

  public func delete() {
    
  }
}
