#!/usr/bin/env bash
#!/bin/sh
#******************************************************************************
# BSD 3-Clause License                                                        * 
#                                                                             * 
# Copyright (c) 2020, Markus Schneider                                        *
# All rights reserved.                                                        * 
#                                                                             *
# Redistribution and use in source and binary forms, with or without          *
# modification, are permitted provided that the following conditions are met: *
#                                                                             *
# 1. Redistributions of source code must retain the above copyright notice,   * 
#    this list of conditions and the following disclaimer.                    *
#                                                                             *
# 2. Redistributions in binary form must reproduce the above copyright        * 
#    notice, this list of conditions and the following disclaimer in the      *
#    documentation and/or other materials provided with the distribution.     *
#                                                                             *
# 3. Neither the name of the copyright holder nor the names of its            *
#   contributors may be used to endorse or promote products derived from      *
#   this software without specific prior written permission.                  * 
#                                                                             *
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" *
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE   *
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE  *
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE   *
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR         *
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF        *
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR             * 
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,       * 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR     *
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF      * 
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                                  *
#******************************************************************************/

#==============================================================================
# SCRIPT:       set-prereq.sh
# AUTOHR:       Markus Schneider
# CONTRIBUTERS: Markus Schneider,<YOU>
# DATE:         2020-01-22
# REV:          0.1.0
# PLATFORM:     Noarch
# PURPOSE:      set-prereq the MINIOBS environment
#==============================================================================

##----------------------------------------
## SETUP FUNCTIONS
##----------------------------------------
set_prereq() {
    echo "* - nofile 65536" >> /etc/security/limits.conf
    echo "* - memlock unlimited" >> /etc/security/limits.conf
    echo "* - fzise unlimited" >> /etc/security/limits.conf
    echo "vm.max_map_count=262144" > /etc/sysctl.d/max_map_count.conf
    echo "vm.swappiness=0" > /etc/sysctl.d/swappiness.conf
    echo "*    soft nproc  65535" >> /etc/security/limits.conf
    echo "*    hard nproc  65536" >> /etc/security/limits.conf
    echo "*    soft nofile 65535" >> /etc/security/limits.conf
    echo "*    hard nofile 65536" >> /etc/security/limits.conf
    echo "root soft nproc  65536" >> /etc/security/limits.conf
    echo "root hard nproc  65536" >> /etc/security/limits.conf
    echo "root soft nofile 65536" >> /etc/security/limits.conf
    echo "root hard nofile 65536" >> /etc/security/limits.conf

    echo "session required pam_limits.so" >> "/etc/pam.d/common-session"

    echo "DefaultLimitNOFILE=65536" >> /etc/systemd/system.conf
    echo "DefaultLimitNOFILE=65536" >> /etc/systemd/user.conf

    ulimit -a
    sysctl -a
}

##----------------------------------------
## MAIN
##----------------------------------------
run_main() {
   set_prereq
}

run_main "$@"
