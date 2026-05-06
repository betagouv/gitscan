## Changelog : mobilic-api (30 derniers jours, au 05 mai 2026)

### Résumé
Ce mois-ci, les évolutions de l'API Mobilic se concentrent sur l'amélioration de la sécurité (authentification multi-facteurs, protection contre les attaques DoS), l'ajout de fonctionnalités pour le back-office (support administrateur, recherche d'utilisateurs) et la correction de bugs liés à la gestion des timezones et à l'export de données. Des améliorations ont également été apportées à l'intégration avec Brevo et à la recherche NATINF.

### Évolutions fonctionnelles
- Ajout de la prise en charge de l'authentification à deux facteurs (TOTP) avec génération de code via une application mobile. [#685](https://github.com/MTES-MCT/mobilic-api/pull/685)
- Possibilité pour les administrateurs de se connecter en tant qu'autres utilisateurs pour support (impersonation) avec journalisation des actions. [#700](https://github.com/MTES-MCT/mobilic-api/pull/700)
- Amélioration de la recherche NATINF avec la possibilité de créer et supprimer des NATINF personnalisés. [#671](https://github.com/MTES-MCT/mobilic-api/pull/671)
- Ajout d'articles dans les exports PDF BDC. [#72cb185](https://github.com/MTES-MCT/mobilic-api/commit/72cb185)
- Correction de l'affichage des timezones dans les exports et PDF. [#693](https://github.com/MTES-MCT/mobilic-api/pull/693)
- Ajout d'une recherche d'utilisateurs pour la fonctionnalité d'impersonation. [#696](https://github.com/MTES-MCT/mobilic-api/pull/696)

### Évolutions techniques
- Refactorisation de l'impersonation pour utiliser un JWT claim `impersonate_as` au lieu d'un cookie.
- Ajout d'une protection contre les attaques par complexité de requête GraphQL (DoS). [#694](https://github.com/MTES-MCT/mobilic-api/pull/694)
- Amélioration de la sécurité en désactivant GraphiQL en production et en ajoutant une limite de taille pour les requêtes GraphQL.
- Suppression du contexte des accès aux données pour l'activité. [#693](https://github.com/MTES-MCT/mobilic-api/pull/693)
- Correction de l'ordre des révisions de migrations.
- Centralisation d'une fonction pour éviter la duplication de code.
- Sanityzation du nom de l'entreprise Brevo avant la recherche de deal. [#696](https://github.com/MTES-MCT/mobilic-api/pull/696)
- Mise à jour de pipenv et pipfile.lock.
- Ajout de tests unitaires et d'intégration pour la sécurité (IDOR, etc.).

### Autres changements
- Ajout de tests pour couvrir la révocation de jeton côté cible dans le middleware d'impersonation.
- Ajout d'une purge RGPD pour la table `support_action_log`.
- Correction de conflits de merge.
- Correction du format du poids des véhicules BDC. [#691](https://github.com/MTES-MCT/mobilic-api/pull/691)
- Suppression du contexte des accès aux données pour l'activité.
