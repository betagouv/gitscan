## Changelog : drive-migrator (30 derniers jours, au 04/09/2026)

### Résumé
Les récentes évolutions se concentrent sur la fiabilité des processus de migration et la robustesse du système. Les utilisateurs bénéficieront d'une meilleure gestion des erreurs lors des exports (le processus ne s'arrête plus au premier fichier défectueux) et d'une interface d'administration enrichie. Parallèlement, le système d'authentification a été modernisé pour renforcer la sécurité.

### Évolutions fonctionnelles
- **Administration :** 
    - Ajout de nouvelles actions permettant de réinitialiser les connexions Resana ou Drive [#198](https://github.com/suitenumerique/drive-migrator/issues/198).
    - Amélioration de la gestion des utilisateurs dans l'interface admin (ajout de l'email et du nom dans les listes et la recherche).
    - Correction d'un plantage de l'interface d'administration lors de la modification du nom d'un utilisateur de migration.
- **Migration et Export :** 
    - Amélioration de la résilience des exports : le système ignore désormais les fichiers en échec au lieu d'interrompre l'intégralité de l'opération, tout en permettant de suivre les erreurs par fichier.
    - L'export échoue désormais correctement si la totalité des téléchargements de fichiers échoue.
- **Expérience Utilisateur (UX/UI) :** 
    - Refonte du parcours de téléchargement des archives ZIP [#194](https://github.com/suitenumerique/drive-migrator/issues/194).
    - Amélioration de la clarté visuelle : ajout de tooltips pour les titres tronqués [#195](https://github.com/suitenumerique/drive-migrator/issues/195) et précision de la cible de migration (Fichiers/Drive) [#193](https://github.com/suitenumerique/drive-migrator/issues/193).
    - Corrections diverses : résolution d'une boucle infinie sur la page de connexion, correction de l'affichage de la page de fin [#207](https://github.com/suitenumerique/drive-migrator/issues/207) et ajustements des messages d'erreur [#140](https://github.com/suitenumerique/drive-migrator/issues/140).

### Évolutions techniques
- **Authentification et Sécurité :** 
    - Modernisation du flux d'authentification Resana via l'implémentation du module PKCE (connect/callback).
    - Suppression du scraping HTML pour la gestion du CSRF dans le client Resana.
    - Suppression de l'en-tête `x-amz-acl` non signé lors des uploads S3 présignés.
- **Robustesse et Performance :** 
    - Mise en place de mécanismes de tentatives automatiques (retries) pour les téléchargements de fichiers Resana en cas d'erreurs réseau transitoires.
    - Optimisation de la gestion des tokens Resana (sérialisation par utilisateur et stockage de session bridge).
- **Configuration :** 
    - Rendre l'URL du frontend Drive configurable [#103](https://github.com/suitenumerique/drive-migrator/issues/103).
    - Correction de la lecture de la variable d'environnement pour les fichiers statiques.
