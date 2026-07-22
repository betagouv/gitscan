## Changelog : a-just (30 derniers jours, au 21 juillet 2026)

### Résumé
Les dernières mises à jour d'a-just se concentrent sur l'ajout d'une fonctionnalité de feedback utilisateur, des améliorations de l'interface utilisateur et des corrections de bugs, notamment concernant l'affichage des dates et le calcul des graphiques. Une page d'administration pour consulter les feedbacks a également été ajoutée.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité permettant aux utilisateurs de donner leur feedback sur le produit a-just via une note (de 1 à 5 étoiles) et un commentaire [#89024c55](https://github.com/betagouv/a-just/commit/89024c55).
- Une page d'administration a été créée pour visualiser l'historique des feedbacks, les notes moyennes, le nombre total de notes (avec et sans commentaire) ainsi que des statistiques générales [#f3001459](https://github.com/betagouv/a-just/commit/f3001459).
- Le champ "recontact" a été ajouté au modèle UserFeedback, à la route correspondante, à la table et à l'interface utilisateur, ainsi qu'à l'administration [#b949d867](https://github.com/betagouv/a-just/commit/b949d867).
- Amélioration de l'affichage des dates dans la section "Situation à prendre en compte", avec une valeur par défaut pour la date d'arrivée [#aa0879f8](https://github.com/betagouv/a-just/commit/aa0879f8).
- Correction d'un bug lié à l'affichage de "A compter du" sur la page de réaffectation [#8a832abd](https://github.com/betagouv/a-just/commit/8a832abd).
- Correction d'un bug lié à la comparaison de dates ("Date" vs "Aujourd'hui") [#9ad62061](https://github.com/betagouv/a-just/commit/9ad62061).

### Évolutions techniques
- Refactorisation du composant PopinGraphsDetails pour améliorer le calcul et l'affichage des graphiques [#40978a66](https://github.com/betagouv/a-just/commit/40978a66).
- Renommage du fichier de test Cypress pour le feedback en `.js` [#6907d28e](https://github.com/betagouv/a-just/commit/6907d28e).
- Déplacement du composant `popin-feedback` dans le dossier `components` [#fed005fc](https://github.com/betagouv/a-just/commit/fed005fc).
- Correction d'une requête Sequelize pour l'obtention des statistiques sur la table `Userfeedback` [#06e52cb2](https://github.com/betagouv/a-just/commit/06e52cb2).
- Correction d'un problème de validation avec `koa-smart` qui provoquait une erreur 500 au lieu d'une 400 [#ec31cd51](https://github.com/betagouv/a-just/commit/ec31cd51).

### Autres changements
- Modification du nom "banner" en "notifications" pour les blocs publicitaires [#21eb93c4](https://github.com/betagouv/a-just/commit/21eb93c4).
- Amélioration du style de l'affichage des étoiles sur la page d'administration des feedbacks [#e64e5cd0](https://github.com/betagouv/a-just/commit/e64e5cd0).
- Utilisation de constantes de style pour les couleurs sur la page des avis [#f7c74c5a](https://github.com/betagouv/a-just/commit/f7c74c5a).
- Corrections de style et améliorations de l'interface utilisateur pour le banner et le feedback [#f1efb445](https://github.com/betagouv/a-just/commit/f1efb445).
- Ajout de tests E2E pour la fonctionnalité de feedback [#7426d7fb](https://github.com/betagouv/a-just/commit/7426d7fb).
- Mise à jour de la version du projet [#9855e2a7](https://github.com/betagouv/a-just/commit/9855e2a7).
- Suppression de commentaires et correction de la mise en page des bannières [#dcda241d](https://github.com/betagouv/a-just/commit/dcda241d).
- Correction de tests commentés [#89ef876f](https://github.com/betagouv/a-just/commit/89ef876f).
