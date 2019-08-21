load("@build_bazel_rules_swift//swift:swift.bzl", "swift_library")
load("@build_bazel_rules_apple//apple:ios.bzl", "ios_application")

swift_library(
    name = "Sources",
    srcs = glob(["src/**"]),
    data = [
        "Resources/Main.storyboard",
    ],
    deps = [
        "//Lib-Swift:Lib_Swift",
        "@Rx//:RxSwift",
        "@Ml//:MagazineLayout",
    ],
    visibility = ["//visibility:public"]
)

ios_application(
    name = "MagazineApp",
    bundle_id = "be.tulipemoutarde.appa",
    families = ["iphone"],
    infoplists = [":Info.plist"],
    visibility = ["//visibility:public"],
    deps = [":Sources"],
    minimum_os_version = "11.0",
)
