# NET-003 — Logical Network Topology

## 1. Document Mission

The Logical Network Topology document defines the logical organization, segmentation, and communication pathways of the Project Orion infrastructure. It establishes how infrastructure components interact across the network independently of their physical locations.

This document provides the engineering reference for logical connectivity, trust boundaries, traffic flows, security zoning, and future network segmentation. It serves as the foundation for implementing secure communications, network policy, IP addressing, and access control throughout the Project Orion environment.

---

## 2. Document Control

| Field | Value |
|--------|-------|
| **Document ID** | NET-003 |
| **Document Title** | Logical Network Topology |
| **Project** | Project Orion |
| **Project Baseline** | Baseline 1.0 |
| **Owner** | George Jordan |
| **Technical Advisor** | Project Technical Advisor |
| **Version** | 1.0 |
| **Status** | Baselined |
| **Classification** | Internal |
| **Created** | 2026-07-15 |
| **Last Updated** | 2026-07-16 |

---

## 3. Revision History

| Version | Date | Author | Reviewer | Description |
|----------|------|--------|----------|-------------|
| 0.1 | 2026-07-15 | George Jordan | Project Technical Advisor | Initial Logical Network Topology document created. |
| **1.0** | **2026-07-16** | George Jordan | Project Technical Advisor | Baselined following Sprint 2 Network Design Package review. |

---

## 4. Executive Summary

The Logical Network Topology document defines the communication model for the Project Orion infrastructure. It identifies logical relationships between network devices, trusted systems, administrative endpoints, surveillance platforms, automation services, and future IoT components.

The logical design emphasizes secure segmentation, least-privilege communication, controlled administrative access, and scalable network organization. It provides the engineering foundation for IP addressing, security zoning, firewall policy development, and logical implementation planning.

---

## 5. Logical Network Overview

The Project Orion logical network is organized into functional network segments that support secure communication, simplified administration, and future scalability. The logical design separates infrastructure management, administrative devices, surveillance systems, and IoT components into distinct trust domains while allowing only the communications required for normal operation.

The logical topology follows a defense-in-depth approach. Critical infrastructure services are isolated from end-user and IoT devices where practical, reducing the attack surface and supporting future implementation of Zero Trust principles.

Although the initial deployment operates within a residential environment, the logical architecture follows enterprise-inspired practices suitable for a small healthcare organization. The design anticipates future implementation of network segmentation, firewall policies, VLANs, and role-based administrative access.

---

## 6.   Logical Design Objectives

| ID     | Objective            | Description                                                   |
| ------ | -------------------- | ------------------------------------------------------------- |
| LDO-01 | Secure Segmentation  | Separate infrastructure, user, IoT, and surveillance traffic. |
| LDO-02 | Least Privilege      | Allow only required communications between logical segments.  |
| LDO-03 | Scalability          | Support future VLANs and additional services.                 |
| LDO-04 | Manageability        | Simplify administration and troubleshooting.                  |
| LDO-05 | Defense in Depth     | Support layered security controls.                            |
| LDO-06 | Zero Trust Readiness | Prepare the design for future Zero Trust implementation.      |
| **LDO-07** | Operational Resilience | Maintain essential management and monitoring capabilities during component failures or maintenance activities. |

---

## 7. Network Segments

| Segment ID | Logical Network           | Primary Purpose        | Primary Systems                                | Trust Level   |
| ---------- | ------------------------- | ---------------------- | ---------------------------------------------- | ------------- |
| LNS-01     | Infrastructure Management | Network administration | GL.iNet Flint 2, Dell OptiPlex, Home Assistant | **High**      |
| LNS-02     | Administrative Devices    | Administration         | Laptop, Samsung Tablet                         | **High**      |
| LNS-03     | Surveillance              | Cameras                | Reolink Devices                                | **Medium**    |
| LNS-04     | Home Automation           | IoT                    | Zigbee Devices                                 | **Low**       |
| LNS-05     | Guest Network             | Guest Internet         | Guest Devices                                  | **Untrusted** |

---

## 8. Trust Boundaries

| Boundary ID | Source                    | Destination               | Trust      | **Enforcement**                        | Rationale                          |
| ----------- | ------------------------- | ------------------------- | ---------- | -------------------------------------- | ---------------------------------- |
| TB-01       | Infrastructure Management | Administrative Devices    | Trusted    | Authentication + Administrative Access | Administrative management required |
| TB-02       | Administrative Devices    | Surveillance              | Restricted | Firewall Rules                         | Management only                    |
| TB-03       | Home Automation           | Infrastructure Management | Restricted | Allow Required Services Only           | Home Assistant integrations        |
| TB-04       | Surveillance              | Home Automation           | Restricted | Allow Required Services Only           | Automation events                  |
| TB-05       | Guest Network             | Internal Networks         | Denied     | Firewall Isolation                     | Internet only                      |

---

## 9. Traffic Flow

| Flow ID | Source                    | Destination               | Direction     | Traffic Type              | **Protocol / Service** | Status  |
| ------- | ------------------------- | ------------------------- | ------------- | ------------------------- | ---------------------- | ------- |
| TF-01   | Administrative Devices    | Infrastructure Management | Bidirectional | Administrative Management | HTTPS, SSH, RDP        | Allowed |
| TF-02   | Infrastructure Management | Surveillance              | Outbound      | Device Management         | HTTPS                  | Allowed |
| TF-03   | Surveillance              | Home Automation           | Outbound      | Automation Events         | HTTPS / API            | Allowed |
| TF-04   | Home Automation           | Infrastructure Management | Bidirectional | Automation Services       | HTTPS, MQTT            | Allowed |
| TF-05   | Guest Network             | Internal Networks         | Any           | All Traffic               | All                    | Denied  |
| TF-06   | Guest Network             | Internet                  | Outbound      | Internet Access           | HTTP, HTTPS, DNS       | Allowed |

---

## 10. Logical Connectivity Matrix

| Source Network | Infrastructure | Administrative | Surveillance | Home Automation | Guest Network |
|----------------|:--------------:|:--------------:|:------------:|:---------------:|:-------------:|
| Infrastructure | ✓ | ✓ | ✓ | ✓ | ✗ |
| Administrative | ✓ | ✓ | ✓ (Mgmt Only) | ✗ | ✗ |
| Surveillance | ✗ | ✗ | ✓ | ✓ | ✗ |
| Home Automation | ✓ (Required Services) | ✗ | ✓ | ✓ | ✗ |
| Guest Network | ✗ | ✗ | ✗ | ✗ | Internet Only |

### Matrix Legend

- ✓ = Communication permitted
- ✓ (Mgmt Only) = Administrative management traffic only
- ✓ (Required Services) = Only explicitly approved application traffic
- ✗ = Communication denied
- Internet Only = Direct Internet access permitted; no internal network access

---

## 11. Security Zones

| Zone ID | Security Zone               | Included Networks         | Security Level | Primary Controls       | **Typical Users** |
| ------- | --------------------------- | ------------------------- | -------------- | ---------------------- | ----------------- |
| SZ-01   | Trusted Infrastructure Zone | Infrastructure Management | High           | MFA, firewall policies | Administrators    |
| SZ-02   | Administrative Zone         | Administrative Devices    | High           | Endpoint protection    | Administrators    |
| SZ-03   | Surveillance Zone           | Reolink Devices           | Medium         | Network isolation      | Cameras           |
| SZ-04   | IoT Zone                    | Home Automation           | Low            | Least privilege        | IoT Devices       |
| SZ-05   | Guest Zone                  | Guest Network             | Untrusted      | Internet-only          | Guests            |

---

## 12. Future Segmentation Strategy

The logical architecture has been designed to support phased expansion without requiring significant redesign of the underlying infrastructure. As Project Orion evolves, logical network segmentation will be strengthened through the introduction of dedicated VLANs, enhanced firewall policies, and additional security controls.

Future enhancements include:

| Future Enhancement | Purpose |
|--------------------|---------|
| Dedicated Infrastructure VLAN | Isolate network management traffic. |
| Administrative VLAN | Separate administrative workstations from infrastructure services. |
| Surveillance VLAN | Isolate security cameras from user devices. |
| IoT VLAN | Restrict smart devices to approved communications only. |
| Guest VLAN | Provide Internet-only access for guest devices. |
| Healthcare Services VLAN | Support future healthcare-inspired applications and protected services. |
| Zero Trust Policies | Enforce device identity and least-privilege communications. |
| Centralized Monitoring | Expand logging, monitoring, and security analytics. |

The proposed segmentation strategy supports the long-term scalability, maintainability, and security objectives established throughout the Project Orion engineering program.

### Engineering Notes

Future logical segmentation shall preserve the communication model, trust boundaries, and least-privilege principles established within this document.

Any future VLAN implementation shall remain consistent with the Project Orion security architecture and implementation standards.

---

## 13.  High-Level Logical Topology Diagram

                    Internet
                        │
                        ▼
               GL.iNet Flint 2
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
Infrastructure     Administrative   Guest Network
 Management          Devices        (Internet Only)
        │
        │
        ▼
 Home Automation
        ▲
        │
        ▼
 Surveillance

---

## 14.  Related Documents

| Document | Relationship                  |
| -------- | ----------------------------- |
| NET-000  | Network Design Package Index  |
| NET-001  | Approved Network Architecture |
| NET-002  | Physical Network Topology     |
| NET-004  | IP Addressing Plan            |
| PM-001   | Project Control Center        |
| PM-006   | Engineering Session Log       |

---


