## Changelog : aplypro (30 derniers jours, au 01 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la page de rectification des paiements (PFMP), avec des corrections de bugs, des améliorations de l'interface utilisateur et une meilleure gestion des erreurs. Des améliorations ont également été apportées à la gestion des adresses et à la robustesse du système, notamment en cas d'échec de la communication avec l'ASP.

### Évolutions fonctionnelles
- **Rectification PFMP :** Plusieurs corrections de bugs ont été apportées à la page de rectification, améliorant la stabilité et la fiabilité du processus.  Les champs RIB et IBAN sont maintenant gérés correctement, avec des corrections liées à leur effacement et à la recherche d'étudiants. [#1934](https://github.com/betagouv/aplypro/issues/1934), [#1947](https://github.com/betagouv/aplypro/issues/1947)
- **Gestion des adresses :** Amélioration de la gestion des corrections d'adresse via l'ASP, avec l'ajout d'un modèle `ASP::AdresseCorrectionRequest` pour formaliser l'intégration et la gestion des retours. [#1941](https://github.com/betagouv/aplypro/issues/1941)
- **Codes d'extension de voie :**  Gestion des codes d'extension de voie autorisés par l'ASP. [#1951](https://github.com/betagouv/aplypro/issues/1951)
- **Validation :** Amélioration des messages d'erreur de validation sur la page de rectification, avec traduction en français. [#1948](https://github.com/betagouv/aplypro/issues/1948)
- **Gestion des paiements :** Ajout d'un mécanisme de relance en cas d'échec de l'envoi d'une correction. [#1953](https://github.com/betagouv/aplypro/issues/1953)

### Évolutions techniques
- **Refactoring :** Centralisation de la logique de détermination du statut "overpaid?".
- **Tests :** Ajout de tests unitaires et de tests fonctionnels pour la page de rectification, améliorant la couverture et la qualité du code.
- **Optimisations :** Pré-calcul du validateur sur la page de rectification PFMP pour améliorer les performances.
- **Adresseable :** Mise à jour de la gem `addressable` de la version 2.8.9 à la version 2.9.0.
- **Rack-session :** Mise à jour de la gem `rack-session` de la version 2.1.1 à la version 2.1.2.

### Autres changements
- **Documentation :** Amélioration de la documentation et des commentaires dans le code.
- **Nettoyage de code :** Suppression de code inutile et amélioration de la lisibilité du code.
- **Rubocop :** Correction de plusieurs avertissements Rubocop.
- **Version :** La version de l'application a été mise à jour à 2.10.1.
