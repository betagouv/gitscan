## Changelog : mobilic (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a principalement travaillé sur une refonte majeure du tableau d'administration des employés, améliorant l'ergonomie et la gestion des utilisateurs. Des corrections de bugs et des améliorations de la sécurité ont également été apportées, notamment concernant la gestion des cookies et des erreurs d'authentification. Enfin, des ajustements ont été faits pour améliorer la compatibilité et la configuration de l'application.

### Évolutions fonctionnelles
- Ajout d'une page de compatibilité/exigences système pour l'application. [#797](https://github.com/MTES-MCT/mobilic/pull/797)
- Amélioration de l'interface utilisateur du tableau d'administration des employés :
    - Redesign complet du tableau avec édition en ligne.
    - Ajout d'un badge indiquant le statut "inactif" des employés.
    - Amélioration de la modale de résiliation d'un contrat de travail.
    - Ajout d'un dropdown pour gérer les employés inactifs.
    - Tri des employés détachés à la fin du tableau.
- Possibilité de résilier plusieurs contrats de travail en batch pour les employés inactifs.
- Ajout d'un message d'erreur plus clair lorsque l'authentification via un fournisseur d'identité (IDP) est bloquée. [#810](https://github.com/MTES-MCT/mobilic/pull/810)
- Modification du texte pour l'installation de l'application iOS. [#811](https://github.com/MTES-MCT/mobilic/pull/811)
- Correction de l'affichage des infractions dans l'en-tête et le tiroir de navigation.
- Amélioration de la performance du dropdown des employés inactifs.

### Évolutions techniques
- Correction d'un problème de boucle infinie avec le cookie `x-ubika-data` et le WAF (Web Application Firewall). [#808](https://github.com/MTES-MCT/mobilic/pull/808)
- Utilisation de HTTP/1.1 pour les requêtes vers l'API en amont afin de corriger des problèmes avec le proxy Ubika. [#802](https://github.com/MTES-MCT/mobilic/pull/802)
- Mise à jour de la configuration de webpack pour la compatibilité avec la version 5. [#799](https://github.com/MTES-MCT/mobilic/pull/799)
- Refactorisation du code pour centraliser les styles DSFR dans les composants de filtre.
- Utilisation de `useRef` pour optimiser la gestion des bannières.
- Suppression de code inutilisé et amélioration de la qualité du code dans le tableau d'administration.
- Correction de warnings ESLint.
- Amélioration de la gestion des mutations GraphQL pour éviter les doublons.
- Optimisation de la gestion des erreurs d'authentification dans le playground.
- Correction d'erreurs CSS dans le playground.

### Autres changements
- Correction de l'importation des fichiers CSS dans le playground. [#806](https://github.com/MTES-MCT/mobilic/pull/806)
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité. [#791](https://github.com/MTES-MCT/mobilic/pull/791) et [#88d363e6b74ec1047607b6997b2e0a3c](https://github.com/MTES-MCT/mobilic/commit/9bdd4ab81538f7874791d29a269342893442447f)
- Suppression de commentaires inutiles.
- Correction de la taille des titres dans le tableau d'administration.
- Correction de l'ordre des noms dans le tableau d'administration.
- Suppression d'un titre d'action redondant dans le dropdown.
- Corrections UI suite aux tests de l'épopée 12-13-37.
