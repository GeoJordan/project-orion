# NET-004 — IP Addressing Plan

## 1. Document Mission

The IP Addressing Plan defines the IPv4 addressing strategy for Project Orion. It establishes standardized address allocation, static and dynamic IP assignment policies, reserved address ranges, infrastructure management addressing, and future expansion guidelines.

The purpose of this document is to ensure consistent network addressing, simplify administration, reduce configuration errors, and provide a scalable foundation for future network growth.

---

## 2. Document Control

| Field | Value |
|-------|-------|
| Document ID | NET-004 |
| Document Title | IP Addressing Plan |
| Project | Project Orion |
| Project Baseline | Baseline 1.0 |
| Owner | George Jordan |
| Technical Advisor | Project Technical Advisor |
| Version | 1.0 |
| Status | Baselined |
| Classification | Internal |
| Created | 2026-07-15 |
| Last Updated | 2026-07-16 |

---

## 3. Revision History

| Version | Date | Author | Reviewer | Description |
|----------|------------|---------------|---------------------------|--------------------------------|
| 0.1 | 2026-07-15 | George Jordan | Project Technical Advisor | Initial draft created. |
| 1.0 | 2026-07-16 | George Jordan | Project Technical Advisor | Baselined following successful Technical Design Authority review. |

---

## 4. Executive Summary

The Project Orion IP Addressing Plan establishes a standardized IPv4 addressing strategy for all network infrastructure, servers, management systems, IoT devices, and future network segments.

The addressing plan is designed to provide predictable device identification, simplify troubleshooting, improve network administration, and support future expansion without requiring significant redesign.

This document serves as the authoritative reference for all IP address assignments throughout Project Orion and shall be used during implementation, testing, operations, and future engineering changes.

---

## 5. Addressing Design Objectives

The IP addressing strategy for Project Orion shall adhere to the following engineering objectives:

1. Provide a logical and scalable IPv4 addressing structure.

2. Separate infrastructure, management, client, and IoT devices into clearly defined address ranges.

3. Reserve address capacity for future network growth and VLAN implementation.

4. Support simplified network troubleshooting and operational maintenance.

5. Standardize static IP assignments for all critical infrastructure devices.

6. Utilize DHCP for end-user and non-critical client devices where appropriate.

7. Maintain consistent addressing documentation to support engineering, operations, and disaster recovery.

8. Minimize future network redesign by implementing an expandable addressing strategy from project inception.

---

## 6. IPv4 Addressing Standard

Project Orion shall utilize private IPv4 addressing in accordance with RFC 1918.

### Addressing Standard

| Item | Standard |
|------|----------|
| IP Version | IPv4 |
| Address Space | Private Addressing |
| Network Range | 192.168.50.0/24 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.50.1 |
| Address Capacity | 254 Hosts |
| DHCP Support | Enabled |
| Static Address Support | Enabled |
| Future VLAN Support | Reserved |

### Engineering Rationale

The selected /24 subnet provides sufficient address capacity for the current Project Orion deployment while allowing structured address allocation for infrastructure, servers, IoT devices, user devices, and future network expansion.

The addressing strategy prioritizes simplicity, scalability, and maintainability while remaining compatible with enterprise networking best practices.

---

## 7. Network Address Allocation

| Address Range | Purpose | Assignment Method | Primary Devices |
|---------------|---------|-------------------|-----------------|
| 192.168.50.1 | Default Gateway | Static | GL.iNet Flint 2 |
| 192.168.50.2 – 192.168.50.19 | Core Network Infrastructure | Static | Switches, Controllers, Future Infrastructure |
| 192.168.50.20 – 192.168.50.39 | Servers & Management Systems | Static | Dell OptiPlex, Home Assistant, Management Services |
| 192.168.50.40 – 192.168.50.79 | Security & IoT Devices | Static | Reolink Cameras, Zigbee Coordinator, Future IoT |
| 192.168.50.80 – 192.168.50.149 | User Devices | DHCP Reservation / DHCP | Laptops, Tablets, Smartphones |
| 192.168.50.150 – 192.168.50.199 | Infrastructure Expansion | Reserved | Future Servers & Appliances |
| 192.168.50.200 – 192.168.50.254 | Future VLANs / Network Growth | Reserved | Future Networks |

### Engineering Notes

The address allocation strategy intentionally separates infrastructure, management systems, security devices, IoT devices, and end-user devices into dedicated address blocks.

This structured allocation:

- improves operational consistency;
- simplifies troubleshooting;
- minimizes address conflicts;
- supports future VLAN deployment;
- reduces implementation complexity; and
- provides long-term scalability for Project Orion.

---

## 8. Infrastructure Device Addressing

| Device | Planned IP | Assignment | Function |
|--------|--------------------|------------|---------|
| GL.iNet Flint 2 Router | 192.168.50.1 | Static | Default Gateway |
| Dell OptiPlex 7060 | 192.168.50.20 | Static | Home Assistant Host |
| Home Assistant | 192.168.50.21 | Static | Home Automation Platform |
| Reolink Video Doorbell | 192.168.50.40 | Static | Video Surveillance |
| Reolink E1 Outdoor Pro | 192.168.50.41 | Static | Video Surveillance |
| Zigbee Coordinator | 192.168.50.42 | Static | IoT Gateway |
| Samsung Galaxy Tab A9+ | Reserved by DHCP | DHCP Reservation | Home Assistant Dashboard |
| Future Managed Switch | 192.168.50.10 | Reserved | Network Infrastructure |
| Future NAS | 192.168.50.22 | Reserved | Network Storage |

### Engineering Notes

Critical infrastructure devices shall utilize static IPv4 addresses to ensure predictable management, simplified troubleshooting, and reliable integration with automation platforms.

Client devices intended for operational dashboards or recurring management tasks may utilize DHCP reservations to simplify administration while maintaining consistent network identity.

Reserved infrastructure addresses have been allocated to support future Project Orion expansion without requiring redesign of the addressing plan.

See NET-005 – Network Device Inventory for implementation details, hardware lifecycle information, and operational asset tracking.

---

## 9. DHCP Allocation Strategy

| Configuration Item | Value |
|--------------------|-------|
| DHCP Service | GL.iNet Flint 2 |
| DHCP Scope | 192.168.50.80 – 192.168.50.149 |
| Lease Duration | 24 Hours |
| DNS Server | GL.iNet Flint 2 (Default) |
| Gateway | 192.168.50.1 |
| DHCP Reservations | Enabled |
| Static Infrastructure Devices | Excluded from DHCP Scope |

### Engineering Notes

Dynamic IPv4 addressing shall be reserved primarily for end-user devices and temporary network clients.

Critical infrastructure components, management systems, surveillance devices, and automation platforms shall utilize static IP addressing to ensure consistent connectivity, predictable administration, and reliable service discovery.

DHCP reservations may be used for devices that require a consistent network identity while still benefiting from centralized DHCP management.

---

## 10. Reserved Address Ranges

| Address Range | Reserved For | Purpose |
|---------------|--------------|---------|
| 192.168.50.2 – 192.168.50.9 | Future Network Infrastructure | Routers, Firewalls, Core Services |
| 192.168.50.10 – 192.168.50.19 | Network Switching & Management | Managed Switches, Controllers |
| 192.168.50.22 – 192.168.50.39 | Additional Servers | NAS, Monitoring, Automation Services |
| 192.168.50.150 – 192.168.50.199 | Infrastructure Expansion | Future Core Services |
| 192.168.50.200 – 192.168.50.254 | Future VLANs & Network Growth | Segmentation and Expansion |

### Engineering Notes

Reserved address blocks shall remain unallocated until future engineering requirements justify their use.

Maintaining reserved address capacity minimizes future network redesign, preserves addressing consistency, and supports long-term scalability.

---

## 11. Future VLAN Addressing Strategy

Project Orion is initially deployed as a single IPv4 subnet. However, the addressing strategy reserves sufficient address space to support future logical segmentation through Virtual Local Area Networks (VLANs).

### Planned Future Network Segmentation

| VLAN | Purpose | Planned Address Space | Status |
|------|---------|-----------------------|--------|
| VLAN 10 | Network Infrastructure | 192.168.10.0/24 | Future |
| VLAN 20 | Servers & Management | 192.168.20.0/24 | Future |
| VLAN 30 | Security & Surveillance | 192.168.30.0/24 | Future |
| VLAN 40 | IoT Devices | 192.168.40.0/24 | Future |
| VLAN 50 | User Devices | 192.168.50.0/24 | Current |
| VLAN 60 | Guest Network | 192.168.60.0/24 | Future |

### Engineering Notes

The planned VLAN numbering aligns the VLAN identifier with the third octet of the associated IPv4 subnet to simplify administration, troubleshooting, and long-term maintainability.

The initial deployment intentionally utilizes a single subnet to reduce implementation complexity during early project phases.

Future VLAN implementation shall occur only after the network infrastructure, firewall policies, and operational management processes have matured sufficiently to support logical segmentation without introducing unnecessary administrative overhead.

The addressing strategy has been designed to enable future VLAN migration with minimal impact on existing infrastructure.

---

## 12. Address Management Standards

### Address Assignment Standards

| Category | Standard |
|----------|----------|
| Infrastructure Devices | Static IPv4 Address |
| Servers | Static IPv4 Address |
| Network Appliances | Static IPv4 Address |
| Security Devices | Static IPv4 Address |
| IoT Devices | Static IPv4 Address |
| User Devices | DHCP Reservation or DHCP |
| Guest Devices | DHCP Only |

### Documentation Standards

- All static IPv4 assignments shall be documented before implementation.
- Changes to address allocations shall be reflected in this document and related engineering documentation.
- Duplicate IP assignments are prohibited.
- Reserved address ranges shall not be reassigned without engineering review.
- Future VLAN allocations shall be documented prior to implementation.
- IP address changes shall be reviewed and approved through the Project Orion Change Management process before implementation.

### Engineering Notes

Maintaining accurate IP address documentation is essential for operational stability, troubleshooting, disaster recovery, and future engineering activities.

This document shall serve as the authoritative source for all IPv4 address assignments within Project Orion.

---

## 13. Future Expansion Considerations

The Project Orion IP addressing strategy has been designed to support long-term growth while minimizing future redesign efforts.

### Planned Expansion Areas

| Future Capability | Engineering Consideration |
|-------------------|---------------------------|
| Additional Network Infrastructure | Reserved static infrastructure address space supports future switches, firewalls, and network appliances. |
| Additional Servers | Reserved management address ranges accommodate future virtualization hosts, NAS devices, monitoring systems, and automation services. |
| Expansion of IoT Devices | Dedicated IoT address ranges allow additional sensors, controllers, and smart devices without affecting core infrastructure. |
| VLAN Implementation | The addressing strategy supports migration to dedicated VLANs with minimal disruption to existing services. |
| Remote Management | Static addressing simplifies secure remote administration and monitoring. |
| Disaster Recovery | Structured address allocation simplifies documentation restoration and infrastructure recovery. |

### Engineering Notes

The addressing strategy intentionally reserves sufficient capacity for future growth while maintaining predictable address allocation and operational simplicity.

Future expansion activities shall follow this addressing standard unless superseded by an approved engineering design change.

---

## 14. Related Documents

| Document ID | Document Title |
|-------------|----------------|
| PM-001 | Project Control Center |
| PM-005 | Decision Log |
| PM-006 | Engineering Session Log |
| NET-000 | Network Design Package Index |
| NET-001 | Network Architecture |
| NET-002 | Physical Network Topology |
| NET-003 | Logical Network Topology |
| NET-005 | Network Device Inventory |
| NET-006 | Network Naming Standard |
| NET-007 | Security Zones & Access Rules |
| NET-008 | Implementation & Test Plan |
| RFC 1918    | Address Allocation for Private Internets |

### Document Relationship

NET-004 establishes the authoritative IPv4 addressing strategy for Project Orion and supports the implementation, operation, and future evolution of the network infrastructure.

This document shall be referenced during network deployment, configuration management, operational support, and future engineering reviews.

---
