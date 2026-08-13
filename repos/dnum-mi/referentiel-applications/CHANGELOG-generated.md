## Changelog : referentiel-applications (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois-ci, le projet a renforcé ses capacités de gouvernance et de contrôle administratif. Les évolutions majeures concernent l'amélioration de la gestion des utilisateurs (bannissement, suivi des permissions), une refonte de la gestion des stacks technologiques (cycle de vie, documentation) et une optimisation de l'interface utilisateur pour une navigation plus fluide et sécurisée.

### Évolutions fonctionnelles

**Administration et Gouvernance**
- Possibilité pour les administrateurs de bannir des utilisateurs [#2240](https://github.com/dnum-mi/referentiel-applications/issues/2240).
- Mise en place d'un nouveau panneau d'administration pour la gestion des directions métier et leur rattachement aux organisations [#2218](https://github.com/dnum-mi/referentiel-applications/issues/2218).
- Support de plusieurs divisions métier par entité [#2114](https://github.com/dnum-mi/referentiel-applications/issues/2114).
- Ajout de l'historique et de la traçabilité pour l'envoi d'emails [#2223](https://github.com/dnum-mi/referentiel-applications/issues/2223) et pour les modifications de rôles et permissions des utilisateurs [#2207](https://github.com/dnum-mi/referentiel-applications/issues/2207).

**Gestion des Technologies et des Données**
- Refonte complète de la gestion des stacks technologiques incluant le produit, les liens de documentation et la gestion des dates de fin de vie (EOL) [#2058](https://github.com/dnum-mi/referentiel-applications/issues/2058) avec une vérification accrue des dates d'obsolescence [#2234](https://github.com/dnum-mi/referentiel-applications/issues/2234).
- Enrichissement du catalogue de données avec de nouveaux points d'accès (endpoints) et actions en interface [#2024](https://github.com/dnum-mi/referentiel-applications/issues/2024).
- Suppression de la fonctionnalité de gestion des licences [#2057](https://github.com/dnum-mi/referentiel-applications/issues/2057).

**Expérience Utilisateur et Interface**
- Introduction d'un mode maintenance en lecture seule [#2201](https://github.com/dnum-mi/referentiel-applications/issues/2201).
- Amélioration de la fiabilité et de la performance de la recherche globale dans l'en-tête [#2025](https://github.com/dnum-mi/referentiel-applications/issues/2025).
- Harmonisation de l'interface utilisateur (matrice des droits, onglets de la fiche, libellés des formulaires) [#2090](https://github.com/dnum-mi/referentiel-applications/issues/2090) [#2118](https://github.com/dnum-mi/referentiel-applications/issues/2118).
- Ajout d'un avertissement lors de la création d'une application sans permissions de lecture [#2237](https://github.com/dnum-mi/referentiel-applications/issues/2237).

**Sécurité et Permissions**
- Affinement de la matrice des droits, notamment pour l'onglet technologie [#2059](https://github.com/dnum-mi/referentiel-applications/issues/2059).
- Correction des accès : masquage des onglets sans droits suffisants [#2088](https://github.com/dnum-mi/referentiel-applications/issues/2088) et attribution des droits complets aux administrateurs de leurs propres applications [#2028](https://github.com/dnum-mi/referentiel-applications/issues/2028).

### Évolutions techniques

**Architecture et Backend**
- Migration du framework vers NestJS 11 [#2153](https://github.com/dnum-mi/referentiel-applications/issues/2153).
- Ajout d'une option pour désactiver par défaut les tâches automatiques d'envoi d'emails via une variable de configuration [#2216](https://github.com/dnum-mi/referentiel-applications/issues/2216).
- Optimisation de la récupération des campagnes via l'API REST pour éviter les limitations de débit (rate-limiting) [#2053](https://github.com/dnum-mi/referentiel-applications/issues/2053).

**Frontend et Qualité**
- Mise à jour de la version de l'application côté client sans nécessiter de rafraîchissement complet de la page [#2158](https://github.com/dnum-mi/referentiel-applications/issues/2158).
- Amélioration de la suite de tests : correction des tests E2E sur l'édition de lignes [#2052](https://github.com/dnum-mi/referentiel-applications/issues/2052) et isolation de la base de données de développement pour éviter les pollutions de données lors des tests [#2151](https://github.com/dnum-mi/referentiel-applications/issues/2151).

### Autres changements
- Ajout de documents d'architecture (ADR 0001 et 0002) pour documenter les fondations partagées [#2051](https://github.com/dnum-mi/referentiel-applications/issues/2051).
- Mise à jour de la documentation du projet (README) [#2239](https://github.com/dnum-mi/referentiel-applications/issues/2239).
