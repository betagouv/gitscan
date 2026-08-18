## Changelog : mesure-impact (30 derniers jours, au 13 août 2026)

### Résumé
Ce mois a été marqué par le lancement et la structuration initiale du projet. L'accent a été mis sur la mise en place d'une architecture de déploiement robuste, permettant de gérer et de distribuer plusieurs produits via des conteneurs et des outils de gestion de déploiement (Helm/Kubernetes).

### Évolutions fonctionnelles
- Introduction d'une structure multi-produits permettant de segmenter les services au sein de l'outil ([#1](https://github.com/SocialGouv/mesure-impact/issues/1)).

### Évolutions techniques
- **Infrastructure et CI/CD :**
    - Initialisation complète du dépôt, des charts Helm et de la chaîne de livraison Kubernetes.
    - Mise en place de la publication des charts Helm en tant qu'artefacts OCI versionnés ([#3](https://github.com/SocialGouv/mesure-impact/issues/3)).
- **Gestion des déploiements (Helm) :**
    - Adaptation du chart Helm pour supporter la gestion des produits ([#2](https://github.com/SocialGouv/mesure-impact/issues/2)).
    - Intégration du catalogue des produits directement dans le chart publié ([#4](https://github.com/SocialGouv/mesure-impact/issues/4)).
    - Correction de l'étiquette de version pour garantir l'utilisation du tag d'image résolu ([#5](https://github.com/SocialGouv/mesure-impact/issues/5)).

### Autres changements
- Mise à jour de la documentation technique concernant le périmètre de droits (RBAC) du robot de déploiement.
