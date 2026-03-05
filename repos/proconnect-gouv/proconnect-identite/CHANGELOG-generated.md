## Changelog : proconnect-identite (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à ProConnect Identité au cours des 30 derniers jours. Les modifications incluent des corrections de bugs, des améliorations de l'interface utilisateur, des optimisations de performance et des mises à jour de sécurité. Des fonctionnalités ont été ajoutées pour faciliter la gestion des organisations et améliorer l'expérience utilisateur lors de l'authentification, notamment avec FranceConnect.

### Évolutions fonctionnelles
- Possibilité de choisir parmi plusieurs mairies [#1728](https://github.com/proconnect-gouv/proconnect-identite/pull/1728).
- Amélioration de l'algorithme pour déterminer si une organisation est unipersonnelle, corrigeant un bug [#1746](https://github.com/proconnect-gouv/proconnect-identite/pull/1746).
- Ajout d'une alerte en cas d'indisponibilité de l'API Sirene [#1724](https://github.com/proconnect-gouv/proconnect-identite/pull/1724) (révertée depuis).
- Restauration des informations utilisateur obligatoires lors de l'authentification FranceConnect [#1738](https://github.com/proconnect-gouv/proconnect-identite/pull/1738).
- Ajout d'un délai de modération [#1819](https://github.com/proconnect-gouv/proconnect-identite/pull/1819).
- Ajout d'une nouvelle catégorie juridique pour les associations de droit local (Bas-Rhin, Haut-Rhin et Moselle) [#1821](https://github.com/proconnect-gouv/proconnect-identite/pull/1821).
- Suppression de l'option 2FA (authentification à deux facteurs) [#1809](https://github.com/proconnect-gouv/proconnect-identite/pull/1809).
- Ajout d'une barre de progression pour remplacer le stepper [#1811](https://github.com/proconnect-gouv/proconnect-identite/pull/1811).
- Amélioration de la nouvelle version du tunnel de la mairie [#1822](https://github.com/proconnect-gouv/proconnect-identite/pull/1822).
- Ajout d'un badge "certifié" pour les organisations certifiées sur la page d'accueil du dirigeant [#1822](https://github.com/proconnect-gouv/proconnect-identite/pull/1822).

### Évolutions techniques
- Simplification du logger d'événements de débogage [#1747](https://github.com/proconnect-gouv/proconnect-identite/pull/1747).
- Migration de la vérification des petites associations vers le domaine lorsque l'email est vérifié [#1760](https://github.com/proconnect-gouv/proconnect-identite/pull/1760).
- Ajout du champ "status" au cron Metabase [#1739](https://github.com/proconnect-gouv/proconnect-identite/pull/1739).
- Les modérations sont créées avec un statut "en attente" [#1740](https://github.com/proconnect-gouv/proconnect-identite/pull/1740).
- Correction d'un problème où les commentaires de statut bruts étaient perdus [#1696](https://github.com/proconnect-gouv/proconnect-identite/pull/1696).
- Refactorisation du code pour remplacer `Zod .merge` par `Zod .extend(A.shape)` [#1823](https://github.com/proconnect-gouv/proconnect-identite/pull/1823).
- Suppression du champ "comments" de l'exportation de la table des modérations [#1822](https://github.com/proconnect-gouv/proconnect-identite/pull/1822).
- Harmonisation des exports du package `testing` [#1802](https://github.com/proconnect-gouv/proconnect-identite/pull/1802).
- Ajout de tests E2E pour les organisations multiples avec certification [#1782](https://github.com/proconnect-gouv/proconnect-identite/pull/1782).
- Ajout de tests pour l'exécution de la connexion avec le legacy ACR sur CI [#1789](https://github.com/proconnect-gouv/proconnect-identite/pull/1789).
- Ajout de tests pour l'exécution de la connexion avec suggestion sur CI [#1791](https://github.com/proconnect-gouv/proconnect-identite/pull/1791).

### Autres changements
- Mise à jour de la politique de sécurité pour le signalement des vulnérabilités [#1810](https://github.com/proconnect-gouv/proconnect-identite/pull/1810).
- Ajout d'un fichier `SECURITY.md` [#1800](https://github.com/proconnect-gouv/proconnect-identite/pull/1800).
- Mises à jour de dépendances : `redis`, `koa`, `nodemailer`, `cypress-io/github-action`, `hono`, `qs`, `axios`, `minimatch`, `sentry`, `pkgroll`, `moment-timezone`.
- Mise à jour des fichiers de verrouillage des dépendances (package-lock.json).
- Amélioration de la documentation et du code.
