## Changelog : karfur (30 derniers jours, au 8 juillet 2026)

### Résumé
Les dernières mises à jour de karfur se concentrent sur l'amélioration de l'intégration avec l'outil AGIR, notamment la synchronisation des opérateurs et l'affichage de leurs coordonnées sur la carte. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées, ainsi que des optimisations techniques pour le déploiement et la sécurité.

### Évolutions fonctionnelles
- Amélioration de l'affichage des niveaux de français sur l'interface utilisateur [#3835](https://github.com/refugies-info/karfur/pull/3835).
- Amélioration du maillage sémantique des mots-clés [#3836](https://github.com/refugies-info/karfur/pull/3836).
- Surlignage des adresses emails sur les fiches RCO [#3822](https://github.com/refugies-info/karfur/pull/3822).
- Mise à jour du texte sur la page "Mission et Impact" [#3824](https://github.com/refugies-info/karfur/pull/3824).
- Correction de l'affichage responsive des wordings statiques sur mobile [#3813](https://github.com/refugies-info/karfur/pull/3813).
- Mise à jour des coordonnées des opérateurs sur la carte AGIR [#3817](https://github.com/refugies-info/karfur/pull/3817).
- Ajout d'une icône de lien externe aux adresses mail [#3817](https://github.com/refugies-info/karfur/pull/3817).

### Évolutions techniques
- Intégration de la synchronisation des opérateurs AGIR depuis Grist, avec gestion des erreurs et mise à jour des messages.
- Ajout d'un déclenchement admin pour la synchronisation AGIR.
- Préparation de la synchronisation automatique des opérateurs AGIR (lot 2 à venir).
- Amélioration de la copie de l'application construite pour inclure les chunks nécessaires au build Docker.
- Ajout de secrets pour l'API Grist dans la configuration Cloud Build.
- Mise en place d'un workflow CI/CD avec Letta Code pour l'auto-review des PR.
- Correction de la configuration de Letta Code pour l'installation de l'application GitHub.
- Mise à jour de la documentation sur la synchronisation des opérateurs AGIR.
- Ajout de documents de synchronisation des opérateurs AGIR depuis Grist.

### Autres changements
- Suppression de la configuration Claude.
- Correction de typos et amélioration de la lisibilité du code.
- Suppression de div vides.
- Mise à jour de la documentation.
- Correction de la syntaxe des diagrammes Mermaid dans la documentation.
- Suppression de console.log inutiles.
- Correction de problèmes de traduction et de clés manquantes.
- Suppression de références obsolètes à lodash.
- Ajout d'un hook pre-commit GitLeaks pour la détection de secrets.
- Mise à jour des dépendances de sécurité.
