import Foundation
import lib_PrintStream

@objc(OIPrinter)
public class Printer: NSObject {

  private let stream: OIPrintStream
  private let prefix: String

  @objc public init(prefix: NSString) {
    self.stream = OIPrintStream(fileHandle: .standardOutput)
    self.prefix = prefix as String
  }

  @objc public func print(_ message: NSString) {
    stream.print("\(prefix)\(message) + asdf")
  }

  @objc public func greet(_ message: NSString) {
    stream.print("\(message)")
  }

  public func delete() {
    
  }
}
