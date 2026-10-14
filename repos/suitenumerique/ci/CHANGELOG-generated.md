## Changelog : ci (30 derniers jours, au 13 octobre 2026)

### Résumé
Ce mois marque le lancement de la version initiale du dépôt. Il introduit une vaste bibliothèque de workflows GitHub Actions réutilisables conçus pour standardiser et automatiser les processus de développement (CI/CD, tests, sécurité et déploiement) pour l'ensemble des projets de La Suite.

### Évolutions fonctionnelles
- **Docker** : Ajout d'un workflow réutilisable pour la publication d'images, incluant la possibilité de choisir le multi-plateforme et d'activer optionnellement des scans de sécurité.
- **Helm** : Nouveaux workflows pour le linting de fichiers Helmfile et la publication de charts Helm.
- **Python** : Ajout d'un workflow réutilisable pour le linting de code Python.
- **Sécurité** : Intégration d'un workflow dédié aux scans de sécurité avec Zizmor.
- **Internationalisation** : Mise à disposition de workflows pour l'import et l'export des traductions via Crowdin.
- **Qualité & Divers** : 
    - Nouveaux workflows pour la génération automatique de changelogs et le contrôle de la qualité des projets.
    - Ajout d'une action pour la construction de templates d'emails.

### Évolutions techniques
- **Optimisation des performances** : 
    - Mise en place du cache des couches d'images Docker pour accélérer les temps de build.
    - Ajout d'une action de nettoyage de l'espace disque sur les runners.
- **Sécurité et conformité** :
    - Renforcement de la sécurité des workflows par le verrouillage des versions et des SHAs des actions GitHub.
    - Désactivation de `persist-credentials` sur l'action `actions/checkout` pour limiter les risques.
    - Migration et mise à jour des actions de scan de sécurité (Trivy).
- **Maintenance et infrastructure** :
    - Migration des notifications de webhook ArgoCD.
    - Exécution de `actionlint` via Docker avec utilisation de digests d'images pour garantir la reproductibilité.
    - Amélioration de la gestion de la concurrence des workflows via l'utilisation de workflows partagés.

### Autres changements
- **Documentation** : Ajout d'un fichier README détaillant l'organisation et la structure du dépôt.
