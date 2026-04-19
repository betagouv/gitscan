## Changelog : partaj (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les évolutions de Partaj se concentrent sur l'amélioration de l'expérience utilisateur, notamment en matière de notifications et de consultation des saisines. Des corrections et des améliorations ont été apportées au suivi des pièces jointes et à la gestion des versions de projet. L'infrastructure a également été renforcée avec l'ajout d'une intégration GitLab CI.

### Évolutions fonctionnelles
- Les co-demandeurs sont désormais notifiés de l’envoi d’une saisine. [#10](https://github.com/MTES-MCT/partaj/issues/10)
- Un bouton "Consulter la saisine" a été ajouté pour faciliter l'accès aux informations pertinentes. [#12](https://github.com/MTES-MCT/partaj/issues/12)
- Les chargés d’études sont notifiés de l’ajout d’une nouvelle version de projet de réponse par le supérieur hiérarchique. [#8](https://github.com/MTES-MCT/partaj/issues/8)
- Amélioration de la gestion des pièces jointes : correction de bugs, amélioration de l'affichage et de l'enregistrement des pièces jointes.
- Pagination de la base de connaissance avec un composant React DSFR. [#13](https://github.com/MTES-MCT/partaj/issues/13)
- Ajout d'icônes DSFR pour améliorer l'interface utilisateur. [#13](https://github.com/MTES-MCT/partaj/issues/13)

### Évolutions techniques
- Intégration de GitLab CI pour améliorer le processus d'intégration continue et de déploiement.
- Refactorisation du code pour supprimer les importations inutiles.
- Mise à jour de la configuration pour supprimer l'utilisation d'un mode "offline" en développement.
- Mise en place d'une version compatible avec Elastic Search et Scalingo.
- Modification des tests pour assurer la stabilité et la fiabilité des nouvelles fonctionnalités.

### Autres changements
- Le bouton de support a été modifié pour ouvrir un lien externe au lieu d'utiliser Crisp.
- Application de `isort` pour uniformiser le code.
