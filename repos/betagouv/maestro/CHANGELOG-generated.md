## Changelog : maestro (30 derniers jours, au 2026-07-13)

### Résumé
Cette version apporte des améliorations significatives à la gestion des analyses, des prélèvements et des documents, notamment dans les domaines de la gestion des laboratoires, des analyses DAOA, et de l'export des données. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Gestion des laboratoires :
    - Amélioration de l'autocomplete pour la sélection du laboratoire lors de la création d'un prélèvement [#1196](https://github.com/betagouv/maestro/issues/1196).
    - Correction de l'affichage des laboratoires pour les coordinateurs régionaux [#1184](https://github.com/betagouv/maestro/issues/1184).
    - Correction du menu déroulant des laboratoires agréés qui sortait de l'écran [#1145](https://github.com/betagouv/maestro/issues/1145).
- Analyse et données :
    - Gestion de la réception des analyses DAOA [#1149](https://github.com/betagouv/maestro/issues/1149).
    - Stockage de tous les résidus inconnus dès la réception de l'analyse [#1169](https://github.com/betagouv/maestro/issues/1169).
    - Amélioration de l'affichage des cartes du dashboard [#1179](https://github.com/betagouv/maestro/issues/1179).
    - Correction du calcul des pourcentages sur le dashboard [#1188](https://github.com/betagouv/maestro/issues/1188) et [#1189](https://github.com/betagouv/maestro/issues/1189).
    - Ajout d'un bandeau d'alerte pour les dépassements de LMR (Limites Maximales de Résidus) dans le cadre du programme SEVES [#1074](https://github.com/betagouv/maestro/issues/1074).
    - Possibilité de repasser des DAI (Demandes d'Analyse Initiale) en erreur pour les relancer [#1063](https://github.com/betagouv/maestro/issues/1063).
- Documents :
    - Les utilisateurs avec le rôle "Suivi national" peuvent supprimer des documents [#1114](https://github.com/betagouv/maestro/issues/1114).
    - Correction de l'affichage des erreurs liées à la taille maximale des documents [#1122](https://github.com/betagouv/maestro/issues/1122).
- Divers :
    - Amélioration des libellés dans l'administration [#1165](https://github.com/betagouv/maestro/issues/1165).
    - Correction de l'ajout d'options pour les descripteurs [#1180](https://github.com/betagouv/maestro/issues/1180).
    - Correction de l'ordre de l'onglet agréments laboratoire [#1145](https://github.com/betagouv/maestro/issues/1145).
    - Correction de l'affichage des informations de conformité dans l'export [#1078](https://github.com/betagouv/maestro/issues/1078).

### Évolutions techniques
- Refactor de l'implémentation du header avec un nouveau design [#1127](https://github.com/betagouv/maestro/issues/1127).
- Séparation des routes des documents de prélèvements et des ressources [#1123](https://github.com/betagouv/maestro/issues/1123).
- Utilisation d'un outil de génération d'URL pour l'export des données du labcam [#1128](https://github.com/betagouv/maestro/issues/1128).
- Mise à jour de plusieurs dépendances (voir section "Autres changements").
- Correction de l'implémentation de la CSP (Content Security Policy) pour Sentry [#1176](https://github.com/betagouv/maestro/issues/1176).

### Autres changements
- Mises à jour de dépendances : de nombreuses dépendances ont été mises à jour pour bénéficier des dernières corrections de bugs et améliorations de sécurité. Ces mises à jour sont gérées par Dependabot et ne sont pas listées individuellement ici.
- Nettoyage du code et corrections de tests.
- Correction de la configuration du backup Restic [#1155](https://github.com/betagouv/maestro/issues/1155).
- Correction d'un warning lors du déploiement sur Scalingo [#1178](https://github.com/betagouv/maestro/issues/1178).
- Suppression d'une erreur dans la console liée à l'évaluation d'un "eval" [#1177](https://github.com/betagouv/maestro/issues/1177).
- Suppression d'un décalage sur la ligne "Total" de l'export de la programmation [#1185](https://github.com/betagouv/maestro/issues/1185).
- Correction d'un test qui clignotait [#1172](https://github.com/betagouv/maestro/issues/1172).
- Revert d'une fonctionnalité Sacha [#1154](https://github.com/betagouv/maestro/issues/1154).
