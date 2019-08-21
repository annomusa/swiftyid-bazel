
new_pod_repository(
  name = "PINOperation",
  url = "https://github.com/pinterest/PINOperation/archive/1.1.zip",
  owner = "@ios-cx",
)

new_pod_repository(
  name = "PINCache",
  url = "https://github.com/pinterest/PINCache/archive/f9f1e551d6a78d74f5528e43a8575f9d2d329e7d.zip",
  owner = "@ios-cx",
)

new_pod_repository(
  name = "Stripe",
  url = "https://github.com/stripe/stripe-ios/archive/v12.1.2.zip",
  owner = "@ios-action",
  inhibit_warnings = True,

  # Duplicate interface definition issue
  generate_module_map = False,
)

new_pod_repository(
  name = "Texture",
  url = "https://github.com/TextureGroup/Texture/archive/2.8.1.zip",
  owner = "@ios-action",
  inhibit_warnings = True,
  # Undefined symbols
  # Compilation error: triggered module compilation from ObjC code
  generate_module_map = False,
)

new_pod_repository(
  name = "PINRemoteImage",
  url = "https://github.com/pinterest/PINRemoteImage/archive/a06b4746ebbe45c87c2b449e8a40a6b7ddf96051.zip",
  # PINRemoteImage_Core conditionally compiles in PINCache based on these
  # headers
  user_options = ["Core.deps += //Vendor/PINCache:PINCache"],

  # TODO:
  generate_module_map = False
)

new_pod_repository(
  name = "PINOperation",
  url = "https://github.com/pinterest/PINOperation/archive/1.1.zip"
)

new_pod_repository(
  name = "PINCache",
  url = "https://github.com/pinterest/PINCache/archive/d886490de6d297e38f80bb750ff2dec4822fb870.zip"
)
