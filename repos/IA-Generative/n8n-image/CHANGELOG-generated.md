## Changelog : n8n-image (30 derniers jours, au 28 mai 2026)

### Résumé
Ce projet a connu des améliorations significatives concernant la gestion des versions de ses images Docker, notamment pour n8n et Playwright. Les mises à jour visent à stabiliser le processus de construction des images et à faciliter l'utilisation des dernières versions des composants clés. Des optimisations du pipeline CI/CD ont également été apportées.

### Évolutions fonctionnelles
- Mise à jour de la version de n8n-runners à la version 2.17.5 [#1234](https://github.com/IA-Generative/n8n-image/issues/1234).
- Amélioration de la version du nœud Playwright intégré à la version 1.1.1, puis 1.1.0.
- Ajout d'un fichier README pour une meilleure documentation.

### Évolutions techniques
- Factorisation de la version de l'image Playwright et de n8n dans des fichiers `.env` pour une gestion centralisée et simplifiée des versions.
- Optimisation du pipeline CI/CD GitLab pour assurer une construction correcte des images à chaque commit.
- Suppression du fichier `package-lock.json` dans le répertoire des nœuds [#42](https://github.com/IA-Generative/n8n-image/pull/42).
- Modification du fichier `.gitlab-ci-dso.yml` pour s'appuyer sur la version de `playwright-core` [#41](https://github.com/IA-Generative/n8n-image/pull/41).
- Modification du fichier `build-images.yaml` pour intégrer et utiliser la version de `playwright-core` [#40](https://github.com/IA-Generative/n8n-image/pull/40).
- Correction du build de l'image Playwright dans le pipeline CI/CD.
- Fusion de la branche `main` dans `develop`.
