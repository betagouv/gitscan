## Changelog : proconnect-identite (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment en permettant aux mairies de choisir leur adresse email, en affinant la suggestion d'organisations et en modernisant l'interface utilisateur. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des mises à jour de sécurité et de dépendances.

### Évolutions fonctionnelles
- Possibilité pour les mairies de choisir leur adresse email [#1728](https://github.com/proconnect-gouv/proconnect-identite/pull/1728).
- Amélioration de la suggestion d'organisations, avec une meilleure performance [#1832](https://github.com/proconnect-gouv/proconnect-identite/pull/1832), [#1797](https://github.com/proconnect-gouv/proconnect-identite/pull/1797).
- Nouvelle interface utilisateur avec une nouvelle disposition en une colonne [#1769](https://github.com/proconnect-gouv/proconnect-identite/pull/1769).
- Ajout d'un délai de modération [#1819](https://github.com/proconnect-gouv/proconnect-identite/pull/1819).
- Ajout d'un badge "certifié" pour les organisations disposant de cette certification.
- Amélioration de l'affichage des informations de l'organisation sur la page d'accueil du dirigeant.
- Correction d'un bug empêchant la perte de session après le redémarrage de l'application [#1778](https://github.com/proconnect-gouv/proconnect-identite/pull/1778).
- Ajout d'une section "Informations FranceConnect" pour l'anonymisation des données [#1757](https://github.com/proconnect-gouv/proconnect-identite/pull/1757).

### Évolutions techniques
- Suppression du code inutile lié à Crisp.
- Suppression de la route API admin.
- Refactorisation du code pour remplacer `Zod.merge` par `Zod.extend` [#1823](https://github.com/proconnect-gouv/proconnect-identite/pull/1823).
- Suppression du champ "commentaires" de l'export de la table des modérations [#1822](https://github.com/proconnect-gouv/proconnect-identite/pull/1822).
- Migration de la vérification des petites associations vers le domaine lorsque l'email est vérifié [#1761](https://github.com/proconnect-gouv/proconnect-identite/pull/1761), [#1760](https://github.com/proconnect-gouv/proconnect-identite/pull/1760).
- Mise à jour des dépendances : hono, koa, nodemailer, axios, qs, cypress-io/github-action, actions/upload-artifact, docker/login-action, docker/setup-buildx-action, docker/metadata-action, docker/setup-qemu-action, minimatch, sentry.
- Mise à jour de la configuration du workflow CI pour exécuter les tests mensuellement [#1834](https://github.com/proconnect-gouv/proconnect-identite/pull/1834).
- Ajout d'un fichier `SECURITY.md` et d'une politique de sécurité pour la signalisation des vulnérabilités [#1821](https://github.com/proconnect-gouv/proconnect-identite/pull/1821).

### Autres changements
- Amélioration de la documentation et des messages d'erreur (message d'erreur "trop de requêtes").
- Correction de la politique de sécurité pour la signalisation des vulnérabilités.
- Ajout d'une nouvelle catégorie juridique "Association de droit local (Bas-Rhin, Haut-Rhin et Moselle)" [#1820](https://github.com/proconnect-gouv/proconnect-identite/pull/1820).
- Suppression de l'option 2FA.
- Suppression de l'input de rôle sur la page de complétion du profil.
- Ajout de tests E2E pour la certification des organisations avec suggestion.
- Harmonisation des exports des tests.
- Suppression d'une directive inutile dans la CSP pour Crisp.
- Ajout de tests unitaires pour la vérification du type d'utilisateur assigné.
- Mise à jour des fichiers de configuration et des dépendances.
