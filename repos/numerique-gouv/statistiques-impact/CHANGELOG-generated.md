## Changelog : statistiques-impact (30 derniers jours, au 03 avril 2026)

### Résumé
Ce changelog présente les améliorations apportées au site statistiques-impact au cours du dernier mois. Les modifications incluent des améliorations de la gestion des adaptateurs de données, une simplification des clients de données et l'ajout d'un fichier changelog pour suivre les évolutions du projet.

### Évolutions fonctionnelles
- Amélioration du format de retour des méthodes `get_data` des clients de données, pour une meilleure lisibilité et utilisation des données.
- Suppression d'un client en double pour PostHog/Visio, simplifiant ainsi la configuration et la maintenance.

### Évolutions techniques
- Modification des adaptateurs de données pour autoriser les produits sans informations, offrant une plus grande flexibilité dans la configuration des sources de données. [#2](https://github.com/numerique-gouv/statistiques-impact/pulls/2)
- Correction du linting du dernier fichier de migration pour assurer la qualité du code et la conformité aux standards du projet.

### Autres changements
- Ajout d'un fichier `CHANGELOG.md` pour documenter les changements futurs du projet, suivant les conventions [Keep a Changelog](https://keepachangelog.com/en/1.0.0).
