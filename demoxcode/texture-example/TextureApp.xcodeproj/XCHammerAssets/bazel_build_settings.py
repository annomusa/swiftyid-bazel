# Copyright 2018 The Tulsi Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Generated by Tulsi to resolve flags during builds.


import sys


def _StandardizeTargetLabel(label):
  """Convert labels of form //dir/target to //dir/target:target."""
  if label is None:
    return label
  if not label.startswith('//') and not label.startswith('@'):
    sys.stderr.write('[WARNING] Target label "{0}" is not fully qualified. '
                     'Labels should start with "@" or "//".\n\n'.format(label))
    sys.stderr.flush()
  tokens = label.rsplit('/', 1)
  if len(tokens) <= 1:
    return label

  target_base = tokens[0]
  target = tokens[1]

  if '...' in target or ':' in target:
    return label
  return label + ':' + target


class BazelFlags(object):
  """Represents Bazel flags."""

  def __init__(self, startup = [], build = []):
    self.startup = startup
    self.build = build


class BazelFlagsSet(object):
  """Represents a set of Bazel flags which can vary by compilation mode."""

  def __init__(self, debug = None, release = None, flags = None):
    if debug is None:
      debug = flags or BazelFlags()
    if release is None:
      release = flags or BazelFlags()

    self.debug = debug
    self.release = release

  def flags(self, is_debug):
    """Returns the proper flags (either debug or release)."""
    return self.debug if is_debug else self.release


class BazelBuildSettings(object):
  """Represents a Tulsi project's Bazel settings."""

  def __init__(self, bazel, bazelExecRoot,
               defaultPlatformConfigId, platformConfigFlags,
               swiftTargets,
               cacheAffecting, cacheSafe,
               swiftOnly, nonSwiftOnly,
               swiftFeatures, nonSwiftFeatures,
               projDefault, projTargetMap):
    self.bazel = bazel
    self.bazelExecRoot = bazelExecRoot
    self.defaultPlatformConfigId = defaultPlatformConfigId
    self.platformConfigFlags = platformConfigFlags
    self.swiftTargets = swiftTargets
    self.cacheAffecting = cacheAffecting
    self.cacheSafe = cacheSafe
    self.swiftOnly = swiftOnly
    self.nonSwiftOnly = nonSwiftOnly
    self.swiftFeatures = swiftFeatures
    self.nonSwiftFeatures = nonSwiftFeatures
    self.projDefault = projDefault
    self.projTargetMap = projTargetMap

  def features_for_target(self, target, is_swift_override=None):
    """Returns an array of enabled features for the given target."""

    target = _StandardizeTargetLabel(target)
    is_swift = target in self.swiftTargets
    if is_swift_override is not None:
      is_swift = is_swift_override

    return self.swiftFeatures if is_swift else self.nonSwiftFeatures

  def flags_for_target(self, target, is_debug,
                       config, is_swift_override=None):
    """Returns (bazel, startup flags, build flags) for the given target."""

    target = _StandardizeTargetLabel(target)
    target_flag_set = self.projTargetMap.get(target)
    if not target_flag_set:
      target_flag_set = self.projDefault

    is_swift = target in self.swiftTargets
    if is_swift_override is not None:
      is_swift = is_swift_override
    lang = self.swiftOnly if is_swift else self.nonSwiftOnly

    config_flags = self.platformConfigFlags[config]
    cache_affecting = self.cacheAffecting.flags(is_debug)
    cache_safe = self.cacheSafe.flags(is_debug)
    target = target_flag_set.flags(is_debug)
    lang = lang.flags(is_debug)

    startupFlags = []
    startupFlags.extend(target.startup)
    startupFlags.extend(cache_safe.startup)
    startupFlags.extend(cache_affecting.startup)
    startupFlags.extend(lang.startup)

    buildFlags = []
    buildFlags.extend(target.build)
    buildFlags.extend(config_flags)
    buildFlags.extend(cache_safe.build)
    buildFlags.extend(cache_affecting.build)
    buildFlags.extend(lang.build)

    return (self.bazel, startupFlags, buildFlags)

# Default value in case the template does not behave as expected.
BUILD_SETTINGS = None

BUILD_SETTINGS = BazelBuildSettings(
    '/Users/aunorafiq/Pandora/swiftyid/demoxcode/texture-example/tools/bazelwrapper',
    '/private/var/tmp/_bazel_aunorafiq/8ae6dc552537bacf9bd1cdc49a1f5157/execroot/__main__',
    'iphone',
    {
        'ios_x86_64': [
            '--config=ios_x86_64',
        ],
        'ios_arm64': [
            '--config=ios_arm64',
        ],
    },
    set(),
    BazelFlagsSet(),
    BazelFlagsSet(),
    BazelFlagsSet(),
    BazelFlagsSet(),
    [],
    [],
    BazelFlagsSet(),
    {
        '//Vendor/Texture:MapKit': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//Vendor/Texture:Photos': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//Vendor/Stripe:Stripe_Bundle_Stripe': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//ios-app:TextureAppClasses': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//ios-app:ios-app': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--action_env=X=Y',
                    '--action_env=CLI_SDK=$(SDKROOT)',
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//Vendor/Texture:Video': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//Vendor/Texture:AssetsLibrary': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//ios-app:ios-ext-bin': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//Vendor/PINRemoteImage:PINCache': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//ios-app:strings-extension': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//Vendor/PINCache:Core': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//Vendor/PINCache:Arc-exception-safe': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//Vendor/Texture:Core': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//Vendor/PINOperation:PINOperation_cxx': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//ios-app:ios-app-bin': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//Vendor/PINCache:PINCache': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//Vendor/Texture:PINRemoteImage': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//Vendor/Stripe:Stripe': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//ios-app:share-extension': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//Vendor/PINRemoteImage:iOS': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//ios-app:strings-ext-bin': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//Vendor/Texture:Texture': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--apple_platform_type=ios',
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//Vendor/PINOperation:PINOperation': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
        '//Vendor/PINRemoteImage:Core': BazelFlagsSet(
            flags = BazelFlags(
                startup = [],
                build = [
                    '--override_repository=tulsi=/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/Resources',
                    '--build_event_publish_all_actions=true',
                ],
            ),
        ),
    },
)

