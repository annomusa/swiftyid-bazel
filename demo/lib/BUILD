#!/bin/python

load(
    "@build_bazel_rules_swift//swift:swift.bzl",
    "swift_binary", "swift_library",
)

objc_library(
    name = "PrintStream",
    srcs = ["OIPrintStream.m"],
    hdrs = ["OIPrintStream.h"],
)

swift_library(
    name = "Printer",
    srcs = ["Printer.swift"],
    deps = [":PrintStream"],
)

swift_library(
    name = "Article",
    srcs = ["Article.swift"],
    deps = [":Printer"],
)

objc_library(
    name = "Magazine",
    srcs = ["Magazine.m"],
    deps = [
        ":Printer", ":Article",
    ],
)

swift_binary(
    name = "MagazineBinary",
    deps = [":Magazine"],
)
