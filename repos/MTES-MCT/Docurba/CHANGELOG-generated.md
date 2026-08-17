## Changelog : Docurba (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois a été marqué par une restructuration importante de la plateforme pour améliorer sa fiabilité et ses performances. Les utilisateurs bénéficieront d'une interface plus riche grâce au support du format Markdown pour les descriptions, et d'outils d'administration renforcés (archivage d'événements, meilleurs filtres). Techniquement, une grande partie de la logique de données géographiques a été déplacée vers le serveur pour garantir une meilleure cohérence des informations.

### Évolutions fonctionnelles
- **Interface et expérience utilisateur**
    - Support du format Markdown pour les descriptions de procédures et d'événements, incluant la gestion des liens externes.
    - Ajout d'une bannière d'information pour signaler les périodes de vacances.
    - Amélioration de la gestion des types d'événements (loi Huwart, SCOT, etc.).
- **Administration (Backoffice)**
    - Possibilité d'archiver ou de désarchiver des événements directement depuis l'interface d'administration Django.
    - Amélioration du filtrage des procédures dans l'interface d'administration.
- **Corrections**
    - Correction de l'affichage des collaborateurs (gestion de la casse).
    - Amélioration de la robustesse lors du partage de procédures (gestion des formats d'emails).
    - Correction de bugs sur l'export des communes et la gestion des listes de codes SIREN.

### Évolutions techniques
- **Architecture et Migration**
    - Migration massive des services de données (communes, intercommunalités, collectivités, Slack, projets) du frontend Nuxt vers le backend Django pour centraliser la logique métier.
    - Refonte du modèle utilisateur (renommé `SupabaseUser`) et intégration de la gestion des profils.
    - Centralisation de la logique de mise à jour des statuts de procédures via des plugins Nuxt et des fonctions SQL.
- **Optimisation et Performance**
    - Résolution de problèmes de performance de type "N+1" sur l'API interne.
    - Optimisation du chargement conditionnel des données liées aux enquêtes.
- **Maintenance et Qualité**
    - Nettoyage approfondi du code : suppression de composants Nuxt, de fonctions SQL et de fichiers de tests inutilisés.
    - Renforcement de la suite de tests (utilisation de snapshots, nouveaux tests pour l'API interne et amélioration des performances de test).
- **Infrastructure et DevOps**
    - Introduction d'une variable d'environnement `$ENABLE_MIGRATIONS` pour contrôler l'application des migrations.
    - Automatisation de certaines tâches via des commandes de gestion et des processus CRON.

### Autres changements
- **Documentation**
    - Ajout de fiches techniques et de guides méthodologiques : [Fiche technique DGALN-OAP](https://github.com/MTES-MCT/Docurba/issues/2307) et [Guide de rédaction de cahier des charges](https://github.com/MTES-MCT/Docurba/issues/2298).
- **Configuration**
    - Mise à jour des configurations de linting (Ruff) et du fichier `.gitignore`.
