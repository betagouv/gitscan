## Changelog : fisheries-and-environment-data-warehouse (30 derniers jours)

### Résumé
Ce changelog présente les récentes améliorations apportées à l'entrepôt de données dédié aux pêches et à l'environnement marin. Les modifications incluent l'enrichissement des données relatives aux unités de contrôle, l'amélioration du traitement des missions interservices, l'ajout de nouvelles tables pour les menaces et les caractérisations de menaces, ainsi que des mises à jour de sécurité et de dépendances.

### Évolutions fonctionnelles
- Ajout de données relatives aux unités de contrôle dans les requêtes (#159).
- Comptabilisation des missions interservices (#157).
- Ajout de filtres pour les missions complètes et terminées, permettant une analyse plus précise (#154).
- Ajout de nouvelles tables pour les menaces et les caractérisations de menaces (#153).
- Mise à jour des données et de la base de test pour les analyses MonitorFish (#147).

### Évolutions techniques
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité (#158, #157).
- Suppression des colonnes "Facade" et "Mission Type" (#155).
- Mise à jour de la configuration de Trivy pour ignorer certaines vulnérabilités (#151).
- Mise à jour des dépendances Python via Dependabot pour corriger des failles de sécurité et bénéficier des dernières améliorations (#150, #148, #9d8b0fd, #cb9df6f).
- Mise à jour du workflow Dependabot pour une gestion plus efficace des dépendances (#a8ba2ce).

### Autres changements
- Inversion de la logique pour la gestion des colonnes à conserver dans AEM (#152).
- Correction d'un test suite à une mise à jour de dépendance (#fae1964).
- Amélioration de la base de données de test et des données de test pour MonitorEnv (#4a63640).
