## Changelog : fluo-proto (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la modernisation de l'infrastructure de déploiement des prototypes, en particulier pour l'annuaire et les prototypes REA/SPS.  Les prototypes sont désormais déployés comme des conteneurs serverless, ce qui améliore la scalabilité et la maintenance. Des améliorations de sécurité ont également été apportées en supprimant les mots de passe PostgreSQL codés en dur.

### Évolutions fonctionnelles
- L'annuaire a été amélioré avec l'ajout de filtres côté client et la possibilité d'exporter les données statiquement pour GitHub Pages [#1](https://github.com/gip-inclusion/fluo-proto/pull/1), [#2](https://github.com/gip-inclusion/fluo-proto/pull/2), [#3](https://github.com/gip-inclusion/fluo-proto/pull/3), [#4](https://github.com/gip-inclusion/fluo-proto/pull/4).
- Correction des URLs et de la provision pour l'API SCW, qui utilisait des noms de domaine incorrects [#12](https://github.com/gip-inclusion/fluo-proto/pull/12).

### Évolutions techniques
- Les prototypes sont désormais déployés en tant que conteneurs serverless, abandonnant l'export statique via GitHub Pages pour l'annuaire [#6](https://github.com/gip-inclusion/fluo-proto/pull/6).
- Suppression des mots de passe PostgreSQL codés en dur, en utilisant désormais la variable d'environnement `DATABASE_URL` pour la connexion à la base de données.
- Mise à jour de la signature des appels `TemplateResponse` pour la compatibilité avec Starlette 1.x.
- Correction des scripts de déploiement SPS/REA pour utiliser la commande `redeploy` de l'API SCW et une sélection plus précise des noms de conteneurs.
- Mises à jour de la CLI SCW pour la création de conteneurs (arguments `image`, `memory-limit-bytes`, `mvcpu-limit`).
- Suppression du prototype `/prototypes/flux`.

### Autres changements
- Configuration de Dependabot pour la gestion des dépendances (uv, docker, github-actions) [#1](https://github.com/gip-inclusion/fluo-proto/pull/1).
- Formatage du code Python dans le répertoire `annuaire` avec Ruff.
- Mises à jour de dépendances (Starlette, FastAPI, idna, astral-sh/setup-uv, actions) via Dependabot (non listées individuellement pour concision).
