## Changelog : dossierfacile-backend (30 derniers jours, au 05/11/2026)

### Résumé
Les récentes évolutions se sont concentrées sur l'amélioration des outils de gestion pour le support et le backoffice, notamment concernant la validation des revenus et le traitement des dossiers. Des corrections ont également été apportées pour garantir la cohérence des données des garants et la fiabilité de la génération des documents PDF. La version 3.6.0 a été déployée.

### Évolutions fonctionnelles
- **Gestion du support** : Possibilité pour l'équipe support de traiter des dossiers déjà complétés [#1341](https://github.com/MTES-MCT/dossierfacile-backend/issues/1341).
- **Optimisation du Backoffice** : Amélioration de la gestion des revenus pour les locataires et les garants, incluant une meilleure validation et l'autorisation de montants nuls [#1336](https://github.com/MTES-MCT/dossierfacile-backend/issues/1336), [#1337](https://github.com/MTES-MCT/dossierfacile-backend/issues/1337).
- **Fiabilité des données et documents** : Harmonisation des données relatives aux garants et à la résidence, et correction du processus de génération de fichiers PDF [#1334](https://github.com/MTES-MCT/dossierfacile-backend/issues/1334).

### Évolutions techniques
- **Migration** : Migration de la fonctionnalité "demo partner" vers le backend [#1340](https://github.com/MTES-MCT/dossierfacile-backend/issues/1340).
- **Refactoring** : Optimisation du code pour la création d'utilisateurs [#1339](https://github.com/MTES-MCT/dossierfacile-backend/issues/1339).
- **Observabilité** : Ajustement des seuils d'alerte Elastalert pour un meilleur monitoring [#1335](https://github.com/MTES-MCT/dossierfacile-backend/issues/1335).
- **Release** : Passage à la version 3.6.0.

### Autres changements
- **Expérience développeur** : Ajout d'une tâche VS Code permettant de lancer simultanément les applications backend et frontend.
