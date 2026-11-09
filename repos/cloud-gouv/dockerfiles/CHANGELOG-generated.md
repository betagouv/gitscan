## Changelog : dockerfiles (30 derniers jours, au 02 novembre 2026)

### Résumé
Ce mois-ci, le projet a considérablement étendu sa bibliothèque d'outils DevOps en ajoutant de nouveaux conteneurs dédiés à la sécurité, au linting et à la validation de fichiers. Les processus d'automatisation ont également été affinés pour garantir que seuls les changements validés déclenchent des builds, renforçant ainsi la fiabilité des déploiements.

### Évolutions fonctionnelles
- **Nouveaux conteneurs utilitaires :**
    - Ajout de **TFLint** pour le linting Terraform dans les pipelines GitLab CI.
    - Ajout de **Grype** pour l'analyse de vulnérabilités de sécurité.
    - Ajout d'un conteneur de **validation de schémas YAML**.
- **Amélioration des outils de déploiement :**
    - Création d'une nouvelle image dédiée au déploiement avec **OpenTofu**.
    - Enrichissement de l'image OpenTofu avec `git` et `syft` pour permettre une génération de SBOM (Software Bill of Materials) intégrée.
- **Gestion des SBOM :** Amélioration de la capacité d'upload des SBOM grâce à l'intégration de `jq` et du client `swift`.

### Évolutions techniques
- **Optimisation des workflows CI/CD :**
    - Restriction du déclenchement des pipelines : les builds ne s'exécutent désormais que sur les Pull Requests validées et fusionnées dans la branche principale.
    - Automatisation du déploiement OpenTofu lors du taggage de nouvelles versions.
- **Maintenance de l'infrastructure de build :**
    - Ajustements des environnements d'exécution (runners) et correction de la configuration des images de base (`ubuntu-latest`).
