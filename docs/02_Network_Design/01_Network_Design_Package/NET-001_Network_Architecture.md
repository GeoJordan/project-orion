
---

## 1. Document Mission

The Network Architecture document defines the target network architecture for Project Orion and serves as the authoritative high-level design for the network infrastructure.

It establishes the architectural vision, business objectives, engineering principles, and technical requirements that guide the design, implementation, security, and future expansion of the Project Orion network environment.

This document provides the architectural foundation for the physical topology, logical topology, IP addressing plan, security zoning, implementation procedures, and operational documentation contained within the Network Design Package.

The architecture defined in this document shall be reviewed and approved before production network configuration begins, ensuring that implementation activities remain aligned with Project Orion governance, configuration management, cybersecurity, and documentation standards.

---

## 2. Document Control

| Field | Value |
|-------|-------|
| **Document ID** | NET-001 |
| **Document Title** | Network Architecture |
| **Project** | Project Orion |
| **Project Baseline** | Baseline 1.0 |
| **Current Phase** | Phase 2 – Network Infrastructure |
| **Current Sprint** | Sprint 2 |
| **Owner** | George Jordan |
| **Technical Advisor** | Technical Advisor |
| **Document Version** | 1.0 |
| **Status** | Baselined |
| **Classification** | Internal |
| **Created** | 2026-07-13 |
| **Last Updated** | 2026-07-16 |

---

## 3. Revision History

| Version | Date | Author | Reviewer | Description |
|----------|------|--------|----------|-------------|
| 0.1 | 2026-07-13 | George Jordan | Project Technical Advisor | Initial Network Architecture High-Level Design framework established. |
| 0.2     | 2026-07-14 | George Jordan | Project Technical Advisor  | Successfully completed Technical Design Review and Architecture Gate Review 001; approved to proceed to detailed engineering design. |
| **1.0** | **2026-07-16** | George Jordan | Project Technical Advisor | Baselined following Sprint 2 Network Design Package review. |

---

## 4. Executive Summary

Project Orion is an enterprise-inspired infrastructure engineering initiative that applies governance, cybersecurity, and systems engineering best practices to the design and implementation of a secure network environment. The network architecture serves as the foundational platform for all current and future Project Orion infrastructure services.

The architecture is designed to provide secure Internet connectivity, centralized network management, reliable communications, and a scalable foundation capable of supporting server infrastructure, home automation services, network-attached devices, video surveillance, and future technology expansion. The design emphasizes simplicity, maintainability, and operational resilience while remaining appropriate for a small healthcare-inspired environment.

Project Orion adopts a governance-first engineering methodology in which architectural planning, documentation, technical review, and configuration management precede implementation. Every significant design decision is documented, reviewed, and validated before production deployment to ensure consistency with the project's governance standards and cybersecurity objectives.

Upon completion, the network will provide a secure and well-documented infrastructure capable of supporting the GL.iNet Flint 2, Dell OptiPlex server platform, Home Assistant, Reolink surveillance devices, IoT technologies, and future enterprise networking capabilities while serving as a portfolio demonstration of professional infrastructure engineering practices.

## 📋 Architecture at a Glance

| Category | Value |
|----------|-------|
| **Architecture Type** | Enterprise-Inspired Small Healthcare Infrastructure |
| **Project Phase** | Phase 2 – Network Infrastructure |
| **Network Role** | Primary Infrastructure Platform |
| **Primary Router** | GL.iNet Flint 2 |
| **Internet Provider** | Verizon Fios (Ethernet ONT) |
| **Server Platform** | Dell OptiPlex 7060 Micro |
| **Planned Core Services** | Home Assistant, Video Surveillance, IoT Automation, Infrastructure Management |
| **Engineering Methodology** | Governance-First, Security by Design, Documentation Before Implementation |
| **Target State** | Secure, scalable, well-documented enterprise-inspired infrastructure |

---

## 5. Business Objectives

| ID | Business Objective |
|----|--------------------|
| BO-01 | Design and implement a secure, reliable, and scalable network infrastructure that serves as the operational foundation for all Project Orion technology services. |
| BO-02 | Ensure all network engineering activities comply with Project Orion governance, documentation, configuration management, and change control standards. |
| BO-03 | Provide a resilient infrastructure platform capable of supporting server services, home automation, video surveillance, IoT technologies, and future enterprise capabilities. |
| BO-04 | Establish a maintainable and well-documented network architecture that simplifies administration, troubleshooting, recovery, and future expansion. |
| BO-05 | Demonstrate enterprise infrastructure engineering practices through a governance-first implementation methodology suitable for professional portfolio development and continuous technical learning. |

---

## 6. Design Principles

| ID | Principle | Description |
|----|-----------|-------------|
| DP-01 | Security by Design | Security controls shall be incorporated into the network architecture from the outset rather than added after implementation. |
| DP-02 | Governance Before Configuration | All significant architectural and configuration decisions shall be documented, reviewed, and approved before implementation. |
| DP-03 | Documentation Before Implementation | Engineering documentation shall precede production configuration to ensure consistency, traceability, and maintainability. |
| DP-04 | Least Privilege | Administrative access and network permissions shall be limited to the minimum level required for operational responsibilities. |
| DP-05 | Recoverability | Critical infrastructure components shall support documented backup, restoration, and recovery procedures. |
| DP-06 | Scalability | The network architecture shall support future expansion with minimal redesign or disruption to existing services. |
| DP-07 | Simplicity | Network designs should remain as simple as practical while satisfying business, operational, and security requirements. |
| DP-08 | Standardization | Consistent naming conventions, documentation standards, and configuration practices shall be applied throughout the Project Orion environment. |

---

## 7. High-Level Architecture

### Architecture Overview

Project Orion adopts a layered network architecture that separates Internet connectivity, infrastructure services, endpoint devices, automation platforms, and future expansion capabilities into well-defined architectural components. The design emphasizes security, maintainability, scalability, and governance while providing a stable foundation for future enterprise-inspired services.

### Architectural Components

| Layer | Purpose |
|--------|---------|
| Internet Layer | Provides external connectivity through Verizon Fios. |
| Edge Layer | GL.iNet Flint 2 provides routing, firewall, NAT, and network security services. |
| Infrastructure Layer | Dell OptiPlex server hosts core infrastructure services. |
| Service Layer | Home Assistant, surveillance, and automation platforms. |
| Endpoint Layer | Trusted devices, cameras, IoT devices, and guest systems. |

### High-Level Diagram

                    Internet
                        │
                Verizon Fios ONT
                        │
                GL.iNet Flint 2
                        │
        ┌───────────────┼───────────────┐
        │               │               │
   Dell Server      Trusted LAN     Future Expansion
        │
   Home Assistant
        │
 Cameras / IoT Devices

 ---

 ## 8. Design Assumptions

| ID | Assumption | Rationale |
|----|------------|-----------|
| DA-01 | Verizon Fios Internet service is available through an Ethernet-connected ONT. | Provides the external network connection for the Project Orion environment. |
| DA-02 | The GL.iNet Flint 2 will operate as the primary network gateway and firewall. | Establishes a single point of network routing and security management. |
| DA-03 | The Dell OptiPlex 7060 Micro will serve as the primary infrastructure server. | Provides the hosting platform for core infrastructure services. |
| DA-04 | Home Assistant will be deployed after the network and server foundations are validated. | Ensures that application services are introduced only after the underlying infrastructure is stable. |
| DA-05 | Reolink cameras and IoT devices will connect using Wi-Fi unless future infrastructure requirements dictate otherwise. | Supports the initial deployment while allowing for future architectural evolution. |
| DA-06 | Project Orion governance, documentation, and configuration management standards will remain in effect throughout implementation. | Ensures engineering activities remain consistent with approved project governance. |
| DA-07 | Future network segmentation may be introduced without requiring a complete architectural redesign. | Supports scalability and long-term maintainability. |

---

## 9. Network Requirements

| ID | Requirement | Business Objective |
|----|-------------|--------------------|
| NR-01 | The network shall provide secure and reliable Internet connectivity for all authorized Project Orion infrastructure services. | BO-01 |
| NR-02 | The network shall support centralized management of network infrastructure and connected devices. | BO-02 |
| NR-03 | The network shall provide a secure platform capable of supporting server infrastructure, home automation services, surveillance systems, and IoT devices. | BO-03 |
| NR-04 | The network shall support future logical segmentation and expansion without requiring a complete architectural redesign. | BO-04 |
| NR-05 | The network shall provide documented configuration, backup, and recovery capabilities for critical infrastructure components. | BO-04 |
| NR-06 | The network shall support secure administrative access consistent with Project Orion governance and security principles. | BO-02 |
| NR-07 | The network shall maintain architecture, documentation, and configuration consistency throughout the implementation lifecycle. | BO-05 |
| NR-08 | The network shall provide a scalable foundation capable of supporting future enterprise-inspired technologies and services. | BO-03 |

---

## 10. Design Constraints

| ID | Constraint | Impact |
|----|------------|--------|
| DC-01 | The network shall utilize the existing Verizon Fios Internet service and Ethernet ONT as the external connectivity platform. | Internet architecture must integrate with the existing ISP infrastructure. |
| DC-02 | The GL.iNet Flint 2 shall serve as the primary routing and firewall platform for the initial deployment. | Router selection is fixed for Phase 2 implementation. |
| DC-03 | The Dell OptiPlex 7060 Micro shall host the initial server infrastructure. | Infrastructure services must operate within the capabilities of the selected hardware platform. |
| DC-04 | Initial deployment shall utilize existing Wi-Fi connectivity for surveillance cameras and IoT devices. | Physical cabling requirements are minimized during early implementation. |
| DC-05 | Network implementation shall comply with all approved Project Orion governance, documentation, and configuration management standards. | Engineering activities must follow the approved governance framework. |
| DC-06 | The architecture shall support future expansion without requiring a complete redesign of the network foundation. | Long-term scalability must be considered during all design decisions. |
| DC-07 | The design shall remain appropriate for a residential small healthcare-inspired environment while incorporating enterprise engineering practices. | Solutions should balance enterprise capabilities with practical deployment considerations. |
| DC-08 | Project Orion shall prioritize open standards, maintainability, and cost-effective engineering decisions whenever practical. | Technology selections should support long-term sustainability and operational efficiency. |

---

## 11. Success Criteria

| ID | Success Criterion | Verification Method |
|----|-------------------|---------------------|
| SC-01 | Secure Internet connectivity is available to authorized infrastructure services. | Connectivity validation and functional testing. |
| SC-02 | Core infrastructure services operate reliably on the Dell OptiPlex server platform. | Service availability and operational verification. |
| SC-03 | Home Assistant and planned network services integrate successfully with the infrastructure platform. | Functional application testing. |
| SC-04 | Administrative access is secured and documented according to Project Orion governance standards. | Configuration review and security validation. |
| SC-05 | Network documentation accurately reflects the implemented environment. | Documentation review against deployed configuration. |
| SC-06 | Backup and recovery procedures are documented and successfully validated. | Backup restoration testing. |
| SC-07 | The network architecture supports future expansion without requiring structural redesign. | Architecture review and scalability assessment. |
| SC-08 | All implementation activities comply with approved Project Orion governance and configuration management processes. | Governance compliance review and engineering audit. |

---

## 12. Related Documents

| Document | Relationship |
|----------|--------------|
| NET-000 – Network Design Package Index | Master index for all network engineering documentation within the Project Orion Network Design Package. |
| PM-001 – Project Control Center | Provides overall project governance, current work planning, milestones, and engineering progress. |
| PM-003 – Sprint Status Tracker | Tracks Sprint 2 progress, deliverables, risks, and completion status. |
| PM-005 – Decision Log | Records architectural and engineering decisions affecting the network design. |
| PM-006 – Engineering Session Log | Documents engineering activities, lessons learned, and implementation progress throughout Sprint 2. |
| STD-001 – Document Control Standard | Defines document governance, revision control, versioning, approval, and archival requirements applicable to this document. |
| NET-002 – Physical Network Topology | Defines the physical layout and connectivity of the Project Orion network infrastructure. |
| NET-003 – Logical Network Topology | Defines logical network segmentation, traffic flow, and network relationships. |
| NET-004 – IP Addressing Plan | Defines network addressing, subnet allocation, and address management strategy. |
| NET-005 – Network Device Inventory      | Asset inventory and lifecycle management        |
| NET-006 – Network Naming Standard       | Standardized naming conventions                 |
| NET-007 – Security Zones & Access Rules | Security architecture and access control        |
| NET-008 – Implementation & Test Plan    | Deployment, validation, and rollback procedures |

---

