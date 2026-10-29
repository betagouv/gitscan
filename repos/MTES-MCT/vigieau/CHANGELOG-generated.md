## Changelog : vigieau (30 derniers jours, au 28 octobre 2026)

### Résumé
Les récentes évolutions se sont concentrées sur la fiabilisation des données statistiques et la correction de la gestion des zones de restrictions d'eau. Parallèlement, une mise à jour de sécurité importante a été déployée pour protéger l'infrastructure contre les vulnérabilités récentes.

### Évolutions fonctionnelles
- **Fiabilisation des données** : Correction des statistiques de surface départementale, des données d'audience et restauration de collections ainsi que des abonnements par adresse manquants.
- **Gestion des zones de restrictions** : 
    - Amélioration de la distinction entre les conflits de zones superposées et les erreurs serveur.
    - Prise en compte des zones superposées présentant des restrictions équivalentes ([#83](https://github.com/MTES-MCT/vigieau/pull/83)).

### Évolutions techniques
- **Sécurité** : Mise à jour critique des dépendances (Node.js, npm, deepmerge) pour répondre aux correctifs de sécurité d'octobre.
- **Infrastructure et Framework** : Montée de version vers Nuxt 4 et npm 12.
- **Tests** : Renforcement de la couverture des tests de régression de sécurité, notamment sur le parsing multipart et la gestion des sorties CLI.
