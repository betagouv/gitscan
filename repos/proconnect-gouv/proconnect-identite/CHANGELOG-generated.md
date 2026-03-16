## Changelog : proconnect-identite (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur avec une nouvelle interface graphique, des corrections de bugs et des optimisations de performance. Des améliorations ont également été apportées à la gestion des organisations, aux tests automatisés et à la sécurité.

### Évolutions fonctionnelles
- Possibilité de sélectionner un nom après l'authentification via FranceConnect [#1792](https://github.com/proconnect-gouv/proconnect-identite/pull/1792).
- Nouvelle interface utilisateur avec une disposition à une seule colonne [#1679](https://github.com/proconnect-gouv/proconnect-identite/pull/1679).
- Ajout d'un badge "certifié" pour les organisations disposant de cette certification [#1782](https://github.com/proconnect-gouv/proconnect-identite/pull/1782).
- Amélioration de la barre de progression pour remplacer le stepper [#1811](https://github.com/proconnect-gouv/proconnect-identite/pull/1811).
- Correction d'un bug empêchant la redirection après la connexion [#1845](https://github.com/proconnect-gouv/proconnect-identite/pull/1845).
- Correction d'un bug sur le bouton désactivé après un retour en arrière [#1837](https://github.com/proconnect-gouv/proconnect-identite/pull/1837).
- La session n'est plus perdue lors du rechargement de l'application [#1778](https://github.com/proconnect-gouv/proconnect-identite/pull/1778).
- Ajout d'une nouvelle catégorie juridique "Association de droit local (Bas-Rhin, Haut-Rhin et Moselle)" [#1821](https://github.com/proconnect-gouv/proconnect-identite/pull/1821).
- Amélioration du message d'erreur "trop de requêtes" [#1820](https://github.com/proconnect-gouv/proconnect-identite/pull/1820).
- Ajout d'un délai de modération [#1819](https://github.com/proconnect-gouv/proconnect-identite/pull/1819).

### Évolutions techniques
- Amélioration des performances de la recherche d'organisations suggérées [#1780](https://github.com/proconnect-gouv/proconnect-identite/pull/1780).
- Suppression de l'API admin [#1824](https://github.com/proconnect-gouv/proconnect-identite/pull/1824).
- Suppression du champ "comments" de la table des modérations [#1822](https://github.com/proconnect-gouv/proconnect-identite/pull/1822).
- Remplacement de `Zod .merge` par `.extend(A.shape)` [#1823](https://github.com/proconnect-gouv/proconnect-identite/pull/1823).
- Ajout de tests E2E pour la certification des dirigeants avec un flux de suggestion [#1775](https://github.com/proconnect-gouv/proconnect-identite/pull/1775).
- Ajout de tests pour le type de vérification de l'utilisateur [#1759](https://github.com/proconnect-gouv/proconnect-identite/pull/1759).
- Mise à jour des dépendances : hono, @hono/node-server, nodemailer, cypress-io/github-action, actions/upload-artifact, redis, minimatch.
- Mise à jour des actions GitHub : docker/login-action, docker/setup-buildx-action, docker/metadata-action, docker/setup-qemu-action.
- Le workflow de mise à jour du lockfile s'exécute désormais mensuellement [#1834](https://github.com/proconnect-gouv/proconnect-identite/pull/1834).
- Ajout d'une contrainte "not null" pour le type de vérification [#1784](https://github.com/proconnect-gouv/proconnect-identite/pull/1784).

### Autres changements
- Ajout d'un fichier `SECURITY.md` pour la politique de sécurité [#1810](https://github.com/proconnect-gouv/proconnect-identite/pull/1810).
- Suppression de Crisp [#1805](https://github.com/proconnect-gouv/proconnect-identite/pull/1805).
- Suppression de l'option 2FA [#1809](https://github.com/proconnect-gouv/proconnect-identite/pull/1809).
- Ajout de labels de portée manquants dans le fichier `.github/labeler.yml` [#1807](https://github.com/proconnect-gouv/proconnect-identite/pull/1807).
- Correction de la politique de sécurité pour le signalement des vulnérabilités [#1798](https://github.com/proconnect-gouv/proconnect-identite/pull/1798).
- Suppression de l'input de rôle sur la page de complétion du profil [#1800](https://github.com/proconnect-gouv/proconnect-identite/pull/1800).
- Mise à jour de l'icône de la section d'aide [#1773](https://github.com/proconnect-gouv/proconnect-identite/pull/1773).
