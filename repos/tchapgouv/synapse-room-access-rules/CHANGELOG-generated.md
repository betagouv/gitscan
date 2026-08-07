## Changelog : synapse-room-access-rules (30 derniers jours, au 06/08/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'outil de gestion de la rétention des messages (retention fixer). Les changements permettent une gestion plus fine de la durée de conservation des messages dans les salons publics et introduisent un mode de réduction progressive pour protéger la stabilité et les performances des serveurs.

### Évolutions fonctionnelles
- **Amélioration de l'outil de gestion de la rétention (retention fixer) :**
  - Possibilité de configurer spécifiquement la durée de rétention pour les salons publics.
  - Ajout d'un mécanisme de réduction progressive de la rétention afin d'éviter de surcharger les serveurs lors des processus de nettoyage.

### Évolutions techniques
- **Optimisation des performances :**
  - Refactorisation de la gestion de l'état des salons via l'utilisation de `get_room_state` pour une meilleure efficacité.
- **Qualité et maintenance du code :**
  - Modernisation de la chaîne de qualité avec le passage au formateur `ruff` et la mise à jour des linters.
  - Amélioration de la traçabilité du système par l'ajout de nouveaux logs.

### Autres changements
- **Documentation :** Ajout de documentation concernant le fonctionnement du "retention fixer".
- **Nettoyage :** Diverses corrections de style et nettoyage de code (linting).
