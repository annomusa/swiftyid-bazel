#!/bin/python

load("@build_bazel_rules_apple//apple:ios.bzl", "ios_application")
load("@build_bazel_rules_apple//apple:ios.bzl", "ios_extension")
load("@build_bazel_rules_swift//swift:swift.bzl", "swift_library")

package(default_visibility = ["//visibility:public"])

ios_extension(
    name = "share-extension",
    bundle_id = "Google.TextureApp.ShareExtension",
    families = ["iphone"],
    infoplists = ["ShareExtension/ShareExtension-Info.plist"],
    visibility = ["//visibility:public"],
    deps = ["ios-ext-bin"],
    minimum_os_version = "9.3"
)

objc_library(
    name = "ios-ext-bin",
    srcs = ["empty-main.m"],
)

ios_extension(
    name = "strings-extension",
    bundle_id = "Google.TextureApp.StringsExtension",
    families = ["iphone"],
    infoplists = ["StringsExtension/Resources/StringsExtension-Info.plist"],
    visibility = ["//visibility:public"],
    deps = ["strings-ext-bin"],
    minimum_os_version = "9.3"
)

filegroup(
    name = "StringsIntentVocabulary",
    srcs = glob(["StringsExtension/Resources/Localization/*.lproj/*.strings"]),
    visibility = ["//visibility:public"],
)

objc_library(
    name = "strings-ext-bin",
    srcs = native.glob(["StringsExtension/Sources/**/*.m"]),
    hdrs = native.glob(["StringsExtension/Sources/**/*.h"]),
    resources = [
        ":StringsIntentVocabulary",
    ],
)

ios_application(
    name = "ios-app",
    bundle_id = "Google.TextureApp",
    extensions = [
        ":share-extension",
        ":strings-extension",
    ],
    families = ["iphone"],
    infoplists = ["TextureApp/Info.plist"],
    visibility = ["//visibility:public"],
    deps = ["ios-app-bin"],
    minimum_os_version = "9.3"
)

objc_library(
    name = "ios-app-bin",
    srcs = [
        "TextureApp/main.m",
        ":GeneratedSource",
    ],
    defines = [
        "EXAMPLE_DEF=1",
    ],
    deps = [
        ":TextureAppClasses",
    ],
)

genrule(
    name = "GeneratedSource",
    srcs = [],
    outs = ["Generated.m"],
    cmd = "touch $@",
    tags = ["xchammer"],
)

load("@build_bazel_rules_apple//apple:ios.bzl", "ios_unit_test")
load("@build_bazel_rules_apple//apple:ios.bzl", "ios_ui_test")

# Unit Test Target
objc_library(
    name = "TestsLib",
    srcs = native.glob(["UnitTests/**/*.m"]),
    hdrs = native.glob(["UnitTests/**/*.h"]),
    sdk_frameworks = [
        "XCTest",
        "CoreGraphics",
    ],
    visibility = ["//visibility:public"],
    deps = [
        ":TextureAppClasses",
    ],
)

ios_unit_test(
    name = "UnitTests",
    size = "medium",
    minimum_os_version = "9.0",
    visibility = ["//visibility:public"],
    deps = [":TestsLib"],
)

ios_unit_test(
    name = "UnitTestsWithHost",
    size = "medium",
    minimum_os_version = "9.0",
    test_host = "//ios-app:ios-app",
    visibility = ["//visibility:public"],
    deps = [":TestsLib"],
)

ios_ui_test(
    name = "UITests",
    size = "medium",
    minimum_os_version = "9.0",
    test_host = "//ios-app:ios-app",
    visibility = ["//visibility:public"],
    deps = [":TestsLib"],
)

objc_library(
    name = "TextureAppClasses",
    srcs = glob(
        ["TextureApp/*.m"],
        exclude = [
            "TextureApp/NoArc.m",
        ],
    ) + [
        "TextureApp/Some.cc",
    ],
    hdrs = glob([
        "TextureApp/*.h",
        "TextureApp/*.hpp",
    ]),
    non_arc_srcs = [
        "TextureApp/NoArc.m",
    ],
    sdk_frameworks = [
        "CoreLocation",
        "AudioToolbox",
        "Security",
        "UIKit",
        "CoreGraphics",
        "QuartzCore",
        "Foundation",
        "CoreImage",
        "Intents",
    ],
    xibs = ["TextureApp/TextureAppViewController.xib"],
    deps = [
        "//Vendor/PINCache",
        "//Vendor/PINOperation",
        "//Vendor/Stripe",
        "//Vendor/Texture",
    ],
)
