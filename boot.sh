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
# SCRIPT:   boot.sh 
# AUTOHR:   Markus Schneider (schneidermatic)
# DATE:     2020-11-21
# REV:      0.3.0
# PLATFORM: noarch
# PURPOSE:  Bootstrap script for the notifikator service
#==============================================================================

##----------------------------------------
## PYTHON SPECIFIC ENVs
##----------------------------------------
export PYTHONWARNINGS="ignore"

##----------------------------------------
## SUBROUTINES
##----------------------------------------
get_es_cert() {
   if [ -e /notifikator/ssl/elasticsearch.cer ]
   then 
     rm -f /notifikator/ssl/elasticsearch.cer
   fi
   openssl s_client -showcerts -connect ${APP_ES_HOST}:${APP_ES_PORT} -servername ${APP_ES_HOST} </dev/null | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > /notifikator/ssl/elasticsearch.cer
}

get_kb_cert() {
   if [ -e /notifikator/ssl/kibana.cer ]
   then 
     rm -f /notifikator/ssl/kibana.cer
   fi
   openssl s_client -showcerts -connect ${APP_KB_HOST}:${APP_KB_PORT} -servername ${APP_KB_HOST} </dev/null | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > /notifikator/ssl/kibana.cer
}

run() {
  get_es_cert
  get_kb_cert
  if [ "$APP_CONFIG_NAME" = "testing" ]
  then
     echo "FLASK is booting."
     cd /notifikator/app
     FLASK_APP=main.py python -m flask run --host $APP_IPADDRESS --port $APP_PORT
  elif [ "$APP_CONFIG_NAME" = "production" ]
  then
     echo "GUNICORN is booting."
     gunicorn app.main:app -w1 --bind ${APP_IPADDRESS}:${APP_PORT} --log-level=info --capture-output
  fi
}

##----------------------------------------
## MAIN
##----------------------------------------
main() {
    run "$@"
}

main "$@"
