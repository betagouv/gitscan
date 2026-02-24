## Changelog : data_pass (30 derniers jours)

### Résumé
Les dernières mises à jour de DataPass se concentrent sur l'amélioration de l'intégration avec FranceConnect, l'ajout de nouvelles fonctionnalités pour les API partenaires, et la correction de bugs pour une meilleure expérience utilisateur. Des améliorations de sécurité ont également été apportées, notamment avec l'implémentation de l'authentification multi-facteurs pour ProConnect.

### Évolutions fonctionnelles
- Ajout de la page Politique de confidentialité (#1374).
- Ajout de la page Mentions légales (#1371).
- Possibilité de sélectionner le texte dans le champ email pour le transférer (#1364).
- Amélioration de l'historique de validation avec un affichage plus générique pour la consultation (#1349).
- Précision du type d'habilitation dans la liste des habilitations (#1347).
- Possibilité de créer deux habilitations depuis une seule demande (#1344).
- Implémentation des vues pour les champs FranceConnect pour l'API Particulier (#1320).
- Possibilité de créer automatiquement une habilitation FranceConnect depuis l'API Particulier (#1320).
- Configuration des scopes FranceConnect pour l'API Particulier et les éditeurs certifiés (#1324).
- Ajout de nouveaux scopes pour l'API Particulier Extenso (#1338).
- Ajout de scopes pour l'API Particulier tarification cantine collège/lycée (#1334).
- Authentification multi-facteurs (MFA) forcée pour les utilisateurs MonComptePro via ProConnect (#1325).
- Possibilité de changer l'étape de la modalité d'appel (#1327).

### Évolutions techniques
- Amélioration de la gestion des feature flags, notamment pour l'APIPFC (#1379, #1383).
- Refactoring de la logique d'affichage des scopes FranceConnect (#1351).
- Amélioration de la gestion des erreurs pour l'API INSEE (#1333).
- Mise en place de rails_pulse pour le monitoring de l'application (#1359).
- Amélioration de la configuration pour les tests avec et sans Docker (#1338).
- Correction de tests suite à des modifications de code (#1366, #1378).
- Mise à jour des dépendances (Rubocop, Brakeman, Bundler) (#1369, #1368, #1367, #1355, #1354, #1346, #1328).
- Ajout d'un cooldown de 7 jours pour les mises à jour de dépendances par Dependabot (#1342).

### Autres changements
- Mise à jour de la documentation pour les éditeurs certifiés FranceConnect (#1324).
- Correction de l'affichage de la raison d'annulation d'une réouverture dans l'historique (#1381).
- Suppression d'une route inutilisée (#1372).
- Correction de l'affichage des CGU (#1362).
- Ajout de factories pour les nouvelles APIs (#1360).
- Clarification des valeurs par défaut dans la documentation (#1360).
- Correction de l'accessibilité des liens externes sur la page Accessibilité (#1326).
- Suppression des scopes DGFIP pour l'API Entreprise Lutte contre la fraude (#1376).
- Séparation des scopes conformité sociale et fiscale (#1377).
- Mise à jour des numéros de téléphone des contacts techniques (#1379).
- Correction d'un bug lié à l'affichage du cadre juridique FranceConnect (#1348).
- Suppression de l'affichage des scopes FranceConnect sans modalité (#1351).
- Correction d'un bug lié à la validation du numéro de téléphone mobile (#1352).
