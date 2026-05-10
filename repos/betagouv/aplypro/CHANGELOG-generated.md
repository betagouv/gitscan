## Changelog : aplypro (30 derniers jours, au 01 mai 2026)

### Résumé
Ce changelog couvre une période d'amélioration continue de l'application Aplypro, axée sur la correction de bogues, l'amélioration de la gestion des adresses et des corrections de paiements, ainsi que sur l'ajout de tests pour garantir la stabilité et la fiabilité de la plateforme. Des améliorations ont également été apportées à l'interface utilisateur et à la gestion des codes d'extension de voie.

### Évolutions fonctionnelles

- **Gestion des adresses :** Amélioration de la gestion des corrections d'adresses avec l'intégration de `ASP::AdresseCorrectionRequest` et la gestion des retours d'intégration/rejets. [#1941](https://github.com/betagouv/aplypro/issues/1941)
- **Gestion des codes d'extension de voie :** Ajout de la gestion des codes d'extension de voie autorisés par l'ASP. [#1951](https://github.com/betagouv/aplypro/issues/1951)
- **Rectification des paiements :**
    - Amélioration de la gestion des erreurs de validation sur la page de rectification. [#1948](https://github.com/betagouv/aplypro/issues/1948)
    - Correction de plusieurs problèmes mineurs sur la page de rectification. [#1947](https://github.com/betagouv/aplypro/issues/1947)
    - Ajout d'un mécanisme de relance pour les corrections rejetées. [#1953](https://github.com/betagouv/aplypro/issues/1953)
- **Traduction :** Traduction des messages d'erreur en français. [#1944](https://github.com/betagouv/aplypro/issues/1944)

### Évolutions techniques

- **Refactoring :** Centralisation de la définition de la méthode `overpaid?`.
- **Tests :**
    - Ajout de tests unitaires.
    - Ajout de tests fonctionnels sur la page de rectification.
    - Ajout de spécifications pour les méthodes et la méthode `overpaid?`.
- **Optimisations :** Pré-calcul du validateur sur la page de rectification PFMP.
- **Architecture :** Formalisation de l'intégration et des rejets des retours de correction d'adresse.
- **Correction d'adresses :** Ajout du modèle `ASP::AdresseCorrectionRequest`.

### Autres changements

- Mise à jour de la version de l'application à 2.10.0 puis 2.10.1.
- Correction de bugs liés aux mises à jour d'adresses. [#1944](https://github.com/betagouv/aplypro/issues/1944)
- Amélioration de la gestion des doublons.
- Nettoyage du code et correction de problèmes Rubocop.
- Correction de type error.
- Suppression de conditions inutiles.
- Floutage du numéro IBAN sur la page de rectification.
- Amélioration de l'affichage des accordéons.
- Correction de la logique de déduplication.
- Collage du titre de la page de rectification.
