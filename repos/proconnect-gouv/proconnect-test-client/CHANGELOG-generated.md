## Changelog : proconnect-test-client (30 derniers jours, au 2026-06-15)

### Résumé
Ce changelog couvre les dernières améliorations apportées au client de test ProConnect. Les modifications incluent des mises à jour de configuration pour supporter l'authentification multi-facteurs (MFA), des corrections de bugs mineurs, et des mises à jour de dépendances pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Mise à jour de la structure des valeurs ACR pour déclencher l'authentification multi-facteurs (MFA) [#193](https://github.com/proconnect-gouv/proconnect-test-client/pull/193).
- Correction d'un bug lié à un nom de variable incorrect et à la gestion des chaînes de caractères vides [#194](https://github.com/proconnect-gouv/proconnect-test-client/pull/194).

### Évolutions techniques
- Homogénéisation des variables d'environnement pour une meilleure cohérence et maintenabilité [#194](https://github.com/proconnect-gouv/proconnect-test-client/pull/194).
- Nettoyage du fichier `.env` pour supprimer les configurations inutiles [#193](https://github.com/proconnect-gouv/proconnect-test-client/pull/193).

### Autres changements
- Mise à jour de plusieurs dépendances :
    - `esbuild` et `tsx` (#199)
    - `prettier` (#200)
    - `cypress` dans `/e2e` (#201, #197, #188, #189)
    - `morgan` (#198)
    - `ejs` (#196)
    - `qs` et `@cypress/request` (#192, #190, #75cce20)
    - `tmp` (#192, #1a068bd)
    - `systeminformation` (#188, #c592eac)
