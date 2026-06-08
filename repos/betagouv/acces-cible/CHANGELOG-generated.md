## Changelog : acces-cible (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilité et l'efficacité de l'application. Nous avons notamment amélioré la gestion des imports CSV, corrigé des problèmes de performance liés aux requêtes SQL, et intégré un nouveau widget JDMA pour faciliter l'évaluation de l'accessibilité. Des efforts de maintenance ont également été réalisés pour nettoyer le code et supprimer les dépendances inutilisées.

### Évolutions fonctionnelles
- Ajout d'un widget JDMA permettant d'afficher des informations sur l'accessibilité. [#569](https://github.com/betagouv/acces-cible/issues/569)
- Amélioration de la stabilité des imports CSV grâce à un traitement en arrière-plan. [#541](https://github.com/betagouv/acces-cible/issues/541)
- Correction de la normalisation des URLs des sites, assurant une meilleure cohérence des données. [#576](https://github.com/betagouv/acces-cible/issues/576)
- Correction d'un bug empêchant l'import CSV de fonctionner correctement avec des tags en doublon. [#577](https://github.com/betagouv/acces-cible/issues/577)
- Configuration du bouton JDMA via des variables d'environnement pour une plus grande flexibilité. [#578](https://github.com/betagouv/acces-cible/issues/578)

### Évolutions techniques
- Correction de requêtes SQL N+1 pour améliorer les performances. [#538](https://github.com/betagouv/acces-cible/issues/538)
- Refactoring du navigateur utilisé par l'application. [#545](https://github.com/betagouv/acces-cible/issues/545)
- Utilisation du composant DSFR Side Menu pour une meilleure cohérence avec le design system. [#571](https://github.com/betagouv/acces-cible/issues/571)
- Nettoyage du code mort et suppression des dépendances inutilisées. [#542](https://github.com/betagouv/acces-cible/issues/542)
- Suppression de la logique liée à `current` dans le code. [#573](https://github.com/betagouv/acces-cible/issues/573)

### Autres changements
- Correction d'une faute de frappe dans le fichier `queue.yml`. [#567](https://github.com/betagouv/acces-cible/issues/567)
- Ajout de migrations pour mettre à jour les URLs des sites en base de données (plusieurs tentatives et reverts). [#553](https://github.com/betagouv/acces-cible/issues/553), [#554](https://github.com/betagouv/acces-cible/issues/554), [#555](https://github.com/betagouv/acces-cible/issues/555), [#556](https://github.com/betagouv/acces-cible/issues/556), [#557](https://github.com/betagouv/acces-cible/issues/557), [#558](https://github.com/betagouv/acces-cible/issues/558)
