# NET-000 — Network Design Package Index

---

## Document Mission

The Network Design Package Index provides the authoritative inventory and completion status for the Project Orion network architecture documents. It ensures that the physical design, logical design, addressing model, security zones, implementation procedures, and validation requirements are developed and reviewed as a coordinated package before production configuration begins.

---

## Document Control

| Field | Value |
|---|---|
| Document ID | NET-000 |
| Document Title | Network Design Package Index |
| Project | Project Orion |
| Project Baseline | Baseline 1.0 |
| Owner | George Jordan |
| Technical Advisor | Project Technical Advisor |
| Document Version | 1.0 |
| Status | Baselined |
| Classification | Internal |
| Created | 2026-07-12 |
| Last Updated | 2026-07-16 |

---

## Revision History

| Version | Date | Author | Reviewer | Description |
|---|---|---|---|---|
| 0.1 | 2026-07-12 | George Jordan | Project Technical Advisor | Initial Network Design Package Index created. |
| **1.0** | **2026-07-16** | George Jordan | Project Technical Advisor | Baselined following completion of the Sprint 2 Network Design Package. |

---

## Design Package Objective

Design a secure, maintainable, and scalable network foundation for Project Orion before configuring the GL.iNet Flint 2 or connecting production devices.

The package will define:

- Physical network connections and equipment placement.
- Logical security zones and future segmentation.
- IP addressing and DHCP standards.
- Network device naming conventions.
- Administrative and inter-zone access requirements.
- Installation, validation, rollback, and documentation procedures.

---

## Design Package Register

| Document ID | Document Title                |    Status   |
| ----------- | ----------------------------- | :---------: |
| NET-001     | Network Architecture          | ✅ Baselined |
| NET-002     | Physical Network Topology     | ✅ Baselined |
| NET-003     | Logical Network Topology      | ✅ Baselined |
| NET-004     | IP Addressing Plan            | ✅ Baselined |
| NET-005     | Network Device Inventory      | ✅ Baselined |
| NET-006     | Network Naming Standard       | ✅ Baselined |
| NET-007     | Security Zones & Access Rules | ✅ Baselined |
| NET-008     | Implementation & Test Plan    | ✅ Baselined |

---

## Design Assumptions

- Verizon Fios provides Internet service through an Ethernet-connected ONT.
- The GL.iNet Flint 2 will operate as the primary Project Orion router.
- The Dell OptiPlex 7060 Micro will host the planned server platform.
- Home Assistant will be deployed only after the network and server foundations are validated.
- Reolink cameras and IoT devices should be isolated from trusted user devices where technically feasible.
- The Verizon router will be retained as a documented backup option.
- No router configuration will be treated as final until connectivity, security, rollback, and documentation tests pass.

---

## Target Security Zones

| Zone | Purpose | Preliminary Subnet |
|---|---|---|
| Management | Infrastructure administration | 192.168.10.0/24 |
| Trusted | Approved user endpoints | 192.168.20.0/24 |
| IoT | Smart-home and automation devices | 192.168.30.0/24 |
| Cameras | Video surveillance devices | 192.168.40.0/24 |
| Guest | Visitor and temporary devices | 192.168.50.0/24 |

> These subnets are preliminary design reservations and shall not be configured until the logical topology and implementation plan are approved.

---

## Design Approval Gate

Configuration of the production Flint 2 environment may begin only after:

- [x] Physical topology is approved.
- [x] Logical topology is approved.
- [x] IP addressing plan is approved.
- [x] Security-zone rules are approved.
- [x] Implementation and rollback procedures are documented.
- [x] Required configuration evidence and screenshots are defined.

---

## Sprint 2 Completion Summary

The Project Orion Network Design Package has successfully completed architectural design, technical review, and engineering baseline activities.

All network design documents have been reviewed, approved, and baselined through the Project Orion Technical Design Authority process.

This package now serves as the authoritative engineering reference for future implementation, testing, operations, and infrastructure expansion.

---
