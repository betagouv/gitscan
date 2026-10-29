## Changelog : qualicharge (30 derniers jours, au 24 octobre 2026)

### Résumé
Ce mois-ci, qualicharge a amélioré l'accessibilité de ses données grâce à l'exportation des tarifs vers le service OpenData. Le projet a également bénéficié de corrections visant à fiabiliser les calculs d'indicateurs et de mesures de sécurité pour renforcer la robustesse et la fiabilité de la plateforme.

### Évolutions fonctionnelles
- Exportation des tarifs vers le service OpenData via l'outil data7.

### Évolutions techniques
- **Fiabilité des données** : Correction du calcul des indicateurs (e2, e3 et e6) dans Prefect pour gérer correctement les statuts manquants.
- **Sécurité** : Résolution de vulnérabilités et mise à jour de dépendances transitives à risque.
- **Infrastructure & CI/CD** : Correction de l'initialisation de la base de données pour les workflows Prefect dans l'environnement GitHub Actions.
- **Versionning** : Passage de l'API à la version 0.35.1.
