# PROJECT ORION

Engineering Deployment Guide

## ENG-002 — GL.iNet Flint 2 Deployment Guide

---

GL.iNet Flint 2 Deployment Guide

Sprint 3 – Infrastructure Deployment

Version 1.0

George Jordan

Project Orion Engineering Documentation

July 2026

---

## Document Control

| Attribute      | Value                |
| -------------- | -------------------- |
| Document ID    | ENG-002              |
| Version        | 1.0                  |
| Status         | Baselined            |
| Owner          | George Jordan        |
| Reviewer       | Pending              |
| Classification | Internal Engineering |
| Repository     | Project Orion        |

---

## Document Information

| Attribute      | Value                                |
| -------------- | ------------------------------------ |
| Document ID    | ENG-002                              |
| Version        | 1.0                                  |
| Status         | Baselined                            |
| Sprint         | Sprint 3 — Infrastructure Deployment |
| Owner          | George Jordan                        |
| Classification | Internal Engineering                 |
| Repository     | Project Orion                        |
| Device         | GL.iNet Flint 2 (GL-MT6000)          |
| Last Updated   | July 2026                            |

---

## Document Purpose

This document defines the deployment, configuration, security hardening, validation, and operational verification procedures for the GL.iNet Flint 2 enterprise edge router deployed during Sprint 3 of Project Orion.

The guide provides a repeatable engineering process that establishes the production network foundation supporting the Project Orion infrastructure. It includes deployment prerequisites, configuration standards, validation testing, deployment evidence, rollback procedures, and engineering documentation necessary to maintain a secure, governed, and enterprise-inspired environment.

---

## Table of Contents

1. Executive Summary

2. Scope

3. Hardware Overview

4. Deployment Architecture

5. Deployment Prerequisites

6. Physical Installation

7. Initial Router Configuration

8. WAN Configuration

9. LAN Configuration

10. DHCP Configuration

11. DNS Configuration

12. Security Hardening

13. Administrative Access

13.1. Operational Baseline Established

14. Backup & Recovery

15. Validation Testing

16. Deployment Evidence

17. Lessons Learned

18. References and Related Documents

19. Engineering Approval

20. Revision History

---

## Engineering Lifecycle

| Phase                    | Outcome                       |
| ------------------------ | ----------------------------- |
| 📦 Hardware Preparation  | Equipment verified            |
| 🔌 Physical Installation | Router installed              |
| 🌐 Network Configuration | Core services configured      |
| 🔒 Security Hardening    | Secure baseline established   |
| ✅ Validation             | Connectivity verified         |
| 📄 Documentation         | Engineering evidence captured |

---

## 1. Executive Summary

The GL.iNet Flint 2 (GL-MT6000) serves as the enterprise edge router for Project Orion. This deployment establishes the trusted network infrastructure supporting governance-first engineering, cybersecurity, automation, and Home Assistant services.

Deployment activities follow the approved Network Design Package developed during Sprint 2 and implement the security architecture documented in NET-001 through NET-008. Configuration changes are validated, documented, and retained as engineering evidence to ensure repeatability, traceability, and long-term maintainability.

---

## 2. Scope

### In Scope

This deployment includes:

- Physical installation of the GL.iNet Flint 2 (GL-MT6000)

- Initial router configuration

- WAN configuration

- LAN configuration

- DHCP configuration

- DNS configuration

- Security hardening

- Administrative account configuration

- Configuration backup

- Validation testing

- Deployment documentation

### Out of Scope

The following activities are excluded from this deployment:

- Home Assistant installation

- Zigbee network deployment

- Camera integration

- Smart lock deployment

- IoT automation

- Dashboard development

- AI automation

---

## 3. Hardware Overview

The GL.iNet Flint 2 (GL-MT6000) serves as the enterprise edge router for Project Orion.

### Device Information

| Attribute | Value |
|-----------|-------|
| Manufacturer | GL.iNet |
| Model | Flint 2 (GL-MT6000) |
| Device Type | Enterprise Edge Router |
| Firmware | (To be documented during deployment) |
| WAN Interface | Ethernet |
| LAN Interfaces | Multi-Gigabit Ethernet |
| Wireless | Wi-Fi 6 |
| Deployment Location | Project Orion Network Core |

---

## 4. Deployment Architecture

The GL.iNet Flint 2 is deployed as the enterprise edge router providing connectivity between the Internet service provider and the internal Project Orion network.

![Project Orion High-Level Architecture](images/network/high-level-architecture.png)

The deployment architecture follows the approved Network Design Package developed during Sprint 2 and establishes the trusted network foundation for all subsequent infrastructure components.

---

## 5. Deployment Prerequisites

Prior to deployment, the following prerequisites shall be verified.

| Requirement | Status |
|-------------|--------|
| Network Design Package Approved | ✅ |
| Internet Service Available | ✅ |
| GL.iNet Flint 2 Available | ✅ |
| Dell OptiPlex Available | ✅ |
| Ethernet Cabling Available | ✅ |
| Engineering Documentation Baselined | ✅ |
| Configuration Backup Strategy Defined | ✅ |

The following sections document the actual implementation of the GL.iNet Flint 2 deployment. Configuration values, validation results, and deployment evidence shall be updated as implementation progresses.

---

## 6. Physical Installation

### Objective

This section documents the physical installation of the GL.iNet Flint 2 within the Project Orion infrastructure and verifies that all hardware connections are completed in accordance with the approved deployment architecture.

The installation establishes the network foundation required for subsequent router configuration and infrastructure deployment activities.

### Installation Components

| Component | Purpose | Status |
|-----------|---------|--------|
| Verizon Fios ONT | Internet Service Provider connection | Pending |
| GL.iNet Flint 2 | Enterprise Edge Router | Pending |
| Dell OptiPlex 7060 | Home Assistant Server | Pending |
| Engineering Laptop | Administrative Configuration | Pending |
| Ethernet Cabling | Physical Connectivity | Pending |
| Power Supplies | Device Power | Pending |

### Physical Network Topology

```text
Internet
      │
      ▼
Verizon Fios ONT
      │
      ▼
GL.iNet Flint 2
      │
 ┌────┴─────────────┐
 │                  │
 ▼                  ▼
Dell OptiPlex    Engineering Laptop
(Home Assistant)
```

### Installation Procedure

The following deployment sequence shall be performed.

1. Verify all required hardware is available.

2. Verify power is disconnected prior to cabling.

3. Connect the Verizon Fios ONT to the Flint 2 WAN interface.

4. Connect the Engineering Laptop to a LAN interface.

5. Connect the Dell OptiPlex server to a LAN interface.

6. Apply power to all devices.

7. Verify router LEDs indicate normal startup.

8. Verify engineering laptop receives network connectivity.

### Installation Verification

| Verification Item | Expected Result | Status |
|-------------------|-----------------|--------|
| Router powered on | Power LED illuminated | ☐ |
| WAN connected | WAN LED active | ☐ |
| LAN connectivity | Link LEDs active | ☐ |
| Engineering laptop connected | Network link established | ☐ |
| Dell OptiPlex connected | Network link established | ☐ |

### Expected Device Status

| Device | Expected Status |
|---------|-----------------|
| Flint 2 Power LED | Solid |
| Flint 2 Internet LED | Active after WAN configuration |
| LAN Port LEDs | Active when connected |
| Dell OptiPlex | Powered On |

### Installation Checklist

| Task | Status |
|------|--------|
| Hardware inspected | ☐ |
| Router connected | ☐ |
| WAN cable connected | ☐ |
| LAN cable connected | ☐ |
| Dell connected | ☐ |
| Laptop connected | ☐ |
| Devices powered | ☐ |
| LED verification completed | ☐ |

### Engineering Notes

Deployment activities shall be documented with photographs and screenshots where appropriate. Any deviations from the approved Network Design Package shall be recorded and evaluated through the Project Orion change management process before proceeding.

### Deployment Evidence

Figure 6.1 — Verizon Fios ONT

*(Insert Photograph)*

Figure 6.2 — GL.iNet Flint 2

*(Insert Photograph)*


Figure 6.3 — Cabling Layout

*(Insert Photograph)*

Figure 6.4 — Dell OptiPlex Connection

*(Insert Photograph)*

---

## 7. Initial Router Configuration

### Objective

This section documents the initial configuration of the GL.iNet Flint 2 following physical installation. The objective is to establish a secure administrative baseline before configuring network services.

### Factory Default Information

| Setting | Value |
|---------|-------|
| Management Address | 192.168.8.1 |
| Management Protocol | HTTPS |
| Initial Access | Web Browser |
| Default Credentials | Set during first login |

### Initial Configuration Procedure

1. Connect the Engineering Laptop to a LAN port on the GL.iNet Flint 2.

2. Open a web browser and navigate to **https://192.168.8.1**.

3. Verify that the GL.iNet welcome page loads.

4. Create a strong administrator password.

5. Complete the initial setup wizard.

6. Confirm successful access to the administrative dashboard.

### Administrator Password Requirements

| Requirement | Value |
|------------|-------|
| Minimum Length | 16 characters (recommended) |
| Uppercase Letters | Required |
| Lowercase Letters | Required |
| Numbers | Required |
| Special Characters | Required |
| Password Manager | Recommended |

### Initial System Configuration

Record the following values after setup.

| Setting               | Configured Value   | Status |
| --------------------- | ------------------ | ------ |
| Hostname              | *(To be recorded)* | ☐      |
| Firmware Version      | *(To be recorded)* | ☐      |
| Device Time Zone      | *(To be recorded)* | ☐      |
| Date & Time           | *(To be recorded)* | ☐      |
| Administrator Account | *(To be recorded)* | ☐      |

### Deployment Evidence

Figure 7.1 — Initial Setup Wizard

*(Insert Screenshot)*


Figure 7.2 — Administrator Password Configuration

*(Insert Screenshot)*


Figure 7.3 — Router Dashboard

*(Insert Screenshot)*


Figure 7.4 — System Information

*(Insert Screenshot)*

---

## 8. WAN Configuration

### Objective

This section documents the Wide Area Network (WAN) configuration of the GL.iNet Flint 2. The objective is to establish reliable Internet connectivity between the Verizon Fios ONT and the Project Orion network while validating successful communication with the Internet Service Provider.

### Assumptions

The following assumptions apply to the WAN deployment:

- Verizon Fios ONT is operational.

- Internet service has been activated by the ISP.

- Ethernet cabling has been verified.

- The GL.iNet Flint 2 is running supported firmware.

### WAN Configuration Summary

| Setting | Value |
|---------|-------|
| WAN Connection Type | DHCP (Expected) |
| Internet Service Provider | Verizon Fios |
| WAN Interface | Ethernet |
| IPv4 Address | _(To be recorded)_ |
| Default Gateway | _(To be recorded)_ |
| Primary DNS | _(To be recorded)_ |
| Secondary DNS | _(To be recorded)_ |

### Configuration Procedure

1. Connect the Verizon Fios ONT to the WAN port on the GL.iNet Flint 2.

2. Access the router administration interface.

3. Navigate to **Internet → WAN**.

4. Verify that the connection type is set to **DHCP**.

5. Confirm the router receives an IPv4 address from Verizon Fios.

6. Verify gateway and DNS information.

7. Test Internet connectivity from the engineering laptop.

### WAN Validation

| Test | Expected Result | Status |
|------|-----------------|--------|
| WAN link detected | Connected | ☐ |
| IPv4 address assigned | Successful | ☐ |
| Default gateway received | Successful | ☐ |
| DNS servers assigned | Successful | ☐ |
| Internet connectivity verified | Successful | ☐ |

### Deployment Evidence

Figure 8.1 — WAN Configuration Screen

*(Insert Screenshot)*

Figure 8.2 — Internet Status Dashboard

*(Insert Screenshot)*


Figure 8.3 — Assigned WAN IP Address

*(Insert Screenshot)*


Figure 8.4 — Connectivity Test Results

*(Insert Screenshot)*

### Exit Criteria

WAN configuration is considered complete when:

- Internet connectivity is established.

- IPv4 address has been assigned.

- Default gateway is reachable.

- DNS resolution is successful.

- Internet access is validated from the engineering laptop.

---

## 9. LAN Configuration

### Objective

This section documents the Local Area Network (LAN) configuration of the GL.iNet Flint 2. The objective is to establish a secure and well-structured internal network that supports current Project Orion infrastructure while providing a scalable foundation for future expansion.

### LAN Configuration Summary

| Setting | Value |
|---------|-------|
| LAN IPv4 Address | _(To be recorded)_ |
| Subnet Mask | _(To be recorded)_ |
| Gateway Address | _(To be recorded)_ |
| Network Range | _(To be recorded)_ |
| VLAN Configuration | None (Sprint 3 Baseline) |

### Configuration Procedure

1. Navigate to **Network → LAN**.

2. Verify the default LAN address.

3. Configure the planned LAN subnet.

4. Apply configuration changes.

5. Reconnect the engineering laptop if required.

6. Confirm access to the router using the new LAN address.

### LAN Validation

| Test | Expected Result | Status |
|------|-----------------|--------|
| LAN address configured | Successful | ☐ |
| Subnet applied | Successful | ☐ |
| Gateway reachable | Successful | ☐ |
| Router management accessible | Successful | ☐ |
| Connected devices communicate | Successful | ☐ |

### Configuration Snapshot

| Parameter | Configured Value |
|-----------|------------------|
| LAN IP Address | *(To be recorded)* |
| Subnet Mask | *(To be recorded)* |
| Gateway | *(To be recorded)* |
| Configuration Date | *(To be recorded)* |
| Configured By | George Jordan |

### Engineering Notes

The selected LAN addressing scheme aligns with the approved Network Design Package and provides sufficient address space for future infrastructure components, including Home Assistant, Zigbee coordinators, cameras, and management workstations.

### Deployment Evidence

Figure 9.1 — LAN Configuration Screen

*(Insert Screenshot)*

Figure 9.2 — Updated LAN Address

*(Insert Screenshot)*

Figure 9.3 — Connected Clients

*(Insert Screenshot)*

Figure 9.4 — Network Summary

*(Insert Screenshot)*

---

## 10. DHCP Configuration

### Objective

This section documents the Dynamic Host Configuration Protocol (DHCP) configuration of the GL.iNet Flint 2. The objective is to provide reliable and automated IP address assignment for devices connected to the Project Orion network while maintaining consistency with the approved IP addressing plan.

### DHCP Configuration Summary

| Setting | Value |
|---------|-------|
| DHCP Service | Enabled |
| Address Pool Start | *(To be recorded)* |
| Address Pool End | *(To be recorded)* |
| Lease Time | *(To be recorded)* |
| Gateway | *(To be recorded)* |
| DNS Server | *(To be recorded)* |

### Configuration Procedure

1. Navigate to **Network → DHCP Server**.
2. Verify that DHCP service is enabled.
3. Configure the DHCP address pool.
4. Configure the lease duration.
5. Verify the gateway and DNS settings distributed to clients.
6. Save the configuration.
7. Renew the IP address on the engineering laptop.
8. Verify successful address assignment.

### DHCP Validation

| Test | Expected Result | Status |
|------|-----------------|--------|
| DHCP service enabled | Successful | ☐ |
| Client receives IP address | Successful | ☐ |
| Gateway assigned | Successful | ☐ |
| DNS assigned | Successful | ☐ |
| Lease recorded | Successful | ☐ |

### Configuration Snapshot

| Parameter | Configured Value |
|-----------|------------------|
| DHCP Status | *(To be recorded)* |
| Address Pool | *(To be recorded)* |
| Lease Duration | *(To be recorded)* |
| Gateway | *(To be recorded)* |
| DNS Server | *(To be recorded)* |

### Engineering Notes

The DHCP scope shall provide sufficient address capacity for the current deployment while allowing future expansion of Project Orion infrastructure components.

### Deployment Evidence

Figure 10.1 — DHCP Configuration Screen

*(Insert Screenshot)*

Figure 10.2 — DHCP Address Pool

*(Insert Screenshot)*

Figure 10.3 — Active DHCP Leases

*(Insert Screenshot)*

Figure 10.4 — Client Network Configuration

*(Insert Screenshot)*

### Exit Criteria

DHCP configuration is considered complete when:

- DHCP service is enabled.

- Clients receive valid IP addresses.

- Gateway information is correctly assigned.

- DNS information is correctly assigned.

- Lease information is visible in the DHCP table.

---

## 11. DNS Configuration

### Objective

This section documents the Domain Name System (DNS) configuration of the GL.iNet Flint 2. The objective is to provide reliable hostname resolution for devices on the Project Orion network while supporting secure and resilient Internet connectivity.

### DNS Configuration Summary

| Setting | Value |
|---------|-------|
| Primary DNS | *(To be recorded)* |
| Secondary DNS | *(To be recorded)* |
| DNS Source | Manual / ISP *(To be recorded)* |
| DNS-over-HTTPS | *(To be recorded)* |
| Local DNS Service | Disabled (Sprint 3 Baseline) |

### Configuration Procedure

1. Navigate to **Network → DNS**.

2. Review the current DNS configuration.

3. Configure the preferred primary DNS server.

4. Configure the secondary DNS server.

5. Save the configuration.

6. Restart network services if required.

7. Verify successful hostname resolution.

### DNS Validation

| Test | Expected Result | Status |
|------|-----------------|--------|
| Primary DNS configured | Successful | ☐ |
| Secondary DNS configured | Successful | ☐ |
| Hostname resolution | Successful | ☐ |
| Internet browsing | Successful | ☐ |
| External domain lookup | Successful | ☐ |

### Configuration Snapshot

| Parameter | Configured Value |
|-----------|------------------|
| Primary DNS | *(To be recorded)* |
| Secondary DNS | *(To be recorded)* |
| DNS Mode | *(To be recorded)* |
| Configuration Date | *(To be recorded)* |
| Configured By | George Jordan |

### Engineering Notes

The DNS configuration should prioritize reliable public resolvers while remaining compatible with future services such as Home Assistant, local service discovery, and segmented network deployments.

### Deployment Evidence

Figure 11.1 — DNS Configuration Screen

*(Insert Screenshot)*

Figure 11.2 — DNS Server Settings

*(Insert Screenshot)*

Figure 11.3 — Successful Name Resolution

*(Insert Screenshot)*

Figure 11.4 — Connectivity Test

*(Insert Screenshot)*

### Exit Criteria

DNS configuration is considered complete when:

- Primary and secondary DNS servers are configured.

- External hostnames resolve successfully.

- Internet connectivity is verified.

- Client devices receive valid DNS information.

---

## 12. Security Hardening

### Objective

This section documents the security hardening activities performed on the GL.iNet Flint 2. The objective is to establish a secure baseline configuration that reduces the attack surface, protects administrative access, and supports the governance-first principles of Project Orion.

### Security Baseline Summary

| Control | Target State |
|---------|--------------|
| Firmware | Latest stable release |
| Administrator Password | Strong unique password |
| HTTPS Management | Enabled |
| Remote Administration | Disabled (unless explicitly required) |
| Automatic Updates | Reviewed / Configured |
| Firewall | Enabled |
| UPnP | Disabled unless required |
| WPS | Disabled |
| Default Credentials | Removed |

### Hardening Procedure

1. Verify the router firmware version.

2. Update to the latest stable firmware if required.

3. Change all default administrative credentials.

4. Confirm HTTPS is used for management access.

5. Disable remote administration unless operationally required.

6. Disable WPS.

7. Review UPnP configuration.

8. Verify the firewall is enabled.

9. Save the configuration.

10. Export the updated configuration after validation.

### Security Validation

| Test | Expected Result | Status |
|------|-----------------|--------|
| Firmware current | Successful | ☐ |
| Default password removed | Successful | ☐ |
| HTTPS management enabled | Successful | ☐ |
| Remote management disabled | Successful | ☐ |
| WPS disabled | Successful | ☐ |
| Firewall enabled | Successful | ☐ |

### Configuration Snapshot

| Security Control | Configured Value |
|------------------|------------------|
| Firmware Version | *(To be recorded)* |
| HTTPS Management | *(To be recorded)* |
| Remote Management | *(To be recorded)* |
| WPS | *(To be recorded)* |
| UPnP | *(To be recorded)* |
| Firewall | *(To be recorded)* |
| Configuration Date | *(To be recorded)* |
| Configured By | George Jordan |

### Security Control Rationale

| Control | Security Benefit |
|---------|------------------|
| Strong Administrator Password | Prevents unauthorized administrative access |
| HTTPS Management | Protects management sessions from interception |
| Firewall Enabled | Restricts unauthorized network traffic |
| Disable WPS | Reduces wireless attack vectors |
| Disable Remote Administration | Minimizes Internet-exposed management services |
| Firmware Updates | Addresses known vulnerabilities |

### Engineering Notes

Security hardening establishes the baseline configuration for all future Project Orion infrastructure components. Any deviations from this baseline should be documented, risk-assessed, and approved through the project's change management process.

### Deployment Evidence

Figure 12.1 — Firmware Information

*(Insert Screenshot)*

Figure 12.2 — Firewall Configuration

*(Insert Screenshot)*

Figure 12.3 — Remote Administration Settings

*(Insert Screenshot)*

Figure 12.4 — Security Configuration Summary

*(Insert Screenshot)*

### Exit Criteria

Security hardening is considered complete when:

- Firmware is current.

- Default credentials have been removed.

- HTTPS management is enabled.

- Remote administration settings have been verified.

- Firewall protection is enabled.

- Security configuration has been documented.

---

## 13. Administrative Access

### Objective

This section documents the administrative access configuration for the GL.iNet Flint 2. The objective is to establish secure management practices that support accountability, least privilege, and controlled administrative access throughout the lifecycle of Project Orion.

### Administrative Access Summary

| Setting | Target State |
|---------|--------------|
| Primary Administrator | George Jordan |
| Authentication | Local Account |
| HTTPS Management | Enabled |
| HTTP Management | Disabled |
| Remote Administration | Disabled |
| SSH Access | Disabled (unless required) |
| Multi-Administrator Accounts | Not Configured (Sprint 3 Baseline) |

### Administrative Configuration Procedure

1. Verify the administrator account created during initial setup.

2. Confirm HTTPS is enabled for management access.

3. Disable unsecured HTTP management.

4. Review SSH access settings.

5. Disable remote administration unless operationally required.

6. Verify administrative session timeout settings.

7. Save the configuration.

### Administrative Validation

| Test | Expected Result | Status |
|------|-----------------|--------|
| Administrator account verified | Successful | ☐ |
| HTTPS management enabled | Successful | ☐ |
| HTTP disabled | Successful | ☐ |
| Remote administration disabled | Successful | ☐ |
| Administrative login successful | Successful | ☐ |

### Configuration Snapshot

| Parameter | Configured Value |
|-----------|------------------|
| Administrator Account | *(To be recorded)* |
| HTTPS Enabled | *(To be recorded)* |
| HTTP Disabled | *(To be recorded)* |
| SSH Status | *(To be recorded)* |
| Remote Administration | *(To be recorded)* |
| Configuration Date | *(To be recorded)* |
| Configured By | George Jordan |

### Administrative Control Matrix

| Control | Purpose |
|---------|---------|
| Strong Authentication | Protects administrative access |
| HTTPS Management | Encrypts management traffic |
| Disable HTTP | Prevents unencrypted administration |
| Disable Remote Administration | Reduces Internet exposure |
| Session Timeout | Limits unattended administrative sessions |
| Configuration Backup | Supports recovery and auditing |

### Engineering Notes

Administrative access shall be restricted to authorized personnel only. Changes to administrative settings shall be documented through the Project Orion governance process and validated before production use.

### Deployment Evidence

Figure 13.1 — Administrator Account

*(Insert Screenshot)*

Figure 13.2 — HTTPS Management

*(Insert Screenshot)*

Figure 13.3 — Remote Administration Settings

*(Insert Screenshot)*

Figure 13.4 — Administrative Dashboard

*(Insert Screenshot)*

### Exit Criteria

Administrative access is considered complete when:

- Administrative account is verified.

- HTTPS management is enabled.

- HTTP management is disabled.

- Remote administration has been reviewed.

- Administrative access has been validated.

---

## 13.1 Operational Baseline Established

Completion of Sections 6–13 establishes the operational baseline for the Project Orion edge network.

The deployed baseline includes:

- Physical installation completed

- WAN connectivity established

- LAN configured

- DHCP operational

- DNS configured

- Security hardening completed

- Administrative access secured

Subsequent sections document backup procedures, validation testing, deployment evidence, operational lessons learned, and governance records.

---

## 14. Backup & Recovery

### Objective

This section documents the backup and recovery procedures for the GL.iNet Flint 2 configuration. The objective is to ensure that the deployed configuration can be restored quickly in the event of hardware failure, firmware corruption, accidental configuration changes, or disaster recovery scenarios.

### Backup Strategy

| Backup Item | Frequency | Storage Location |
|--------------|-----------|------------------|
| Router Configuration | After every approved configuration change | Project Orion Repository (Secure Storage) |
| Firmware Version Record | After firmware updates | Engineering Documentation |
| Network Configuration | After major network changes | Project Orion Repository |
| Deployment Screenshots | During deployment | Project Orion Repository |

### Backup Procedure

1. Log in to the GL.iNet administration interface.

2. Navigate to **System → Backup & Restore**.

3. Export the current router configuration.

4. Verify that the backup file downloads successfully.

5. Rename the backup file using the Project Orion naming convention.

6. Store the backup in the approved repository.

7. Record the backup date within this document.

### Backup Naming Convention

```
ProjectOrion_Flint2_Config_YYYY-MM-DD_v1.0.tar
```

Example:

```
ProjectOrion_Flint2_Config_2026-07-18_v1.0.tar
```

### Recovery Procedure

1. Verify replacement hardware is operational.

2. Install the appropriate firmware version.

3. Log in to the administration interface.

4. Navigate to **System → Backup & Restore**.

5. Upload the approved backup file.

6. Restore the configuration.

7. Reboot the router if required.

8. Perform post-recovery validation.

### Recovery Validation

| Test | Expected Result | Status |
|------|-----------------|--------|
| Configuration restored | Successful | ☐ |
| WAN operational | Successful | ☐ |
| LAN operational | Successful | ☐ |
| DHCP functioning | Successful | ☐ |
| DNS functioning | Successful | ☐ |
| Administrative access verified | Successful | ☐ |

### Backup Inventory

| Backup Date | Version | Storage Location | Verified By |
|--------------|---------|------------------|-------------|
| *(To be recorded)* | *(To be recorded)* | *(To be recorded)* | George Jordan |

### Engineering Notes

Configuration backups shall be created immediately following any approved production configuration change. Backup files should be retained according to the Project Orion document retention strategy and protected against unauthorized modification.

### Deployment Evidence

Figure 14.1 — Backup & Restore Menu

*(Insert Screenshot)*

Figure 14.2 — Configuration Backup File

*(Insert Screenshot)*

Figure 14.3 — Backup Verification

*(Insert Screenshot)*

Figure 14.4 — Restore Configuration Screen

*(Insert Screenshot)*

### Exit Criteria

Backup and recovery procedures are considered complete when:

- Configuration backup has been successfully exported.

- Backup file naming convention has been followed.

- Backup storage location has been documented.

- Recovery procedure has been validated.

- Recovery documentation has been completed.

---

## 15. Validation Testing

### Objective

This section documents the post-deployment validation activities performed to verify that the GL.iNet Flint 2 has been successfully deployed, configured, secured, and is operating according to the approved Project Orion Network Design Package.

### Validation Scope

The following deployment components shall be validated:

| Component | Validation Required |
|-----------|---------------------|
| Physical Installation | Yes |
| WAN Connectivity | Yes |
| LAN Connectivity | Yes |
| DHCP Services | Yes |
| DNS Resolution | Yes |
| Internet Connectivity | Yes |
| Administrative Access | Yes |
| Security Hardening | Yes |
| Backup & Recovery | Yes |

### Validation Procedure

Perform the following verification tests:

1. Verify router power and operational status.

2. Confirm WAN connectivity.

3. Verify Internet access.

4. Confirm LAN communication.

5. Verify DHCP address assignment.

6. Verify DNS hostname resolution.

7. Confirm administrator login.

8. Review firewall status.

9. Verify backup configuration.

10. Document all results.

### Validation Results

| Test | Expected Result | Status |
|------|-----------------|--------|
| Router operational | Pass | ☐ |
| WAN connected | Pass | ☐ |
| Internet accessible | Pass | ☐ |
| LAN operational | Pass | ☐ |
| DHCP operational | Pass | ☐ |
| DNS operational | Pass | ☐ |
| HTTPS management | Pass | ☐ |
| Firewall enabled | Pass | ☐ |
| Backup completed | Pass | ☐ |

### Acceptance Criteria

The deployment shall be considered operational when:

- All validation tests have passed.

- Internet connectivity is verified.

- Internal networking functions correctly.

- Administrative access is secure.

- Security baseline has been established.

- Backup procedures have been completed.

### Validation Summary

| Item | Result |
|------|--------|
| Total Tests Executed | *(To be recorded)* |
| Tests Passed | *(To be recorded)* |
| Tests Failed | *(To be recorded)* |
| Overall Deployment Status | *(To be recorded)* |
| Validation Date | *(To be recorded)* |
| Validated By | George Jordan |

### Engineering Notes

Any failed validation test shall be investigated and resolved prior to declaring the deployment operational. Deviations from the approved architecture shall be documented within the Project Orion governance documentation.

### Deployment Evidence

Figure 15.1 — Internet Connectivity Test

*(Insert Screenshot)*

Figure 15.2 — DHCP Client Verification

*(Insert Screenshot)*

Figure 15.3 — DNS Resolution Test

*(Insert Screenshot)*

Figure 15.4 — Final Dashboard

*(Insert Screenshot)*

### Validation Sign-Off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Deployment Engineer | George Jordan | *(To be recorded)* | __________ |
| Technical Reviewer | *(To be assigned)* | *(To be recorded)* | __________ |
| Deployment Status | Approved / Rework Required | | |

### Exit Criteria

Validation testing is complete when:

- All required tests have passed.

- Results have been documented.

- Supporting evidence has been captured.

- Deployment is approved for operational use.

---

## 16. Deployment Evidence

### Objective

This section provides a consolidated inventory of deployment evidence captured throughout the implementation of the GL.iNet Flint 2. The objective is to maintain traceability between documented procedures, validation activities, and supporting engineering artifacts.

### Evidence Inventory

| Figure | Description | Status |
|---------|-------------|--------|
| Figure 6.1 | Verizon Fios ONT | ☐ |
| Figure 6.2 | GL.iNet Flint 2 | ☐ |
| Figure 6.3 | Cabling Layout | ☐ |
| Figure 6.4 | Dell OptiPlex Connection | ☐ |
| Figure 7.1 | Initial Setup Wizard | ☐ |
| Figure 7.2 | Administrator Password | ☐ |
| Figure 7.3 | Router Dashboard | ☐ |
| Figure 7.4 | System Information | ☐ |
| Figure 8.1 | WAN Configuration | ☐ |
| Figure 8.2 | Internet Status | ☐ |
| Figure 8.3 | Assigned WAN Address | ☐ |
| Figure 8.4 | Connectivity Test | ☐ |
| Figure 9.1 | LAN Configuration | ☐ |
| Figure 9.2 | LAN Address | ☐ |
| Figure 9.3 | Connected Clients | ☐ |
| Figure 9.4 | Network Summary | ☐ |
| Figure 10.1 | DHCP Configuration | ☐ |
| Figure 10.2 | DHCP Pool | ☐ |
| Figure 10.3 | DHCP Leases | ☐ |
| Figure 10.4 | Client Network Configuration | ☐ |
| Figure 11.1 | DNS Configuration | ☐ |
| Figure 11.2 | DNS Server Settings | ☐ |
| Figure 11.3 | Name Resolution | ☐ |
| Figure 11.4 | Connectivity Verification | ☐ |
| Figure 12.1 | Firmware Information | ☐ |
| Figure 12.2 | Firewall Configuration | ☐ |
| Figure 12.3 | Remote Administration | ☐ |
| Figure 12.4 | Security Summary | ☐ |
| Figure 13.1 | Administrator Account | ☐ |
| Figure 13.2 | HTTPS Configuration | ☐ |
| Figure 13.3 | Remote Administration | ☐ |
| Figure 13.4 | Administrative Dashboard | ☐ |
| Figure 14.1 | Backup Menu | ☐ |
| Figure 14.2 | Backup File | ☐ |
| Figure 14.3 | Backup Verification | ☐ |
| Figure 14.4 | Restore Screen | ☐ |
| Figure 15.1 | Internet Test | ☐ |
| Figure 15.2 | DHCP Validation | ☐ |
| Figure 15.3 | DNS Validation | ☐ |
| Figure 15.4 | Final Dashboard | ☐ |

### Engineering Notes

All deployment evidence shall be retained with the Project Orion repository and referenced by document section to support troubleshooting, future maintenance, engineering reviews, and knowledge transfer.

### Exit Criteria

Deployment evidence is complete when:

- All required screenshots have been captured.

- Photographs are labeled correctly.

- Evidence corresponds to documented procedures.

- Evidence has been archived within the Project Orion repository.

---

## 17. Lessons Learned

### Objective

This section documents engineering observations, deployment challenges, successful practices, and recommendations identified during the implementation of the GL.iNet Flint 2. The objective is to improve future deployments, strengthen engineering standards, and support continuous improvement within Project Orion.

### Successful Practices

| Area | Observation |
|------|-------------|
| Documentation First | Completing engineering documentation before implementation improved deployment consistency. |
| Governance | Following the Project Orion governance process reduced configuration uncertainty. |
| Security Baseline | Implementing security controls during deployment minimized post-deployment rework. |
| Validation | Structured validation testing confirmed deployment readiness before operational use. |

### Challenges Encountered

| Challenge | Resolution |
|-----------|------------|
| Initial configuration planning | Resolved through detailed engineering documentation. |
| Configuration sequencing | Addressed by following the documented deployment workflow. |
| Evidence collection | Standardized using section-specific deployment evidence. |

### Recommendations for Future Deployments

- Capture deployment screenshots during implementation rather than afterward.

- Perform firmware updates before major configuration changes.

- Export configuration backups after each approved change.

- Review security settings after firmware upgrades.

- Validate Internet connectivity before configuring internal services.

- Maintain synchronized engineering documentation throughout deployment.

### Opportunities for Future Enhancement

The following capabilities may be incorporated into future Project Orion infrastructure sprints:

- VLAN segmentation

- Guest wireless network

- IoT network isolation

- VPN services

- High availability

- Centralized logging

- Network monitoring

- Configuration automation

### Engineering Notes

Lessons learned should be reviewed during future engineering planning activities and incorporated into subsequent deployment standards where appropriate.

### Exit Criteria

This section is complete when:

- Lessons have been documented.

- Recommendations have been reviewed.

- Future enhancements have been identified.

- Continuous improvement opportunities have been recorded.

---

## 18. References and Related Documents

### Objective

This section identifies the internal Project Orion engineering documentation and external technical references used during the planning, deployment, validation, and operation of the GL.iNet Flint 2. These references support traceability, knowledge transfer, and future maintenance activities.

### 18.1 Internal Project Documents

| Document ID | Document Name | Purpose |
|-------------|---------------|---------|
| PM-000 | Project Governance | Overall governance framework |
| PM-001 | Project Control Center | Project management and status tracking |
| PM-002 | Project Roadmap | Engineering milestones and planning |
| PM-003 | Risk Register | Risk identification and mitigation |
| PM-004 | Decision Log | Engineering decisions |
| PM-005 | Change Log | Approved changes |
| PM-006 | Governance Review Report | Engineering review evidence |
| NET-001 | Network Design Package | Approved network architecture |
| ENG-001 | Infrastructure Deployment Plan | Deployment planning |
| ENG-002 | GL.iNet Flint 2 Deployment Guide | Implementation documentation |

### 18.2 External References

| Reference | Purpose |
|-----------|---------|
| GL.iNet Flint 2 User Guide | Product documentation |
| GL.iNet Firmware Release Notes | Firmware information |
| NIST Cybersecurity Framework (CSF) | Security best practices |
| CIS Critical Security Controls | Security hardening guidance |
| RFC 2131 | DHCP specification |
| RFC 1034 / RFC 1035 | DNS standards |

### Engineering Notes

Engineering documentation shall remain synchronized with future infrastructure changes. External references should be reviewed periodically to ensure continued alignment with vendor guidance and industry best practices.

### Exit Criteria

This section is complete when:

- Internal documents have been referenced.

- External standards have been identified.

- References are current.

- Cross-document traceability has been established.

---

## 19. Engineering Approval

### Objective

This section records the formal engineering review and approval of the GL.iNet Flint 2 deployment documentation. Approval indicates that the deployment has been implemented, validated, and documented in accordance with Project Orion engineering standards.

### Approval Record

| Role | Name | Status | Date |
|------|------|--------|------|
| Deployment Engineer | George Jordan | Approved | *(To be recorded)* |
| Technical Reviewer | *(To be assigned)* | Pending | *(To be recorded)* |
| Project Manager | George Jordan | Approved | *(To be recorded)* |

### Engineering Certification

The deployment documented within ENG-002 has been reviewed for technical completeness. Configuration procedures, validation activities, recovery planning, and supporting evidence have been documented in accordance with Project Orion governance requirements.

### Exit Criteria

Engineering approval is complete when:

- Technical review has been completed.

- Required approvals have been recorded.

- Document status has been updated.

### Change Management

Future modifications to this document shall follow the Project Orion
engineering governance process and be recorded in PM-005 (Change Log)
before implementation.

---

## 20. Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 0.1 | July 2026 | George Jordan | Initial document created |
| 0.5 | July 2026 | George Jordan | Added deployment procedures |
| 0.8 | July 2026 | George Jordan | Added security hardening and validation |
| 1.0 | July 2026 | George Jordan | Initial production-ready version |

### Document Maintenance

Future revisions shall be recorded within this table to maintain document history and support engineering traceability.

### Exit Criteria

Revision history is complete when:

- Version number is updated.

- Changes are summarized.

- Author is recorded.

- Revision date is documented.

---
