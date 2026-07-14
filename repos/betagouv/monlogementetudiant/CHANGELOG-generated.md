## Changelog : monlogementetudiant (30 derniers jours, au 2026-07-13)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'implémentation d'un système d'alertes pour les étudiants, leur permettant d'être notifiés des nouvelles offres de logement correspondant à leurs critères. Des travaux importants ont également été réalisés sur l'intégration de données externes (Ramses, Wordpress) et sur l'amélioration de la gestion des propriétaires et des logements.

### Évolutions fonctionnelles
- Les étudiants peuvent désormais gérer leurs préférences de notifications. [#352](https://github.com/betagouv/monlogementetudiant/pull/352)
- Une alerte est affichée aux étudiants lorsqu'une offre de logement correspondant à leurs critères est disponible.
- Les étudiants peuvent désormais consulter des articles de blog hébergés sur Wordpress.
- Amélioration de l'affichage des statistiques pour les propriétaires.
- Possibilité d'exporter des données (départements, régions) au format CSV.
- Les propriétaires peuvent désormais uploader des fichiers associés à leurs logements.
- Ajout d'un lien cliquable sur l'icône du propriétaire.
- Amélioration de la page d'alerte des étudiants, affichage d'un modal en mode "shallow". [#350](https://github.com/betagouv/monlogementetudiant/pull/350)

### Évolutions techniques
- Migration des schémas de base de données pour améliorer la structure et les relations.
- Intégration d'une API externe et création d'un module de consommateurs pour gérer les données externes.
- Mise en place d'un système de limitation de débit (rate limiting) pour l'envoi d'emails via Brevo.
- Amélioration de l'efficacité des requêtes d'insertion pour les alertes afin d'éviter les erreurs liées aux limites de paramètres de PostgreSQL.
- Refonte de l'intégration des données Ramses.
- Utilisation de `isomorphic-dompurify` pour la sanitisation des descriptions des logements.
- Mise en place de jobs cron pour l'envoi des alertes (production uniquement) et la détection des nouvelles offres.
- Amélioration de la gestion du cache pour les assets Wordpress.
- Suppression de composants inutilisés (deepsec, store, ramseses).
- Migration vers un format camelCase pour les champs de l'API.

### Autres changements
- Correction de bugs et améliorations diverses de l'interface utilisateur.
- Mise à jour de la documentation et des textes de l'application.
- Ajout de tests unitaires.
- Correction de problèmes liés à la gestion des paramètres et des liens.
- Mise à jour des budgets pour les freelances.
- Ajout de tests d'intégration pour l'API v1.
- Correction d'un problème d'affichage d'une page blanche pour les alertes des étudiants.
- Correction d'un problème de sanitisation des descriptions.
- Ajout d'une URL pour les contacts Brevo.
- Mise à jour des dépendances.
