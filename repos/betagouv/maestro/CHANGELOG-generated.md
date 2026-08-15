## Changelog : maestro (30 derniers jours, au 13 août 2026)

### Résumé
Ce mois-ci, Maestro a franchi des étapes importantes dans l'automatisation des échanges avec les laboratoires (lecture de rapports PDF, gestion SFTP et réponses emails automatiques) et dans l'autonomie des coordinateurs pour la gestion de leurs utilisateurs. L'outil est également devenu plus performant grâce à une meilleure gestion de la mémoire et propose des outils de pilotage enrichis avec de nouvelles statistiques et des filtres de recherche.

### Évolutions fonctionnelles
- **Gestion des utilisateurs** : Les coordinateurs disposent désormais de la possibilité de gérer directement leurs propres utilisateurs [#1280](https://github.com/betagouv/maestro/issues/1280).
- **Intégration et données laboratoires** :
    - Lecture automatisée des rapports PDF provenant des LNR [#1304](https://github.com/betagouv/maestro/issues/1304).
    - Amélioration de la gestion des transferts SFTP lors de l'envoi de DAI (gestion du fichier déclencheur) [#1289](https://github.com/betagouv/maestro/issues/1289).
    - Optimisation du traitement des données provenant de divers laboratoires (Inovalys, Girpa, Cereco) et harmonisation de l'extraction des références Maestro [#1276, #1275, #1265, #1264, #1247](https://github.com/betagouv/maestro/issues/1247).
    - Ajout de la substance active *cyprosulfamide* au référentiel [#1246](https://github.com/betagouv/maestro/issues/1246).
    - Envoi automatique d'une réponse par email au laboratoire en cas d'adresse incorrecte [#1305](https://github.com/betagouv/maestro/issues/1305).
- **Pilotage et interface utilisateur** :
    - Ajout de nouvelles statistiques sur le tableau de bord [#949](https://github.com/betagouv/maestro/issues/949).
    - Ajout d'un filtre sur la date d'envoi de la DAI pour faciliter les recherches [#1231](https://github.com/betagouv/maestro/issues/1231).
    - Améliorations ergonomiques : affichage des détails de prélèvement, ouverture par défaut des accordéons d'échantillons, correction de l'affichage des noms de documents et de l'historique des rapports [#1288, #1229, #1232, #1230, #1155](https://github.com/betagouv/maestro/issues/1155).

### Évolutions techniques
- **Performance** : La mise à jour des départements est passée en mode non automatique afin de réduire la consommation de mémoire vive (RAM) du système [#1260](https://github.com/betagouv/maestro/issues/1260).
- **Qualité et Build** :
    - Refactorisation du code pour centraliser l'extraction des références Maestro [#1247](https://github.com/betagouv/maestro/issues/1247).
    - Nettoyage des avertissements (warnings) lors du processus de build Vite [#1261](https://github.com/betagouv/maestro/issues/1261).
