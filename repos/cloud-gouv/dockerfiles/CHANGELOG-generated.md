## Changelog : dockerfiles (30 derniers jours, au 02/11/2026)

### Résumé
Le projet s'enrichit de nouveaux outils pour renforcer la sécurité et la qualité des configurations (linting, analyse de vulnérabilités, validation de schémas YAML). Les processus de construction automatisés ont également été optimisés pour garantir que seuls les changements validés et fusionnés déclenchent de nouveaux déploiements.

### Évolutions fonctionnelles
- **Nouveaux conteneurs disponibles** :
    - Ajout d'un conteneur `tflint` pour le linting Terraform dans GitLab CI.
    - Ajout d'une image `grype` pour l'analyse de vulnérabilités.
    - Ajout d'un conteneur de validation de schémas YAML.
- **Amélioration des outils d'infrastructure** :
    - Enrichissement de l'image de déploiement OpenTofu avec l'intégration de `git` et `syft` pour une gestion simplifiée des SBOM (Software Bill of Materials).
    - Ajout de `jq` et du client `swift` pour faciliter l'upload des SBOM.

### Évolutions techniques
- **Optimisation des pipelines CI/CD** :
    - Restriction des déclenchements de build : les pipelines ne s'exécutent désormais que sur les PR validées et fusionnées dans la branche principale.
    - Automatisation du déploiement OpenTofu lors du processus de taggage.
    - Ajustement des environnements d'exécution (passage sur `ubuntu-latest`).
- **Maintenance** :
    - Intégration de la pull request [#53](https://github.com/cloud-gouv/dockerfiles/pull/53).
