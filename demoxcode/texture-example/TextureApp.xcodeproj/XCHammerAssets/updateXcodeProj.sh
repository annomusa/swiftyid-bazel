# This file is governed by XCHammer
set -e

if [[ $ACTION == "clean" ]]; then
    exit 0
fi

PREV_STAT=`/usr/bin/stat -f %c "/Users/aunorafiq/Pandora/swiftyid/demoxcode/texture-example/TextureApp.xcodeproj/XCHammerAssets/genStatus"`
/Users/aunorafiq/Pandora/swiftyid/demoxcode/xchammer.app/Contents/MacOS/XCHammer generate /Users/aunorafiq/Pandora/swiftyid/demoxcode/texture-example/XCHammer.yaml --workspace_root /Users/aunorafiq/Pandora/swiftyid/demoxcode/texture-example --bazel /Users/aunorafiq/Pandora/swiftyid/demoxcode/texture-example/tools/bazelwrapper
STAT=`/usr/bin/stat -f %c "/Users/aunorafiq/Pandora/swiftyid/demoxcode/texture-example/TextureApp.xcodeproj/XCHammerAssets/genStatus"`
if [[ "$PREV_STAT" != "$STAT" ]]; then
    echo "error: Xcode project was out-of-date so we updated it for you! Please build again."
    exit 1
fi