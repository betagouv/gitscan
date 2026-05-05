## Changelog : Resultats-Elections-FPT (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'interface utilisateur et la correction de bugs, notamment au niveau du tableau de résultats, de la cartographie et du formulaire de scrutin. Des optimisations ont été apportées pour améliorer l'expérience utilisateur et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout de la sélection de ligne dans le tableau des résultats via un curseur grist. [#49](https://github.com/betagouv/Resultats-Elections-FPT/pull/49)
- Amélioration du formulaire de scrutin : suppression du message de résultat vide lors d'une nouvelle recherche. [#48](https://github.com/betagouv/Resultats-Elections-FPT/pull/48)
- Affichage du tag "doublon" sur la cartographie avec le style "erreur" pour une meilleure visibilité. [#46](https://github.com/betagouv/Resultats-Elections-FPT/pull/46)
- Le tableau des résultats ne se filtre plus automatiquement, mais uniquement lors d'un clic sur le bouton "Appliquer les filtres". [#45](https://github.com/betagouv/Resultats-Elections-FPT/pull/45)
- Ajout d'un type d'affichage de cellule "badge" pour le tableau des résultats. [#37](https://github.com/betagouv/Resultats-Elections-FPT/pull/37)
- Ajout de filtres au tableau des résultats. [#30](https://github.com/betagouv/Resultats-Elections-FPT/pull/30)
- La recherche de scrutin est désormais insensible aux accents et affiche automatiquement la liste complète si la recherche est vide. [#29](https://github.com/betagouv/Resultats-Elections-FPT/pull/29)

### Évolutions techniques
- Suppression des anciennes vues HTML remplacées par des vues génériques, allégeant ainsi le code. [#47](https://github.com/betagouv/Resultats-Elections-FPT/pull/47)
- Création d'une version figée pour les custom widgets à la version v0.12. [#38](https://github.com/betagouv/Resultats-Elections-FPT/pull/38)

### Autres changements
- Correction du badge optionnel dans la fiche d'une entité. [#50](https://github.com/betagouv/Resultats-Elections-FPT/pull/50)
- Diverses corrections et améliorations générales. [#44](https://github.com/betagouv/Resultats-Elections-FPT/pull/44) & [#39](https://github.com/betagouv/Resultats-Elections-FPT/pull/39)
- Correction du formulaire de modalités de scrutins (multiples CAP et bug d'affichage). [#42](https://github.com/betagouv/Resultats-Elections-FPT/pull/42)
- Correction de l'affichage du formulaire sur la vue cartographie. [#41](https://github.com/betagouv/Resultats-Elections-FPT/pull/41)
- Création d'une vue pour afficher un bouton. [#40](https://github.com/betagouv/Resultats-Elections-FPT/pull/40)
- Réduction de la taille de la modale du tableau. [#32](https://github.com/betagouv/Resultats-Elections-FPT/pull/32)
- Modification de l'option 'vide' du select et ajout d'une option pour cacher le formulaire. [#34](https://github.com/betagouv/Resultats-Elections-FPT/pull/34)
- Rendre la colonne badge optionnelle dans la recherche de scrutin. [#33](https://github.com/betagouv/Resultats-Elections-FPT/pull/33)
