## Changelog : hyyypertool (30 derniers jours, au 23/09/2026)

### Résumé
Ce mois-ci, hyyypertool a progressé sur deux axes majeurs : l'efficacité opérationnelle, avec l'introduction de la création massive d'organisations, et la robustesse technique, grâce à une refonte complète de notre système de tests automatisés.

### Évolutions fonctionnelles
- Ajout de la création massive d'organisations via le numéro SIRET [#1762](https://github.com/proconnect-gouv/hyyypertool/issues/1762).
- Amélioration de la gestion des domaines : la fonction de récupération ne retourne désormais que les domaines d'e-mails approuvés [#1782](https://github.com/proconnect-gouv/hyyypertool/issues/1782).
- Correction du système de chat : bascule automatique vers une nouvelle conversation Crisp en cas de ticket obsolète [#1800](https://github.com/proconnect-gouv/hyyypertool/issues/1800).

### Évolutions techniques
- **Tests de bout en bout (E2E) :** Migration massive de la suite de tests de Cypress vers Bunwright, incluant la gestion de la liste de modération et plusieurs scénarios métiers (vérification de domaine, gestion des membres internes, gestion des doublons) [#1801](https://github.com/proconnect-gouv/hyyypertool/issues/1801), [#1802](https://github.com/proconnect-gouv/hyyypertool/issues/1802), [#1803](https://github.com/proconnect-gouv/hyyypertool/issues/1803), [#1805](https://github.com/proconnect-gouv/hyyypertool/issues/1805), [#1809](https://github.com/proconnect-gouv/hyyypertool/issues/1809), [#1811](https://github.com/proconnect-gouv/hyyypertool/issues/1811), [#1815](https://github.com/proconnect-gouv/hyyypertool/issues/1815).
- **Environnement de développement :** Ajout d'un Nix flake pour permettre un environnement de développement sans privilèges sudo [#1783](https://github.com/proconnect-gouv/hyyypertool/issues/1783).
- **Architecture :** Extraction du thème Tailwind DSFR dans un package workspace dédié pour améliorer la modularité du projet [#1791](https://github.com/proconnect-gouv/hyyypertool/issues/1791).
- **Maintenance :** Mise à jour de l'environnement d'exécution Bun (v1.4.2) [#1790](https://github.com/proconnect-gouv/hyyypertool/issues/1790) et actualisation des dépendances internes du projet [#1792](https://github.com/proconnect-gouv/hyyypertool/issues/1792).
