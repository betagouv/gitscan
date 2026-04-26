## Changelog : aplypro (30 derniers jours, au 24 avril 2026)

### Résumé
Cette période a été marquée par des améliorations significatives sur la page de rectification des PFMP (Primes de Formation en Milieu Professionnel), avec une attention particulière portée à la correction de bugs et à l'amélioration de l'expérience utilisateur. Des corrections liées à l'adresse et aux paiements MASA ont également été apportées, ainsi que des améliorations concernant la gestion des élèves et de leur scolarité.

### Évolutions fonctionnelles
- Amélioration de la page de rectification des PFMP :
    - Affichage des messages d'erreur du formulaire de rectification. [#1948]
    - Correction de plusieurs problèmes mineurs sur cette page. [#1947]
    - Correction du problème de réinitialisation du champ IBAN.
    - Correction du bouton de suppression du RIB.
    - Collage du titre de la page de rectification.
- Déblocage des paiements MASA. [#1933]
- Gestion de la double scolarité d'un élève dans une même classe. [#1923]
- Affichage d'informations complémentaires sur la page de détail de l'élève.
- Modification visuelle des informations de l'élève.
- Modification de la logique et de l'affichage du bouton d'abrogation.
- Correction d'un bug empêchant la recherche d'étudiants.

### Évolutions techniques
- Intégration de `ASP::AdresseCorrectionRequest` pour formaliser l'intégration et la gestion des retours de la correction d'adresse. [#1941]
- Centralisation de la définition de la méthode `overpaid?`.
- Pré-calcul du validateur pour la rectification PFMP afin d'optimiser les performances.
- Amélioration de la logique de déduplication.
- Correction de plusieurs erreurs de type dans le code.
- Mise à jour de la logique de gestion des codes INSEE.
- Amélioration de la gestion des majuscules/minuscules pour la correction d'adresse.
- Correction de tests et ajout de tests fonctionnels sur la page de rectification.
- Suppression de code inutile et nettoyage du code.

### Autres changements
- Traduction des messages d'erreur en français.
- Mise à jour de certaines dépendances : `addressable`, `rack-session`, `rack`.
- Bump de version : 2.9.1, 2.9.2, 2.9.3, 2.9.4, 2.10.0.
- Correction de Rubocop.
