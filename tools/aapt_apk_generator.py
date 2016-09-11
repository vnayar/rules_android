"""Invokes aapt to generate resources apk.

This python script is an internal dependency used by Blaze.

USAGE: aapt_apk_generator [<resources_arguments>] [<assets_arguments>]
       <aapt cmdline>

NOTES: <resources_arguments> is optional and contains:
          start_resources <destination_dir>
            <artifact_exec_path> <resources_dir_relative_path>...
            end_resources
       <assets_arguments> is optional and contains:
          start_assets <destination_dir>
            <artifact_exec_path> <assets_dir_relative_path>...
            end_assets
       <aapt_argument> is mandatory and contains aapt invocation.
"""

import sys

from rules_android.tools import aapt_common

if __name__ == '__main__':
  args = aapt_common.MaybeUnpackParamFile(sys.argv[1:])
  aapt_common.RunAapt(args)
