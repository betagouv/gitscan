## Changelog : api-engagement (30 derniers jours)

### Résumé
Cette période a été marquée par des améliorations significatives de la stabilité et de la performance de l'API et des applications associées, notamment grâce à des mises à jour de dépendances et des corrections de bugs. Des efforts ont également été déployés pour améliorer l'expérience utilisateur, en particulier au niveau du tableau de bord de modération et de l'intégration des widgets. Enfin, des optimisations ont été apportées à l'infrastructure et aux processus de CI/CD.

### Évolutions fonctionnelles
- Ajout d'un bouton "événements en direct" sur les listes de campagnes et de widgets. [#809](https://github.com/betagouv/api-engagement/pull/809)
- Amélioration de la recherche d'organisations avec l'ajout d'un champ `search_text`. [#817](https://github.com/betagouv/api-engagement/pull/817)
- Ajout d'un environnement de "sandbox" pour les tests et le développement. [#850](https://github.com/betagouv/api-engagement/pull/850)
- Correction d'un bug empêchant l'affichage correct de l'organisation du publiateur dans les statistiques des missions. [#852](https://github.com/betagouv/api-engagement/issues/852) et [#854](https://github.com/betagouv/api-engagement/issues/854)
- Correction d'un bug lié à la localisation de grimp.io dans le tableau de bord. [#851](https://github.com/betagouv/api-engagement/issues/851)
- Amélioration de l'interface de modération : nettoyage du tableau, amélioration de la navigation et des filtres, ajout d'éléments d'accessibilité. [#820](https://github.com/betagouv/api-engagement/issues/820), [#821](https://github.com/betagouv/api-engagement/issues/821), [#822](https://github.com/betagouv/api-engagement/issues/822), [#842](https://github.com/betagouv/api-engagement/issues/842)
- Ajout de métriques de taux de conversion dans l'analyse des données. [#811](https://github.com/betagouv/api-engagement/pull/811)

### Évolutions techniques
- Mise à jour de la version de Prisma à la version 7. [#812](https://github.com/betagouv/api-engagement/pull/812)
- Ajout de tests de non-régression pour la fonctionnalité de modération. [#818](https://github.com/betagouv/api-engagement/pull/818)
- Mise à jour de la version de Node.js à la version 24. [#802](https://github.com/betagouv/api-engagement/pull/802)
- Refactorisation de la logique d'agrégation des widgets. [#790](https://github.com/betagouv/api-engagement/pull/790)
- Ajout de l'instrumentation et de la journalisation pour le widget. [#775](https://github.com/betagouv/api-engagement/pull/775)
- Ajout d'un identifiant de requête (request-id) avec support Sentry. [#780](https://github.com/betagouv/api-engagement/pull/780)
- Amélioration de la gestion des erreurs et ajout de la journalisation avec Sentry. [#797](https://github.com/betagouv/api-engagement/pull/797)
- Ajout d'un index composite pour optimiser les recherches d'adresses. [#774](https://github.com/betagouv/api-engagement/pull/774) et [#806](https://github.com/betagouv/api-engagement/pull/806)
- Refactorisation de la relation entre les missions et les activités pour utiliser une table de jointure N-N. [#757](https://github.com/betagouv/api-engagement/pull/757)
- Correction de problèmes liés à la construction du client Prisma.
- Amélioration des jobs CI/CD, notamment pour la gestion des variables d'environnement et la synchronisation des environnements.
- Ajout d'un proxy WAF pour le widget. [#795](https://github.com/betagouv/api-engagement/pull/795)

### Autres changements
- Mise à jour de la documentation concernant l'organisation du publiateur. [#840](https://github.com/betagouv/api-engagement/issues/840)
- Amélioration de l'accessibilité de l'application (ajout d'attributs ARIA, amélioration du contraste, etc.). [#770](https://github.com/betagouv/api-engagement/pull/770)
- Nettoyage du code et suppression de code inutilisé.
- Correction de problèmes de compatibilité zoom sur l'application.
- Suppression de jobs obsolètes (kpi, kpibotless).
- Mise à jour des dépendances.
