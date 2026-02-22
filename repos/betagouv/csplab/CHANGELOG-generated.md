## Changelog : csplab (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'ingestion et du traitement des offres d'emploi, ainsi que sur le développement de nouvelles fonctionnalités pour le module Tycho, notamment l'intégration des CV et la recherche de candidats. Des améliorations techniques ont également été apportées à l'infrastructure et aux outils de développement.

### Évolutions fonctionnelles
- **Tycho (Candidats):** Intégration de la gestion des CV, avec la possibilité de les télécharger, de les traiter et de les associer aux offres d'emploi (#167). Une première version de page de résultats de recherche de CV est disponible (#180, #182, #179, #164, #162, #161, #160, #151).
- **Ingestion des offres:** Amélioration de l'ingestion des offres d'emploi par lots (#208) et vectorisation des offres pour une recherche plus performante (#166).
- **Interface utilisateur:** Mise à jour de la page d'accueil de Tycho (#180) et ajout de filtres simples pour les résultats de CV (#178).

### Évolutions techniques
- **Authentification:** Toutes les API sont désormais protégées par une authentification JWT (#210).
- **Infrastructure:** Mise à jour de Django vers la version 6.0.1 (#143) et de psycopg vers la version 3.3.2 (#144).
- **Outils de développement:** Amélioration de la configuration de l'environnement de développement avec l'ajout du Django Debug Toolbar (#186) et la possibilité de définir des endpoints tiers personnalisés (#188).
- **Refactoring:** Refactorisation des administrateurs Django pour rendre certains champs en lecture seule (#184) et remplacement des identifiants d'entités par des UUID (#201).
- **Tests:** Réduction de la verbosité des tests (#199) et amélioration des tests d'ingestion (#130).
- **CI/CD:** Mise à jour de la configuration Sentry (#192) et correction de la vérification du format du commit en faveur de la vérification du titre de la PR (#190, #207).
- **Style:** Mise en place de règles de style SCSS et mise à jour des outils de l'éditeur (prettier, stylelint) (#122, #121).

### Autres changements
- Nettoyage du code et de la configuration du dépôt (#211).
- Mise à jour de la documentation et du fichier CHANGELOG (#131, #87).
- Exploration des DTOs Talentsoft dans le notebook (#124).
- Correction de bugs mineurs dans l'ingestion et le traitement des offres (#168, #154).
- Correction d'un problème de "polling" qui causait un dépassement de capacité (#165).
