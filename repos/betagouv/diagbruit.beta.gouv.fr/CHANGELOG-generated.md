## Changelog : diagbruit.beta.gouv.fr (30 derniers jours, au 8 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur concernant les préconisations, notamment avec l'ajout d'une médiathèque pour enrichir le contenu proposé. L'intégration des données des établissements scolaires a également été initiée, permettant d'affiner l'analyse du bruit et des recommandations associées. Plusieurs corrections de bugs et optimisations techniques ont été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Médiathèque :** Ajout d'une page dédiée à la médiathèque, permettant de gérer et d'afficher des ressources associées aux préconisations. Cela inclut la création d'une collection Strapi dédiée, l'ajout de slugs pour les éléments de la médiathèque et la possibilité d'intégrer du contenu HTML enrichi.
- **Préconisations :**
    - Ajout des sections "à retenir" et "points clés" dans les préconisations, avec la possibilité d'utiliser un éditeur HTML pour le contenu "à retenir".
    - Amélioration de l'affichage des cartes de recommandations.
    - Refonte de la formulation des sources de bruit.
- **Données scolaires :** Intégration des données des établissements scolaires, incluant l'ingestion des données, l'ajout de champs spécifiques (code département, slug) et l'association avec les sources de bruit.
- **Recherche :** Amélioration de la barre de recherche avec un état vide plus clair.
- **Affichage des données :** Correction de l'affichage des tableaux de données et des images.

### Évolutions techniques
- **Optimisation des requêtes :** Optimisation des requêtes pour améliorer les performances, notamment lors de l'ingestion des données scolaires.
- **Refactoring :** Refactoring de plusieurs composants et hooks pour améliorer la maintenabilité du code.
- **Pipelines :** Renommage et correction des pipelines CI/CD.
- **Index géométriques :** Correction d'un problème lié à la suppression des index géométriques.
- **Strapi :** Mise à jour des options du plugin CKEditor dans Strapi.
- **Sécurité :** Correction d'une vulnérabilité (CVE).

### Autres changements
- Mise à jour de la documentation.
- Correction de problèmes de style et d'affichage mineurs.
- Ajout de tests pour les nouvelles fonctionnalités.
- Amélioration de la gestion des erreurs et des logs.
- Correction de la projection des écoles OSM.
- Suppression de collections Strapi inutilisées.
- Normalisation de l'entrée de recherche.
- Ajout d'un contact `contact@diagbruit.fr` en copie cachée des emails.
