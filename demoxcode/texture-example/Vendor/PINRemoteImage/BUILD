load(
  "//Vendor/rules_pods/BazelExtensions:extensions.bzl",
  "pch_with_name_hint",
  "acknowledged_target",
  "gen_module_map",
  "gen_includes"
  )
# Add a config setting release for compilation mode
# Assume that people are using `opt` for release mode
# see the bazel user manual for more information
# https://bazel.build/versions/master/docs/bazel-user-manual.html
native.config_setting(
  name = "release",
  values = {
    "compilation_mode": "opt"
  }
  )
filegroup(
  name = "PINRemoteImage_hdrs",
  srcs = glob(
    [
      "pod_support/Headers/Public/**/*"
    ],
    exclude_directories = 1
    ) + [

  ] + [
    ":PINCache_hdrs"
  ],
  visibility = [
    "//visibility:public"
  ]
  )
gen_includes(
  name = "PINRemoteImage_includes",
  include = [
    "Vendor/PINRemoteImage/pod_support/Headers/Public/"
  ]
  )
gen_module_map(
  "PINRemoteImage",
  "PINRemoteImage_module_map",
  "PINRemoteImage",
  [
    "PINRemoteImage_hdrs"
  ]
  )
objc_library(
  name = "PINRemoteImage",
  enable_modules = 1,
  hdrs = [
    ":PINRemoteImage_hdrs"
  ],
  pch = pch_with_name_hint(
    "PINRemoteImage",
    [

    ]
    ),
  deps = [
    ":PINCache"
  ] + [
    ":PINRemoteImage_includes"
  ],
  copts = [
    "-Wnon-modular-include-in-framework-module",
    "-g",
    "-stdlib=libc++",
    "-DCOCOAPODS=1",
    "-DOBJC_OLD_DISPATCH_PROTOTYPES=0",
    "-fdiagnostics-show-note-include-stack",
    "-fno-common",
    "-fembed-bitcode-marker",
    "-fmessage-length=0",
    "-fpascal-strings",
    "-fstrict-aliasing",
    "-Wno-error=nonportable-include-path"
  ] + select(
    {
      "//conditions:default": [
        "-DPOD_CONFIGURATION_RELEASE=0"
      ],
      ":release": [
        "-DPOD_CONFIGURATION_RELEASE=1",
        "-DNS_BLOCK_ASSERTIONS=1"
      ]
    }
    ) + [
    "-IVendor/PINRemoteImage/pod_support/Headers/Public/PINRemoteImage/"
  ] + [
    "-fmodule-name=PINRemoteImage_pod_module"
  ],
  visibility = [
    "//visibility:public"
  ]
  )
acknowledged_target(
  name = "PINRemoteImage_acknowledgement",
  deps = [

  ],
  value = "//Vendor/PINRemoteImage/pod_support_buildable:acknowledgement_fragment"
  )
filegroup(
  name = "Core_hdrs",
  srcs = glob(
    [
      "Source/Classes/**/*.h"
    ],
    exclude = [
      "Source/Classes/PINCache/*.h"
    ],
    exclude_directories = 1
    ),
  visibility = [
    "//visibility:public"
  ]
  )
filegroup(
  name = "Core_union_hdrs",
  srcs = [
    "Core_hdrs",
    "PINRemoteImage_hdrs"
  ],
  visibility = [
    "//visibility:public"
  ]
  )
gen_includes(
  name = "Core_includes",
  include = [
    "Vendor/PINRemoteImage/pod_support/Headers/Public/"
  ]
  )
objc_library(
  name = "Core",
  enable_modules = 1,
  srcs = glob(
    [
      "Source/Classes/**/*.m"
    ],
    exclude = [
      "Source/Classes/PINCache/*.m"
    ],
    exclude_directories = 1
    ),
  hdrs = [
    ":Core_union_hdrs"
  ],
  pch = pch_with_name_hint(
    "PINRemoteImage",
    [
      "Source/**/*.pch"
    ]
    ),
  sdk_frameworks = [
    "ImageIO",
    "Accelerate"
  ],
  deps = [
    "//Vendor/PINCache:PINCache",
    "//Vendor/PINOperation:PINOperation"
  ] + [
    ":Core_includes"
  ],
  copts = [
    "-Wnon-modular-include-in-framework-module",
    "-g",
    "-stdlib=libc++",
    "-DCOCOAPODS=1",
    "-DOBJC_OLD_DISPATCH_PROTOTYPES=0",
    "-fdiagnostics-show-note-include-stack",
    "-fno-common",
    "-fembed-bitcode-marker",
    "-fmessage-length=0",
    "-fpascal-strings",
    "-fstrict-aliasing",
    "-Wno-error=nonportable-include-path"
  ] + select(
    {
      "//conditions:default": [
        "-DPOD_CONFIGURATION_RELEASE=0"
      ],
      ":release": [
        "-DPOD_CONFIGURATION_RELEASE=1",
        "-DNS_BLOCK_ASSERTIONS=1"
      ]
    }
    ) + [
    "-IVendor/PINRemoteImage/pod_support/Headers/Public/PINRemoteImage/"
  ] + [
    "-fmodule-name=PINRemoteImage_pod_module"
  ],
  visibility = [
    "//visibility:public"
  ]
  )
acknowledged_target(
  name = "Core_acknowledgement",
  deps = [
    "//Vendor/PINCache:PINCache_acknowledgement",
    "//Vendor/PINOperation:PINOperation_acknowledgement"
  ],
  value = "//Vendor/PINRemoteImage/pod_support_buildable:acknowledgement_fragment"
  )
filegroup(
  name = "iOS_hdrs",
  srcs = [

  ],
  visibility = [
    "//visibility:public"
  ]
  )
filegroup(
  name = "iOS_union_hdrs",
  srcs = [
    "iOS_hdrs",
    "PINRemoteImage_hdrs"
  ],
  visibility = [
    "//visibility:public"
  ]
  )
gen_includes(
  name = "iOS_includes",
  include = [
    "Vendor/PINRemoteImage/pod_support/Headers/Public/"
  ]
  )
objc_library(
  name = "iOS",
  enable_modules = 1,
  hdrs = [
    ":iOS_union_hdrs"
  ],
  pch = pch_with_name_hint(
    "PINRemoteImage",
    [

    ]
    ),
  sdk_frameworks = [
    "UIKit"
  ],
  deps = [
    ":Core"
  ] + [
    ":iOS_includes"
  ],
  copts = [
    "-Wnon-modular-include-in-framework-module",
    "-g",
    "-stdlib=libc++",
    "-DCOCOAPODS=1",
    "-DOBJC_OLD_DISPATCH_PROTOTYPES=0",
    "-fdiagnostics-show-note-include-stack",
    "-fno-common",
    "-fembed-bitcode-marker",
    "-fmessage-length=0",
    "-fpascal-strings",
    "-fstrict-aliasing",
    "-Wno-error=nonportable-include-path"
  ] + select(
    {
      "//conditions:default": [
        "-DPOD_CONFIGURATION_RELEASE=0"
      ],
      ":release": [
        "-DPOD_CONFIGURATION_RELEASE=1",
        "-DNS_BLOCK_ASSERTIONS=1"
      ]
    }
    ) + [
    "-IVendor/PINRemoteImage/pod_support/Headers/Public/PINRemoteImage/"
  ] + [
    "-fmodule-name=PINRemoteImage_pod_module"
  ],
  visibility = [
    "//visibility:public"
  ]
  )
acknowledged_target(
  name = "iOS_acknowledgement",
  deps = [

  ],
  value = "//Vendor/PINRemoteImage/pod_support_buildable:acknowledgement_fragment"
  )
filegroup(
  name = "OSX_hdrs",
  srcs = [

  ],
  visibility = [
    "//visibility:public"
  ]
  )
filegroup(
  name = "OSX_union_hdrs",
  srcs = [
    "OSX_hdrs",
    "PINRemoteImage_hdrs"
  ],
  visibility = [
    "//visibility:public"
  ]
  )
gen_includes(
  name = "OSX_includes",
  include = [
    "Vendor/PINRemoteImage/pod_support/Headers/Public/"
  ]
  )
objc_library(
  name = "OSX",
  enable_modules = 1,
  hdrs = [
    ":OSX_union_hdrs"
  ],
  pch = pch_with_name_hint(
    "PINRemoteImage",
    [

    ]
    ),
  sdk_frameworks = [
    "Cocoa",
    "CoreServices"
  ],
  deps = [
    ":Core"
  ] + [
    ":OSX_includes"
  ],
  copts = [
    "-Wnon-modular-include-in-framework-module",
    "-g",
    "-stdlib=libc++",
    "-DCOCOAPODS=1",
    "-DOBJC_OLD_DISPATCH_PROTOTYPES=0",
    "-fdiagnostics-show-note-include-stack",
    "-fno-common",
    "-fembed-bitcode-marker",
    "-fmessage-length=0",
    "-fpascal-strings",
    "-fstrict-aliasing",
    "-Wno-error=nonportable-include-path"
  ] + select(
    {
      "//conditions:default": [
        "-DPOD_CONFIGURATION_RELEASE=0"
      ],
      ":release": [
        "-DPOD_CONFIGURATION_RELEASE=1",
        "-DNS_BLOCK_ASSERTIONS=1"
      ]
    }
    ) + [
    "-IVendor/PINRemoteImage/pod_support/Headers/Public/PINRemoteImage/"
  ] + [
    "-fmodule-name=PINRemoteImage_pod_module"
  ],
  visibility = [
    "//visibility:public"
  ]
  )
acknowledged_target(
  name = "OSX_acknowledgement",
  deps = [

  ],
  value = "//Vendor/PINRemoteImage/pod_support_buildable:acknowledgement_fragment"
  )
filegroup(
  name = "tvOS_hdrs",
  srcs = [

  ],
  visibility = [
    "//visibility:public"
  ]
  )
filegroup(
  name = "tvOS_union_hdrs",
  srcs = [
    "tvOS_hdrs",
    "PINRemoteImage_hdrs"
  ],
  visibility = [
    "//visibility:public"
  ]
  )
gen_includes(
  name = "tvOS_includes",
  include = [
    "Vendor/PINRemoteImage/pod_support/Headers/Public/"
  ]
  )
objc_library(
  name = "tvOS",
  enable_modules = 1,
  hdrs = [
    ":tvOS_union_hdrs"
  ],
  pch = pch_with_name_hint(
    "PINRemoteImage",
    [

    ]
    ),
  deps = [
    ":iOS"
  ] + [
    ":tvOS_includes"
  ],
  copts = [
    "-Wnon-modular-include-in-framework-module",
    "-g",
    "-stdlib=libc++",
    "-DCOCOAPODS=1",
    "-DOBJC_OLD_DISPATCH_PROTOTYPES=0",
    "-fdiagnostics-show-note-include-stack",
    "-fno-common",
    "-fembed-bitcode-marker",
    "-fmessage-length=0",
    "-fpascal-strings",
    "-fstrict-aliasing",
    "-Wno-error=nonportable-include-path"
  ] + select(
    {
      "//conditions:default": [
        "-DPOD_CONFIGURATION_RELEASE=0"
      ],
      ":release": [
        "-DPOD_CONFIGURATION_RELEASE=1",
        "-DNS_BLOCK_ASSERTIONS=1"
      ]
    }
    ) + [
    "-IVendor/PINRemoteImage/pod_support/Headers/Public/PINRemoteImage/"
  ] + [
    "-fmodule-name=PINRemoteImage_pod_module"
  ],
  visibility = [
    "//visibility:public"
  ]
  )
acknowledged_target(
  name = "tvOS_acknowledgement",
  deps = [

  ],
  value = "//Vendor/PINRemoteImage/pod_support_buildable:acknowledgement_fragment"
  )
filegroup(
  name = "WebP_hdrs",
  srcs = [

  ],
  visibility = [
    "//visibility:public"
  ]
  )
filegroup(
  name = "WebP_union_hdrs",
  srcs = [
    "WebP_hdrs",
    "PINRemoteImage_hdrs"
  ],
  visibility = [
    "//visibility:public"
  ]
  )
gen_includes(
  name = "WebP_includes",
  include = [
    "Vendor/PINRemoteImage/pod_support/Headers/Public/"
  ]
  )
objc_library(
  name = "WebP",
  enable_modules = 1,
  hdrs = [
    ":WebP_union_hdrs"
  ],
  pch = pch_with_name_hint(
    "PINRemoteImage",
    [

    ]
    ),
  deps = [
    "//Vendor/libwebp:libwebp",
    ":Core"
  ] + [
    ":WebP_includes"
  ],
  copts = [
    "-DPIN_WEBP=1",
    "-Wnon-modular-include-in-framework-module",
    "-g",
    "-stdlib=libc++",
    "-DCOCOAPODS=1",
    "-DOBJC_OLD_DISPATCH_PROTOTYPES=0",
    "-fdiagnostics-show-note-include-stack",
    "-fno-common",
    "-fembed-bitcode-marker",
    "-fmessage-length=0",
    "-fpascal-strings",
    "-fstrict-aliasing",
    "-Wno-error=nonportable-include-path"
  ] + select(
    {
      "//conditions:default": [
        "-DPOD_CONFIGURATION_RELEASE=0"
      ],
      ":release": [
        "-DPOD_CONFIGURATION_RELEASE=1",
        "-DNS_BLOCK_ASSERTIONS=1"
      ]
    }
    ) + [
    "-IVendor/PINRemoteImage/pod_support/Headers/Public/PINRemoteImage/"
  ] + [
    "-fmodule-name=PINRemoteImage_pod_module"
  ],
  visibility = [
    "//visibility:public"
  ]
  )
acknowledged_target(
  name = "WebP_acknowledgement",
  deps = [
    "//Vendor/libwebp:libwebp_acknowledgement"
  ],
  value = "//Vendor/PINRemoteImage/pod_support_buildable:acknowledgement_fragment"
  )
filegroup(
  name = "PINCache_hdrs",
  srcs = glob(
    [
      "Source/Classes/PINCache/*.h"
    ],
    exclude_directories = 1
    ),
  visibility = [
    "//visibility:public"
  ]
  )
filegroup(
  name = "PINCache_union_hdrs",
  srcs = [
    "PINCache_hdrs",
    "PINRemoteImage_hdrs"
  ],
  visibility = [
    "//visibility:public"
  ]
  )
gen_includes(
  name = "PINCache_includes",
  include = [
    "Vendor/PINRemoteImage/pod_support/Headers/Public/"
  ]
  )
objc_library(
  name = "PINCache",
  enable_modules = 1,
  srcs = glob(
    [
      "Source/Classes/PINCache/*.m"
    ],
    exclude_directories = 1
    ),
  hdrs = [
    ":PINCache_union_hdrs"
  ],
  pch = pch_with_name_hint(
    "PINRemoteImage",
    [
      "Source/**/*.pch"
    ]
    ),
  deps = [
    "//Vendor/PINCache:PINCache",
    ":Core"
  ] + [
    ":PINCache_includes"
  ],
  copts = [
    "-Wnon-modular-include-in-framework-module",
    "-g",
    "-stdlib=libc++",
    "-DCOCOAPODS=1",
    "-DOBJC_OLD_DISPATCH_PROTOTYPES=0",
    "-fdiagnostics-show-note-include-stack",
    "-fno-common",
    "-fembed-bitcode-marker",
    "-fmessage-length=0",
    "-fpascal-strings",
    "-fstrict-aliasing",
    "-Wno-error=nonportable-include-path"
  ] + select(
    {
      "//conditions:default": [
        "-DPOD_CONFIGURATION_RELEASE=0"
      ],
      ":release": [
        "-DPOD_CONFIGURATION_RELEASE=1",
        "-DNS_BLOCK_ASSERTIONS=1"
      ]
    }
    ) + [
    "-IVendor/PINRemoteImage/pod_support/Headers/Public/PINRemoteImage/"
  ] + [
    "-fmodule-name=PINRemoteImage_pod_module"
  ],
  visibility = [
    "//visibility:public"
  ]
  )
acknowledged_target(
  name = "PINCache_acknowledgement",
  deps = [
    "//Vendor/PINCache:PINCache_acknowledgement"
  ],
  value = "//Vendor/PINRemoteImage/pod_support_buildable:acknowledgement_fragment"
  )