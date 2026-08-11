## Changelog : data_pass (30 derniers jours, au 10 août 2026)

### Résumé
Ce mois-ci, l'outil s'est enrichi de nouveaux éditeurs et de nouveaux types de formulaires, notamment pour l'API Particulier. L'expérience utilisateur a été améliorée par une meilleure visibilité des emails automatiques et une clarification des droits et rôles. Parallèlement, des mesures de sécurité importantes et des optimisations d'infrastructure ont été déployées.

### Évolutions fonctionnelles
- **Expansion de l'écosystème d'éditeurs et de formulaires** :
    - Ajout de l'éditeur Ianord et de ses formulaires pour les cantines (lycées/collèges) [#1710](https://github.com/etalab/data_pass/issues/1710).
    - Introduction d'un nouveau type de formulaire : "API Particulier" via Démarche numérique [#1682](https://github.com/etalab/data_pass/issues/1682).
    - Ajout des éditeurs Hoptis Software et EAJE avec leurs formulaires respectifs.
    - Renommage de certaines solutions logicielles (Familea Diabolo et Mikado) pour plus de précision.
- **Gestion des accès et périmètres (scopes)** :
    - Ajout du périmètre (scope) INE.
    - Affichage des scopes AEEH et régime pensionnat sur les formulaires CapDemat [#1709](https://github.com/etalab/data_pass/issues/1709).
- **Améliorations de l'interface (UI/UX)** :
    - Mise en place d'une interface permettant de consulter les emails automatiques envoyés.
    - Clarification de l'affichage des rôles et des niveaux de droits dans les index.
    - Ajout de fils d'Ariane (breadcrumbs) pour faciliter la navigation.
    - Amélioration de l'accessibilité de l'interface.
- **Nouvelles fonctionnalités et corrections** :
    - Transmission automatique de la convention aux contacts lors de la validation (projet DINUM).
    - Correction de la proactivité CNOUS (utilisation du contact métier via le bridge HubEE).
    - Résolution de bugs concernant la suppression involontaire de droits lors d'ajouts et la gestion des identifiants France Connect.

### Évolutions techniques
- **Sécurité** :
    - Mise à jour de Rails vers la version 8.1.3.1 pour corriger la vulnérabilité CVE-2026-66066.
    - Restriction des privilèges OAuth pour HubEE : passage du scope `ADMIN` au scope `DATAPASS` pour limiter les risques [#1723](https://github.com/etalab/data_pass/issues/1723).
- **Infrastructure et Observabilité** :
    - Suppression des configurations d'environnement locales (prod, staging, sandbox) au profit d'une gestion centralisée via Ansible.
    - Migration de la production des journaux (logs) vers le format JSON via Logstasher pour faciliter l'analyse.
- **Refactoring** :
    - Nettoyage de la base de données avec le remplacement de l'ancien champ `cnous_statut_bourse` par une nomenclature unifiée `_boursier`.

### Autres changements
- Affinage des libellés et des textes de l'interface suite aux retours du pôle juridique.
