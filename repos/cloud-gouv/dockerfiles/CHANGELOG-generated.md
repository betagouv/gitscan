## Changelog : dockerfiles (30 derniers jours, au 02 novembre 2026)

### Résumé
Le projet a considérablement enrichi sa bibliothèque de conteneurs pour renforcer la qualité et la sécurité des pipelines CI/CD. L'accent a été mis sur l'ajout de nouveaux outils de vérification (linting, validation de schémas et scan de vulnérabilités) et l'amélioration des images existantes pour faciliter l'automatisation des processus DevOps.

### Évolutions fonctionnelles
- Ajout de nouveaux conteneurs spécialisés : TFLint (linting Terraform), Grype (analyse de vulnérabilités) et un validateur de schémas YAML.
- Amélioration de l'image OpenTofu par l'intégration de `syft` et `git` pour simplifier les opérations de scan et de gestion de versions.
- Ajout de `jq` et du client `swift` pour permettre l'envoi automatisé des rapports SBOM (Software Bill of Materials).

### Évolutions techniques
- Optimisation du workflow OpenTofu pour déclencher les exécutions lors du taggage.
- Ajustements de l'infrastructure de build pour l'utilisation de `ubuntu-latest`.
- Intégration de la pull request [#53](https://github.com/cloud-gouv/dockerfiles/pull/53).
