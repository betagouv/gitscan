## Changelog : karfur (30 derniers jours, au 27 octobre 2026)

### Résumé
Ce mois a été marqué par le lancement de l'Espace FR dédié aux cours de français et par un effort massif de mise en conformité avec les normes d'accessibilité (RGAA). La plateforme est devenue plus robuste grâce à une série de mises à jour de sécurité et à l'amélioration des performances de recherche et de navigation.

### Évolutions fonctionnelles
- **Lancement de l'Espace FR** : Intégration complète des cours de français dans la navigation (header, footer, sitemap), ajout d'un carrousel sur la page d'accueil et mise en place d'une recherche par localisation (département/ville) [#3957](https://github.com/refugies-info/karfur/pull/3957).
- **Accessibilité (RGAA)** : Amélioration significative de l'expérience utilisateur pour les personnes utilisant des outils d'assistance (corrections des contrastes de couleurs, gestion du zoom à 200%, et optimisation de l'affichage sur petits écrans pour éviter les débordements).
- **Recherche et navigation** : Amélioration de la fluidité des résultats de recherche et de la gestion des états vides ou d'erreur.
- **Expérience mobile** : Correction de plusieurs bugs liés à l'enregistrement des données, aux notifications doubles et au partage par SMS.
- **Internationalisation** : Mise à jour des traductions pour les nouveaux contenus et harmonisation des termes de recherche dans les différentes langues.

### Évolutions techniques
- **Administration des widgets** : Mise en place d'une nouvelle API et d'un modèle de configuration pour permettre une gestion simplifiée des widgets via le backoffice [#4027](https://github.com/refugies-info/karfur/pull/4027).
- **Performances** : Optimisation de la recherche et de la pagination via l'implémentation de SWR pour un chargement plus rapide et une meilleure gestion du cache [#4019](https://github.com/refugies-info/karfur/pull/4019).
- **Sécurité** : Campagnes de nettoyage intensives pour corriger des vulnérabilités critiques (Storybook, Handlebars, etc.) et intégration de l'outil de scan OSV-Scanner dans le pipeline CI.
- **CI/CD et Infrastructure** :
    - Automatisation du versioning lors des déploiements en production.
    - Mise à jour de l'environnement Node.js (v24.22.1) [#4031](https://github.com/refugies-info/karfur/pull/4031).
    - Ajout de notifications Slack pour informer automatiquement des nouvelles versions publiées.
- **Refactoring** : Nettoyage du code client avec la suppression des fonctionnalités de widgets obsolètes et des pages d'intégration inutilisées [#4028](https://github.com/refugies-info/karfur/pull/4028).

### Autres changements
- **Documentation** : Ajout de précisions dans le README concernant l'importance du système de versioning pour le projet.
