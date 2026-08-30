## Changelog : les-emplois (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec le déploiement complet du module d'orientation (Insertion), permettant un suivi beaucoup plus fin des parcours. Les outils de gestion pour les accompagnateurs et les administrateurs ont été enrichis, tandis que l'expérience utilisateur a été fluidifiée par une meilleure gestion de la sécurité et des redirections de domaine.

### Évolutions fonctionnelles
- **Module d'Orientation (Insertion) :** Déploiement d'un système complet de suivi incluant des vues détaillées, des listes filtrables (par bénéficiaire, structure, expéditeur ou statut) et la possibilité de gérer des pièces jointes.
- **Gestion des parcours et accompagnateurs :** Amélioration de la visibilité des informations de contact des conseillers et ajout de nouveaux filtres de recherche (fin de parcours IAE, membres d'organisations spécifiques comme GEIQ ou OPCS).
- **Administration et Pilotage :** Nouvelles capacités pour les administrateurs, notamment pour commenter les dossiers annulés, visualiser les informations de sécurité (2FA) et lier les orientations aux événements de mobilisation.
- **Expérience utilisateur et Sécurité :** Optimisation du processus de double authentification (MFA) avec de meilleurs messages d'accompagnement et ajout d'indicateurs de statut sur les profils certifiés.
- **Données et Filtres :** Intégration de nouveaux filtres liés au handicap et amélioration de l'importation des offres d'emploi France Travail pour les employeurs engagés.

### Évolutions techniques
- **Refonte de la gestion des utilisateurs :** Optimisation du modèle d'affectation des chercheurs d'emploi pour automatiser la clôture des missions et améliorer la précision du suivi des actions (`last_action_at`).
- **Optimisation des performances :** Amélioration des requêtes de base de données pour les vues candidats et restructuration de certains composants pour une meilleure maintenabilité.
- **Infrastructure et CI/CD :** Modernisation des workflows de tests et possibilité de déclenchement manuel des processus d'intégration continue.
- **Migration et Redirection :** Mise en place d'un système de redirection automatique vers le nouveau domaine avec affichage d'une bannière d'information pour les utilisateurs.
- **Sécurité des échanges :** Réduction des permissions (scopes) utilisées lors des communications avec l'API France Travail.

### Autres changements
- **Documentation :** Ajout de documentation concernant l'utilisation de Podman comme alternative à Docker.
- **Maintenance et Nettoyage :** Suppression de fonctionnalités obsolètes (gestion GPS), nettoyage des templates et des tests inutilisés.
