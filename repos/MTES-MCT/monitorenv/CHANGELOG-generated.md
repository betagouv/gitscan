## Changelog : monitorenv (30 derniers jours, au 21 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des missions, notamment au niveau de la sélection des unités de contrôle, de la gestion des dates et de l'ajout d'informations complémentaires aux navires. Des corrections ont également été apportées pour améliorer la fiabilité des données affichées dans les rapports et les visualisations, ainsi que pour optimiser l'expérience utilisateur globale.

### Évolutions fonctionnelles
- Possibilité d'ajouter des informations et des fichiers supplémentaires aux navires.
- Amélioration de la gestion des dates dans la liste des missions et les rapports.
- Correction d'un bug empêchant la sélection de la même unité de contrôle plusieurs fois dans une mission.
- Ajout de tags aux missions pour une meilleure organisation et filtrage.
- Les missions peuvent être mises à jour à partir des données de rapportnav [#40bbc44](https://github.com/MTES-MCT/monitorenv/commit/40bbc44).
- Amélioration de l'affichage des noms de façade (maintenant appelés "zone maritime") dans les panneaux.
- Correction du retour des noms de façade distincts via l'API seafront [#5440c30](https://github.com/MTES-MCT/monitorenv/commit/5440c30).
- Ajout de la validation du nom complet des tags de mission.
- Amélioration de la gestion des tags de mission, notamment lors de la création et de la mise à jour.

### Évolutions techniques
- Refactorisation du code lié aux façades (renommées en "zone maritime") pour utiliser l'API dédiée.
- Utilisation du composant FileUploader de monitor-ui pour la gestion des fichiers.
- Correction de l'utilisation de `ST_MakeValid` pour le calcul des zones maritimes [#89726c5](https://github.com/MTES-MCT/monitorenv/commit/89726c5).
- Amélioration de la gestion des données externes modifiées lors de la sauvegarde d'une mission [#d658689](https://github.com/MTES-MCT/monitorenv/commit/d658689).
- Ajout d'un debounce pour le filtre de recherche des missions afin d'optimiser les performances.
- Correction de l'actualisation des données des tableaux lors du changement d'onglet.

### Autres changements
- Corrections de divers bugs et améliorations de l'expérience utilisateur (UX).
- Corrections de tests unitaires et d'intégration (Cypress, Pytest).
- Correction de bugs liés à la mise à jour des zones réglementaires CACEM.
- Correction de l'affichage des dates dans les rapports.
- Correction de l'affichage du nombre de personnes concernées dans les missions.
- Correction de l'affichage des tags de mission en fonction de la date de début de la mission ou de l'action.
