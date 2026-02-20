## Changelog : data_pass (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment autour de l'intégration de FranceConnect et de la gestion des habilitations. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de la plateforme. De nouvelles fonctionnalités ont été ajoutées pour faciliter la gestion des accès et des autorisations, en particulier pour les API.

### Évolutions fonctionnelles
- Ajout d'une page Politique de confidentialité (#1374).
- Ajout d'une page Mentions légales (#1371).
- Amélioration de l'affichage du motif d'annulation de la réouverture dans l'historique (#1381).
- Possibilité de sélectionner du texte dans le champ email pour le transférer (#1364).
- Amélioration de la gestion des habilitations FranceConnect pour les API Particulier, avec l'ajout de champs pré-remplis et la configuration des scopes (#1320, #1324, #1351, #1352, #1356).
- Ajout de la possibilité de créer deux habilitations depuis une seule demande (#1344).
- Ajout de la possibilité de changer l'étape de la modalité d'appel (#1327).
- Ajout de la gestion de l'authentification multi-facteurs (MFA) pour les utilisateurs ProConnect (#1325).
- Ajout de la possibilité de filtrer les autorisations et les demandes par numéro SIRET dans l'API (#1321).
- Ajout de la possibilité de marquer un éditeur comme certifié FranceConnect (#1319).
- Amélioration de l'affichage des politiques et de la hiérarchie des onglets (#1329).
- Ajout de liens vers la documentation pour les scopes API Impot Particulier (#1323).
- Ajout de la gestion de nouveaux scopes pour API Particulier Extenso (#1338).
- Ajout de scopes pour la tarification cantine collège/lycée (#1326).
- Implémentation de la gestion des erreurs 422 avec internationalisation (#1326).

### Évolutions techniques
- Mise en place de tests pour les CGU FranceConnect dans le form builder (#1384).
- Refactoring de la logique de visibilité des cases à cocher FranceConnect (#1357).
- Amélioration de la configuration des tests pour fonctionner avec des feature flags (#1371).
- Mise en place d'un système de feature flags pour l'APIFC (#1383).
- Amélioration de la gestion des abonnements HubEE (#1372).
- Mise en place de rails_pulse pour le monitoring de la performance (#1359).
- Correction d'un test défaillant pour les formulaires certifiés FranceConnect (#1366).
- Amélioration de la gestion des erreurs et des réponses non-JSON de l'API INSEE (#1333).
- Mise à jour des dépendances (Rubocop, Brakeman, production et development dependencies) (#1337, #1342, #1348, #1354, #1355, #1367, #1368, #1369).
- Amélioration de la configuration du worktree Git pour faciliter le développement parallèle (#1365).
- Ajout d'un cooldown pour Dependabot (#1343).

### Autres changements
- Clarification des valeurs par défaut dans la documentation (#1360).
- Ajout de factories pour les nouvelles APIs (GUNenv et Inser Jeunes Sup) (#1360).
- Correction de l'accessibilité des liens externes sur la page Accessibilité (#1322).
- Suppression d'une route inutilisée (#1385).
- Suppression des scopes DGFIP pour la lutte contre la fraude dans certains formulaires (#1377, #1382).
- Correction de l'affichage du motif de réouverture dans l'historique (#1381).
- Suppression de l'affichage des scopes DGFIP pour l'API Entreprise dans le formulaire de lutte contre la fraude (#1377).
- Séparation des scopes de conformité sociale et fiscale (#1377).
- Correction de l'affichage des CGU FranceConnect (#1362).
- Correction d'un bug lié à la validation du numéro de téléphone mobile (#1352).
- Suppression de typos (#1370).
- Ajout de documentation pour les nouvelles habilitations (#1370).
- Suppression d'un "f" en trop (#1370).
- Ajout de commentaires et de documentation dans le code.
