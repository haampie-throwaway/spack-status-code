# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Fails(Package):
    """Package that fails"""

    homepage = "http://www.example.com"
    url      = "https://github.com/eth-cscs/SpFFT/archive/v1.0.1.zip"

    version('1.0.1', 'f8ab706309776cfbd2bfd8e29a6a9ffb5c8f3cd62399bf82db1e416ae5c490c8')

    def install(self, spec, prefix):
        raise InstallError("failed to install")

