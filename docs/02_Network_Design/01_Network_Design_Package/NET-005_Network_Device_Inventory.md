# NET-005 — Network Device Inventory

---

## 1. Document Mission

The Network Device Inventory provides the authoritative record of all network-connected infrastructure, servers, security devices, management systems, end-user devices, and supporting hardware deployed within Project Orion.

This document establishes standardized inventory management practices to support engineering operations, configuration management, lifecycle planning, asset accountability, troubleshooting, disaster recovery, and future infrastructure expansion.

The inventory serves as the primary engineering reference for physical and logical network assets throughout the lifecycle of Project Orion.

---

## 2. Document Control

| Field | Value |
|-------|-------|
| Document ID | NET-005 |
| Document Title | Network Device Inventory |
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
| **1.0** | **2026-07-16** | George Jordan | Project Technical Advisor | Baselined following Sprint 2 Network Design Package review. |

---

## 4. Executive Summary

The Project Orion Network Device Inventory establishes the authoritative inventory of all physical and logical network-connected assets deployed throughout the Project Orion environment.

The inventory provides standardized documentation for infrastructure devices, servers, management systems, security equipment, surveillance devices, IoT components, and end-user systems.

Maintaining a comprehensive and accurate inventory supports engineering operations, asset accountability, configuration management, lifecycle planning, security management, disaster recovery, and future infrastructure expansion.

This document serves as the primary operational reference for network asset management throughout the lifecycle of Project Orion.

---

## 5. Inventory Objectives

The Network Device Inventory supports the following engineering objectives:

1. Maintain a complete and accurate inventory of all network-connected assets.

2. Establish standardized asset identification and classification.

3. Support configuration management and operational maintenance.

4. Improve asset accountability throughout the Project Orion lifecycle.

5. Facilitate troubleshooting, incident response, and disaster recovery.

6. Support security monitoring, vulnerability management, and compliance activities.

7. Track asset lifecycle status, including planned, active, maintenance, and retired devices.

8. Provide a scalable inventory framework that supports future infrastructure expansion.

---

## 6. Asset Classification Standard

Project Orion classifies network-connected assets according to their operational role, engineering function, and lifecycle management requirements.

### Asset Classification Matrix

| Asset Class | Prefix | Examples | Management Priority |
|-------------|--------|----------|---------------------|
| Network Infrastructure | NW | Router, Managed Switches | Critical |
| Servers & Management Systems | SRV | Dell OptiPlex, Home Assistant | Critical |
| Security & Surveillance | CAM | Reolink Cameras, Doorbell | High |
| IoT Devices | IOT | Zigbee Coordinator, Smart Sensors | Medium |
| End-User Devices | USR | Tablets, Laptops, Smartphones | Medium |
| Future Infrastructure | FUT | Planned Equipment | Planned |

### Asset Identification Standard

Each inventoried device shall receive a unique Asset ID using the following naming convention:

| Asset Type | Format | Example |
|------------|--------|---------|
| Network Infrastructure | NW-### | NW-001 |
| Servers | SRV-### | SRV-001 |
| Cameras | CAM-### | CAM-001 |
| IoT Devices | IOT-### | IOT-001 |
| User Devices | USR-### | USR-001 |
| Future Assets | FUT-### | FUT-001 |

### Engineering Notes

The standardized asset classification and identification scheme provides consistent engineering documentation, improves operational management, supports configuration control, and simplifies future asset lifecycle tracking.

Unique Asset IDs shall remain permanent throughout the lifecycle of each asset and shall not be reused after retirement.

---

## 7. Core Infrastructure Inventory

### Core Network Infrastructure

| Asset ID | Device | Manufacturer / Model | Planned IP | Physical Location | Lifecycle Status |
|----------|--------|----------------------|------------|-------------------|------------------|
| NW-001 | Primary Router | GL.iNet Flint 2 (GL-MT6000) | 192.168.50.1 | Network Cabinet | Active |
| NW-002 | Verizon Fios ONT | Verizon Optical Network Terminal | ISP Managed | Utility Entry Point | Active |
| NW-003 | Future Managed Switch | TBD | 192.168.50.10 | Network Cabinet | Planned |

### Engineering Notes

The Core Infrastructure Inventory identifies devices responsible for providing network connectivity and routing services throughout Project Orion.

Each infrastructure device shall maintain a permanent Asset ID, documented management information, and lifecycle status to support engineering operations, configuration management, and future infrastructure expansion.

---

## 8. Servers & Management Systems

### Server & Management Inventory

| Asset ID | Device | Manufacturer / Model | Planned IP | Primary Function | Physical Location | Lifecycle Status |
|----------|--------|----------------------|------------|------------------|-------------------|------------------|
| SRV-001 | Dell OptiPlex 7060 Micro | Dell OptiPlex 7060 Micro | 192.168.50.20 | Virtualization / Home Assistant Host | Office | Active |
| SRV-002 | Home Assistant | Home Assistant OS | 192.168.50.21 | Home Automation Platform | Dell OptiPlex 7060 | Active |
| SRV-003 | Future NAS | TBD | 192.168.50.22 | Centralized Storage & Backup | Network Cabinet | Planned |

### Engineering Notes

Servers and management systems provide the core operational services supporting Project Orion. These systems shall utilize static IPv4 addressing, maintain documented configuration information, and be included in backup, monitoring, and lifecycle management processes.

Future management platforms shall follow the established Project Orion asset identification and documentation standards.

---

## 9. Security & Surveillance Devices

### Security & Surveillance Inventory

| Asset ID | Device | Manufacturer / Model | Planned IP | Primary Function | Physical Location | Lifecycle Status |
|----------|--------|----------------------|------------|------------------|-------------------|------------------|
| CAM-001 | Reolink Video Doorbell | Reolink Wi-Fi Video Doorbell | 192.168.50.40 | Front Door Surveillance | Front Entrance | Active |
| CAM-002 | Reolink E1 Outdoor Pro | Reolink E1 Outdoor Pro | 192.168.50.41 | Exterior Surveillance | Exterior | Active |
| IOT-001 | Zigbee Coordinator | SONOFF Zigbee USB Coordinator | 192.168.50.42 | Zigbee Network Gateway | Dell OptiPlex 7060 | Planned |

### Engineering Notes

Security and surveillance devices provide continuous monitoring, physical security awareness, and support for home automation workflows.

All security devices shall utilize static IPv4 addressing, maintain documented configuration information, and be included within routine monitoring, firmware maintenance, and lifecycle management activities.

IoT gateway devices shall be documented separately from endpoint sensors to simplify operational management and future expansion.

---

## 10. End-User Devices

### End-User Device Inventory

| Asset ID | Device | Manufacturer / Model | Planned IP | Primary Function | Assigned User | Lifecycle Status |
|----------|--------|----------------------|------------|------------------|---------------|------------------|
| USR-001 | Samsung Galaxy Tab A9+ | Samsung Galaxy Tab A9+ | DHCP Reservation | Home Assistant Dashboard | Project Orion | Active |
| USR-002 | Engineering Workstation | Windows 11 Workstation | DHCP | Project Administration & Engineering | George Jordan | Active |
| USR-003 | Future Mobile Device | TBD | DHCP | Mobile Management | Project Orion | Planned |

### Engineering Notes

End-user devices provide operational access to Project Orion services, administration platforms, dashboards, and engineering resources.

User devices shall utilize DHCP or DHCP reservations as appropriate and shall comply with Project Orion security, maintenance, and lifecycle management standards.

Only authorized devices shall receive access to infrastructure management interfaces.

---

## 11. Device Lifecycle Management

### Lifecycle Status Definitions

| Lifecycle Status | Description |
|------------------|-------------|
| Planned | Approved for future deployment but not yet installed. |
| Active | Installed, configured, and operational. |
| Maintenance | Temporarily unavailable due to maintenance activities. |
| Retired | Permanently removed from operational service. |

### Lifecycle Management Standards

- Every inventoried asset shall have an assigned lifecycle status.
- Lifecycle status shall be reviewed during each engineering review cycle.
- Planned assets shall be updated to Active following successful deployment and validation.
- Retired assets shall remain documented for historical reference and audit purposes.
- Asset records shall be updated whenever significant hardware or configuration changes occur.

### Engineering Notes

Lifecycle management ensures that the Network Device Inventory accurately reflects the operational state of Project Orion.

Maintaining current lifecycle information supports engineering planning, configuration management, asset accountability, operational continuity, and audit readiness.

---

## 12. Inventory Maintenance Standards

### Inventory Update Requirements

| Activity | Requirement |
|----------|-------------|
| New Device Deployment | Inventory updated before production use. |
| Device Retirement | Inventory updated immediately following retirement. |
| Hardware Replacement | Asset record updated with new hardware information. |
| IP Address Changes | Inventory synchronized with NET-004 IP Addressing Plan. |
| Engineering Reviews | Inventory reviewed during each Project Orion engineering review cycle. |

### Documentation Standards

- All managed network-connected assets shall be recorded within this inventory.
- Asset records shall remain synchronized with the corresponding engineering documentation.
- Asset identifiers shall remain permanent and shall not be reassigned.
- Significant configuration changes shall be reflected in both inventory and related engineering documents.
- Inventory accuracy shall be verified during major project milestones and technical reviews.

### Engineering Notes

Maintaining an accurate inventory is essential for engineering operations, configuration management, incident response, disaster recovery, security management, and future infrastructure planning.

This document serves as the authoritative operational inventory for all managed Project Orion assets.

### Engineering Notes

The Network Device Inventory shall serve as the authoritative source for asset identification, lifecycle status, and operational ownership within Project Orion.

Engineering teams shall update this inventory whenever infrastructure assets are added, modified, relocated, or retired to ensure continued accuracy and operational readiness.

---

## 13. Future Expansion

The Network Device Inventory has been designed to support future growth while maintaining a consistent asset classification and documentation standard.

### Planned Expansion Areas

| Future Capability | Inventory Impact |
|-------------------|------------------|
| Additional Managed Switches | New NW asset records |
| Network Attached Storage (NAS) | Additional SRV asset records |
| Additional Security Cameras | Additional CAM asset records |
| Smart Home Sensors | Additional IOT asset records |
| Guest & Mobile Devices | Additional USR asset records |
| Future VLAN Infrastructure | Additional NW and SRV records |

### Engineering Notes

Future infrastructure shall be documented using the established Project Orion asset classification and identification standards.

The inventory structure has been intentionally designed to scale without requiring changes to document organization or asset identification methodology.

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
| NET-004 | IP Addressing Plan |
| NET-006 | Network Naming Standard |
| NET-007 | Security Zones & Access Rules |
| NET-008 | Implementation & Test Plan |

### Document Relationship

NET-005 serves as the authoritative operational inventory for Project Orion and complements the engineering design documents by documenting deployed and planned network assets.

This inventory shall remain synchronized with related engineering documentation throughout the Project Orion lifecycle.

---



