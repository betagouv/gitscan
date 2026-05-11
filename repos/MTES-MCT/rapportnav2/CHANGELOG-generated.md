## Changelog : rapportnav2 (30 derniers jours, au 7 mai 2026)

### Résumé
Cette version apporte des améliorations à la recherche d'établissements, des corrections de sécurité et de stabilité, ainsi que des mises à jour de l'infrastructure et des dépendances. L'outil a également bénéficié d'améliorations continues du pipeline CI/CD pour une meilleure qualité et rapidité de déploiement.

### Évolutions fonctionnelles
- Amélioration de la recherche d'établissements. [#d6abde6](https://github.com/MTES-MCT/rapportnav2/commit/d6abde6d85e5ca95115d5069d1f551fa3afa3a5a)
- Ajout de la liste des criées et des endpoints associés, avec une interface d'administration correspondante. [#87347da](https://github.com/MTES-MCT/rapportnav2/commit/87347da60441820928154361236850892534266f)
- Correction pour permettre l'ajout de nouvelles infractions lors de la création d'un nouveau contrôle. [#32f22a7](https://github.com/MTES-MCT/rapportnav2/commit/32f22a7149a338d59697b683159378813759318d)

### Évolutions techniques
- Mise à jour de Vite vers la version 8. [#8937f8f](https://github.com/MTES-MCT/rapportnav2/commit/8937f8ff92695852f2364cb690fe43d963f1e142)
- Refonte du pipeline CI/CD pour utiliser GitLab Forge. [#7b6bf05](https://github.com/MTES-MCT/rapportnav2/commit/7b6bf053678d0989396071b7bc60b81c0b2b9111)
- Mise à jour de plusieurs dépendances : Kotlin, Flyway, Monitor-UI, Gradle, Spring Boot.
- Amélioration de la configuration de SonarQube et correction de problèmes liés à la couverture du code.
- Mise à jour de l'image Docker PostgreSQL vers la version 15.17.
- Correction de problèmes liés à l'analyse de sécurité avec Trivy et Snyk.
- Suppression de fichiers `.env` inutilisés.

### Autres changements
- Suppression de fausses alertes de vulnérabilités via la configuration de suppressions CVE.
- Mise à jour de la configuration de release-please.
- Correction de problèmes mineurs et amélioration de la qualité du code.
- Mise à jour de la documentation et des snapshots de tests.
- Correction de problèmes liés à la validation du schéma lors de la création de missions.
- Correction d'un problème de boucle infinie dans le frontend.
- Correction d'un problème de fallback sur l'adresse pour l'utilisation de l'API d'établissement.
