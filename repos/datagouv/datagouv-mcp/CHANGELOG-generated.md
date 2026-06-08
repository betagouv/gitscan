## Changelog : datagouv-mcp (30 derniers jours, au 2 juin 2026)

### Résumé
Ce mois-ci, les améliorations apportées à datagouv-mcp se concentrent sur l'amélioration des fonctionnalités de recherche de datasets et la correction de bugs. Les utilisateurs peuvent désormais trier les résultats de recherche et filtrer par date de dernière mise à jour. Une correction a également été apportée pour assurer l'exactitude du nombre de ressources retournées par la recherche.

### Évolutions fonctionnelles
- Ajout de paramètres de tri et de filtrage par date de dernière mise à jour à la recherche de datasets ([#113](https://github.com/datagouv/datagouv-mcp/pull/113)).
- Correction du nombre de ressources retournées par la recherche de datasets, qui affiche désormais la valeur correcte ([#115](https://github.com/datagouv/datagouv-mcp/pull/115)).

### Évolutions techniques
- Correction de problèmes de typage dans le code.
- Suppression d'une contrainte temporaire sur la librairie `urllib3`.
- Mise à jour des dépendances du projet.
- Correction d'une vulnérabilité de sécurité dans `urllib3` ([#112](https://github.com/datagouv/datagouv-mcp/pull/112)).

### Autres changements
- Publication des versions 0.2.26 et 0.2.25.
