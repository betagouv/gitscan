## Changelog : aplypro (30 derniers jours, au 14 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des corrections d'adresses et des paiements, notamment un mécanisme de relance automatique en cas d'échec, une meilleure gestion des codes d'extension de voie et une pagination des rapports pour une meilleure performance. Des corrections de validation et des améliorations de l'interface utilisateur ont également été apportées.

### Évolutions fonctionnelles
- **Corrections d'adresses :** Ajout d'un mécanisme de relance automatique pour les corrections d'adresses qui échouent [#1953](https://github.com/betagouv/aplypro/issues/1953).
- **Gestion des codes d'extension de voie :** Amélioration de la gestion des codes d'extension de voie autorisés par l'ASP [#1951](https://github.com/betagouv/aplypro/issues/1951).
- **Pagination des rapports :** La page d'index des rapports est désormais paginée pour améliorer les performances [#1956](https://github.com/betagouv/aplypro/issues/1956).
- **Validation des paiements :** Amélioration des messages d'erreur de validation sur la page de rectification des paiements [#1948](https://github.com/betagouv/aplypro/issues/1948).
- **Affichage IBAN :** L'IBAN est désormais flouté sur la page de rectification pour des raisons de sécurité.

### Évolutions techniques
- **Version :** Mise à jour de la version de l'application à 2.10.0 puis 2.10.1.
- **Tests :** Ajout de tests unitaires et de tests fonctionnels pour la page de rectification et la pagination des rapports.
- **Refactoring :** Suppression de conditions inutiles et nettoyage du code.
- **Méthodes :** Ajout de la méthode `complete?` pour divers objets.

### Autres changements
- Mise à jour des dépendances (bundle).
- Amélioration de l'affichage des accordéons.
- Ajout de specs pour la méthode `overpaid?`.
