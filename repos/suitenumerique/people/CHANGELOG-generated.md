## Changelog : people (30 derniers jours, au 20 avril 2026)

Ce mois-ci, les améliorations se concentrent sur la sécurité, l'expérience utilisateur et la gestion des invitations. Les utilisateurs bénéficieront notamment de l'envoi de liens de connexion au lieu de mots de passe, d'une meilleure gestion des erreurs et de corrections de vulnérabilités. Des améliorations de l'interface utilisateur et des corrections de bugs ont également été apportées.

### Évolutions fonctionnelles

- **Sécurité :** Envoi de liens de connexion au lieu de mots de passe pour une meilleure sécurité lors de l'invitation d'utilisateurs. [#1108](https://github.com/suitenumerique/people/issues/1108)
- **Invitations :** Correction d'une potentielle escalade de privilèges lors de l'invitation d'utilisateurs.
- **Gestion des erreurs :** Amélioration du message d'erreur lorsque l'utilisateur n'a pas d'adresse email secondaire.
- **Interface utilisateur :** Amélioration du message affiché lorsqu'il n'y a pas d'alias sur la page de domaine.
- **Administration :** Possibilité d'exporter les informations de contact du domaine pour l'administration.
- **Langues :** Correction de l'affichage de la langue actuelle dans le menu de profil.

### Évolutions techniques

- **Sécurité :** Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (Pillow, Django, lodash, Next.js, pytest).
- **Dimail :** Correction d'un problème d'importation des boîtes aux lettres fonctionnelles.
- **Dimail :** Mise à jour de la documentation concernant dimail.
- **Tests :** Vérification que les accès créés par email ont le rôle attendu.

### Autres changements

- **Internationalisation (i18n) :** Mise à jour des chaînes de caractères traduites.
- **Version :** Publication de la version 1.25.0.
- **UI :** Suppression d'une bordure inutile dans l'interface utilisateur.
