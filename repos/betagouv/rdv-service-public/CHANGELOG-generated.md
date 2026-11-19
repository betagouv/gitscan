## Changelog : rdv-service-public (30 derniers jours, au 18/11/2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de l'expérience de visioconférence et la fiabilité de la synchronisation des agendas (CalDAV). Le service est devenu plus robuste grâce à des mises à jour de sécurité majeures et une interface utilisateur plus accessible et moderne. Les administrateurs bénéficient également de nouveaux outils de gestion des organisations et de renforcement de la sécurité (2FA).

### Évolutions fonctionnelles
- **Visioconférence** : Intégration de la solution Menshen pour la création automatique de salons et une gestion plus fluide des liens de réunion (#6942, #6913, #6878, #6863).
- **Synchronisation d'agendas (CalDAV)** : Amélioration de l'affichage (événements sur la journée entière, liste des participants par email) et meilleure gestion des erreurs de synchronisation, notamment pour Zimbra (#6917, #6910, #6885, #6903, #6798).
- **Administration et Sécurité** : Possibilité de forcer la double authentification (2FA) sur un espace (#6909), gestion simplifiée des organisations pour les administrateurs (#6838, #6836) et import automatique des espaces de l'État via le CRM (#6869).
- **Expérience utilisateur (UI/UX)** : Optimisation de l'affichage mobile pour les détails de rendez-vous (#6914), passage à une saisie d'adresse plus accessible (#6837), et mise à jour esthétique de l'interface (boutons, icônes, contrastes) (#6948, #6952, #6944, #6945).
- **Corrections** : Résolution de problèmes de création de doublons (usagers et rendez-vous) (#6955, #6884), correction des dates dans les exports (#6949) et résolution de bugs de connexion via ProConnect (#6876).
- **Site vitrine** : Enrichissement du site avec de nouvelles pages (Nouveautés, Fonctionnalités, Webinaires) (#6785, #6848, #6867).

### Évolutions techniques
- **Sécurité** : Mises à jour critiques des frameworks et environnements (Rails 8.1 [#6924, #6872], Node.js [#6936, #6926]) et correction de plusieurs vulnérabilités (CVE) (#6919, #6905).
- **Performance** : Optimisation des recherches géographiques (#6890), du chargement des plages horaires (#6934) et mise en place du chargement différé (*lazy loading*) de l'historique des rendez-vous (#6921).
- **Fiabilité et Monitoring** : Amélioration de la gestion des tâches de fond (priorisation des emails, règles de concurrence) et renforcement du suivi d'erreurs avec Sentry (#6912, #6911, #6904).
- **Infrastructure** : Migration vers Ruby 3.4 (#6896) et mise à jour de GoodJob vers la version 4 (#6845).

### Autres changements
- **Maintenance** : Nettoyage du code, suppression de fonctionnalités obsolètes et correction de la documentation de l'API OAuth 2 (#6842, #6889, #6941).
