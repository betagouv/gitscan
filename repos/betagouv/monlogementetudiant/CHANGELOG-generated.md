## Changelog : monlogementetudiant (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'importation de données, l'ajout de nouvelles fonctionnalités pour les gestionnaires (statistiques, gestion des propriétaires) et une refonte de l'interface utilisateur, notamment la page d'accueil et les détails des logements. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- **Import CSV :** Validation des données lors de l'importation de fichiers CSV pour une meilleure qualité des données. [#9342a18](https://github.com/betagouv/monlogementetudiant/commit/9342a18)
- **Fac Habitat :** Amélioration de la gestion des logements Fac Habitat, incluant la prise en compte de la superficie et du nombre de logements disponibles, ainsi que la correction d'erreurs d'affichage.
- **Page d'accueil :** Refonte complète de la page d'accueil avec de nouvelles sections, une meilleure organisation de l'information et une adaptation pour les appareils mobiles.
- **Détails des logements :** Nouvelle présentation des détails des logements avec un système d'onglets pour une meilleure lisibilité et une expérience utilisateur améliorée.
- **Visites virtuelles :** Ajout de la possibilité d'intégrer des liens vers des visites virtuelles (3D) des logements.
- **Candidatures :** Ajout d'une fonctionnalité de gestion des candidatures, avec la possibilité de masquer l'onglet si le propriétaire n'accepte pas les dossiers faciles.
- **Gestion des propriétaires :** Possibilité de lier un compte administrateur à un propriétaire.
- **Statistiques :** Ajout de statistiques pour les administrateurs.
- **Export CSV :** Possibilité d'exporter les données des logements au format CSV. [#207cb55](https://github.com/betagouv/monlogementetudiant/commit/207cb55)
- **Schéma.org :** Amélioration du balisage Schema.org pour une meilleure indexation des logements par les moteurs de recherche.

### Évolutions techniques
- **Mises à jour Next.js :** Mise à jour de Next.js en version 16.2.
- **Migrations Drizzle :** Plusieurs corrections et optimisations des migrations Drizzle.
- **S3 :** Implémentation du stockage des images sur Amazon S3.
- **PostGIS :** Indexation de la base de données PostGIS pour améliorer les performances des requêtes géographiques.
- **Healthcheck :** Ajout d'un healthcheck pour les villes.
- **Refactoring :** Refactoring de plusieurs composants pour améliorer la maintenabilité du code.
- **Tests :** Ajout et correction de tests unitaires et d'intégration.
- **Sentry :** Réactivation de Sentry pour la surveillance des erreurs.

### Autres changements
- **Documentation :** Mise à jour de la documentation et du fichier README.
- **Wording :** Corrections de wording et amélioration de la clarté des textes.
- **Design :** Améliorations visuelles et corrections de bugs d'affichage.
- **Suppression de logos :** Suppression des logos des partenaires dans le footer.
- **Configuration :** Synchronisation du fichier `.env.dist` avec le Dockerfile.
- **robots.txt :** Ajout d'un fichier `robots.txt` pour contrôler l'indexation par les moteurs de recherche.
