## Changelog : monitorenv (30 derniers jours, au 14 avril 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'interface utilisateur, notamment pour la gestion des zones de vigilance et des zones réglementaires, avec des options de filtrage, de tri et de mise en évidence. Des corrections et optimisations ont également été apportées au niveau des données et de l'API, en particulier concernant les navires et les thématiques associées.

### Évolutions fonctionnelles
- Ajout d'un filtre pour afficher les zones récentes dans la gestion des zones ([#405b92e](https://github.com/MTES-MCT/monitorenv/commit/405b92e)).
- Amélioration de l'affichage des zones de vigilance avec des lignes expansibles et des colonnes épinglées ([#bf53348](https://github.com/MTES-MCT/monitorenv/commit/bf53348), [#6430d0f](https://github.com/MTES-MCT/monitorenv/commit/6430d0f), [#207f6a8](https://github.com/MTES-MCT/monitorenv/commit/207f6a8)).
- Mise en évidence des nouvelles zones de vigilance et des zones réglementaires épinglées sur la carte ([#882d0bc](https://github.com/MTES-MCT/monitorenv/commit/882d0bc), [#5bb0165](https://github.com/MTES-MCT/monitorenv/commit/5bb0165)).
- Amélioration de la gestion des zones réglementaires, notamment avec des corrections de tri par façade maritime ([#c25727b](https://github.com/MTES-MCT/monitorenv/commit/c25727b)).
- Ajout du tonnage brut des navires UMS ([#a3ed217](https://github.com/MTES-MCT/monitorenv/commit/a3ed217)).
- Amélioration du flux de données AMP et mise en évidence des nouveaux AMP ([#eed0ba0](https://github.com/MTES-MCT/monitorenv/commit/eed0ba0), [#dd1f770](https://github.com/MTES-MCT/monitorenv/commit/dd1f770)).

### Évolutions techniques
- Ajout d'un index sur les données d'identification pour optimiser les performances ([#eb8cb9d](https://github.com/MTES-MCT/monitorenv/commit/eb8cb9d)).
- Refactorisation du code pour utiliser les identifiants corrects des navires et des lots de données ([#7c55253](https://github.com/MTES-MCT/monitorenv/commit/7c55253)).
- Correction du nom du champ `sent_at` et refactorisation utilisant le timestamp de la clé primaire ([#e09f81e](https://github.com/MTES-MCT/monitorenv/commit/e09f81e)).
- Amélioration de la gestion des erreurs lors de la désérialisation des données ([#b394679](https://github.com/MTES-MCT/monitorenv/commit/b394679), [#32a154a](https://github.com/MTES-MCT/monitorenv/commit/32a154a), [#1bcb610](https://github.com/MTES-MCT/monitorenv/commit/1bcb610)).
- Vérification de la présence de la revendication `organizational_unit` pour renforcer la sécurité ([#1608c9c](https://github.com/MTES-MCT/monitorenv/commit/1608c9c)).
- Refactorisation du contrôle pour utiliser les natinfs suggérées ([#bd0a29e](https://github.com/MTES-MCT/monitorenv/commit/bd0a29e)).
- Ajout d'une API pour récupérer les natinfs à partir des thèmes ([#8681d70](https://github.com/MTES-MCT/monitorenv/commit/8681d70)).

### Autres changements
- Correction de l'URL de la favicon ([#24ee410](https://github.com/MTES-MCT/monitorenv/commit/24ee410)).
- Suppression d'un indicateur de fonctionnalité obsolète pour les zones réglementaires ([#23a0420](https://github.com/MTES-MCT/monitorenv/commit/23a0420)).
- Suppression de secrets inutiles ([#6ec036f](https://github.com/MTES-MCT/monitorenv/commit/6ec036f)).
- Correction des tests unitaires ([#bf3541b](https://github.com/MTES-MCT/monitorenv/commit/bf3541b)).
- Ajout d'un titre aux options du sélecteur Natinf ([#096ccb4](https://github.com/MTES-MCT/monitorenv/commit/096ccb4)).
- Configuration d'un délai de refroidissement de 30 jours pour les mises à jour de dépendances ([#ca95117](https://github.com/MTES-MCT/monitorenv/commit/ca95117)).
- Correction de l'affichage des identifiants des thèmes ([#ab2e38f](https://github.com/MTES-MCT/monitorenv/commit/ab2e38f)).
- Suppression de la clé étrangère des thèmes natinfs ([#aad5ab9](https://github.com/MTES-MCT/monitorenv/commit/aad5ab9)).
- Correction de la gestion des photos nulles ([#7c2d38a](https://github.com/MTES-MCT/monitorenv/commit/7c2d38a)).
- Ajout d'un ordre de tri aux thèmes factices pour éviter les problèmes de déplacement d'ID ([#7c9a703](https://github.com/MTES-MCT/monitorenv/commit/7c9a703)).
- Ajout d'un flux pour associer les thèmes aux natinfs ([#14e855e](https://github.com/MTES-MCT/monitorenv/commit/14e855e)).
- Empêcher la mise à jour des zones réglementaires dans la base de données CACEM sur le serveur d'intégration ([#d753c0f](https://github.com/MTES-MCT/monitorenv/commit/d753c0f)).
- Correction de l'aperçu des calques et des axes des zones réglementaires dans le tableau de bord ([#6aeff26](https://github.com/MTES-MCT/monitorenv/commit/6aeff26)).
- Correction des zones réglementaires par axe ([#268c4c1](https://github.com/MTES-MCT/monitorenv/commit/268c4c1)).
