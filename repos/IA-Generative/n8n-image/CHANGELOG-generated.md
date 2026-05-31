## Changelog : n8n-image (30 derniers jours, au 28 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées au projet n8n-image au cours du dernier mois. Les modifications se concentrent sur la stabilisation du processus de construction des images Docker, l'amélioration de la gestion des versions de n8n et Playwright, et l'ajout d'une meilleure documentation. Ces changements visent à faciliter le déploiement et l'utilisation de n8n avec des fonctionnalités étendues.

### Évolutions fonctionnelles
- Amélioration de la construction des images Docker pour une plus grande fiabilité, notamment lors des commits.
- Mise à jour de la version de n8n-runners vers la version 2.17.5 [#42](https://github.com/IA-Generative/n8n-image/pull/42).
- Mise à jour de la version du nœud Playwright vers 1.1.1 et 1.1.0.
- Ajout d'un fichier README pour une meilleure documentation du projet [#42](https://github.com/IA-Generative/n8n-image/pull/42).

### Évolutions techniques
- Factorisation de la version de l'image Playwright et de n8n dans des fichiers `.env` pour une gestion centralisée et simplifiée des versions.
- Modification du fichier `.gitlab-ci-dso.yml` pour améliorer le processus de CI/CD [#41](https://github.com/IA-Generative/n8n-image/pull/41).
- Modification du fichier `build-images.yaml` pour s'appuyer sur la version de `playwright-core` [#40](https://github.com/IA-Generative/n8n-image/pull/40).
- Suppression du fichier `nodes/package-lock.json` pour simplifier la structure du projet [#40](https://github.com/IA-Generative/n8n-image/pull/40).
- Correction du build de l'image Playwright dans le CI GitLab.
- Fusion de la branche `main` dans `develop`.
