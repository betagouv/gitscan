## Changelog : a-just (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a-just s'est concentrée sur l'amélioration de l'expérience utilisateur, notamment en ajoutant une fonctionnalité de feedback pour recueillir l'avis des utilisateurs, et en améliorant la gestion des dates et des situations. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité de feedback utilisateur permettant de noter l'application et de laisser un commentaire [#89024c55](https://github.com/betagouv/a-just/commit/89024c55).
- Affichage automatique de la fenêtre de feedback pour les utilisateurs utilisant le produit depuis plus d'un mois [#00e867fa](https://github.com/betagouv/a-just/commit/00e867fa).
- Amélioration de la gestion des dates de début de statut lors de la création d'un agent [#b27b19f7](https://github.com/betagouv/a-just/commit/b27b19f7).
- Possibilité de saisir manuellement une date dans les composants de sélection de date (aj-date-select et aj-date-select-blue) [#761752ed](https://github.com/betagouv/a-just/commit/761752ed).
- Duplication de la situation actuelle [#0f3dbfdc](https://github.com/betagouv/a-just/commit/0f3dbfdc).
- Ajout du nom de l'agent au nom d'utilisation [#cc8242bc](https://github.com/betagouv/a-just/commit/cc8242bc).

### Évolutions techniques
- Refactorisation du code pour déplacer le composant `popin-feedback` dans le dossier `components` [#fed005fc](https://github.com/betagouv/a-just/commit/fed005fc).
- Correction d'une requête Sequelize pour l'obtention des statistiques de feedback [#06e52cb2](https://github.com/betagouv/a-just/commit/06e52cb2).
- Correction d'un bug dans la logique de comparaison de dates [#8a832abd](https://github.com/betagouv/a-just/commit/8a832abd).
- Correction d'un problème de validation avec Koa-smart, qui provoquait une erreur 500 au lieu d'une 400 [#ec31cd51](https://github.com/betagouv/a-just/commit/ec31cd51).
- Mise à jour des tests E2E pour la fonctionnalité de feedback [#7426d7fb](https://github.com/betagouv/a-just/commit/7426d7fb).
- Réécriture des tests E2E pour l'ajout d'agent afin d'utiliser l'entrée manuelle ajoutée au composant de sélection de date [#57939669](https://github.com/betagouv/a-just/commit/57939669).

### Autres changements
- Renommage de "banner" en "notifications" pour les blocs publicitaires [#21eb93c4](https://github.com/betagouv/a-just/commit/21eb93c4).
- Amélioration du style de la page d'administration des feedbacks [#e64e5cd0](https://github.com/betagouv/a-just/commit/e64e5cd0).
- Correction de fautes de français [#36d68aa1](https://github.com/betagouv/a-just/commit/36d68aa1), [#9ad62061](https://github.com/betagouv/a-just/commit/9ad62061).
- Mise à jour du contenu des démos Panorama et Calculateur [#41f42fc2](https://github.com/betagouv/a-just/commit/41f42fc2), [#be445df2](https://github.com/betagouv/a-just/commit/be445df2), [#3600abc2](https://github.com/betagouv/a-just/commit/3600abc2).
- Suppression de commentaires et de logs inutiles [#a9b5435b](https://github.com/betagouv/a-just/commit/a9b5435b), [#8223a9b1](https://github.com/betagouv/a-just/commit/8223a9b1), [#32a0f972](https://github.com/betagouv/a-just/commit/32a0f972).
- Correction de titres d'infobulles TMD [#6587b216](https://github.com/betagouv/a-just/commit/6587b216).
- Suppression d'un fichier d'extension de test Cypress au format ts et remplacement par js [#6907d28e](https://github.com/betagouv/a-just/commit/6907d28e).
- Correction d'un bug sur la page de réaffectation [#8a832abd](https://github.com/betagouv/a-just/commit/8a832abd).
- Correction d'un bug sur les statistiques de notation [#46580931](https://github.com/betagouv/a-just/commit/46580931).
- Correction d'un bug sur le bouton de documentation E2E [#48fd46c5](https://github.com/betagouv/a-just/commit/48fd46c5).
- Correction de l'affichage de la date d'arrivée [#aa0879f8](https://github.com/betagouv/a-just/commit/aa0879f8).
- Amélioration du style des avis en utilisant les constantes de style [#f7c74c5a](https://github.com/betagouv/a-just/commit/f7c74c5a).
- Ajout d'une page d'administration des avis pour visualiser l'historique, la note moyenne, le nombre total d'avis, avec et sans commentaire, ainsi que des statistiques générales [#f3001459](https://github.com/betagouv/a-just/commit/f3001459).
- Suppression de tests commentés [#89ef876f](https://github.com/betagouv/a-just/commit/89ef876f).
- Correction de la mise en page des bannières [#dcda241d](https://github.com/betagouv/a-just/commit/dcda241d).
- Commentaire temporaire de la bannière de feedback pour vérifier si les tests E2E étaient affectés [#abdd7a76](https://github.com/betagouv/a-just/commit/abdd7a76).
- Mise à jour de la version [#9855e2a7](https://github.com/betagouv/a-just/commit/9855e2a7).
- Correction d'un warning sur la page panorama [#faec5186](https://github.com/betagouv/a-just/commit/faec5186).
- Préttier sur le composant feedback-banner [#0adb9d13](https://github.com/betagouv/a-just/commit/0adb9d13).
- Hauteur minimale pour le conteneur wrapper [#7ef3acad](https://github.com/betagouv/a-just/commit/7ef3acad).
