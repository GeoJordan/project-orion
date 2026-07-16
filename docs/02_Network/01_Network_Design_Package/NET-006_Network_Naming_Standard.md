# NET-006 — Network Naming Standard

---

## 1. Document Mission

The Network Naming Standard establishes standardized naming conventions for all infrastructure devices, servers, network services, security systems, IoT devices, end-user equipment, and future technology assets within Project Orion.

The purpose of this standard is to promote consistency, improve operational management, simplify troubleshooting, support automation, and ensure scalable engineering practices throughout the lifecycle of Project Orion.

---

## 2. Document Control

| Field | Value |
|--------|-------|
| Document ID | NET-006 |
| Document Title | Network Naming Standard |
| Project | Project Orion |
| Project Baseline | Baseline 1.0 |
| Owner | George Jordan |
| Technical Advisor | Project Technical Advisor |
| Version | 1.0 |
| Status | Baselined |
| Classification | Internal |
| Created | 2026-07-16 |
| Last Updated | 2026-07-16 |

---

## 3. Revision History

| Version | Date | Author | Reviewer | Description |
|---------|------|--------|----------|-------------|
| 0.1 | 2026-07-16 | George Jordan | Project Technical Advisor | Initial draft created. |
| **1.0** | **2026-07-16** | George Jordan | Project Technical Advisor | Baselined following successful Technical Design Authority review. |


---

## 4. Executive Summary

The Network Naming Standard establishes consistent naming conventions for all managed devices, services, infrastructure components, and network resources within Project Orion.

Standardized naming improves operational efficiency by simplifying device identification, troubleshooting, configuration management, automation, monitoring, documentation, and future infrastructure expansion.

This document serves as the authoritative naming reference for all current and future Project Orion engineering assets and shall be applied consistently across all related engineering documentation.

---

## 5. Naming Objectives

The Network Naming Standard supports the following engineering objectives:

1. Establish consistent naming conventions across all Project Orion infrastructure.

2. Improve device identification during engineering operations and troubleshooting.

3. Support automation, scripting, monitoring, and configuration management.

4. Reduce ambiguity by assigning descriptive and standardized names.

5. Improve documentation consistency across all engineering deliverables.

6. Support future infrastructure growth without requiring changes to the naming methodology.

7. Align naming practices with enterprise infrastructure management principles.

8. Provide a scalable standard that supports long-term operational governance.

---

## 6. Naming Principles

Project Orion shall apply the following naming principles to all managed infrastructure, systems, and network resources.

### Naming Standards

| Principle | Standard |
|-----------|----------|
| Character Case | Uppercase letters |
| Separator | Hyphen (-) |
| Spaces | Not permitted |
| Special Characters | Not permitted |
| Prefix | Mandatory |
| Sequential Numbering | Three-digit format (001, 002, 003) |
| Abbreviations | Standardized throughout Project Orion |
| Readability | Human-readable and automation-friendly |

### General Naming Format

```
<PREFIX>-<FUNCTION>-<NUMBER>
```

Example:

```
SRV-HA-001
```

Where:

- **PREFIX** identifies the asset type.
- **FUNCTION** identifies the primary purpose.
- **NUMBER** provides a unique sequential identifier.

### Engineering Notes

Naming conventions shall remain consistent throughout Project Orion to improve operational management, scripting, automation, documentation, troubleshooting, and future infrastructure expansion.

Naming standards shall be applied consistently across all engineering documentation and deployed systems.

---

## 7. Infrastructure Device Naming Standards

### Infrastructure Naming Matrix

| Device Type | Prefix | Naming Format | Example |
|-------------|--------|---------------|---------|
| Router | RTR | RTR-<FUNCTION>-### | RTR-EDGE-001 |
| Managed Switch | SW | SW-<FUNCTION>-### | SW-CORE-001 |
| Firewall (Future) | FW | FW-<FUNCTION>-### | FW-EDGE-001 |
| Wireless Access Point (Future) | AP | AP-<LOCATION>-### | AP-MAIN-001 |

### Infrastructure Naming Notes

Infrastructure device names shall clearly identify the device type and operational role.

Examples:

- RTR-EDGE-001
- SW-CORE-001
- FW-EDGE-001
- AP-MAIN-001

Infrastructure names shall remain unique throughout Project Orion and shall not be reassigned after device retirement.

---

## 8. Server & Management System Naming Standards

### Server Naming Matrix

| System Type | Prefix | Naming Format | Example |
|-------------|--------|---------------|---------|
| Physical Server | SRV | SRV-<FUNCTION>-### | SRV-HOST-001 |
| Home Assistant | SRV | SRV-HA-### | SRV-HA-001 |
| Network Attached Storage (Future) | SRV | SRV-NAS-### | SRV-NAS-001 |
| Management Platform (Future) | SRV | SRV-MGMT-### | SRV-MGMT-001 |

### Server Naming Notes

Server names shall identify both the platform type and its primary operational function.

Examples:

- SRV-HOST-001
- SRV-HA-001
- SRV-NAS-001
- SRV-MGMT-001

Server names shall remain unique, descriptive, and consistent with the Project Orion Naming Principles.

---

## 9. Security & IoT Device Naming Standards

### Security & IoT Naming Matrix

| Device Type | Prefix | Naming Format | Example |
|-------------|--------|---------------|---------|
| Security Camera | CAM | CAM-<LOCATION>-### | CAM-FRONT-001 |
| Video Doorbell | CAM | CAM-DOORBELL-### | CAM-DOORBELL-001 |
| Zigbee Coordinator | IOT | IOT-ZB-### | IOT-ZB-001 |
| Door Sensor | IOT | IOT-DOOR-### | IOT-DOOR-001 |
| Motion Sensor | IOT | IOT-MOTION-### | IOT-MOTION-001 |
| Leak Sensor | IOT | IOT-LEAK-### | IOT-LEAK-001 |

### Security & IoT Naming Notes

Security and IoT device names shall identify both the device type and its physical location or operational function.

Examples:

- CAM-FRONT-001
- CAM-DOORBELL-001
- IOT-ZB-001
- IOT-DOOR-001
- IOT-MOTION-001
- IOT-LEAK-001

Device names shall remain unique and consistent with the Project Orion Naming Principles.

---

## 10. End-User Device & Wireless Naming Standards

### End-User Device Naming Matrix

| Device Type | Prefix | Naming Format | Example |
|-------------|--------|---------------|---------|
| Engineering Workstation | WS | WS-ENG-### | WS-ENG-001 |
| Tablet | TAB | TAB-OPS-### | TAB-OPS-001 |
| Laptop (Future) | LAP | LAP-USER-### | LAP-USER-001 |
| Smartphone (Future) | MOB | MOB-USER-### | MOB-USER-001 |

### Wireless Network Naming Matrix

| Network Type | SSID | Purpose |
|--------------|------|---------|
| Primary Network | ORION-PRIMARY | Trusted devices |
| IoT Network (Future) | ORION-IOT | IoT devices |
| Guest Network (Future) | ORION-GUEST | Guest access |
| Management Network (Future) | ORION-MGMT | Infrastructure management |

### Engineering Notes

End-user device names shall clearly identify the device type and operational role.

Wireless SSIDs shall remain descriptive, consistent, and aligned with the Project Orion network segmentation strategy defined in NET-003.

---

## 11. Naming Governance

### Naming Governance Requirements

| Activity | Requirement |
|----------|-------------|
| New Device Deployment | Assign a compliant name before production deployment. |
| Device Replacement | Retain the naming convention while updating inventory records as required. |
| New Services | Apply the appropriate naming standard before implementation. |
| Documentation Updates | Ensure all related engineering documents reflect approved names. |
| Engineering Reviews | Verify naming compliance during technical design reviews. |

### Engineering Notes

The Network Naming Standard shall serve as the authoritative reference for all hostnames, device names, wireless network identifiers, and management system names used within Project Orion.

All future engineering documentation shall comply with this standard.

---

## 12. Future Expansion

The Network Naming Standard has been designed to support future infrastructure growth without modification to the established naming methodology.

### Planned Expansion Areas

| Future Capability | Naming Impact |
|-------------------|---------------|
| Additional Network Devices | Apply existing infrastructure prefixes |
| Additional Servers | Continue SRV naming sequence |
| Additional Cameras | Continue CAM naming sequence |
| Additional IoT Devices | Continue IOT naming sequence |
| Additional End-User Devices | Continue WS, TAB, LAP, and MOB naming sequences |
| Future Cloud Services | Extend the standard using approved prefixes |

### Engineering Notes

Future technologies shall adopt the Project Orion Naming Principles while preserving consistency, readability, and scalability.

---

## 13. Related Documents

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
| NET-005 | Network Device Inventory |
| NET-007 | Security Zones & Access Rules |
| NET-008 | Implementation & Test Plan |

### Document Relationship

NET-006 establishes the authoritative naming conventions used throughout the Project Orion engineering documentation and complements the Network Device Inventory by defining standardized operational names for managed assets.

---

## 14. Approved Abbreviations

| Abbreviation | Meaning |
|--------------|---------|
| RTR | Router |
| SW | Managed Switch |
| FW | Firewall |
| AP | Wireless Access Point |
| SRV | Server |
| CAM | Camera |
| IOT | Internet of Things Device |
| WS | Workstation |
| TAB | Tablet |
| LAP | Laptop |
| MOB | Mobile Device |
| HA | Home Assistant |
| NAS | Network Attached Storage |
| MGMT | Management |
| EDGE | Edge Network |
| CORE | Core Infrastructure |

### Engineering Notes

These abbreviations are approved for use across Project Orion engineering documentation.

Future abbreviations shall be added to this appendix to maintain consistency across all technical standards.

