"""
/*********************************************************************
* Copyright (c) 2023 the Qrisp Authors
*
* This program and the accompanying materials are made
* available under the terms of the Eclipse Public License 2.0
* which is available at https://www.eclipse.org/legal/epl-2.0/
*
* SPDX-License-Identifier: EPL-2.0
**********************************************************************/
"""


from qrisp.interface import VirtualBackend, VirtualQiskitBackend

# def_backend = VirtualQiskitBackend()
from qrisp.simulator.simulator import run

#
def_backend = VirtualBackend(run, port=8080)