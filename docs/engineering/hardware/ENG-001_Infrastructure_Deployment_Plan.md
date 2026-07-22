# ENG-001 — Infrastructure Deployment Plan

## Document Information

| Attribute | Value |
|-----------|-------|
| Document ID | ENG-001 |
| Version | 1.0 |
| Status | Approved |
| Sprint | Sprint 3 — Infrastructure Deployment |
| Owner | George Jordan |
| Classification | Internal Engineering |
| Repository | Project Orion |
| Related Documents | NET-001 through NET-008 |
| Last Updated | July 2026 |

---

## Document Purpose

This document defines the controlled deployment methodology for Sprint 3 of Project Orion and establishes the engineering standards, deployment sequence, validation criteria, and governance required to transition the approved network design into a production-ready infrastructure.

---

## Table of Contents

1. Executive Summary

2. Purpose

3. Background

4. Engineering Objectives

5. Scope

6. Infrastructure Overview

7. Deployment Strategy

8. Deployment Phases

9. Prerequisites

10. Required Equipment

11. Risk Assessment

12. Rollback Plan

13. Validation Plan

14. Deliverables

15. Engineering Approval

16. Revision History

## Engineering Lifecycle

| Phase                     | Outcome                          |
| ------------------------- | -------------------------------- |
| 🏛 Architecture           | Enterprise design approved       |
| 📐 Network Design         | Engineering baseline established |
| 🚀 Deployment             | Infrastructure implementation    |
| ✅ Validation              | Technical verification           |
| 📄 Documentation          | Evidence and records             |
| 🔄 Continuous Improvement | Future enhancements              |

---

## 1. Executive Summary

Project Orion enters Sprint 3 by transitioning from engineering design into infrastructure deployment. During Sprint 2, the enterprise network architecture, physical topology, logical topology, IP addressing plan, security zones, implementation strategy, and engineering governance documentation were completed and approved.

This document defines the controlled deployment process that will transform the approved design into a functioning enterprise-inspired infrastructure environment. Deployment activities will follow governance-first engineering principles, ensuring that all implementation steps are documented, validated, and version controlled before being accepted into the production baseline.

---

## 2. Purpose

The purpose of this document is to establish the engineering deployment methodology for Sprint 3.

It defines:

- deployment scope

- engineering sequence

- validation procedures

- rollback procedures

- required documentation

- project success criteria

The objective is to ensure infrastructure deployment is repeatable, auditable, and aligned with the approved Network Design Package.

---

## 3. Background

Project Orion is an enterprise-inspired infrastructure engineering portfolio designed to demonstrate modern engineering practices across governance, cybersecurity, infrastructure deployment, automation, and operational excellence.

Rather than beginning with hardware installation, the project first established a complete engineering baseline through documented architecture, security planning, implementation procedures, and governance reviews. Sprint 3 marks the transition from planning into execution.

### Engineering Assumptions

The following assumptions apply throughout Sprint 3:

- Verizon Fios Internet service remains operational.

- Existing network connectivity is available before deployment.

- Hardware has been inspected and is operational.

- The approved Network Design Package accurately reflects the intended deployment.

- Deployment activities are performed in accordance with governance-first engineering practices.

---

## 4. Engineering Objectives

Sprint 3 has six primary engineering objectives:

1. Deploy the GL.iNet Flint 2 enterprise edge router.

2. Build the core trusted network infrastructure.

3. Deploy the Dell OptiPlex 7060 Home Assistant server.

4. Establish secure network services and administrative access.

5. Validate infrastructure functionality against the approved design.

6. Produce enterprise-grade engineering documentation for all deployment activities.

---

## 5. Scope

### In Scope

- Internet connectivity

- Router deployment

- LAN configuration

- DHCP configuration

- DNS configuration

- Static addressing

- Firewall configuration

- Dell OptiPlex deployment

- Home Assistant installation

- Administrative access

- Initial infrastructure validation

### Out of Scope

- Zigbee automation

- Camera deployment

- Dashboard development

- Smart locks

- Motion sensors

- Predictive automation

- AI services

These activities will be completed during future engineering sprints.

---

## 6. Infrastructure Overview

The following architecture represents the approved deployment baseline for Sprint 3.

![Project Orion High-Level Architecture](images/network/high-level-architecture.png)

Approved Engineering Baseline

The following engineering artifacts have been completed and approved prior to deployment.

| Document                              | Status   |
| ------------------------------------- | -------- |
| NET-001 Network Architecture          | Approved |
| NET-002 Physical Topology             | Approved |
| NET-003 Logical Topology              | Approved |
| NET-004 IP Addressing Plan            | Approved |
| NET-005 Device Inventory              | Approved |
| NET-006 Naming Standards              | Approved |
| NET-007 Security Zones & Access Rules | Approved |
| NET-008 Implementation & Test Plan    | Approved |

---

## 7. Deployment Strategy

Infrastructure deployment will follow a phased engineering implementation model that prioritizes repeatability, security, validation, and controlled change management.

### Phase 1 — Core Network

- Deploy GL.iNet Flint 2

- Verify Internet connectivity

- Configure LAN

- Configure DHCP

- Configure DNS

### Phase 2 — Server Platform

- Prepare Dell OptiPlex

- Install Home Assistant

- Configure management interface

- Verify connectivity

### Phase 3 — Validation

- Test Internet access

- Verify DHCP leases

- Verify DNS resolution

- Verify administrative access

- Verify Home Assistant accessibility

### Phase 4 — Documentation

- Capture deployment evidence

- Update topology diagrams

- Produce validation reports

- Publish repository updates

---

## 8. Deployment Phases

| Phase | Activity           | Deliverable     |
| ----- | ------------------ | --------------- |
| 1     | Network Deployment | ENG-002         |
| 2     | Server Deployment  | HW-001          |
| 3     | Home Assistant     | HA-001          |
| 4     | Validation         | ENG-003         |
| 5     | Documentation      | Sprint 3 Report |

---

## 9. Prerequisites

The following prerequisites must be satisfied before deployment begins:

- Approved Network Design Package

- Current repository synchronized

- Engineering documentation baselined

- Hardware inventory verified

- Internet service operational

- Required firmware available

- Backup procedures documented

---

## 10. Required Equipment

| Component                         | Status    |
| --------------------------------- | --------- |
| Verizon Fios ONT                  | Available |
| GL.iNet Flint 2 Router            | Available |
| Dell OptiPlex 7060 Micro          | Available |
| Home Assistant Installation Media | Ready     |
| Engineering Laptop                | Available |
| Ethernet Cables                   | Available |
| Engineering Documentation         | Approved  |

---

## 11. Risk Assessment

| Risk                      | Likelihood | Impact | Mitigation                                    |
| ------------------------- | ---------- | ------ | --------------------------------------------- |
| Internet interruption     | Low        | Medium | Schedule deployment during maintenance window |
| Router misconfiguration   | Medium     | High   | Export configuration backup                   |
| Server deployment failure | Low        | High   | Validate installation media before deployment |
| Configuration drift       | Medium     | Medium | Document every engineering change             |
| Hardware failure          | Low        | High   | Maintain recovery documentation               |

---

## 12. Rollback Plan

If deployment fails:

- Restore previous router configuration.

- Disconnect new infrastructure.

- Restore backup configuration.

- Verify Internet connectivity.

- Document failure.

- Correct engineering issue.

- Schedule redeployment.

---

## 13. Validation Plan

Successful deployment requires validation of:

- Internet connectivity

- Router accessibility

- DHCP functionality

- DNS resolution

- Static IP assignments

- Administrative access

- Home Assistant availability

- Firewall rules

- Network documentation

- Repository updates

Validation activities will be documented and retained as deployment evidence supporting the Version 1.0 engineering baseline.

### Engineering Success Criteria

Sprint 3 deployment will be considered successful when:

- Core network is operational.

- Internet connectivity is verified.

- DHCP and DNS services are functioning.

- Administrative access has been validated.

- Home Assistant is accessible.

- Engineering documentation has been updated.

- Validation testing has been completed.

--- 

## 14. Deliverables

Sprint 3 will produce the following engineering artifacts:

| Deliverable                       | Planned Document |
| --------------------------------- | ---------------- |
| Flint 2 Deployment Guide          | ENG-002          |
| Network Validation Report         | ENG-003          |
| Dell OptiPlex Build Guide         | HW-001           |
| Home Assistant Installation Guide | HA-001           |
| Updated Network Diagrams          | NET-001 Revision |
| Sprint 3 Engineering Report       | Final Report     |

---

## 15. Related Documents

- NET-001 Network Architecture

- NET-004 IP Addressing Plan

- NET-007 Security Zones & Access Rules

- NET-008 Implementation & Test Plan

---

## 16. References

- NIST Cybersecurity Framework (CSF) 2.0

- NIST SP 800-53 Revision 5

- Home Assistant Documentation

- GL.iNet Flint 2 Administration Guide

- GitHub Documentation

---

## 17. Engineering Approval

| Role                         | Name          | Status   |
| ---------------------------- | ------------- | -------- |
| Project Manager              | George Jordan | Approved  |
| Lead Infrastructure Engineer | George Jordan | Approved  |

---

## 18. Revision History

| Version | Date      | Author        | Description                            |
| ------- | --------- | ------------- | -------------------------------------- |
| 1.0     | July 2026 | George Jordan | Initial Infrastructure Deployment Plan |

---

## Document Classification

This document is maintained as part of the Project Orion Engineering Documentation Library.

Changes to this document shall follow the Project Orion Change Management Process and shall be version controlled through Git and GitHub Releases.

This document represents the approved deployment baseline for Sprint 3.
