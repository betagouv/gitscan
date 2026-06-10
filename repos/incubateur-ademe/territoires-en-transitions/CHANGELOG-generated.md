## Changelog : territoires-en-transitions (30 derniers jours, au 09 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'import de plans d'action, notamment avec l'ajout de fonctionnalités d'extraction de données depuis différents formats de fichiers et de consolidation des actions. Des améliorations significatives ont également été apportées à l'interface utilisateur, notamment pour la gestion des référentiels et des actions, ainsi que des corrections de sécurité et des optimisations de performance.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité de duplication d'un plan d'action, incluant les preuves/documents et les budgets détaillés. [#1234](https://github.com/incubateur-ademe/territoires-en-transitions/issues/1234)
- Amélioration de l'affichage des snapshots dans l'ordre chronologique.
- Possibilité de filtrer les mesures désactivées par la personnalisation.
- Ajout d'une modale pour détailler une action à la tâche.
- Implémentation d'une vue tabulaire éditable pour les référentiels.
- Ajout d'une page publique pour la matrice d'impact.
- Ajout d'une fonctionnalité permettant de demander un audit depuis les référentiels.
- Amélioration de la gestion des annexes des fiches.
- Ajout d'une page "mesure désactivée".
- Amélioration de l'import de plans avec l'extraction de texte depuis des fichiers PDF, CSV et Excel.

### Évolutions techniques
- Refactor de l'import de plans d'action avec une meilleure séparation des responsabilités et une gestion asynchrone des archives ZIP.
- Utilisation de `mapWithConcurrency` pour la consolidation des actions à faible score.
- Migration de plusieurs composants vers le design system DSTET.
- Migration de certaines requêtes vers tRPC pour améliorer la performance et la cohérence.
- Suppression de dépendances inutilisées et nettoyage du code.
- Amélioration de la sécurité en bloquant l'injection SQL sur la recherche de collectivités et en restreignant l'accès horizontal aux données sensibles.
- Mise à jour de plusieurs dépendances.
- Amélioration de la configuration CI/CD.
- Utilisation de serveurs de recherche full-text pour la recherche de collectivités.
- Refactor de la gestion des labels JSX pour une meilleure maintenabilité.
- Amélioration de la gestion des tests E2E et unitaires.

### Autres changements
- Documentation de la création de client ID/secret via curl.
- Ajout de fixtures pour les tests.
- Amélioration de la configuration Tailwind.
- Correction de typos et amélioration de la lisibilité du code.
- Ajout de metadata pour la nouvelle page plateforme du site.
- Suppression de fichiers et de symboles exportés non utilisés.
- Mise à jour de la configuration TypeScript.
- Amélioration de la robustesse des tests d'envoi de mails.
- Ajout de commentaires et de documentation pour clarifier le code.
