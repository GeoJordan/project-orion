# NET-007 — Security Zones & Access Rules

---

## 1. Document Mission

The Security Zones & Access Rules document defines the logical security boundaries, trust relationships, and communication policies for Project Orion.

Its purpose is to establish a defense-in-depth architecture by separating infrastructure into security zones, controlling communication between those zones, and documenting the principles that govern secure network access.

This document serves as the authoritative reference for network segmentation and access control throughout the Project Orion environment.

---

## 2. Document Control

| Field | Value |
|--------|-------|
| Document ID | NET-007 |
| Document Title | Security Zones & Access Rules |
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

The Security Zones & Access Rules document establishes the logical security architecture for Project Orion by defining security zones, trust boundaries, and permitted communication paths between network segments.

The document supports a defense-in-depth strategy by minimizing unnecessary communication, enforcing least-privilege access, and providing a structured framework for future network segmentation, firewall policies, and access control decisions.

This document serves as the authoritative security architecture reference for all network communication within Project Orion.

---

## 5. Security Objectives

The Security Zones & Access Rules document supports the following engineering objectives:

1. Establish clearly defined security zones throughout Project Orion.

2. Protect critical infrastructure through logical network segmentation.

3. Apply the principle of least privilege to network communications.

4. Reduce attack surface by limiting unnecessary connectivity.

5. Support secure administration of infrastructure components.

6. Improve visibility into trusted and untrusted communication paths.

7. Provide a scalable foundation for future firewall and VLAN implementations.

8. Align Project Orion with enterprise security architecture best practices.

---

## 6. Security Zone Definitions

### Security Zone Matrix

| Security Zone | Purpose | Typical Assets |
|---------------|---------|----------------|
| Internet Zone | External networks and Internet connectivity | ISP, Public Internet |
| Management Zone | Infrastructure administration | GL.iNet Flint 2, Future Management Interfaces |
| Trusted User Zone | Authorized user devices | Engineering Workstation, Samsung Galaxy Tab A9+ |
| Server Zone | Core application and infrastructure services | Home Assistant Server, Future NAS |
| Security Zone | Surveillance systems | Reolink Cameras, Reolink Doorbell |
| IoT Zone | Smart devices and sensors | Zigbee Coordinator, Door Sensors, Motion Sensors |
| Guest Zone (Future) | Visitor devices | Guest Wi-Fi Clients |

### Engineering Notes

Each security zone represents a logical trust boundary.

Communication between zones shall be explicitly authorized based on operational requirements and the principle of least privilege.

Zones shall remain logically isolated unless documented access rules permit communication.

---

## 7. Zone Access Matrix

### Zone Communication Matrix

| Source Zone | Destination Zone | Allowed | Security Principle | Purpose |
|--------------|------------------|:------:|-------------------|---------|
| Trusted User Zone | Management Zone | ✅ | Least Privilege | Router and infrastructure administration |
| Trusted User Zone | Server Zone | ✅ | Business Need | Home Assistant management |
| Trusted User Zone | Security Zone | ✅ | Business Need | View live camera feeds and recordings |
| Trusted User Zone | IoT Zone | ✅ | Controlled Access | Configure and manage IoT devices |
| Management Zone | Server Zone | ✅ | Administrative Access | Infrastructure management |
| Management Zone | Security Zone | ✅ | Administrative Access | Camera administration |
| Management Zone | IoT Zone | ✅ | Administrative Access | Zigbee coordinator management |
| Server Zone | Security Zone | ✅ | Service Integration | Home Assistant camera integration |
| Server Zone | IoT Zone | ✅ | Service Integration | Home Assistant automation and sensor integration |
| Security Zone | Server Zone | ✅ | Service Integration | Camera event notifications and video streams |
| IoT Zone | Server Zone | ✅ | Service Integration | Sensor telemetry and automation events |
| Guest Zone | Management Zone | ❌ | Default Deny | Administrative systems isolated |
| Guest Zone | Server Zone | ❌ | Default Deny | Internal services protected |
| Guest Zone | Security Zone | ❌ | Default Deny | Security devices protected |
| Guest Zone | IoT Zone | ❌ | Default Deny | IoT devices isolated |
| IoT Zone | Internet Zone | ❌* | Controlled Exception | Internet access only when explicitly required |
| Security Zone | Internet Zone | ❌* | Controlled Exception | Cloud connectivity only if explicitly approved |

### Engineering Notes

Project Orion follows a **default-deny** security model.

Communication between security zones shall only be permitted when there is a documented operational requirement.

Administrative access shall originate only from the Trusted User Zone or Management Zone.

Future firewall rules, VLAN policies, and ACLs shall be derived from this Zone Communication Matrix.

### Security Zone Overview (Illustrative)

```text
                Internet
                    │
            ┌──────────────┐
            │ Management   │
            └──────┬───────┘
                   │
      ┌────────────┼────────────┐
      │            │            │
 Trusted User   Server Zone   Guest
      │            │            │
      │       ┌────┴────┐       │
      │       │         │       │
 Security   IoT Zone   (No Access)
```

*Figure 1. High-level logical security zone relationships within Project Orion. This diagram is illustrative and complements the detailed Zone Communication Matrix.*

---

## 8. Trust Boundaries

### Trust Boundary Matrix

| Boundary | Description | Security Objective |
|----------|-------------|--------------------|
| Internet → Project Orion | External traffic entering the network | Protect against unauthorized access and external threats |
| Trusted User Zone → Management Zone | Administrative access to network infrastructure | Restrict administration to authorized users only |
| Trusted User Zone → Server Zone | Access to Home Assistant and future services | Protect critical services while allowing legitimate management |
| Server Zone → IoT Zone | Automation and sensor communications | Permit only required service integrations |
| Server Zone → Security Zone | Camera integration and event processing | Allow monitored communication for surveillance services |
| Guest Zone → Internal Network | Separation of guest devices from trusted infrastructure | Prevent lateral movement and unauthorized access |

### Trust Boundary Principles

Project Orion implements the following trust boundary principles:

- Every security zone represents a logical trust boundary.
- Communication across trust boundaries shall require an approved operational purpose.
- Administrative interfaces shall never be directly accessible from untrusted networks.
- Security controls shall enforce the principle of least privilege.
- Future firewall rules and VLAN segmentation shall reinforce these trust boundaries.

### Engineering Notes

Trust boundaries reduce the likelihood of unauthorized lateral movement within the network.

Each boundary provides an opportunity to apply security controls such as:

- Firewall policies
- VLAN segmentation
- Access Control Lists (ACLs)
- Authentication and authorization
- Network monitoring and logging

Trust boundaries shall be reviewed whenever new devices, services, or security zones are introduced into Project Orion.

---

## 9. Administrative Access Rules

### Administrative Access Matrix

| Managed System | Authorized Zone | Approved Protocols | Authentication Requirement |
|----------------|-----------------|--------------------|----------------------------|
| GL.iNet Flint 2 Router | Trusted User Zone | HTTPS | Strong administrator password |
| Home Assistant Server | Trusted User Zone | HTTPS | Individual user accounts with strong passwords |
| Future NAS | Trusted User Zone | HTTPS / SSH | Individual administrator accounts |
| Reolink Cameras | Trusted User Zone | HTTPS | Administrator account |
| Zigbee Coordinator | Server Zone | Internal Integration | Managed through Home Assistant |
| Future Managed Switch | Management Zone | HTTPS / SSH | Administrator account |

### Administrative Security Requirements

- Administrative access shall originate only from authorized management devices.
- Default administrative credentials shall be changed before production deployment.
- Administrative interfaces shall never be exposed directly to the Internet.
- Strong, unique passwords shall be used for all administrative accounts.
- Administrative activity should be logged whenever supported by the platform.

### Engineering Notes

Administrative access represents the highest level of trust within Project Orion.

Management interfaces shall be protected through logical network segmentation and authenticated administrative access.

Future implementations may include multi-factor authentication (MFA) where supported by the platform.

---

## 10. Security Design Principles

Project Orion applies the following security design principles throughout the network architecture.

### Security Principles

| Principle | Description |
|-----------|-------------|
| Defense in Depth | Multiple layers of security controls protect critical assets. |
| Least Privilege | Access is granted only when required for legitimate operational purposes. |
| Default Deny | Network communication is denied unless explicitly authorized. |
| Network Segmentation | Security zones isolate systems with different trust levels. |
| Secure Administration | Administrative interfaces are accessible only from authorized zones. |
| Minimized Attack Surface | Unnecessary services and communication paths are eliminated whenever possible. |
| Scalability | Security controls support future infrastructure growth without redesign. |
| Continuous Improvement | Security architecture shall be periodically reviewed and updated as Project Orion evolves. |

### Engineering Notes

These principles provide the foundation for all future firewall policies, VLAN configurations, access control rules, and infrastructure security decisions within Project Orion.

All future engineering documents shall align with these principles.

---

## 11. Future Expansion

The Security Zones & Access Rules architecture has been designed to support future infrastructure growth while maintaining the security principles established in this document.

### Planned Security Expansion

| Future Capability | Security Consideration |
|-------------------|------------------------|
| Additional VLANs | Extend the existing security zone model while preserving logical isolation. |
| Additional Servers | Place new services within the appropriate security zone and apply least-privilege access. |
| Network Attached Storage (NAS) | Deploy within the Server Zone with restricted administrative access. |
| Additional IoT Devices | Assign devices to the IoT Zone and limit communications to approved services. |
| Additional Security Cameras | Place all surveillance devices within the Security Zone using existing access policies. |
| Guest Wireless Network | Isolate guest devices from all internal security zones. |
| Remote Administrative Access | Require VPN connectivity, strong authentication, and encrypted management protocols. |
| Cloud Service Integration | Permit only documented and approved outbound communications using secure protocols. |

### Engineering Notes

Future infrastructure shall adopt the security zone model, trust boundaries, and access control principles defined in this document.

New systems shall be evaluated through the Project Orion engineering governance process before being integrated into the production environment.

Security architecture shall be reviewed whenever significant infrastructure changes are introduced to ensure continued alignment with Project Orion security objectives.

---

## 12. Related Documents

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
| NET-006 | Network Naming Standard |
| NET-008 | Implementation & Test Plan |

### Document Relationship

NET-007 establishes the authoritative security architecture for Project Orion by defining security zones, trust boundaries, communication policies, and administrative access requirements.

This document complements:

- NET-003 by securing the logical network architecture.
- NET-004 by governing communication between IP address ranges.
- NET-005 by protecting managed infrastructure assets.
- NET-006 by applying security policies to standardized network identities.

NET-008 will implement and validate the security architecture defined within this document.

