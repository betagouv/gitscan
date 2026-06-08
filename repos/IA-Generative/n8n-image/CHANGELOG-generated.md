## Changelog : n8n-image (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilisation et la flexibilité du processus de construction des images Docker pour n8n. Plusieurs mises à jour de versions de composants clés ont été effectuées, notamment n8n, n8n-runners et Playwright, pour bénéficier des dernières corrections et fonctionnalités. Des modifications de configuration ont été apportées pour faciliter la gestion des versions et améliorer la robustesse du build.

### Évolutions fonctionnelles
- Mise à jour de la version de n8n à la version 2.17.5 [#dfd9cff](https://github.com/IA-Generative/n8n-image/commit/dfd9cff).
- Mise à jour de la version de n8n-runners à la version 2.17.5 [#0c15063](https://github.com/IA-Generative/n8n-image/commit/0c15063).
- Amélioration de l'intégration du nœud Playwright avec la version 1.1.1 puis 1.1.0 [#b353b97](https://github.com/IA-Generative/n8n-image/commit/b353b97), [#725ffed](https://github.com/IA-Generative/n8n-image/commit/725ffed).

### Évolutions techniques
- Factorisation de la version de l'image Playwright et de n8n dans des fichiers `.env` pour une gestion plus centralisée et simplifiée [#1e848e2](https://github.com/IA-Generative/n8n-image/commit/1e848e2), [#def8252](https://github.com/IA-Generative/n8n-image/commit/def8252).
- Modification du fichier `.gitlab-ci-dso.yml` pour améliorer le processus de build [#6dbe556](https://github.com/IA-Generative/n8n-image/commit/6dbe556).
- Modification du fichier `build-images.yaml` pour s'appuyer sur la version de `playwright-core` [#c960f71](https://github.com/IA-Generative/n8n-image/commit/c960f71).
- Correction du build lors d'un commit push [#6fe4783](https://github.com/IA-Generative/n8n-image/commit/6fe4783).

### Autres changements
- Suppression du fichier `nodes/package-lock.json` [#c393ebf](https://github.com/IA-Generative/n8n-image/commit/c393ebf).
- Ajout d'un fichier README [#1e848e2](https://github.com/IA-Generative/n8n-image/commit/1e848e2).
