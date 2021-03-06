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

"""
Proxy Routines to link to PLUMgrid Library
"""

from networking_plumgrid._i18n import _LI
from oslo_log import log as logging
from plumgridlib import plumlib

LOG = logging.getLogger(__name__)


class Plumlib(object):
    """Class PLUMgrid Python Library.

    This library is a third-party tool
    needed by PLUMgrid plugin to implement all core API in Neutron.
    """

    def __init__(self):
        LOG.info(_LI('Python PLUMgrid Library Proxy Started '))

    def director_conn(self, director_plumgrid, director_port, timeout,
                      director_admin, director_password):
        self.plumlib = plumlib.Plumlib(director_plumgrid,
                                       director_port,
                                       timeout,
                                       director_admin,
                                       director_password)

    def create_network(self, tenant_id, net_db, network, **kwargs):
        self.plumlib.create_network(tenant_id, net_db, network, **kwargs)

    def update_network(self, tenant_id, net_id, network, orig_net_db):
        self.plumlib.update_network(tenant_id, net_id, network, orig_net_db)

    def delete_network(self, net_db, net_id):
        self.plumlib.delete_network(net_db, net_id)

    def create_subnet(self, sub_db, net_db, ipnet):
        self.plumlib.create_subnet(sub_db, net_db, ipnet)

    def update_subnet(self, orig_sub_db, new_sub_db, ipnet, net_db):
        self.plumlib.update_subnet(orig_sub_db, new_sub_db, ipnet, net_db)

    def delete_subnet(self, tenant_id, net_db, net_id, sub_db):
        self.plumlib.delete_subnet(tenant_id, net_db, net_id, sub_db)

    def create_port(self, port_db, router_db, subnet_db):
        self.plumlib.create_port(port_db, router_db, subnet_db)

    def update_port(self, port_db, router_db, subnet_db):
        self.plumlib.update_port(port_db, router_db, subnet_db)

    def delete_port(self, port_db, router_db):
        self.plumlib.delete_port(port_db, router_db)

    def create_router(self, tenant_id, router_db):
        self.plumlib.create_router(tenant_id, router_db)

    def update_router(self, router_db, router_id):
        self.plumlib.update_router(router_db, router_id)

    def delete_router(self, tenant_id, router_id):
        self.plumlib.delete_router(tenant_id, router_id)

    def add_router_interface(self, tenant_id, router_id, port_db, ipnet,
                             ip_version):
        self.plumlib.add_router_interface(tenant_id, router_id, port_db, ipnet,
                                          ip_version)

    def remove_router_interface(self, tenant_id, net_id, router_id):
        self.plumlib.remove_router_interface(tenant_id, net_id, router_id)

    def create_floatingip(self, floating_ip):
        self.plumlib.create_floatingip(floating_ip)

    def update_floatingip(self, floating_ip_orig, floating_ip, id):
        self.plumlib.update_floatingip(floating_ip_orig, floating_ip, id)

    def delete_floatingip(self, floating_ip_orig, id):
        self.plumlib.delete_floatingip(floating_ip_orig, id)

    def disassociate_floatingips(self, floating_ip, port_id):
        self.plumlib.disassociate_floatingips(floating_ip, port_id)

    def create_security_group(self, sg_db):
        self.plumlib.create_security_group(sg_db)

    def update_security_group(self, sg_db):
        self.plumlib.update_security_group(sg_db)

    def delete_security_group(self, sg_db):
        self.plumlib.delete_security_group(sg_db)

    def create_security_group_rule(self, sg_rule_db):
        self.plumlib.create_security_group_rule(sg_rule_db)

    def create_security_group_rule_bulk(self, sg_rule_db):
        self.plumlib.create_security_group_rule_bulk(sg_rule_db)

    def delete_security_group_rule(self, sg_rule_db):
        self.plumlib.delete_security_group_rule(sg_rule_db)

    def create_l2_gateway(self, director_plumgrid,
                          director_admin,
                          director_password,
                          gateway_info,
                          vendor_type,
                          sw_username,
                          sw_password):
        self.plumlib.create_l2_gateway(director_plumgrid,
                                       director_admin,
                                       director_password,
                                       gateway_info,
                                       vendor_type,
                                       sw_username,
                                       sw_password)

    def delete_l2_gateway(self, gw_info):
        self.plumlib.delete_l2_gateway(gw_info)

    def add_l2_gateway_connection(self, gw_conn_info):
        self.plumlib.add_l2_gateway_connection(gw_conn_info)

    def delete_l2_gateway_connection(self, gw_conn_info):
        self.plumlib.delete_l2_gateway_connection(gw_conn_info)

    def create_physical_attachment_point(self, physical_attachment_point):
        self.plumlib.create_physical_attachment_point(
                     physical_attachment_point)

    def update_physical_attachment_point(self, physical_attachment_point):
        self.plumlib.update_physical_attachment_point(
                     physical_attachment_point)

    def delete_physical_attachment_point(self, pap_id):
        self.plumlib.delete_physical_attachment_point(pap_id)

    def create_transit_domain(self, transit_domain, transit_domain_data):
        self.plumlib.create_transit_domain(transit_domain, transit_domain_data)

    def update_transit_domain(self, transit_domain, transit_domain_data):
        self.plumlib.update_transit_domain(transit_domain, transit_domain_data)

    def delete_transit_domain(self, tvd_id):
        self.plumlib.delete_transit_domain(tvd_id)

    def get_available_interface(self):
        return self.plumlib.get_phyattpoint_available_interface()

    def create_policy_tag(self, tenant_id, policy_tag_db):
        return self.plumlib.create_policy_tag(tenant_id, policy_tag_db)

    def delete_policy_tag(self, tenant_id, ptag_id):
        return self.plumlib.delete_policy_tag(tenant_id, ptag_id)

    def create_endpoint_group(self, tenant_id, ep_grp, ptag_db):
        return self.plumlib.create_endpoint_group(tenant_id, ep_grp,
                                                  ptag_db)

    def delete_endpoint_group(self, tenant_id, epg_id, ptag_db):
        return self.plumlib.delete_endpoint_group(tenant_id, epg_id,
                                                  ptag_db)

    def update_endpoint_group(self, tenant_id, epg_id, epg_db, ptag_db):
        return self.plumlib.update_endpoint_group(tenant_id, epg_id, epg_db,
                                                  ptag_db)

    def create_policy_service(self, tenant_id, ps_db, ps_mac_list):
        self.plumlib.create_policy_service(tenant_id, ps_db, ps_mac_list)

    def delete_policy_service(self, tenant_id, ps_id):
        self.plumlib.delete_policy_service(tenant_id, ps_id)

    def update_policy_service(self, tenant_id, ps_id, ps_db, ps_mac_list):
        self.plumlib.update_policy_service(tenant_id, ps_id, ps_db,
                                           ps_mac_list)

    def create_policy_rule(self, tenant_id, pr_db):
        self.plumlib.create_policy_rule(tenant_id, pr_db)

    def delete_policy_rule(self, tenant_id, pr_id):
        self.plumlib.delete_policy_rule(tenant_id, pr_id)

    def create_endpoint(self, tenant_id, ep_db, port_mac=None):
        self.plumlib.create_endpoint(tenant_id, ep_db, port_mac=port_mac)

    def delete_endpoint(self, tenant_id, ep_id, ep_db, port_mac=None):
        self.plumlib.delete_endpoint(tenant_id, ep_id, ep_db,
                                     port_mac=port_mac)

    def update_endpoint(self, tenant_id, ep_id, ep_db, port_mac=None):
        self.plumlib.update_endpoint(tenant_id, ep_id, ep_db,
                                     port_mac=port_mac)
