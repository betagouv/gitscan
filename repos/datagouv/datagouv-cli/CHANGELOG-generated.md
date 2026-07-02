## Changelog : datagouv-cli (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, l'outil `datagouv-cli` a connu une refonte majeure. Le code de l'interface en ligne de commande a été migré du paquet `datagouv_client` vers ce dépôt, permettant une distribution plus autonome et des builds pour différents systèmes d'exploitation (macOS, Windows).  Des améliorations ont été apportées à la documentation et aux processus de construction pour faciliter la maintenance et la publication de nouvelles versions.

### Évolutions fonctionnelles
- Le nom de la commande CLI a été corrigé pour être `datagouv` au lieu de `datagouv-cli` [#1234](https://github.com/datagouv/datagouv-cli/issues/1234).
- Ajout de la prise en charge de la construction pour Windows.
- Intégration de Homebrew pour macOS, permettant une installation facile via le gestionnaire de paquets.

### Évolutions techniques
- Migration du code CLI depuis `datagouv_client` vers ce dépôt, permettant une gestion indépendante.
- Utilisation de `datagouv-client` version 0.5.0 comme dépendance.
- Refonte du processus de construction pour macOS avec un layout "onedir" pour PyInstaller, améliorant la portabilité.
- Ajout de pre-commit pour formater le code et assurer la cohérence.
- Amélioration des noms des workflows CI pour une meilleure clarté.
- Ajout d'une étape `brew trust` pour macOS afin de faciliter l'installation.

### Autres changements
- Réorganisation et mise à jour de la documentation README et RELEASING.md.
- Correction de typos dans les docstrings.
- Mise à jour de la description du projet dans la documentation.
- Initialisation du dépôt avec un scaffold de base.
- Correction de l'installation du bundle onedir après le changement de répertoire dans Homebrew.
