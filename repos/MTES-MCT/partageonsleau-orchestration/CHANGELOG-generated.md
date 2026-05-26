## Changelog : partageonsleau-orchestration (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, l'orchestrateur Partageons l'eau a bénéficié d'améliorations significatives concernant la gestion des connecteurs, l'importation de données et le calcul des volumes. Des corrections et des optimisations ont également été apportées pour améliorer la stabilité et la configuration du système.

### Évolutions fonctionnelles
- Ajout d'un parser pour BV Tech, permettant l'intégration de nouvelles sources de données. [#9](https://github.com/MTES-MCT/partageonsleau-orchestration/pulls/9)
- Prise en charge de multiples connecteurs simultanément, améliorant la capacité à traiter des données provenant de diverses sources. [#9](https://github.com/MTES-MCT/partageonsleau-orchestration/pulls/9)
- Amélioration du lien entre l'orchestrateur et la plateforme Partageons l'eau pour une meilleure cohérence des données.
- Implémentation du calcul des volumes à partir de l'index, permettant une analyse plus précise des données de consommation. [#7](https://github.com/MTES-MCT/partageonsleau-orchestration/pulls/7)
- Possibilité de gérer différentes politiques de conflits lors de l'importation des données.
- Prise en charge de plusieurs fichiers lors de l'importation de données.

### Évolutions techniques
- Correction d'une dépréciation de SCW (Service Cloud Waly).
- Ajout d'une interface d'administration BullMQ pour la surveillance et la gestion des queues de tâches.
- Amélioration de la gestion des variables d'environnement et des secrets pour une configuration plus sécurisée.
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et améliorations.
- Correction de plusieurs erreurs de linting et de build.
- Utilisation d'une granularité quotidienne pour Willie afin d'éviter des consommations nulles.

### Autres changements
- Mise à jour du fichier README pour une meilleure documentation du projet.
- Modification du port par défaut de l'application.
- Ajout d'un fichier `deploy.yml` pour faciliter le déploiement.
- Ajout de certificats Redis pour une connexion sécurisée.
