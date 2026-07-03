## Changelog : dahlia (30 derniers jours, au 01 juillet 2026)

### Résumé
Le projet Dahlia a connu un mois de juin riche en améliorations, axées sur l'expérience utilisateur, la robustesse du système et l'automatisation des tâches. Les principales évolutions concernent l'ajout de nouvelles fonctionnalités comme le téléchargement de listes de dossiers, l'édition des métadonnées des pièces, et des améliorations significatives du scrapping et de la recherche. L'infrastructure a également été renforcée avec une meilleure gestion des dépendances et l'intégration du SSO ProConnect.

### Évolutions fonctionnelles
- Ajout d'un bouton pour télécharger la liste des dossiers [#57](https://github.com/MTES-MCT/dahlia/issues/57).
- Possibilité d'éditer les métadonnées des pièces jointes à un dossier [#51](https://github.com/MTES-MCT/dahlia/issues/51).
- Amélioration de la recherche et du tri des dossiers et des pièces [#19](https://github.com/MTES-MCT/dahlia/issues/19), [#22](https://github.com/MTES-MCT/dahlia/issues/22).
- Ajout d'un bandeau d'alerte pour indiquer l'environnement (non-production) [#20](https://github.com/MTES-MCT/dahlia/issues/20).
- Ajout d'un badge "très urgent" pour signaler la criticité des dossiers [#21](https://github.com/MTES-MCT/dahlia/issues/21).
- Amélioration de la gestion des tableaux avec une meilleure organisation [#53](https://github.com/MTES-MCT/dahlia/issues/53).
- Affichage des pièces anonymisées dans tous les environnements, sauf en production [#55](https://github.com/MTES-MCT/dahlia/issues/55).
- Script pour télécharger les fichiers et bouton de rafraîchissement des dossiers, avec gestion des dossiers supprimés [#16](https://github.com/MTES-MCT/dahlia/issues/16).
- Ajout de détails dans les dossiers pour une meilleure information [#13](https://github.com/MTES-MCT/dahlia/issues/13).
- Ajout de la date de délétion des dossiers [#40](https://github.com/MTES-MCT/dahlia/issues/40).
- Ajout de la colonne "dernier producteur" pour identifier l'équipe responsable [#44](https://github.com/MTES-MCT/dahlia/issues/44).

### Évolutions techniques
- Intégration du SSO ProConnect pour l'authentification [#7](https://github.com/MTES-MCT/dahlia/issues/7).
- Amélioration du scrapping pour une meilleure récupération des données et gestion des erreurs temporaires [#6](https://github.com/MTES-MCT/dahlia/issues/6), [#8](https://github.com/MTES-MCT/dahlia/issues/8).
- Mise en place d'une synchronisation nocturne des données [#12](https://github.com/MTES-MCT/dahlia/issues/12).
- Refonte de la configuration de Dependabot pour une gestion plus efficace des dépendances [#30](https://github.com/MTES-MCT/dahlia/issues/30), [#36](https://github.com/MTES-MCT/dahlia/issues/36).
- Mise à jour massive des dépendances pour bénéficier des dernières corrections et améliorations [#45](https://github.com/MTES-MCT/dahlia/issues/45).
- Réorganisation des tests unitaires et d'intégration pour une meilleure couverture et maintenabilité [#56](https://github.com/MTES-MCT/dahlia/issues/56).
- Correction d'un problème de déconnexion intempestive après authentification [#10](https://github.com/MTES-MCT/dahlia/issues/10).
- Ajout de permissions pour la CI afin de garantir la sécurité des déploiements [#48](https://github.com/MTES-MCT/dahlia/issues/48).
- Mise en place de la création de releases et du déploiement en production [#17](https://github.com/MTES-MCT/dahlia/issues/17).

### Autres changements
- Mise à jour de la documentation INVESTIGATION [#37](https://github.com/MTES-MCT/dahlia/issues/37).
- Amélioration de la gestion du header et des filtres [#23](https://github.com/MTES-MCT/dahlia/issues/23).
- Mise en forme du code avec Prettier et Linter pour une meilleure lisibilité [#15](https://github.com/MTES-MCT/dahlia/issues/15).
- Correction de l'anonymisation incomplète des données [#11](https://github.com/MTES-MCT/dahlia/issues/11).
- Anonymisation du scrapping en fonction de l'environnement [#14](https://github.com/MTES-MCT/dahlia/issues/14).
