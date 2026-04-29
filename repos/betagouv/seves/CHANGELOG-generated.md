## Changelog : seves (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les évolutions de Sèves se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de l'édition et de la visualisation des données, ainsi que sur la correction de bugs et l'optimisation de la performance. Des améliorations ont été apportées aux formulaires, aux tableaux de données et à la gestion des fichiers. Des corrections de sécurité et des mises à jour de dépendances ont également été effectuées.

### Évolutions fonctionnelles
- Amélioration de l'historique pour les Suivis Sanitaires (SV) [#5565d54](https://github.com/betagouv/seves/commit/5565d54).
- Possibilité de prévisualiser les images et les fichiers PDF [#3bdeb05](https://github.com/betagouv/seves/commit/3bdeb05).
- Ajout du numéro RASFF aux objets TIAC [#b6469bf](https://github.com/betagouv/seves/commit/b6469bf).
- Ajout de la date de publication sur tous les objets "fiche" [#51fa26d](https://github.com/betagouv/seves/commit/51fa26d).
- Amélioration de la précision des notifications dans le contexte des Situations Sanitaires Aggravées (SSA) [#107ac35](https://github.com/betagouv/seves/commit/107ac35).
- Ajout d'un champ "Date de réception" avec une date maximale dans l'interface utilisateur [#16c371b](https://github.com/betagouv/seves/commit/16c371b).
- Possibilité de mettre à jour une fiche ayant une relation avec un objet supprimé [#5289058](https://github.com/betagouv/seves/commit/5289058).
- Ajout d'un indicateur d'accessibilité pour la "fiche zone délimitée" dans le tableau des événements SV [#bb0c0ad](https://github.com/betagouv/seves/commit/bb0c0ad).
- Amélioration de l'affichage des dates des messages [#034ca53](https://github.com/betagouv/seves/commit/034ca53).
- Correction de l'affichage pour l'éditeur de texte enrichi [#42a13ee](https://github.com/betagouv/seves/commit/42a13ee) et [#6debe44](https://github.com/betagouv/seves/commit/6debe44).
- Ajout de l'option "ON" pour les SV [#6b49448](https://github.com/betagouv/seves/commit/6b49448).
- Correction pour autoriser les lettres dans le numéro d'agrément des établissements [#2055cfe](https://github.com/betagouv/seves/commit/2055cfe).
- Correction de la date utilisée pour les messages lors de l'export en Docx [#a4125dd](https://github.com/betagouv/seves/commit/a4125dd).
- Correction de l'affichage pour l'ancien sélecteur d'arbre (Treeselect) [#e8f5590](https://github.com/betagouv/seves/commit/e8f5590).
- Correction d'une régression avec GEA sur le nouveau Treeselect [#e8f5590](https://github.com/betagouv/seves/commit/e8f5590).

### Évolutions techniques
- Mise à jour de Django vers la version 6 [#e760f3f](https://github.com/betagouv/seves/commit/e760f3f).
- Ajout d'un timeout sur les requêtes OIDC pour éviter les interruptions des workers en production [#0d85baf](https://github.com/betagouv/seves/commit/0d85baf).
- Refactorisation de l'implémentation du Treeselect, abandon de l'ancienne implémentation TIAC [#f0246ed](https://github.com/betagouv/seves/commit/f0246ed).
- Amélioration de la performance de la vue de liste des SSA [#8e5af29](https://github.com/betagouv/seves/commit/8e5af29).
- Ajout de la reconnection à Redis pour Celery [#9dab5ba](https://github.com/betagouv/seves/commit/9dab5ba).
- Suppression des révisions ajoutées par les signaux dans SV [#c3a59b4](https://github.com/betagouv/seves/commit/c3a59b4).
- Désactivation des warnings Python sur CI pour améliorer la lisibilité [#d067195](https://github.com/betagouv/seves/commit/d067195).
- Remplacement de Clamav par une solution antivirus en ligne [#65c5b00](https://github.com/betagouv/seves/commit/65c5b00).

### Autres changements
- Correction de l'aperçu PDF pour le navigateur Brave [#5565d54](https://github.com/betagouv/seves/commit/5565d54).
- Correction de l'ellipses tooltip sur TIAC [#6a09d39](https://github.com/betagouv/seves/commit/6a09d39).
- Correction de l'affichage des noms de fichiers longs dans le tableau des documents [#5acac94](https://github.com/betagouv/seves/commit/5acac94).
- Uniformisation des liens d'annulation sur les objets "fiche" [#98d3a21](https://github.com/betagouv/seves/commit/98d3a21).
- Changement des formats des filtres "année" et "numéro" [#f6b7c47](https://github.com/betagouv/seves/commit/f6b7c47).
- Ajout de boutons d'action du formulaire en bas de page [#8e96590](https://github.com/betagouv/seves/commit/8e96590).
- Corrections de design sur SV [#e9b2045](https://github.com/betagouv/seves/commit/e9b2045) et [#8bda377](https://github.com/betagouv/seves/commit/8bda377).
- Correction de l'affichage du menu de domaine sur la page de détails de l'événement [#ede7dea](https://github.com/betagouv/seves/commit/ede7dea).
- Correction d'un assert flaky dans les tests [#1ff40d2](https://github.com/betagouv/seves/commit/1ff40d2).
- Refactorisation de l'utilisation de `and_more_ellipsis_tooltip` [#b3d398d](https://github.com/betagouv/seves/commit/b3d398d).
- Correction de l'état lors de la modification après clôture [#0e74ffa](https://github.com/betagouv/seves/commit/0e74ffa).
