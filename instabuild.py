import commands
import time

## Instabuild takes an xcode project, builds it, signs it, and sends it to testflight.
## Author: Addison Hardy
## http://github.com/addisonhardy

################################

# Path to root of xcode project (include trailing slash)
project_path = "###"

# Path to .xcodeproj file in root of app folder
xcode_proj_path = project_path + "###" + ".xcodeproj"

# Path to .app file in /build/Release-iphoneos/ folder in app folder
xcode_build_path = project_path + "build/Release-iphoneos/" + "###" + ".app"

# Path to output the built .ipa
output_path = "###.ipa"

## TestFlight API key
testflight_key = "###"

## TestFlight Team Token
testflight_team_token = "###"

## TestFlight Distribution Lists (comma separated)
testflight_dist_lists = "###"

## TestFlight Send Notifications (True|False)
testflight_notify = "True"

## TestFlight Build Notes
testflight_build_notes = "###"

################################

commands.getstatusoutput("xcodebuild -project " + xcode_proj_path + " -alltargets")

print "Building app xcode project..."

time.sleep(4)

commands.getstatusoutput("/usr/bin/xcrun -sdk iphoneos PackageApplication -v " + xcode_build_path + " -o " + output_path)

print "Creating output .ipa file..."

testflight = commands.getoutput("curl http://testflightapp.com/api/builds.json -F file=" + output_path + " -F api_token='" + api_token + "' -F team_token='" + team_token + "' -F notes='" + testflight_build_notes + "' -F notify=" + testflight_notify + " -F distribution_lists='" + testflight_dist_lists + "'")

print "Uploading to TestFlight..."
