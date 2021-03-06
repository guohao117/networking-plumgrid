# Copyright 2015 PLUMgrid, Inc. All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from networking_plumgrid._i18n import _LI
from neutron.extensions import providernet as provider
from oslo_log import log as logging

LOG = logging.getLogger(__name__)


class Plumlib(object):
    """Class PLUMgrid Fake Library.

    This library is a by-pass implementation for the PLUMgrid Library.
    This class is being used by the unit test integration in Neutron.
    """

    def __init__(self):
        LOG.info(_LI('Python PLUMgrid Fake Library Started '))
        pass

    def director_conn(self, director_plumgrid, director_port, timeout,
                      director_admin, director_password):
        LOG.info(_LI('Fake Director: %s'),
                 director_plumgrid + ':' + str(director_port))
        pass

    def create_network(self, tenant_id, net_db, network, **kwargs):
        net_db["network"] = {}
        for key in (provider.NETWORK_TYPE,
                    provider.PHYSICAL_NETWORK,
                    provider.SEGMENTATION_ID):
            net_db["network"][key] = network["network"][key]
        return net_db

    def update_network(self, tenant_id, net_id, network, orig_net_db):
        pass

    def delete_network(self, net_db, net_id):
        pass

    def create_subnet(self, sub_db, net_db, ipnet):
        pass

    def update_subnet(self, orig_sub_db, new_sub_db, ipnet, net_db):
        pass

    def delete_subnet(self, tenant_id, net_db, net_id, sub_db):
        pass

    def create_port(self, port_db, router_db, subnet_db):
        pass

    def update_port(self, port_db, router_db, subnet_db):
        pass

    def delete_port(self, port_db, router_db):
        pass

    def create_router(self, tenant_id, router_db):
        pass

    def update_router(self, router_db, router_id):
        pass

    def delete_router(self, tenant_id, router_id):
        pass

    def add_router_interface(self, tenant_id, router_id, port_db, ipnet,
                             ip_version):
        pass

    def remove_router_interface(self, tenant_id, net_id, router_id):
        pass

    def create_floatingip(self, floating_ip):
        pass

    def update_floatingip(self, floating_ip_orig, floating_ip, id):
        pass

    def delete_floatingip(self, floating_ip_orig, id):
        pass

    def disassociate_floatingips(self, fip, port_id):
        return dict((key, fip[key]) for key in ("id", "floating_network_id",
                                                "floating_ip_address"))

    def create_security_group(self, sg_db):
        pass

    def update_security_group(self, sg_db):
        pass

    def delete_security_group(self, sg_db):
        pass

    def create_security_group_rule(self, sg_rule_db):
        pass

    def create_security_group_rule_bulk(self, sg_rule_db):
        pass

    def delete_security_group_rule(self, sg_rule_db):
        pass

    def create_l2_gateway(self, director_plumgrid,
                          director_admin,
                          director_password,
                          gateway_info,
                          vendor_type,
                          sw_username,
                          sw_password):
        pass

    def delete_l2_gateway(self, gw_info):
        pass

    def add_l2_gateway_connection(self, gw_conn_info):
        pass

    def delete_l2_gateway_connection(self, gw_conn_info):
        pass

    def create_physical_attachment_point(self, physical_attachment_point):
        pass

    def update_physical_attachment_point(self, physical_attachment_point):
        pass

    def delete_physical_attachment_point(self, pap_id):
        pass

    def create_transit_domain(self, transit_domain, db):
        pass

    def update_transit_domain(self, transit_domain, db):
        pass

    def delete_transit_domain(self, tvd_id):
        pass

    def get_available_interface(self):
        return "host1", "ifc1"

    def create_policy_tag(self, tenant_id, policy_tag_db):
        pass

    def delete_policy_tag(self, tenant_id, ptag_id):
        pass

    def create_endpoint_group(self, tenant_id, ep_grp, ptag_db):
        pass

    def delete_endpoint_group(self, tenant_id, epg_id, ptag_db):
        pass

    def update_endpoint_group(self, tenant_id, epg_id, epg_db, ptag_db):
        pass

    def create_policy_service(self, tenant_id, ps_db, ps_mac_list):
        pass

    def delete_policy_service(self, tenant_id, ps_id):
        pass

    def update_policy_service(self, tenant_id, ps_id, ps_db, ps_mac_list):
        pass

    def create_policy_rule(self, tenant_id, pr_db):
        pass

    def delete_policy_rule(self, tenant_id, pr_id):
        pass

    def create_endpoint(self, tenant_id, ep_db, port_mac=None):
        pass

    def delete_endpoint(self, tenant_id, ep_id, ep_db, port_mac=None):
        pass

    def update_endpoint(self, tenant_id, ep_id, ep_db, port_mac=None):
        pass
