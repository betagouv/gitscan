## Changelog : sante-psy (30 derniers jours, au 17 août 2026)

### Résumé
Cette période a été marquée par une amélioration significative de la gestion des dossiers étudiants (création, mise à jour et ajout de certificats) et une stabilisation des échanges avec les services externes (API INE). L'interface utilisateur a également été affinée pour offrir une meilleure clarté, notamment pour les psychologues et dans les messages d'aide.

### Évolutions fonctionnelles
- **Gestion des étudiants** : Refonte du processus de création et de mise à jour des informations des étudiants [#869](https://github.com/betagouv/sante-psy/issues/869), [#876](https://github.com/betagouv/sante-psy/issues/876), [#877](https://github.com/betagouv/sante-psy/issues/877).
- **Certificats** : Ajout de la fonctionnalité de téléchargement de certificats sur la plateforme [#870](https://github.com/betagouv/sante-psy/issues/870).
- **Interface psychologues** : Correction de l'affichage des cases à cocher lors des premiers rendez-vous de l'année [#884](https://github.com/betagouv/sante-psy/issues/884).
- **Expérience utilisateur** : Optimisation des libellés pour la FAQ, le support et l'annuaire afin d'améliorer la compréhension [#867](https://github.com/betagouv/sante-psy/issues/867), [#868](https://github.com/betagouv/sante-psy/issues/868).

### Évolutions techniques
- **Fiabilité de l'API INE** : Mise en place de timeouts et de mécanismes de gestion d'erreurs pour mieux supporter les instabilités de l'API INE [#874](https://github.com/betagouv/sante-psy/issues/874), [#880](https://github.com/betagouv/sante-psy/issues/880).
- **Optimisation de la base de données** : Amélioration de la gestion des patients supprimés (mise à jour de la ligne existante au lieu d'une recréation) [#878](https://github.com/betagouv/sante-psy/issues/878).
- **Robustesse de l'API** : Correction de la gestion des erreurs (400/404) et optimisation de la récupération des données patients et des rendez-vous liés [#883](https://github.com/betagouv/sante-psy/issues/883).
- **Refactoring** : Restructuration de certaines fonctions de mise à jour pour améliorer la maintenance du code.

### Autres changements
- **Outils internes** : Création d'un script utilitaire pour le téléchargement groupé de certificats pour une liste d'étudiants [#882](https://github.com/betagouv/sante-psy/issues/882).
- **Maintenance** : Nettoyage du code (linting).
