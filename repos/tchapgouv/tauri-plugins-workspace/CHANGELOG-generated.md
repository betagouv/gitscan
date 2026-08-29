## Changelog : tauri-plugins-workspace (30 derniers jours, au 27 août 2026)

### Résumé
Ce mois-ci, les plugins ont bénéficié d'une meilleure connectivité réseau grâce à l'intégration du support des proxys système. Des correctifs importants ont également été apportés pour stabiliser le déploiement sur Android et la gestion des permissions de fichiers.

### Évolutions fonctionnelles
- Ajout de la prise en charge du proxy système pour les modules HTTP ([#3528](https://github.com/tchapgouv/tauri-plugins-workspace/issues/3528)) et Updater ([#3526](https://github.com/tchapgouv/tauri-plugins-workspace/issues/3526)).
- Correction d'un problème de compilation sur Android dû à un fichier de règles manquant ([#3531](https://github.com/tchapgouv/tauri-plugins-workspace/issues/3531)).
- Correction de la gestion des permissions par défaut pour le module de système de fichiers (fs) ([#3507](https://github.com/tchapgouv/tauri-plugins-workspace/issues/3507)).

### Évolutions techniques
- Renforcement de la sécurité des workflows CI/CD par l'ajout de permissions explicites pour les jetons (tokens).

### Autres changements
- Mise à jour de la documentation concernant les fonctionnalités Cargo ([#3527](https://github.com/tchapgouv/tauri-plugins-workspace/issues/3527)).
- Nettoyage du code par la suppression de fonctionnalités de production obsolètes ([#3525](https://github.com/tchapgouv/tauri-plugins-workspace/issues/3525)).
