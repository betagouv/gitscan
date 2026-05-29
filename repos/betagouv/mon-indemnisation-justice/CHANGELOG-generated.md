## Changelog : mon-indemnisation-justice (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la refonte de l'application, notamment la migration vers des versions plus récentes de Symfony et Doctrine (8.0), l'amélioration de l'expérience utilisateur avec l'introduction d'étapes de saisie plus claires et la gestion des brouillons de dossiers, ainsi que des corrections de bugs et des améliorations de la sécurité. L'intégration de France Connect a également été améliorée avec une meilleure gestion des erreurs et un suivi via Sentry.

### Évolutions fonctionnelles
- Amélioration de la gestion des erreurs France Connect avec affichage de messages plus clairs et suivi via Sentry [#02a5a80](https://github.com/betagouv/mon-indemnisation-justice/commit/02a5a80).
- Introduction d'un système de brouillons pour les dossiers, permettant de sauvegarder les informations saisies et de les reprendre plus tard [#1c8d00b](https://github.com/betagouv/mon-indemnisation-justice/commit/1c8d00b).
- Création des étapes de saisie du dossier avec une interface utilisateur améliorée et des validations en temps réel [#e92aee5](https://github.com/betagouv/mon-indemnisation-justice/commit/e92aee5).
- Ajout de la possibilité de télécharger des pièces jointes avec prévisualisation [#492209e](https://github.com/betagouv/mon-indemnisation-justice/commit/492209e).
- Amélioration de l'affichage des informations sur les dossiers dans l'espace rédacteur [#f804ad4](https://github.com/betagouv/mon-indemnisation-justice/commit/f804ad4).
- Ajout de la gestion des personnes morales avec des champs spécifiques et l'affichage des informations correspondantes [#983a864](https://github.com/betagouv/mon-indemnisation-justice/commit/983a864).
- Implémentation d'une fonctionnalité d'autocomplétion pour le champ adresse [#fa556ec](https://github.com/betagouv/mon-indemnisation-justice/commit/fa556ec).
- Ajout de la possibilité de modifier les informations du dossier [#80116ad](https://github.com/betagouv/mon-indemnisation-justice/commit/80116ad).
- Correction de l'affichage de l'explication de la clôture sur la page "mes demandes" [#31fb116](https://github.com/betagouv/mon-indemnisation-justice/commit/31fb116).
- Ajout de la mention "Référence à rappeler" dans l'email de confirmation de dépôt [#b288a5c](https://github.com/betagouv/mon-indemnisation-justice/commit/b288a5c).

### Évolutions techniques
- Mise à jour de Symfony et Doctrine vers les versions 8.0 [#3fdeb3f](https://github.com/betagouv/mon-indemnisation-justice/commit/3fdeb3f).
- Suppression de l'utilisation d'API Platform [#c35c0d1](https://github.com/betagouv/mon-indemnisation-justice/commit/c35c0d1).
- Refonte de la gestion des routes API avec l'utilisation de Tanstack Router [#2d83035](https://github.com/betagouv/mon-indemnisation-justice/commit/2d83035).
- Simplification du mapping des données et suppression des classes de mapper [#5328499](https://github.com/betagouv/mon-indemnisation-justice/commit/5328499).
- Amélioration de la gestion des erreurs et ajout de logs avec Sentry [#ce93268](https://github.com/betagouv/mon-indemnisation-justice/commit/ce93268).
- Mise à jour de l'image Docker pour retirer APP_RUNTIME [#80fbfc6](https://github.com/betagouv/mon-indemnisation-justice/commit/80fbfc6).
- Correction de bugs liés à Doctrine [#b658ff5](https://github.com/betagouv/mon-indemnisation-justice/commit/b658ff5).
- Normalisation des adresses en base de données et en entrée [#20ec301](https://github.com/betagouv/mon-indemnisation-justice/commit/20ec301).
- Ajout de tests unitaires et end-to-end pour assurer la qualité du code [#4f806fb](https://github.com/betagouv/mon-indemnisation-justice/commit/4f806fb).

### Autres changements
- Mise à jour de la documentation des procédures de déclaration PN [#3988978](https://github.com/betagouv/mon-indemnisation-justice/commit/3988978).
- Installation de Crisp pour le support utilisateur [#5ccb161](https://github.com/betagouv/mon-indemnisation-justice/commit/5ccb161).
- Documentation du schéma de base de données [#f73e851](https://github.com/betagouv/mon-indemnisation-justice/commit/f73e851).
- Correction de typos et amélioration de la lisibilité du code [#cf1093f](https://github.com/betagouv/mon-indemnisation-justice/commit/cf1093f).
- Correction de plusieurs bugs mineurs et améliorations de la performance [#b83b7ca](https://github.com/betagouv/mon-indemnisation-justice/commit/b83b7ca).
- Ajout du SIRET de l'administration à l'agent [#7c59e9a](https://github.com/betagouv/mon-indemnisation-justice/commit/7c59e9a).
- Correction de l'affichage du badge "Declaration FDO" [#cd805a5](https://github.com/betagouv/mon-indemnisation-justice/commit/cd805a5).
- Ajustements post SF8 [#5a5597b](https://github.com/betagouv/mon-indemnisation-justice/commit/5a5597b).
- Correction d'un bug lié à la configuration obsolète de Doctrine en production [#b83b7ca](https://github.com/betagouv/mon-indemnisation-justice/commit/b83b7ca).
