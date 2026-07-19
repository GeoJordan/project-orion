# NET-002 — Physical Network Topology

## 1. Document Mission

The Physical Network Topology document defines the physical layout, placement, and interconnection of all infrastructure components within Project Orion. It provides the authoritative engineering reference for device locations, physical connectivity, cabling, power distribution, installation planning, and infrastructure deployment.

This document supports implementation of the approved network architecture by translating high-level architectural concepts into a practical physical design. It serves as the foundation for installation, maintenance, troubleshooting, infrastructure expansion, and future engineering activities throughout the Project Orion lifecycle.

---

## 2. Document Control

| Field | Value |
|--------|-------|
| **Document ID** | NET-002 |
| **Document Title** | Physical Network Topology |
| **Project** | Project Orion |
| **Project Baseline** | Baseline 1.0 |
| **Owner** | George Jordan |
| **Technical Advisor** | Project Technical Advisor |
| **Version** | 1.0 |
| **Status** | Baselined |
| **Classification** | Internal |
| **Created** | 2026-07-14 |
| **Last Updated** | 2026-07-16 |

---

## 3. Revision History

| Version | Date | Author | Reviewer | Description |
|----------|------|--------|----------|-------------|
| 0.1 | 2026-07-14 | George Jordan | Project Technical Advisor | Initial Physical Network Topology document created. |
| **1.0** | **2026-07-16** | George Jordan | Project Technical Advisor | Baselined following Sprint 2 Network Design Package review. |

---

## 4. Executive Summary

The Physical Network Topology document defines the physical deployment of the Project Orion infrastructure environment. It identifies the placement of networking equipment, server infrastructure, surveillance devices, administrative workstations, and supporting technologies required to implement the approved network architecture.

The design emphasizes simplicity, maintainability, physical security, and scalability while ensuring that infrastructure components are positioned to support reliable operation, efficient maintenance, and future expansion.

The physical topology serves as the implementation blueprint for subsequent network engineering activities, including logical network design, IP addressing, security zoning, and deployment planning.

---

## 5. Physical Environment

| Category | Description |
|----------|-------------|
| **Deployment Type** | Residential home office supporting a small healthcare-inspired environment |
| **Internet Service Provider** | Verizon Fios |
| **Internet Entry Point** | Verizon Optical Network Terminal (ONT) |
| **Primary Network Equipment** | GL.iNet Flint 2 |
| **Server Platform** | Dell OptiPlex 7060 Micro |
| **Primary Platform** | Home Assistant |
| **Surveillance Platform** | Reolink Security Cameras |
| **Administrative Devices** | Windows Laptop, Samsung Galaxy Tab A9+ |
| **Future Expansion** | Zigbee coordinator, smart sensors, smart locks, additional cameras |

---

## 6. Physical Design Objectives

| ID | Design Objective | Description |
|----|------------------|-------------|
| PDO-01 | Reliable Connectivity | Ensure all infrastructure components maintain stable and resilient physical network connectivity. |
| PDO-02 | Simplified Installation | Minimize installation complexity through organized device placement and structured cabling. |
| PDO-03 | Maintainability | Position infrastructure components to allow efficient maintenance, troubleshooting, and upgrades. |
| PDO-04 | Physical Security | Locate critical equipment to minimize unauthorized access and accidental damage. |
| PDO-05 | Scalability | Support future expansion including additional IoT devices, cameras, smart sensors, and network services without major redesign. |
| PDO-06 | Power Reliability | Organize power distribution to support stable operation and future UPS integration. |
| PDO-07 | Cable Management | Minimize cable clutter while maintaining clear identification and serviceability. |
| PDO-08 | Standards Compliance | Ensure the physical design supports the governance, documentation, and engineering standards established throughout Project Orion. |

---

## 7. Infrastructure Components

| ID | Component | Function | Status |
|----|-----------|----------|--------|
| NIC-01 | Verizon Fios ONT | Internet service termination point providing WAN connectivity to the Project Orion network. | Existing |
| NIC-02 | GL.iNet Flint 2 | Primary router, firewall, and network gateway supporting wired and wireless connectivity. | Existing |
| NIC-03 | Dell OptiPlex 7060 Micro | Primary infrastructure server hosting Home Assistant and future network services. | Existing |
| NIC-04 | Home Assistant | Central automation, monitoring, and smart home management platform. | Planned Deployment |
| NIC-05 | Samsung Galaxy Tab A9+ | Dedicated infrastructure dashboard and Home Assistant control interface. | Existing |
| NIC-06 | Reolink Video Doorbell | Smart entrance monitoring and visitor management. | Existing |
| NIC-07 | Reolink E1 Outdoor Pro | Outdoor surveillance camera supporting perimeter monitoring. | Existing |
| NIC-08 | Administrative Laptop | Engineering workstation used for administration, documentation, and infrastructure management. | Existing |
| NIC-09 | Zigbee Coordinator | Future wireless coordinator supporting low-power IoT devices. | Future |
| NIC-10 | Smart Sensors & Locks | Future environmental monitoring and physical access devices. | Future |

---

## 8. Device Placement

| ID | Component | Proposed Location | Installation Considerations |
|----|-----------|-------------------|-----------------------------|
| NIC-01 | Verizon Fios ONT | Utility area / Internet entry point | Existing ISP installation. |
| NIC-02 | GL.iNet Flint 2 | Central office location | Maximize Wi-Fi coverage and simplify cable runs. |
| NIC-03 | Dell OptiPlex 7060 | Office workstation area | Close to router, protected from dust and heat. |
| NIC-04 | Home Assistant | Hosted on NIC-03 | Virtual deployment on Dell OptiPlex server. |
| NIC-05 | Samsung Galaxy Tab A9+ | Office wall mount / desktop stand | Dedicated infrastructure dashboard. |
| NIC-06 | Reolink Video Doorbell | Main entrance | Existing doorbell replacement. |
| NIC-07 | Reolink E1 Outdoor Pro | Exterior corner overlooking driveway | Maximize surveillance coverage. |
| NIC-08 | Administrative Laptop | Office workspace | Primary engineering workstation. |
| NIC-09 | Zigbee Coordinator | USB extension from Dell OptiPlex | Reduce RF interference from server chassis. |
| NIC-10 | Smart Sensors & Locks | Doors, windows, monitored rooms | Future phased deployment. |

---

## 9. Physical Connectivity

| Connection ID | Source | Destination | Connection Type | Purpose |
|--------------|--------|-------------|-----------------|---------|
| PC-01 | Verizon Fios ONT | GL.iNet Flint 2 | Ethernet (WAN) | Internet connectivity |
| PC-02 | GL.iNet Flint 2 | Dell OptiPlex 7060 | Ethernet (LAN) | Primary infrastructure connectivity |
| PC-03 | GL.iNet Flint 2 | Administrative Laptop | Ethernet / Wi-Fi | Infrastructure administration |
| PC-04 | GL.iNet Flint 2 | Samsung Galaxy Tab A9+ | Wi-Fi | Home Assistant dashboard access |
| PC-05 | GL.iNet Flint 2 | Reolink Video Doorbell | Wi-Fi | Video surveillance |
| PC-06 | GL.iNet Flint 2 | Reolink E1 Outdoor Pro | Wi-Fi | Outdoor surveillance |
| PC-07 | Dell OptiPlex 7060 | Zigbee Coordinator | USB | Zigbee device communication |
| PC-08 | Zigbee Coordinator | Smart Sensors & Locks | Zigbee Wireless | Future IoT connectivity |

---

## 10. Cabling Strategy

| Cable ID | Connection | Cable Type | Routing Strategy | Notes |
|----------|------------|------------|------------------|-------|
| CB-01 | ONT → Flint 2 | Cat6 Ethernet | Existing ISP cable path | WAN connection |
| CB-02 | Flint 2 → Dell OptiPlex | Cat6 Ethernet | Office cable run | Primary LAN |
| CB-03 | Flint 2 → Administrative Laptop | Cat6 Ethernet / Wi-Fi | Office workspace | Flexible connectivity |
| CB-04 | Dell → Zigbee Coordinator | USB Extension Cable | Short USB extension | Minimize RF interference |

### Cabling Standards

- Use Cat6 Ethernet cabling for all wired network connections.
- Maintain cable separation from power lines where practical.
- Label all permanent Ethernet cables at both ends.
- Bundle and secure cables using reusable Velcro straps.
- Maintain service loops where appropriate to simplify maintenance.
- Document all future cable additions within this topology document.

---

## 11. Power Strategy

| Power ID | Component | Power Source | Backup Strategy | Notes |
|----------|-----------|--------------|-----------------|-------|
| PW-01 | Verizon Fios ONT | AC Mains | Existing ISP battery (if available) | Existing installation |
| PW-02 | GL.iNet Flint 2 | AC Adapter | Future UPS | Maintain Internet connectivity |
| PW-03 | Dell OptiPlex 7060 | AC Power | Future UPS | Protect Home Assistant services |
| PW-04 | Samsung Galaxy Tab A9+ | Internal Battery / Charger | Battery operation | Dashboard remains portable |
| PW-05 | Reolink Devices | Manufacturer Power Supply | None | Future UPS evaluation |

### Engineering Notes

The physical topology has been designed to minimize cable length, simplify maintenance, improve equipment accessibility, and support future infrastructure expansion without requiring major redesign.

Physical installation shall follow the placement, connectivity, cabling, and power strategies defined within this document.
---

## 12. Installation Considerations

| Category | Consideration |
|----------|---------------|
| Physical Security | Install critical infrastructure in controlled indoor locations. |
| Environmental Protection | Protect equipment from moisture, dust, and excessive heat. |
| Accessibility | Maintain sufficient clearance for servicing equipment. |
| Wireless Coverage | Position Wi-Fi equipment centrally to maximize coverage. |
| Cable Management | Route cables neatly and label permanent connections. |
| Future Expansion | Reserve space for additional IoT devices and infrastructure. |
| Documentation | Update Project Orion documentation after all installation changes. |

### Engineering Notes

Future logical segmentation shall preserve the communication model, trust boundaries, and least-privilege principles established within this document.

Any future VLAN implementation shall remain consistent with the Project Orion security architecture and implementation standards.

---

## 13. High-Level Physical Topology

                Internet
                    │
                    │
           Verizon Fios ONT
                    │
          WAN (Cat6 Ethernet)
                    │
             GL.iNet Flint 2
        ┌───────────┼────────────┐
        │           │            │
   Dell OptiPlex  Laptop     Wi-Fi Clients
        │
        │ USB
        ▼
 Zigbee Coordinator
        │
  Smart Sensors

Wi-Fi:
───────────────
Samsung Tablet
Reolink Doorbell
Reolink E1 Outdoor Pro

---

## 14.  Related Documents

| Document | Relationship                  |
| -------- | ----------------------------- |
| NET-000  | Network Design Package Index  |
| NET-001  | Approved Network Architecture |
| NET-003  | Logical Network Topology      |
| NET-004  | IP Addressing Plan            |
| PM-001   | Project Control Center        |
| PM-006   | Engineering Session Log       |

---

