## Changelog : infomedicament (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'optimisation des performances, l'ajout de nouvelles fonctionnalités concernant les interactions médicamenteuses et la refonte de certains composants de l'interface utilisateur. Des améliorations de la structure du code et des scripts de déploiement ont également été apportées.

### Évolutions fonctionnelles
- Ajout de classes cliniques avec pathos, améliorant la catégorisation des médicaments. [#212](https://github.com/betagouv/infomedicament/issues/212)
- Mise en place d'une nouvelle fonctionnalité permettant de rechercher et d'afficher les interactions médicamenteuses, incluant une version intégrable (widget) pour d'autres sites.
- Ajout de chapeaux et gestion des cas "autres..." pour les classes d'interactions.
- Correction d'un problème sur la page médicament où toutes les données n'étaient pas affichées. [#192](https://github.com/betagouv/infomedicament/issues/192)
- Refonte des menus d'en-tête et de pied de page pour une meilleure expérience utilisateur.
- Ajout d'un sitemap.xml pour améliorer le référencement.

### Évolutions techniques
- Optimisation des performances en mettant en cache les requêtes statiques à la base de données avec `unstable_cache` pour réduire la charge lors de la génération statique des pages (SSG).
- Amélioration de la gestion du cache pour éviter les collisions de clés.
- Utilisation de `generateStaticParams` pour la génération statique des listes alpha et du glossaire.
- Refactorisation du code pour déplacer la récupération des données vers des composants serveur.
- Utilisation du compilateur SWC pour optimiser les styles en production.
- Extraction de la logique de récupération des badges de niveau dans un module séparé avec ajout de tests unitaires.
- Déplacement des composants d'en-tête et de pied de page vers un layout conteneur.
- Ajout de scripts pour importer les données PDBM et initialiser la base de données, notamment pour les environnements de développement et de déploiement (Scalingo).
- Mise à jour de la configuration du proxy pour limiter le nombre de requêtes par minute.
- Correction de la sérialisation de l'arbre ATC complet dans le code HTML.

### Autres changements
- Ajout de tests d'intégration pour les nouvelles API d'interactions.
- Nettoyage et renommage de certains fichiers et variables pour améliorer la lisibilité du code.
- Ajout de la possibilité de faire des frames de la page `/interactions/embed` par n'importe quelle origine.
- Correction de la commande `db:seed-review-app` pour utiliser le script inclus.
- Ajout de la configuration `.next/server` à la liste des fichiers à ignorer lors de la construction.
- Suppression des artefacts `.next/cache` pour réduire la taille de l'image de l'application.
