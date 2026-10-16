## Changelog : mycollections (30 derniers jours, au 15/10/2026)

### Résumé
Ce mois-ci, mycollections a franchi une étape importante dans la maturité de son interface et de ses processus de gestion. Les utilisateurs bénéficient d'une expérience plus fluide, notamment sur mobile, et de nouvelles fonctionnalités liées à la qualité de la génération IA. En parallèle, l'infrastructure a été renforcée pour garantir une meilleure sécurité et une stabilité accrue lors de l'indexation des documents.

### Évolutions fonctionnelles
- **Génération & Qualité** : Introduction de questions par persona, de jeux de questions de référence et d'une page dédiée au suivi de la Qualité [#61].
- **Catalogue & Recherche** : Ajout de catégories repliables [#42], amélioration de la précision des résultats de recherche et de la visibilité des catégories.
- **Expérience Utilisateur (UX)** : Optimisation de l'ergonomie mobile (accès au menu, gestion du focus), amélioration de l'accessibilité, généralisation des messages d'erreur en français et enrichissement du parcours d'accueil.
- **Gestion des Collections** : Amélioration du flux de publication (historique lisible, archivage), intégration simplifiée avec l'assistant et gestion plus intuitive des demandes utilisateurs (formulaires repliables).
- **Visualisation & Sources** : Passage du graphe en mode plein écran, possibilité d'importer des graphes externes et amélioration de la lisibilité des sources via un proxy sécurisé.

### Évolutions techniques
- **Sécurité & Accès** : Renforcement des droits d'administration (gestion par variables), gestion granulaire des permissions sur les actions critiques (archiver, purger) et sécurisation des liens partagés.
- **Indexation & Données** : Amélioration de la résilience de l'indexation (reprise automatique après redémarrage), suppression des doublons lors de la réindexation et optimisation du découpage des documents.
- **Infrastructure & CI/CD** : Migration de la gestion des dépendances vers `uv`, mise en place d'une nouvelle chaîne CI/CD, déploiement via Helm et mise à jour de l'image Nginx pour corriger une vulnérabilité critique.
- **Observabilité** : Ajout d'endpoints pour le versioning de l'application et le suivi de l'état de santé (healthcheck) des dépendances.

### Autres changements
- **Documentation** : Mise à jour du README, des procédures de déploiement et de la documentation relative à la consultation des sources.
- **Nettoyage** : Retrait des identifiants d'infrastructure du code source pour des raisons de sécurité.
