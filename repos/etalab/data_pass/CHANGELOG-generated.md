## Changelog : data_pass (30 derniers jours)

### Résumé
Les dernières mises à jour de data_pass se concentrent sur l'amélioration de l'intégration de FranceConnect, notamment pour les API partenaires, avec une configuration plus fine des scopes et l'ajout de champs pré-remplis. Des améliorations ont également été apportées à l'expérience utilisateur, comme la gestion des habilitations et l'historique des validations, ainsi qu'à la sécurité avec l'ajout de l'authentification multi-facteurs pour les utilisateurs ProConnect.

### Évolutions fonctionnelles
- Ajout de champs pré-remplis pour FranceConnect dans les formulaires API Particulier (#1346, #1320).
- Amélioration de l'historique des validations et génération automatique, avec une présentation plus générique des actions (#1349).
- Précision du type d'habilitation dans la liste des habilitations (#1347).
- Possibilité de créer deux habilitations à partir d'une seule demande (#1344).
- Amélioration de la navigation dans les formulaires FranceConnect pour les éditeurs certifiés, en commençant directement par l'étape des modalités (#1327).
- Ajout de la possibilité de changer l'étape de la modalité d'appel (#1327).
- Implémentation de vues pour les champs FranceConnect dans API Particulier (#1320).
- Ajout de la configuration des scopes FranceConnect pour API Particulier et éditeurs certifiés (#1324).
- Ajout de la page Mentions légales et Politique de confidentialité (#1374, #1384).
- Ajout de l'iframe opt-out Matomo pour la politique de confidentialité (#1384).
- Mise à jour des numéros de téléphone des contacts techniques pour APIPFC (#1379).
- Correction de l'affichage du motif d'annulation de la réouverture dans l'historique (#1385).

### Évolutions techniques
- Refactorisation de la logique de visibilité des champs FranceConnect (#1320).
- Amélioration de la gestion des erreurs pour l'API INSEE (#1333).
- Mise en place d'un système de feature flags pour l'APIPFC (#1383, #1380).
- Mise à jour des dépendances (Rubocop, Brakeman, Bundler) (#1369, #1368, #1367, #1354, #1328).
- Ajout de tests pour les CGU FranceConnect dans le form builder (#1382).
- Mise en place de Rails Pulse pour le monitoring des performances (#1359).
- Amélioration de la configuration du worktree Git pour faciliter le développement parallèle (#1365).
- Correction d'un problème de test intermittent (#1343).
- Ajout d'une protection contre les réponses non-JSON de l'API INSEE (#1333).
- Implémentation de l'authentification multi-facteurs (MFA) pour les utilisateurs ProConnect (#1325).
- Gestion des abonnements HubEE existants (#1372).
- Séparation des scopes de conformité sociale et fiscale (#1377).

### Autres changements
- Mise à jour de la documentation pour les éditeurs certifiés FranceConnect (#1324).
- Correction de l'accessibilité des liens externes sur la page Accessibilité (#1362).
- Clarification des valeurs par défaut dans la documentation (#1360).
- Ajout de factories pour les nouvelles APIs (#1360).
- Amélioration du message d'erreur pour la recherche d'abonnement HubEE (#1372).
- Suppression de routes inutilisées (#1385).
- Correction d'un bug dans l'affichage du cadre juridique FranceConnect (#1348).
- Ajout d'un cooldown de 7 jours pour les mises à jour de dépendances (#1342).
- Correction d'un bug lié à la validation du numéro de téléphone mobile (#1352).
- Suppression de scopes DGFIP pour l'API Entreprise Lutte contre la Fraude (#1376).
- Ajout de scopes pour l'API Particulier Extenso (#1339).
- Correction d'un bug lié à l'affichage des CGU FranceConnect (#1362).
